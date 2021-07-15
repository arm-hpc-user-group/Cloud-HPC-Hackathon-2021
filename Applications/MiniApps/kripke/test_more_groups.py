import reframe as rfm
import reframe.utility.sanity as sn
import hackathon as hack
from datetime import datetime

@rfm.simple_test
class KripkeTest(hack.HackathonBase):
    # Where to run the binaries 'aws:c6gn' on Arm or 'aws:c5n' on Intel
    valid_systems = ['aws:c6gn']

    # Logging Variables
    log_team_name = 'Dogecointothemoon'
    log_app_name = 'Kripke'
    log_test_name = 'large_group'

    # Define test case
    # In this case we download the file from GitHub and write as clover.in - the expected input file
    # prerun_cmds = ['wget -O clover.in https://raw.githubusercontent.com/UK-MAC/CloverLeaf_ref/master/InputDecks/clover_bm16_short.in']

    # Define Execution
    # Binary to run
    executable = 'kripke.exe'
    # Command line options to pass
    executable_opts = ['--zones 32,32,32 --groups 64 > Kripke.out']
    # Where the output is written to
    logfile = 'Kripke.out'
    # Store the output file (used for validation later)
    keep_files = [logfile]

    # Parameters - Compilers - Defined as their Spack specs (use spec or hash)
    spec = parameter([
        'kripke@1.2.4%gcc@10.3.0',
        'kripke@1.2.4%arm@21.0.0.879',     # Kripke with the ARM compiler
        'kripke@1.2.4%nvhpc@21.2',
    ])

    # Parameters - MPI / Threads - Used for scaling studies
    parallelism = parameter([
        { 'nodes' : 1, 'mpi' : 1, 'omp' : 1, 'extra-cmd': '1,1,1'},
        { 'nodes' : 1, 'mpi' : 2, 'omp' : 1, 'extra-cmd': '1,1,2'},
        { 'nodes' : 1, 'mpi' : 4, 'omp' : 1, 'extra-cmd': '1,1,4'},
        { 'nodes' : 1, 'mpi' : 8, 'omp' : 1, 'extra-cmd': '1,2,4'},
        { 'nodes' : 1, 'mpi' : 16, 'omp' : 1, 'extra-cmd': '1,4,4'},
        { 'nodes' : 1, 'mpi' : 32, 'omp' : 1, 'extra-cmd': '2,4,4'},
        { 'nodes' : 1, 'mpi' : 64, 'omp' : 1, 'extra-cmd': '4,4,4'},
        { 'nodes' : 2, 'mpi' : 128, 'omp' : 1, 'extra-cmd': '4,4,8'},
        { 'nodes' : 4, 'mpi' : 256, 'omp' : 1, 'extra-cmd': '4,8,8'},
    ])
    @run_before('run')
    def set_config(self):
        self.executable_opts.append('--procs')
        self.executable_opts.append(self.parallelism['extra-cmd'])

    # Request exclusive nodes from slurm
    @rfm.run_before('run')
    def prepare_job(self):
       self.job.options += ['--exclusive=user']

    @run_before('sanity')
    def set_sanity_patterns(self):
        #Validate the particle in the last iter
        particle_regex = r'iter 9: particle count=(\d+\.\d+e\+\d+)'
        change_regex = r'iter 9: particle count=\d+\.\d+e\+\d+, change=(\d+\.\d+e-\d+)'

        particle = sn.extractsingle(particle_regex, self.logfile, 1, float)
        change = sn.extractsingle(change_regex, self.logfile, 1, float)

        expected_particle_lower = 1.684725e+08
        expected_particle_upper = 1.684735e+08

        self.sanity_patterns = sn.assert_bounded(particle, expected_particle_lower, expected_particle_upper)

        pref_regex = r'Solve\s*[1]\s*(\d+\.\d+)'
        self.reference = {
            '*': {'Total Time': (0, None, None, 's'), }
        }
        x = sn.extractsingle(pref_regex, self.stagedir + "/" + self.logfile, 1, float, item=-1) 
        self.perf_patterns = {
            'Total Time': sn.extractsingle(pref_regex, self.stagedir + "/" + self.logfile, 1, float, item=-1)
        }

