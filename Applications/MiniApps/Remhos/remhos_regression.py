import reframe as rfm
import reframe.utility.sanity as sn
import hackathon as hack

class RemhosRegressionTestBase(hack.HackathonBase):
    valid_systems = ['aws:c6gn']
    
    log_team_name = 'C3SR'
    log_app_name = 'Remhos'

    executable = 'time -p remhos'
    
    logfile = 'remhos.out'

    keep_files = [logfile]

    spec = parameter([
        'remhos@1.0%arm@21.0.0.879/q2vad4t', # OpenBLAS w/o flag
        'remhos@1.0%arm@21.0.0.879/orhbc67', # OpenBLAS w/ cppflags="-Ofast -mcpu=native -ffast-math"
    ])

    parallelism = parameter([
        { 'nodes' : 1, 'mpi' : 1, 'omp' : 1},
        { 'nodes' : 1, 'mpi' : 2, 'omp' : 1},
        { 'nodes' : 1, 'mpi' : 4, 'omp' : 1},
        { 'nodes' : 1, 'mpi' : 8, 'omp' : 1},
        { 'nodes' : 1, 'mpi' : 16, 'omp' : 1},
        { 'nodes' : 1, 'mpi' : 32, 'omp' : 1},
        { 'nodes' : 1, 'mpi' : 64, 'omp' : 1},
    ])

    @run_before('performance')
    def set_perf_patterns(self):
        self.reference = {
            '*': {'Total Time': (0, None, None, 's'),}
        }

        perf_regex = r'real\s+(\S+)'
        self.perf_patterns = {
            'Total Time': sn.max(sn.extractall(perf_regex, self.stderr, 1, float))
        }

    @run_before('run')
    def prepare_job(self):
       self.job.options += ['--exclusive']

@rfm.simple_test
class Remhos2DRemapRegressionTest(RemhosRegressionTestBase):
    log_test_name = 'Remhos2DRemapRegressionTest'

    prerun_cmds = ['wget https://raw.githubusercontent.com/CEED/Remhos/v1.0/data/inline-quad.mesh']
    executable_opts = ['-m', 'inline-quad.mesh',
                       '-p', '14',
                       '-rs', '1',
                       '-dt', '0.001',
                       '-tf', '0.75',
                       '-ho', '1',
                       '-lo', '4',
                       '-fct', '2',
                       '> remhos.out']

    # Code validation
    @run_before('sanity')
    def set_sanity_patterns(self):

       # Final mass: 0.08479546727
       mass_regex = r'Final mass:\s+(\S+)'
       result_mass = sn.extractsingle(mass_regex, self.logfile, 1, float)
       
       expected_mass = 0.08479546727
       expected_mass_lower = expected_mass * (1 - 1e-9)
       expected_mass_upper = expected_mass * (1 + 1e-9)

       # Max value:  0.8378749205
       max_regex = r'Max value:\s+(\S+)'
       result_max = sn.extractsingle(max_regex, self.logfile, 1, float)

       expected_max = 0.8378749205
       expected_max_lower = expected_max * (1 - 1e-9)
       expected_max_upper = expected_max * (1 + 1e-9)

       self.sanity_patterns = sn.all([
           sn.assert_bounded(result_mass, expected_mass_lower, expected_mass_upper),
           sn.assert_bounded(result_max, expected_max_lower, expected_max_upper),
       ])

