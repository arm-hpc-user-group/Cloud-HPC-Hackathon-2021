import os

os.environ['FI_EFA_FORK_SAFE'] = '1'

import reframe as rfm
import reframe.utility.sanity as sn
import reframe.utility.udeps as udeps
import hackathon as hack


# Where to run the binaries 'aws:c6gn' on Arm or 'aws:c5n' on Intel
my_valid_systems = ['aws:c5n' if os.uname().machine == 'x86_64' else 'aws:c6gn']

# Logging Variables
my_log_team_name = 'TeamEPCC'
my_log_app_name = 'meme'

rfile = 'lex0.fna.txt'  # reference output
ofile = 'lex0.fna.out'  # actual output

my_prerun_cmds = [
    f'wget https://meme-suite.org/meme/doc/examples/example-datasets/lex0.fna',                      # dataset
    f'wget https://meme-suite.org/meme/doc/examples/meme_example_output_files/meme.txt -O {rfile}',  # reference output
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
    f"cp lex0.fna.d/meme.txt {ofile}",  # output generated
    f"tail -n +12 {rfile} | head -n -4 | grep -v 'PRIMARY SEQUENCES=\|command:\|Time' > {rfile}.clean",
    f"tail -n +12 {ofile} | head -n -4 | grep -v 'PRIMARY SEQUENCES=\|command:\|Time' > {ofile}.clean",
    f'diff -q {rfile}.clean {ofile}.clean && echo PASS || echo FAIL',
]

@rfm.simple_test
class MemeLex09(hack.HackathonBase):
    valid_systems = my_valid_systems

    log_team_name = my_log_team_name
    log_app_name  = my_log_app_name
    log_test_name = __name__[4:]

    prerun_cmds = my_prerun_cmds

    # Define Execution
    executable = 'meme'
    executable_opts = [
        'lex0.fna', '-oc', 'lex0.fna.d', '-dna', '-mod', 'zoops', '-nmotifs', '3', '-revcomp',
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
            '*': {'Total Time': (0, None, None, 's'),}
        }

        perf_regex = r'^Time\s+(\S+) secs.'  # Time 73.34 secs.
        self.perf_patterns = {
            'Total Time': sn.extractsingle(perf_regex, ofile, 1, float, item=-1)
        }
