import reframe as rfm
import reframe.utility.sanity as sn
import hackathon as hack
#
#@rfm.simple_test
#class SiestaTest(hack.HackathonBase):
#    # Where to run the binaries 'aws:c6gn' on Arm or 'aws:c5n' on Intel
#    test_name = parameter( ['si64_coop', 'h2o', 'n_chain', 'carbon_nanoscroll'] ) 
#
#    valid_systems = ['aws:c6gn']
#
#    # Logging Variables
#    log_team_name = 'GarotesdePremia'
#    log_app_name = 'SIESTA'
#
#
#    executable = 'siesta'
#
#    spec = parameter([
#        'siesta@4.0.1 %gcc@10.3.0'      # Siesta GCC
#    ])
#
#    parallelism = parameter([
#        { 'nodes' : 1, 'mpi' : 4, 'omp' : 1},
#    ])
#
#    @run_after('init')
#    def get_name(self):
#        name=self.test_name
#        self.log_test_name = 'Test {} input'.format(name)
#        self.prerun_cmds = ['cp -r /home/gnuille/siesta_exec/siesta .', 'cd siesta/Tests/{}'.format(name), 'for spec in `cat {}.pseudos`; do ln ../Pseudos/$spec.psf . ; done'.format(name) ]
#        self.executable_opts = ['<', '{}.fdf'.format(name)]
#        self.logfile = 'test_{}.log'.format(name)
#        self.keep_files = [self.logfile]
#
#    @run_before('sanity')
#    def set_sanity_patterns(self):
#        self.sanity_patterns = sn.assert_found('Job completed', sn.print(self.stdout))

@rfm.simple_test
class SiestaScalabilityTest(hack.HackathonBase):

    #test_name = parameter( ['h2o_2', 'h2o_4', 'h2o_512'] ) 
    test_name = parameter( ['h2o_64'] ) 

    # Where to run the binaries 'aws:c6gn' on Arm or 'aws:c5n' on Intel
    valid_systems = ['aws:c6gn']

    # Logging Variables
    log_team_name = 'GarotesdePremia'
    log_app_name = 'SIESTA'


    executable = 'siesta'

    spec = parameter([
        'siesta@4.0.1 %gcc@10.3.0 +metis'      # Siesta GCC metis
    ])

    parallelism = parameter([
        { 'nodes' : 1, 'mpi' : 8, 'omp' : 1},
        { 'nodes' : 1, 'mpi' : 16, 'omp' : 1},
        { 'nodes' : 1, 'mpi' : 32, 'omp' : 1},
        { 'nodes' : 1, 'mpi' : 64, 'omp' : 1},
        { 'nodes' : 2, 'mpi' : 128, 'omp' : 1},
        { 'nodes' : 4, 'mpi' : 256, 'omp' : 1},
    ])

    @run_after('init')
    def get_name(self):
        name=self.test_name
        self.log_test_name = 'Scalability {} input'.format(name)
        self.prerun_cmds = ['cp -r /scratch/home/jvinyals/siesta .', 'cd siesta/Tests/{}'.format(name), 'for spec in `cat {}.pseudos`; do ln ../Pseudos/$spec.psf . ; done'.format(name) ]
        self.executable_opts = ['<', '{}.fdf'.format(name)]
        self.logfile = 'test_{}.log'.format(name)
        self.keep_files = [self.logfile]

    @run_before('sanity')
    def set_sanity_patterns(self):
        self.sanity_patterns = sn.assert_found('Job completed', sn.print(self.stdout))

    @run_before('run')
    def set_timmer(self):
        self.job.launcher.options = ['/usr/bin/time -f "Elapsed for reframe: %e"']

    @run_before('performance')
    def set_perf_pattern(self):
            self.perf_patterns = {
                    'Run Time': sn.max(sn.extractall(r'Elapsed for reframe:\s+(\S+).*', self.stderr, 1, float))
            }
