import reframe as rfm
import reframe.utility.sanity as sn
import hackathon as hack

@rfm.simple_test
class Amg2013Test(hack.HackathonBase):
    # Where to run the binaries 'aws:c6gn' on Arm or 'aws:c5n' on Intel
    valid_systems = ['aws:c6gn']

    # Logging Variables
    log_team_name = 'HPCNepal'
    log_app_name = 'amg2013'
    log_test_name = 'amg2013_0'

    # Define test case
    # In this case we download the file from GitHub and write as clover.in - the expected input file
    prerun_cmds = ["wget https://asc.llnl.gov/sites/asc/files/2021-01/amg2013_0.tgz","tar xzf amg2013_0.tgz"]
    # Define Execution
    # Binary to run
    executable = 'amg2013'
    # Command line options to pass
    executable_opts = ['-in', './AMG2013/test/sstruct.in.MG.FD']
    # Where the output is written to
    logfile = 'amg2013.out'
    # Store the output file (used for validation later)
    keep_files = []


    # Parameters - Compilers - Defined as their Spack specs (use spec or hash)
    spec = parameter([
        'amg2013 %gcc@10.3.0',     # MiniTri with the GCC compiler
        'amg2013 %arm@21.0.0.879', # MiniTri with the Arm compiler
        'amg2013 %nvhpc@21.2'      # MiniTri with the NVIDIA compiler
    ])

    parallelism = parameter([
        { 'nodes' : 1, 'mpi' : 1, 'omp' : 1},
        { 'nodes' : 1, 'mpi' : 1, 'omp' : 2},
        { 'nodes' : 1, 'mpi' : 1, 'omp' : 4},
        { 'nodes' : 1, 'mpi' : 1, 'omp' : 8},
        { 'nodes' : 1, 'mpi' : 1, 'omp' : 16},
        { 'nodes' : 1, 'mpi' : 1, 'omp' : 32},
        { 'nodes' : 1, 'mpi' : 1, 'omp' : 64},
    ])

    @run_before('run')
    def prepare_job(self):
       self.job.options += ['--exclusive=user']
       self.job.launcher.options = ['time']

    # Code validation
    @run_before('sanity')
    def set_sanity_patterns(self):

       # Use the logfile for validation testing and performance

       # Regex - Number of Iterations
       sol_regex = r'Final Relative Residual Norm = (\S+)'
       # Validate for Relative Residual Norm (1)
       no_of_final_rrn_count = sn.extractsingle(sol_regex, self.stdout, 1, float)

       expected_upper = 1
       expected_lower = 0

       # Perform a bounded assert
       self.sanity_patterns = sn.assert_bounded(no_of_final_rrn_count,expected_lower, expected_upper)

       # Performance Testing - FOM Total Time units 's'
       # We dont set an expected value
       self.reference = {
          '*': {'Total Time': (0, None, None, 's'),}
       }

       pref_regex = r'System Size \* Iterations \/ Solve Phase Time: (\S+)'
       self.perf_patterns = {
               'Total Time': sn.extractsingle(pref_regex, self.stdout, 1, float, item=-1)
       }
