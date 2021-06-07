import reframe as rfm
import reframe.utility.sanity as sn
import hackathon as hack

@rfm.simple_test
class CloverLeafTest(hack.HackathonBase):
    # Where to run the binaries
    valid_systems = ['aws:c6g', 'aws:c6gn'] 

    # Logging Variables
    log_team_name = 'TeamArm'
    log_app_name = 'CloverLeaf'
    log_test_name = 'BM512_short'

    # Define test case
    prerun_cmds = ['wget -O clover.in https://raw.githubusercontent.com/UK-MAC/CloverLeaf_ref/master/InputDecks/clover_bm512_short.in']

    # Define Execution
    logfile = 'clover.out'
    executable = 'clover_leaf'
    executable_opts = []
    keep_files = [logfile]

    # Parameters - Compilers
    spec = parameter([
        'cloverleaf@1.1 %gcc@10.3.0',
        'cloverleaf@1.1 %arm@21.0.0.879'
    ])

    # Parameters - MPI / Threads
    parallelism = parameter([
        { 'nodes' : 1, 'mpi' : 32, 'omp' : 1},
        { 'nodes' : 1, 'mpi' : 64, 'omp' : 1},
        { 'nodes' : 2, 'mpi' : 128, 'omp' : 1},
        { 'nodes' : 4, 'mpi' : 256, 'omp' : 1},
    ])

    @rfm.run_before('sanity')
    def set_sanity_patterns(self):
       # Validation at step 87 (BM_short)
       # Regex - Volume   Mass   Density   Pressure   Internal Energy   Kinetic Energy   Total Energy
       sol_regex = r'\s+step:\s+87\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)'

       # Validate for kenetic energy (6) = 0.3075
       kenetic_energy = sn.extractsingle(sol_regex, self.logfile, 6, float)
       self.sanity_patterns = sn.assert_bounded(kenetic_energy, 0.038605, 0.038615)

       # Performance Testing
       self.reference = {
          '*': {'Total Time': (0, None, None, 's'),}
       }

       # Extract wall clock values
       pref_regex = r'\s+Wall clock\s+(\S+)'
       times = sn.extractall(pref_regex,self.logfile, 1, float)

       # Use last wall clock
       self.perf_patterns = { 
               'Total Time':  times[sn.count(times) -1],
       }


