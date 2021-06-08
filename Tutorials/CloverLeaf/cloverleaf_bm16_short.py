import reframe as rfm
import reframe.utility.sanity as sn
import hackathon as hack

@rfm.simple_test
class CloverLeafTest(hack.HackathonBase):
    # Where to run the binaries
    valid_systems = ['aws:c6g'] #, 'aws:c6gn'] 

    # Logging Variables
    log_team_name = 'TeamArm'
    log_app_name = 'CloverLeaf'
    log_test_name = 'BM16_short'

    # Define test case
    # In this case we download the file from GitHub and write as clover.in - the expected input file
    prerun_cmds = ['wget -O clover.in https://raw.githubusercontent.com/UK-MAC/CloverLeaf_ref/master/InputDecks/clover_bm16_short.in']

    # Define Execution
    # Binary to run
    executable = 'clover_leaf'
    # Command line options to pass
    executable_opts = []
    # Where the output is written to
    logfile = 'clover.out'
    # Store the output file (used for validation later)
    keep_files = [logfile]


    # Parameters - Compilers - Defined as their Spack specs (use spec or hash)
    spec = parameter([
        'cloverleaf@1.1 %gcc@10.3.0',    # CloverLeaf with the GCC compiler
        'cloverleaf@1.1 %arm@21.0.0.879' # CloverLeaf with the Arm compiler
    ])

    # Parameters - MPI / Threads - Used for scaling studies
    parallelism = parameter([
        { 'nodes' : 1, 'mpi' : 1, 'omp' : 1},
        { 'nodes' : 1, 'mpi' : 2, 'omp' : 1},
        { 'nodes' : 1, 'mpi' : 4, 'omp' : 1},
        { 'nodes' : 1, 'mpi' : 8, 'omp' : 1},
        { 'nodes' : 1, 'mpi' : 16, 'omp' : 1},
        { 'nodes' : 1, 'mpi' : 32, 'omp' : 1},
        { 'nodes' : 1, 'mpi' : 64, 'omp' : 1},
    ])


    # Code validation
    @rfm.run_before('sanity')
    def set_sanity_patterns(self):

       # Use the logfile for validation testing and performance 

       # Validation at step 87 (BM_short)
       # Regex - Volume   Mass   Density   Pressure   Internal Energy   Kinetic Energy   Total Energy
       sol_regex = r'\s+step:\s+87\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)'
       # Validate for kenetic energy (6) 
       kenetic_energy = sn.extractsingle(sol_regex, self.logfile, 6, float)

       # expected = 0.3075
       expected_lower = 0.30745
       expected_upper = 0.30755
       
       # Perform a bounded assert
       self.sanity_patterns = sn.assert_bounded(kenetic_energy, expected_lower, expected_upper)

       # Performance Testing - FOM Total Time units 's'
       # We dont set an expected value
       self.reference = {
          '*': {'Total Time': (0, None, None, 's'),}
       }

       # CloverLeaf prints the 'Wall clock' every timestep - so extract all lines matching the regex
       pref_regex = r'\s+Wall clock\s+(\S+)'
       times = sn.extractall(pref_regex,self.logfile, 1, float)

       # Use the last wall clock entry in the list (Step 87)
       self.perf_patterns = { 
               'Total Time':  times[sn.count(times) -1],
       }

