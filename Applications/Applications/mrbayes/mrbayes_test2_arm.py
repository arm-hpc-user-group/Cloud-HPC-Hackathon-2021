import reframe as rfm
import reframe.utility.sanity as sn
import hackathon as hack

@rfm.simple_test
class MrBayesTest(hack.HackathonBase):
    # Where to run the binaries 'aws:c6gn' on Arm or 'aws:c5n' on Intel
    valid_systems = ['aws:c6gn']

    # Logging Variables
    log_team_name = 'Dogecointothemoon'
    log_app_name = 'MrBayes'
    log_test_name = 'case2_arm'

    timefile = 'time.out'

    # Define Execution
    # Binary to run
    # examl -t ../49.tree -m PSR -s ../49.unpartitioned.binary -n T1
    executable = 'time -p -o ' + timefile + ' mb'
    # Command line options to pass
    # executable_opts = ['/home/peize/mrbayes-test/cynmix.nex > output.out']
    executable_opts = ['/home/peize/mrbayes-test/kim.nex > output.out']
    # executable_opts = ['/home/peize/mrbayes-test/hym.nex > output.out']
    # executable_opts = ['/home/peize/mrbayes-test/primates.nex > output.out']
    # Where the output is written to
    logfile = 'output.out'
    # Store the output file (used for validation later)
    keep_files = [logfile, timefile]

    # Parameters - Compilers - Defined as their Spack specs (use spec or hash)
    spec = parameter([
        # 'mrbayes@3.2.7a%gcc@10.3.0/ly2t2fo',
        'mrbayes@3.2.7a%arm@21.0.0.879/qxbrwxu',
    ])

    # Parameters - MPI / Threads - Used for scaling studies
    parallelism = parameter([
        { 'nodes' : 1, 'mpi' : 1, 'omp' : 1, 'extra-cmd': '1,1,1'},
        { 'nodes' : 1, 'mpi' : 2, 'omp' : 1, 'extra-cmd': '1,1,2'},
        { 'nodes' : 1, 'mpi' : 4, 'omp' : 1, 'extra-cmd': '1,1,4'},
        { 'nodes' : 1, 'mpi' : 8, 'omp' : 1, 'extra-cmd': '1,2,4'},
        { 'nodes' : 1, 'mpi' : 16, 'omp' : 1, 'extra-cmd': '1,4,4'},
        { 'nodes' : 1, 'mpi' : 32, 'omp' : 1, 'extra-cmd': '2,4,4'},
        { 'nodes' : 1, 'mpi' : 64, 'omp' : 1, 'extra-cmd': '4,4,4'},
        { 'nodes' : 2, 'mpi' : 128, 'omp' : 1, 'extra-cmd': '4,4,8'},
        { 'nodes' : 4, 'mpi' : 256, 'omp' : 1, 'extra-cmd': '4,8,8'},
    ])

    @run_before('run')
    def set_config(self):
        # self.executable_opts.append('--procs')
        self.executable_opts.append(self.parallelism['extra-cmd'])

    @run_before('run')
    def prepare_job(self):
       self.job.options += ['--exclusive=user']

    @run_before('sanity')
    def set_sanity_patterns(self):
        #Validate the particle in the last iter
        # particle_regex = r'      TOTAL   (-?\d+)(\.\d+)        (-?\d+)(\.\d+)'
        # particle = sn.extractsingle(particle_regex, self.logfile, 1, float)
        # expected_particle_lower = particle * 1.05
        # expected_particle_upper = particle * 0.95
        # self.sanity_patterns = sn.assert_bounded(particle, expected_particle_lower, expected_particle_upper)

        # Time prints the real time so extract it.
        pref_regex = r'\s*real\s+(\S+)'
        self.perf_patterns = {
            'Total Time': sn.extractsingle(pref_regex, self.stagedir + "/" + self.timefile, 1, float, item=-1)
        }
