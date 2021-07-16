import csv
import os

os.environ['FI_EFA_FORK_SAFE'] = '1'

import reframe as rfm
import reframe.utility.sanity as sn
import reframe.utility.udeps as udeps
import hackathon as hack

from reframe.core.launchers import LauncherWrapper


# Where to run the binaries 'aws:c6gn' on Arm or 'aws:c5n' on Intel
my_valid_systems = ['aws:c5n' if os.uname().machine == 'x86_64' else 'aws:c6gn']

# Logging Variables
my_log_team_name = 'TeamEPCC'
my_log_app_name = 'meme'

rfile = 'Klf1.fna.txt'  # reference output
ofile = 'Klf1.fna.out'  # actual output

my_prerun_cmds = [
    f'wget https://raw.githubusercontent.com/rj-jesus/Cloud-HPC-Hackathon-2021/app/meme/Applications/Applications/meme/inputs/Klf1.fna',
    f'wget https://raw.githubusercontent.com/rj-jesus/Cloud-HPC-Hackathon-2021/app/meme/Applications/Applications/meme/outputs/Klf1.fna.txt -O {rfile}',
]

# Parameters - Compilers - Defined as their Spack specs (use spec or hash)
my_spec = [
    # Intel
    'meme/ylex6xs',  # Meme with the Gnu compiler
    'meme/ucxv6oz',  # Meme with the Nvidia compiler
] if 'aws:c5n' in my_valid_systems else [
    # Arm
    'meme/csigtg7',  # Meme with the Arm compiler
    'meme/xzjirlu',  # Meme with the Gnu compiler
    'meme/fifpy6p',  # Meme with the Nvidia compiler
]

# Parameters - MPI / Threads - Used for scaling studies
my_parallelism = [
    { 'nodes' : 1, 'mpi' :   1, 'omp' : 1},
    { 'nodes' : 1, 'mpi' :   3, 'omp' : 1},
    { 'nodes' : 1, 'mpi' :   9, 'omp' : 1},
    { 'nodes' : 1, 'mpi' :  18, 'omp' : 1},
    { 'nodes' : 1, 'mpi' :  36, 'omp' : 1},
    { 'nodes' : 1, 'mpi' :  72, 'omp' : 1},
    { 'nodes' : 2, 'mpi' : 144, 'omp' : 1},
    { 'nodes' : 4, 'mpi' : 288, 'omp' : 1},
    { 'nodes' : 8, 'mpi' : 576, 'omp' : 1},
] if 'aws:c5n' in my_valid_systems else [
    { 'nodes' : 1, 'mpi' :   1, 'omp' : 1},
    { 'nodes' : 1, 'mpi' :   2, 'omp' : 1},
    { 'nodes' : 1, 'mpi' :   4, 'omp' : 1},
    { 'nodes' : 1, 'mpi' :   8, 'omp' : 1},
    { 'nodes' : 1, 'mpi' :  16, 'omp' : 1},
    { 'nodes' : 1, 'mpi' :  32, 'omp' : 1},
    { 'nodes' : 1, 'mpi' :  64, 'omp' : 1},
    { 'nodes' : 2, 'mpi' : 128, 'omp' : 1},
    { 'nodes' : 4, 'mpi' : 256, 'omp' : 1},
    { 'nodes' : 8, 'mpi' : 512, 'omp' : 1},
]

my_postrun_cmds = [
    f"tail -n +12 {rfile} | head -n -4 | grep -v 'PRIMARY SEQUENCES=\|command:\|Time' > {rfile}.clean",
    f"tail -n +12 {ofile} | head -n -4 | grep -v 'PRIMARY SEQUENCES=\|command:\|Time' > {ofile}.clean",
    f'diff -q {rfile}.clean {ofile}.clean && echo PASS || echo FAIL',
]

@rfm.simple_test
class MemeKlf1(hack.HackathonBase):
    valid_systems = my_valid_systems

    log_team_name = my_log_team_name
    log_app_name  = my_log_app_name
    log_test_name = __name__[4:]
    log_test_type = 'profile'

    prerun_cmds = my_prerun_cmds

    # Define Execution
    executable = 'meme'
    executable_opts = [
        'Klf1.fna', '-oc', 'Klf1.fa.d', '-dna', '-text', '-nmotifs', '16', '-maxsize', '100000000', '-maxw', '25', f'>{ofile}'
    ]

    spec = parameter(my_spec)
    parallelism = parameter(my_parallelism)

    postrun_cmds = my_postrun_cmds

    # Request exclusive nodes from slurm
    @run_before('run')
    def prepare_job(self):
        self.job.options += ['--exclusive']

    # Code validation
    @run_before('sanity')
    def set_sanity_patterns(self):
        pass_regex = r'^PASS$'
        m = sn.len(sn.findall(pass_regex, self.stdout))
        self.sanity_patterns = sn.assert_found(pass_regex, self.stdout)

        # Performance Testing - Total Time units 's'
        # We dont set an expected value
        self.reference = {
            '*': { 'Total Time': (0, None, None, 's'), }
        }

        perf_regex = r'^Time\s+(\S+) secs.'  # Time 73.34 secs.
        self.perf_patterns = {
            'Total Time': sn.extractsingle(perf_regex, ofile, 1, float, item=-1),
        }

    # Before we run, add MAP to the launcher
    @run_before('run')
    def set_profiler(self):
        self.proffile = 'prof.csv'
        self.keep_files.append(self.proffile)
        self.modules.append('arm-forge@21.0')
        self.job.launcher = LauncherWrapper(self.job.launcher, 'map', ['--profile', f'--export-functions={self.proffile}'])

    # Now we retrieve the CSV file and parse it into the `hot_spots' variable
    @run_before('sanity')
    def get_prof_data(self):
        self.hot_spots = []
        with open(os.path.join(self.stagedir, self.proffile), newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            next(reader, None)  # skip header
            for index, row in zip(range(10), reader):
               self.hot_spots.append({
                   "position" : index,
                   "name" : row[7],
                   "percent" : row[2],
                   "mpi_percent" : row[4]
               })
