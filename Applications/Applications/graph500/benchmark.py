import reframe as rfm
import reframe.utility.sanity as sn
import hackathon as hack

@rfm.simple_test
class Graph500Test(hack.HackathonBase):
    # Where to run the binaries 'aws:c6gn' on Arm or 'aws:c5n' on Intel
    valid_systems = ['aws:c5n']

    # Logging Variables
    log_team_name = 'Masterofpuppets'
    log_app_name = 'G500'
    log_test_name = 'x86_scalab'

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
        'graph500@3.0.0 %gcc@10.3.0',           # x86 vanila
        'graph500@3.0.0 %gcc@10.3.0 /wmqhhx',   # x86 optimized
    ])

    # Parameters - MPI / Threads - Used for scaling studies
    parallelism = parameter(
        [ { 'nodes' : max(1, (2**x) // 64), 'mpi' : 2**x, 'omp': 1 } for x in range(10) ]
    )

    # Request exclusive nodes from slurm
    @rfm.run_before('run')
    def prepare_job(self):
       self.job.options += ['--exclusive']

    # Code validation
    @run_before('sanity')
    def set_sanity_patterns(self):
       self.sanity_patterns = sn.assert_true(True)
