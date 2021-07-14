import reframe as rfm
import reframe.utility.sanity as sn
import hackathon as hack

class RemhosStrongScalingTestBase(hack.HackathonBase):
    valid_systems = ['aws:c6gn']
    
    log_team_name = 'C3SR'
    log_app_name = 'Remhos'

    executable = 'time -p remhos'
    
    logfile = 'remhos.out'

    keep_files = [logfile]

    spec = parameter([
        'remhos@1.0%gcc@10.3.0',
        'remhos@1.0%arm@21.0.0.879',
        'remhos@1.0%nvhpc@21.2'
    ])

    parallelism = parameter([
        { 'nodes' : 1, 'mpi' : 16, 'omp' : 1},
        { 'nodes' : 1, 'mpi' : 32, 'omp' : 1},
        { 'nodes' : 1, 'mpi' : 64, 'omp' : 1},
        { 'nodes' : 2, 'mpi' : 16, 'omp' : 1},
        { 'nodes' : 2, 'mpi' : 32, 'omp' : 1},
        { 'nodes' : 2, 'mpi' : 64, 'omp' : 1},
        { 'nodes' : 4, 'mpi' : 16, 'omp' : 1},
        { 'nodes' : 4, 'mpi' : 32, 'omp' : 1},
        { 'nodes' : 4, 'mpi' : 64, 'omp' : 1},
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
class Remhos2DRemapStrongScalingTest(RemhosStrongScalingTestBase):
    log_test_name = 'Remhos2DRemapStrongScalingTest'

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

@rfm.simple_test
class Remhos3DRemapStrongScalingTest(RemhosStrongScalingTestBase):
    log_test_name = 'Remhos3DRemapStrongScalingTest'

    prerun_cmds = ['wget https://raw.githubusercontent.com/CEED/Remhos/v1.0/data/cube01_hex.mesh']
    executable_opts = ['-m', 'cube01_hex.mesh',
                       '-p', '10',
                       '-rs', '1',
                       '-o', '2',
                       '-dt', '0.02',
                       '-tf', '0.8',
                       '-ho', '1',
                       '-lo', '4',
                       '-fct', '2',
                       '> remhos.out']

    # Code validation
    @run_before('sanity')
    def set_sanity_patterns(self):

       # Final mass: 0.1197297047
       mass_regex = r'Final mass:\s+(\S+)'
       result_mass = sn.extractsingle(mass_regex, self.logfile, 1, float)
       
       expected_mass = 0.1197297047
       expected_mass_lower = expected_mass * (1 - 1e-9)
       expected_mass_upper = expected_mass * (1 + 1e-9)

       # Max value:  0.9985405673
       max_regex = r'Max value:\s+(\S+)'
       result_max = sn.extractsingle(max_regex, self.logfile, 1, float)

       expected_max = 0.9985405673
       expected_max_lower = expected_max * (1 - 1e-9)
       expected_max_upper = expected_max * (1 + 1e-9)

       self.sanity_patterns = sn.all([
           sn.assert_bounded(result_mass, expected_mass_lower, expected_mass_upper),
           sn.assert_bounded(result_max, expected_max_lower, expected_max_upper),
       ])

@rfm.simple_test
class Remhos2DTransportStrongScalingTest(RemhosStrongScalingTestBase):
    log_test_name = 'Remhos2DTransportStrongScalingTest'

    prerun_cmds = ['wget https://raw.githubusercontent.com/CEED/Remhos/v1.0/data/periodic-square.mesh']
    executable_opts = ['-m', 'periodic-square.mesh',
                       '-p', '5',
                       '-rs', '3',
                       '-dt', '0.002',
                       '-tf', '0.8',
                       '-ho', '1',
                       '-lo', '4',
                       '-fct', '2',
                       '> remhos.out']

    # Code validation
    @run_before('sanity')
    def set_sanity_patterns(self):

       # Final mass: 0.1623263888
       mass_regex = r'Final mass:\s+(\S+)'
       result_mass = sn.extractsingle(mass_regex, self.logfile, 1, float)
       
       expected_mass = 0.1623263888
       expected_mass_lower = expected_mass * (1 - 1e-9)
       expected_mass_upper = expected_mass * (1 + 1e-9)

       # Max value:  0.7469836332
       max_regex = r'Max value:\s+(\S+)'
       result_max = sn.extractsingle(max_regex, self.logfile, 1, float)

       expected_max = 0.7469836332
       expected_max_lower = expected_max * (1 - 1e-9)
       expected_max_upper = expected_max * (1 + 1e-9)

       self.sanity_patterns = sn.all([
           sn.assert_bounded(result_mass, expected_mass_lower, expected_mass_upper),
           sn.assert_bounded(result_max, expected_max_lower, expected_max_upper),
       ])

@rfm.simple_test
class Remhos3DTransportStrongScalingTest(RemhosStrongScalingTestBase):
    log_test_name = 'Remhos3DTransportStrongScalingTest'

    prerun_cmds = ['wget https://raw.githubusercontent.com/CEED/Remhos/v1.0/data/periodic-cube.mesh']
    executable_opts = ['-m', 'periodic-cube.mesh',
                       '-p', '0',
                       '-rs', '1',
                       '-o', '2',
                       '-dt', '0.014',
                       '-tf', '8',
                       '-ho', '1',
                       '-lo', '4',
                       '-fct', '2',
                       '> remhos.out']

    # Code validation
    @run_before('sanity')
    def set_sanity_patterns(self):

       # Final mass: 0.9607429525
       mass_regex = r'Final mass:\s+(\S+)'
       result_mass = sn.extractsingle(mass_regex, self.logfile, 1, float)
       
       expected_mass = 0.9607429525
       expected_mass_lower = expected_mass * (1 - 1e-9)
       expected_mass_upper = expected_mass * (1 + 1e-9)

       # Max value:  0.767823337
       max_regex = r'Max value:\s+(\S+)'
       result_max = sn.extractsingle(max_regex, self.logfile, 1, float)

       expected_max = 0.767823337
       expected_max_lower = expected_max * (1 - 1e-9)
       expected_max_upper = expected_max * (1 + 1e-9)

       self.sanity_patterns = sn.all([
           sn.assert_bounded(result_mass, expected_mass_lower, expected_mass_upper),
           sn.assert_bounded(result_max, expected_max_lower, expected_max_upper),
       ])
