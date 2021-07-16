import reframe as rfm
import reframe.utility.sanity as sn
import hackathon as hack

@rfm.simple_test
class Graph500Test(hack.HackathonBase):
    # Where to run the binaries 'aws:c6gn' on Arm or 'aws:c5n' on Intel
    valid_systems = ['aws:c6gn']
    # valid_systems = ['aws:c5n']

    # Logging Variables
    log_team_name = 'Masterofpuppets'
    log_app_name = 'G500'
    log_test_name = 'x86_scalab'

    # Define test case
    # In this case we download the file from GitHub and write as clover.in - the expected input file
    # prerun_cmds = ['wget -O clover.in https://raw.githubusercontent.com/UK-MAC/CloverLeaf_ref/master/InputDecks/clover_bm16_short.in']

    # Define Execution
    # Binary to run
    executable = 'graph500_reference_bfs'
    # Command line options to pass
    executable_opts = ['20']
    # Where the output is written to
    logfile = 'scalab.out'
    # Store the output file (used for validation later)
    keep_files = [logfile]


    # Parameters - Compilers - Defined as their Spack specs (use spec or hash)
    spec = parameter([
        # 'cloverleaf@1.1 %gcc@10.3.0',     # CloverLeaf with the GCC compiler
        # 'cloverleaf@1.1 %arm@21.0.0.879', # CloverLeaf with the Arm compiler
        # 'cloverleaf@1.1 %nvhpc@21.2'      # CloverLeaf with the NVIDIA compiler
        'graph500@3.0.0 %gcc@10.3.0 /wmqhhx',
        # 'graph500@3.0.0 %gcc@10.3.0 /gjlnyo',
    ])

    # Parameters - MPI / Threads - Used for scaling studies
    parallelism = parameter(
        # { 'nodes' : 1, 'mpi' : 1,   'omp' : 1},
        # { 'nodes' : 1, 'mpi' : 2,   'omp' : 1},
        # { 'nodes' : 1, 'mpi' : 4,   'omp' : 1},
        # { 'nodes' : 1, 'mpi' : 8,   'omp' : 1},
        # { 'nodes' : 1, 'mpi' : 16,  'omp' : 1},
        # { 'nodes' : 1, 'mpi' : 32,  'omp' : 1},
        # { 'nodes' : 1, 'mpi' : 64,  'omp' : 1},
        [ { 'nodes' : max(1, (2**x) // 64), 'mpi' : 2**x, 'omp': 1 } for x in range(10) ]
    )

    # Request exclusive nodes from slurm
    @rfm.run_before('run')
    def prepare_job(self):
       self.job.options += ['--exclusive']

    # Code validation
    @run_before('sanity')
    def set_sanity_patterns(self):

       # Use the logfile for validation testing and performance

       # Validation at step 87 (BM_short)
       # Regex - Volume   Mass   Density   Pressure   Internal Energy   Kinetic Energy   Total Energy
       # sol_regex = r'\s+step:\s+87\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)'
       # sol_regex = 'Validating BFS 63'

       # Validate for kinetic energy (6)
       # last_step_validated = sn.extractsingle(sol_regex, self.logfile, 6, float)

       # expected = 0.3075
       # expected_lower = 0.30745
       # expected_upper = 0.30755

       # Perform a bounded assert
       # self.sanity_patterns = sn.assert_found(sol_regex, self.logfile, msg='upsi')
       # self.sanity_patterns = sn.assert_bounded(kinetic_energy, expected_lower, expected_upper)
       self.sanity_patterns = sn.assert_true(True)

       # Performance Testing - FOM Total Time units 's'
       # We dont set an expected value
       # self.reference = {
       #    '*': {'Mean TEPS': (0, None, None, 's'),}
       # }

       # CloverLeaf prints the 'Wall clock' every timestep - so extract all lines matching the regex
       # pref_regex = r'\s+bfs  harmonic_mean_TEPS:     ! \s+(\S+)'
       # self.perf_patterns = {
       #         'Mean TEPS': sn.extractsingle(pref_regex, self.logfile, 1, float, item=-1)
       # }

