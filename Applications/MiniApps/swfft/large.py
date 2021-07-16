import reframe as rfm
import reframe.utility.sanity as sn
import hackathon as hack
import os


@rfm.simple_test
class SWFFTTest(hack.HackathonBase):
    # Where to run the binaries 'aws:c6gn' on Arm or 'aws:c5n' on Intel
    valid_systems = ['aws:c6gn']

    # Logging Variables
    log_team_name = 'ElkNet'
    log_app_name = 'SWFFT'
    log_test_name = 'SWFFT-LARGE'

    # Define test case
    # In this case we download the file from GitHub and write as clover.in - the expected input file
    # prerun_cmds = ['wget -O clover.in https://raw.githubusercontent.com/UK-MAC/CloverLeaf_ref/master/InputDecks/clover_bm16_short.in']

    # Define Execution
    # Where the output is written to
    logfile = 'TestDfft.out'
    timefile = 'time.out'
    # Binary to run
    executable = 'time -p -o ' + timefile + ' TestDfft'
    # Command line options to pass
    executable_opts = ['5 1024 > ' + logfile]
    # Store the output files (used for validation later)
    keep_files = [logfile, timefile]

    # Parameters - Compilers - Defined as their Spack specs (use spec or hash)
    spec = parameter([
        'swfft@1.0%gcc@10.3.0',      # SWFFT with the GCC compiler
        'swfft@1.0%arm@21.0.0.879',  # SWFFT with the Arm compiler
        'swfft@1.0%nvhpc@21.2'       # SWFFT with the NVIDIA compiler
    ])

    # Parameters - MPI / Threads - Used for scaling studies
    parallelism = parameter([
        {'nodes': 1, 'mpi': 32, 'omp': 1},
        {'nodes': 1, 'mpi': 64, 'omp': 1},
        {'nodes': 2, 'mpi': 128, 'omp': 1},
        {'nodes': 4, 'mpi': 256, 'omp': 1},
    ])

    # Request exclusive nodes from slurm
    @run_before('run')
    def prepare_job(self):
        self.job.options += ['--exclusive']

    # Code validation
    @run_before('sanity')
    def set_sanity_patterns(self):
        # Use the logfile for validation testing and performance

        # Validation regex
        sol_regex = r'^(?!(FORWARD|BACKWARD|Initializing|distribution)).*$'

        # Validate the output (without the timings)
        script_path = os.path.dirname(__file__)
        expected_output = sn.extractall(
            sol_regex, script_path + "/reference-large.txt")
        output = sn.extractall(sol_regex, self.stagedir + "/" + self.logfile)

        # Perform a bounded assert
        self.sanity_patterns = sn.assert_eq(output, expected_output, msg=None)

        # Performance Testing - FOM Total Time units 's'
        # We dont set an expected value
        self.reference = {
            '*': {'Total Time': (0, None, None, 's'), }
        }

        # Time prints the real time so extract it.
        pref_regex = r'\s*real\s+(\S+)'
        self.perf_patterns = {
            'Total Time': sn.extractsingle(pref_regex, self.stagedir + "/" + self.timefile, 1, float, item=-1)
        }
