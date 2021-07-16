import os
import sys

import reframe as rfm
import reframe.utility.sanity as sn
import reframe.utility.udeps as udeps
import hackathon as hack


# Where to run the binaries 'aws:c6gn' on Arm or 'aws:c5n' on Intel
my_valid_systems = ['aws:c6gn']

# Logging Variables
my_log_team_name = 'TeamEPCC'
my_log_app_name = 'meme'
my_log_test_name = 'meme'

my_prerun_cmds = [
    'wget https://raw.githubusercontent.com/rj-jesus/Cloud-HPC-Hackathon-2021/app/meme/Applications/Applications/meme/inputs/Klf1.fna',
    'wget https://raw.githubusercontent.com/rj-jesus/Cloud-HPC-Hackathon-2021/app/meme/Applications/Applications/meme/outputs/Klf1.fna.txt',
]

# Where the output is written to
ofile = 'Klf1.fna.out'

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
    #{ 'nodes' : 1, 'mpi' :  1, 'omp' : 1},
    #{ 'nodes' : 1, 'mpi' :  2, 'omp' : 1},
    #{ 'nodes' : 1, 'mpi' :  4, 'omp' : 1},
    #{ 'nodes' : 1, 'mpi' :  8, 'omp' : 1},
    #{ 'nodes' : 1, 'mpi' : 16, 'omp' : 1},
    { 'nodes' : 1, 'mpi' : 32, 'omp' : 1},
    { 'nodes' : 1, 'mpi' : 64, 'omp' : 1},
]

my_postrun_cmds = [
    "tail -n +12 Klf1.fna.txt | head -n -4 | grep -v 'PRIMARY SEQUENCES=\|command:\|Time' > Klf1.fna.txt.clean",
    f"tail -n +12 {ofile}     | head -n -4 | grep -v 'PRIMARY SEQUENCES=\|command:\|Time' > {ofile}.clean",
    f'diff -q Klf1.fna.txt.clean {ofile}.clean && echo PASS || echo FAIL',
]

@rfm.simple_test
class MemeKlf1(hack.HackathonBase):
    valid_systems = my_valid_systems

    log_team_name = my_log_team_name
    log_app_name  = my_log_app_name
    log_test_name = my_log_test_name

    prerun_cmds = my_prerun_cmds

    # Define Execution
    executable = 'meme'
    executable_opts = [
        'Klf1.fna', '-oc', 'Klf1.fa.meme', '-dna', '-text', '-nmotifs', '16', '-maxsize', '100000000', '-maxw', '25', f'>{ofile}'
    ]

    spec = parameter(my_spec)
    parallelism = parameter(my_parallelism)

    postrun_cmds = my_postrun_cmds

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
