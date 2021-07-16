import reframe as rfm
import reframe.utility.sanity as sn
import reframe.core.launchers as rcl
import hackathon as hack

@rfm.simple_test
class MiniGMGAllOptTest1GCC(hack.HackathonBase): ################################################### class name
    # Where to run the binaries 'aws:c6gn' on Arm or 'aws:c5n' on Intel
    valid_systems = ['aws:c6gn']

    # Logging Variables
    log_team_name = 'Wolfpack'
    log_app_name = 'miniGMG'
    log_test_name = 'minigmg_allopt_gcc' ############################################ test name

    # Define Execution
    # Binary to run
    executable = 'run.miniGMG'
    # Command line options to pass
    executable_opts = ['6 8 8 8 1 1 1'] #######################################################

    # Parameters - Compilers - Defined as their Spack specs (use spec or hash)
    spec = parameter([    #####################################################################
        'minigmg@local%gcc@10.3.0',
        # 'minigmg@local%nvhpc@21.2',    
        # 'minigmg@local%arm@21.0.0.879',
        # 'minigmg@qidong%gcc@10.3.0',
    ])

    # Parameters - MPI / Threads - Used for scaling studies
    parallelism = parameter([ #################################################################
        { 'nodes' : 1, 'mpi' : 1, 'omp' : 64},
        { 'nodes' : 1, 'mpi' : 1, 'omp' : 32},
        { 'nodes' : 1, 'mpi' : 1, 'omp' : 16},
        { 'nodes' : 1, 'mpi' : 1, 'omp' : 8},
        { 'nodes' : 1, 'mpi' : 1, 'omp' : 4},
        { 'nodes' : 1, 'mpi' : 1, 'omp' : 2},
        { 'nodes' : 1, 'mpi' : 1, 'omp' : 1}
    ])

    @run_before('run')
    def prepare_job(self):
        self.job.launcher = rcl.LauncherWrapper(self.job.launcher, 'time -p')
        self.job.launcher.options = ['--exclusive']

    @sn.sanity_function
    def get_time_in_sec_list(self, min_list, sec_list):
        return list(x * 60 + y
                    for x, y in sn.zip(min_list, sec_list))

    # Code validation
    @run_before('sanity')
    def set_sanity_patterns(self):
        sol_regex = r'v-cycle=(\S+),\s+norm=(\S+)\s+\((\S+)\)\ndone'
        norm_list = sn.extractall(sol_regex, self.stdout, 3, float)
        self.sanity_patterns = sn.assert_lt(sn.max(norm_list), 1e-15)

        self.reference = {
            '*': {'v-cycles Time': (0, None, None, 's'),
                  'Total Time':       (0, None, None, 's'),}
        }

        perf_regex_real = r'real\s+(\S+)'
        real = sn.extractsingle(perf_regex_real, self.stderr, 1, float)

        self.perf_patterns = {
            # 'v-cycles Time': sn.extractsingle(perf_regex_vcycles, self.stdout, 1, float),
            'Total Time': real,
        }
