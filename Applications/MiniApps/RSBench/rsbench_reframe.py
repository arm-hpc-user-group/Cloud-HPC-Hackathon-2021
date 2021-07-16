import reframe as rfm
import reframe.utility.sanity as sn
import hackathon as hack

@rfm.simple_test
class RSbenchTest(hack.HackathonBase):
    # Where to run the binaries 'aws:c6gn' on Arm or 'aws:c5n' on Intel
    valid_systems = ['aws:c6gn', 'aws:c5n']

    # Logging Variables
    log_team_name = 'DeepNeuron Purple'
    log_app_name = 'RSbench'
    log_test_name = 'openmp'

    # Define test case
    # In this case we download the file from GitHub and write as ---.in - the expected input file
    prerun_cmds = []

    # Define Execution
    # Binary to run
    executable = 'rsbench'
    # Command line options to pass
    executable_opts = []
    # Where the output is written to
    logfile = 'rsbench.out'
    # Store the output file (used for validation later)
    keep_files = [logfile]


    # Parameters - Compilers - Defined as their Spack specs (use spec or hash)
    spec = parameter([
        'rsbench@12% gcc@10.3.0',     #GCC compiler
        #'rsbench@1.1 %arm@21.0.0.879', #Intel compiler
        'rsbench@12% nvhpc@21.2'      #PGI compiler
    ])

    # Parameters - MPI / Threads - Used for scaling studies
    parallelism = parameter([
        # { 'nodes' : 1, 'mpi' : 1, 'omp' : 1}
        { 'nodes' : 1, 'mpi' : 1, 'omp' : 1},
        { 'nodes' : 1, 'mpi' : 1, 'omp' : 2},
        { 'nodes' : 1, 'mpi' : 1, 'omp' : 4},
        { 'nodes' : 1, 'mpi' : 1, 'omp' : 8},
	{ 'nodes' : 1, 'mpi' : 1, 'omp' : 16},
	{ 'nodes' : 1, 'mpi' : 1, 'omp' : 32},
	{ 'nodes' : 1, 'mpi' : 1, 'omp' : 64},
    ])


    # Code validation
    @run_before('sanity')
    def set_sanity_patterns(self):

       # Validation Testing
       self.sanity_patterns = sn.assert_found(
            r'Simulation Complete.', self.stdout)

       # Performance Testing - FOM Total Time units 's'
       # We dont set an expected value
       self.reference = {
          '*': {'Total Time': (0, None, None, 's'),}
       }

       # CloverLeaf prints the 'Wall clock' every timestep - so extract all lines matching the regex
       pref_regex = r'Runtime:\s+(\S+)'
       self.perf_patterns = {
               'Total Time': sn.extractsingle(pref_regex, self.stdout, 1, float, item=-1)
       }
