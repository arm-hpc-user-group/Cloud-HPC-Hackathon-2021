import reframe as rfm
import reframe.utility.sanity as sn
import hackathon as hack

@rfm.simple_test
class MiniViteTest(hack.HackathonBase):
    # Where to run the binaries 'aws:c6gn' on Arm or 'aws:c5n' on Intel
    valid_systems = ['aws:c6gn']

    # Logging Variables
    log_team_name = 'GarotesdePremia'
    log_app_name = 'miniVite'
    log_test_name = 'N 1000000'

    # Define Execution
    # Binary to run
    executable = 'miniVite'
    # Command line options to pass
    executable_opts = ['-n 1000000']
    # Where the output is written to
    logfile = 'minivite.out'
    # Store the output file (used for validation later)
    keep_files = [logfile]


    # Parameters - Compilers - Defined as their Spack specs (use spec or hash)
    spec = parameter([
        'minivite@1.1 %gcc@10.3.0',     # Minivite with the GCC compiler
        'minivite@1.1 %arm@21.0.0.879', # Minivite with the Arm compiler
        'minivite@1.1 %nvhpc@21.2'      # Minivite with the NVIDIA compiler
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

    @run_before('sanity')
    def set_sanity_patterns(self):
        self.sanity_patterns = sn.assert_found('Modularity', sn.print(self.stdout))


    @run_before('performance')
    def set_perf_pattern(self):
        self.perf_patterns = {
                'Run Time': sn.extractsingle(r'.*Time \(in s\):\s+(\S+).*', self.stdout, 1, float)}
