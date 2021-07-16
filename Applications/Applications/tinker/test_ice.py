import reframe as rfm
import reframe.utility.sanity as sn
import hackathon as hack

@rfm.simple_test
class TinkerTest(hack.HackathonBase):
    # Where to run the binaries 'aws:c6gn' on Arm or 'aws:c5n' on Intel
    valid_systems = ['aws:c6gn', 'aws:c5n']

    # Logging Variables
    log_team_name = 'Dogecointothemoon'
    log_app_name = 'tinker'
    log_test_name = 'ice'

    # Define Execution
    # Binary to run
    prerun_cmds = ['cp /home/s2039047/Cloud-HPC-Hackathon-2021/Applications/Applications/tinker/test/ice* .' , 'cp -r /home/s2039047/Cloud-HPC-Hackathon-2021/Applications/Applications/tinker/params ./.. ']

    # Command line options to pass
    executable_opts = [' > Kripke.out']
    # Where the output is written to
    logfile = 'Kripke.out'
    timefile = 'time.out'
    executable = 'time -p -o ' + timefile + ' dynamic.x ice 100 1.0 0.1 4 253.0 2960.0'
    # Store the output file (used for validation later)
    keep_files = [logfile, timefile]

    # Parameters - Compilers - Defined as their Spack specs (use spec or hash)
    spec = parameter([
        'tinker@8.7.1%gcc@10.3.0/dqija4h', #with openmp
        'tinker@8.7.1%gcc@10.3.0/oxk2q3c', #without openmp
        'tinker@8.7.1%arm@21.0.0.879/ynitubh',  #with openmp 
        'tinker@8.7.1%nvhpc@21.2/qszz7b5', #with openmp but seems no effect
    ])

    # Parameters - MPI / Threads - Used for scaling studies
    parallelism = parameter([
        { 'nodes' : 1, 'mpi' : 1, 'omp' : 1, },
        { 'nodes' : 1, 'mpi' : 1, 'omp' : 2, },
        { 'nodes' : 1, 'mpi' : 1, 'omp' : 4, },
        { 'nodes' : 1, 'mpi' : 1, 'omp' : 8, },
    ])

    @rfm.run_before('run')
    def prepare_job(self):
       self.job.options += ['--exclusive=user']

    @run_before('sanity')
    def set_sanity_patterns(self):
        #Validate the total energy between -8300~-8600
        energy_regex = r'Total Energy\s*(-\d+)'

        energy = sn.extractsingle(energy_regex, self.logfile, 1, float)
        expected_energy_lower = -8600
        expected_energy_upper = -8300

        self.sanity_patterns = sn.assert_bounded(energy, expected_energy_lower, expected_energy_upper)

        pref_regex = r'\s*real\s+(\S+)'
        self.reference = {
            '*': {'Total Time': (0, None, None, 's'), }
        }
        self.perf_patterns = {
            'Total Time': sn.extractsingle(pref_regex, self.stagedir + "/" + self.timefile , 1, float, item=-1)
        }
