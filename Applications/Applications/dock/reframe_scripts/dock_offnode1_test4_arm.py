import reframe as rfm
import reframe.utility.sanity as sn
import reframe.core.launchers as rcl
import hackathon as hack

@rfm.simple_test
class DockOffnode1Test4Arm(hack.HackathonBase): ###################################################
    # Where to run the binaries 'aws:c6gn' on Arm or 'aws:c5n' on Intel
    valid_systems = ['aws:c6gn']
    # valid_prog_environs = ['*']

    # Logging Variables
    log_team_name = 'Wolfpack'
    log_app_name = 'dock'
    log_test_name = 'dock_test4' ############################################

    # Define Execution
    # Binary to run
    executable = 'dock6.mpi'
    input_file = 'mpi3.in' #################################################
    # Command line options to pass
    executable_opts = ['-i', '/scratch/dock6/tutorials/mpi_demo/4_dock/'+input_file, '-o', 'mpi.out']#, '> miniGMG.out'] ####################################
    # Where the output is written to
    # logfile = 'miniGMG.out'
    # # Store the output file (used for validation later)
    # keep_files = [logfile]


    # Parameters - Compilers - Defined as their Spack specs (use spec or hash)
    spec = parameter([    #####################################################################
        # 'dock@6.9%gcc@10.3.0',
        'dock@6.9%arm@21.0.0.879',
        # 'dock@6.9%nvhpc@21.2',
    ])

    # Parameters - MPI / Threads - Used for scaling studies
    parallelism = parameter([ #################################################################
        { 'nodes' : 2, 'mpi' : 64, 'omp' : 1},
    ])

    @run_before('run')
    def prepare_job(self):
        self.job.launcher = rcl.LauncherWrapper(self.job.launcher, 'time -p')
        self.job.launcher.options = ['--exclusive']

    # @run_before('run')
    # def set_profiler(self):
    #     self.proffile = 'profile.map'
    #     self.keep_files = [self.proffile]

    #     # self.modules.append('arm-forge@21.0')

    #     self.job.launcher = rcl.LauncherWrapper(self.job.launcher, 'map', ['--profile', '--output='+self.proffile])

    # @run_before('run')
    # def perf_libs_tools(self):
    #     apl_dir = 'plt_out'
    #     self.prerun_cmds.append('mkdir {0}'.format(apl_dir))
    #     self.variables['ARMPL_SUMMARY_FILEROOT'] = '$PWD/{0}/'.format(apl_dir)
    #     self.keep_files = [apl_dir]

    #     self.job.launcher.options = ['--export=ALL,LD_PRELOAD=libarmpl_mp-summarylog.so']
    #     apl_file = '{0}_{1}_apl_summary.log'.format(self.log_app_name, self.log_test_name)
    #     self.postrun_cmds.append('process_summary.py {0}/*.apl > {1}'.format(apl_dir, apl_file))
    #     self.keep_files.append(apl_file)

    # /scratch/opt/spack/linux-amzn2-graviton2/gcc-10.3.0/perf-libs-tools-git-master-ja4rifwkuuj4nw2c7usikdlomimo6yxm/lib/

    # @sn.sanity_function
    # def get_time_in_sec_list(self, min_list, sec_list):
    #     return list(x * 60 + y
    #                 for x, y in sn.zip(min_list, sec_list))

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
        