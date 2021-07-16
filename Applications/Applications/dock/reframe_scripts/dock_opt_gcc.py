import reframe as rfm
import reframe.utility.sanity as sn
import reframe.core.launchers as rcl
import hackathon as hack

@rfm.simple_test
class Dockopt1Test1Arm(hack.HackathonBase): ###################################################
    # Where to run the binaries 'aws:c6gn' on Arm or 'aws:c5n' on Intel
    valid_systems = ['aws:c6gn']
    # valid_prog_environs = ['*']

    # Logging Variables
    log_team_name = 'Wolfpack'
    log_app_name = 'dock'
    log_test_name = 'dock_opt_test1' ############################################

    # Define Execution
    # Binary to run
    executable = 'dock6.mpi'
    input_file = 'mpi3.in' #################################################
    # Command line options to pass
    executable_opts = ['-i', '/scratch/dock6/tutorials-yh/mpi_demo/4_dock/'+input_file, '-o', 'mpi.out']#, '> miniGMG.out'] ####################################
    # Where the output is written to
    # logfile = 'miniGMG.out'
    # # Store the output file (used for validation later)
    # keep_files = [logfile]


    # Parameters - Compilers - Defined as their Spack specs (use spec or hash)
    spec = parameter([    #####################################################################
        'dock@6.9%gcc@10.3.0',
        # 'dock@6.9%arm@21.0.0.879',
        # 'dock@6.9%nvhpc@21.2',
    ])

    # Parameters - MPI / Threads - Used for scaling studies
    parallelism = parameter([ #################################################################
        { 'nodes' : 1, 'mpi' : 8, 'omp' : 1},
        { 'nodes' : 1, 'mpi' : 16, 'omp' : 1},
        { 'nodes' : 1, 'mpi' : 32, 'omp' : 1},
        { 'nodes' : 1, 'mpi' : 64, 'omp' : 1},
    ])

    @run_before('run')
    def prepare_job(self):
        self.job.launcher = rcl.LauncherWrapper(self.job.launcher, 'time -p')
        self.job.launcher.options = ['--exclusive']

    @run_before('sanity')
    def set_sanity_patterns(self):
        if self.input_file != 'mpi1.in':
            valid_regex = r'Molecule:\s+ZINC00001555\n\n\s+Anchors:\s+(\S+)\n\s+Orientations:\s+(\S+)\n\s+Conformations:\s+(\S+)\n\n\s+Grid_Score:\s+(\S+)'
            Grid_Score = sn.extractsingle(valid_regex, 'mpi.out', 4, float)
            expected_lower = -25.860000
            expected_upper = -25.830000
            self.sanity_patterns = sn.assert_bounded(Grid_Score, expected_lower, expected_upper)
        else:
            valid_regex = r'grid box quantifiers.\n\n-+\nMolecule:\s+1VRT.lig\n\n\s+Anchors:\s+(\S+)\n\s+Orientations:\s+(\S+)\n\s+Conformations:\s+(\S+)\n\n\s+Grid_Score:\s+(\S+)'
            Grid_Score = sn.extractsingle(valid_regex, 'mpi.out', 4, float)
            expected_lower = -60.900000
            expected_upper = -60.870000
            self.sanity_patterns = sn.assert_bounded(Grid_Score, expected_lower, expected_upper)

        self.reference = {
            '*': {'Total Time':       (0, None, None, 's'),}
        }

        perf_regex_real = r'real\s+(\S+)'
        real = sn.extractsingle(perf_regex_real, self.stderr, 1, float)

        self.perf_patterns = {
            'Total Time': real,
        }
        
