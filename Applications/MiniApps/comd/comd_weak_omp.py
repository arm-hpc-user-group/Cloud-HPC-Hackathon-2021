import reframe as rfm
import reframe.utility.sanity as sn
import hackathon as hack

@rfm.simple_test
class CoMDTest(hack.HackathonBase):
    # Where to run the binaries 'aws:c6gn' on Arm or 'aws:c5n' on Intel
    valid_systems = ['aws:c6gn', 'aws:c5n']

    # Logging Variables
    log_team_name = 'Falkners'
    log_app_name = 'CoMD'
    log_test_name = 'CoMD_weak_omp'

    # Define test case
    # In this case we download the file from GitHub and write as clover.in - the expected input file
    prerun_cmds = [
        'mkdir ./pots',
        'wget -O ./pots/Cu_u6.eam https://raw.githubusercontent.com/ECP-copa/CoMD/master/pots/Cu_u6.eam'
    ]

    # Define Execution
    # Binary to run
    executable = 'CoMD-openmp'
    # Command line options to pass
    executable_opts = ['&> comd.out -e -i 1 -j 1 -k 1 -x 20 -y 20 -z 20']
    # Where the output is written to
    logfile = 'comd.out'
    # Store the output file (used for validation later)
    keep_files = [logfile]


    # Parameters - Compilers - Defined as their Spack specs (use spec or hash)
    spec = parameter([
        'comd@1.1 %gcc@10.3.0',     # CoMD with the GCC compiler
        'comd@1.1 %arm@21.0.0.879', # CoMD with the Arm compiler
        'comd@1.1 %nvhpc@21.2'      # CoMD with the NVIDIA compiler
    ])

    # Parameters - MPI / Threads - Used for scaling studies
    parallelism = parameter([
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

        # Use the logfile for validation testing and performance
        ratio_regex = r'\s+eFinal/eInitial\s+:\s+(\S+)'
        energy_ratio = sn.extractsingle(ratio_regex, self.logfile, 1, float)

        expected_lower = 0.99
        expected_upper = 1.01

        self.sanity_patterns = sn.assert_bounded(energy_ratio, expected_lower, expected_upper)

        self.reference = {
            '*': {'Total Time': (0, None, None, 's'),}
        }

        pref_regex = r'\s+total\s+1\s+(\S+)'
        self.perf_patterns = {
            'Total Time': sn.extractsingle(pref_regex, self.logfile, 1, float, item=-1)
        }
