import reframe as rfm
import reframe.utility.sanity as sn
import hackathon as hack

@rfm.simple_test
class MiniTriTest(hack.HackathonBase):
    # Where to run the binaries 'aws:c6gn' on Arm or 'aws:c5n' on Intel
    valid_systems = ['aws:c6gn','aws:c5n']

    # Logging Variables
    log_team_name = 'HPCNepal'
    log_app_name = 'miniTri'
    log_test_name = 'ca-GrQc'

    # Define test case
    # In this case we download the file from GitHub and write as clover.in - the expected input file
    prerun_cmds = ["wget https://sparse.tamu.edu/MM/SNAP/ca-GrQc.tar.gz","tar xzf ca-GrQc.tar.gz"]
    # Define Execution
    # Binary to run
    executable = 'miniTri.exe'
    # Command line options to pass
    executable_opts = ['./ca-GrQc/ca-GrQc.mtx']
    # Where the output is written to
    logfile = 'miniTri.out'
    # Store the output file (used for validation later)
    keep_files = []


    # Parameters - Compilers - Defined as their Spack specs (use spec or hash)
    spec = parameter([
        'minitri %gcc@10.3.0',     # MiniTri with the GCC compiler
        'minitri %arm@21.0.0.879', # MiniTri with the Arm compiler
        'minitri %nvhpc@21.2'      # MiniTri with the NVIDIA compiler
    ])

    parallelism = parameter([
        { 'nodes' : 1, 'mpi' : 1, 'omp' : 1}
    ])

    @run_before('run')
    def prepare_job(self):
       self.job.options += ['--exclusive=user']
       self.job.launcher.options = ['time']

    # Code validation
    @run_before('sanity')
    def set_sanity_patterns(self):

       # Use the logfile for validation testing and performance

       # Validation at step 87 (BM_short)
       # Regex - Number of Trianlges
       sol_regex = r'Number of Triangles:\s+(\S+)'
       # Validate for Total number of triangles (1)
       no_of_triangle_count = sn.extractsingle(sol_regex, self.stdout, 1, float)

       expected = 48283

       # Perform a bounded assert
       self.sanity_patterns = sn.assert_eq(no_of_triangle_count,expected)

       # Performance Testing - FOM Total Time units 's'
       # We dont set an expected value
       self.reference = {
          '*': {'Total Time': (0, None, None, 's'),}
       }

       pref_regex = r'TIME - Time to compute C = L\*B:\s+(\S+)'
       self.perf_patterns = {
               'Total Time': sn.extractsingle(pref_regex, self.stdout, 1, float, item=-1)
       }
