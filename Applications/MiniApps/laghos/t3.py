import reframe as rfm
import reframe.utility.sanity as sn
import hackathon as hack
from reframe.core.launchers import LauncherWrapper
import os
import enum

EXCLUSIVE = True


@enum.unique
class RunMode(enum.IntEnum):
    DEFAULT_RUN = -1
    PROFILE_RUN = 0
    DEBUG_RUN = 1
    SSCALING_RUN = 2
    MATH_RUN = 3
    CCOMP_RUN = 4    # this run is to compare compiler flag tunings


run_mode = RunMode.CCOMP_RUN


def parselog(lines):
    steps = []
    perf = dict()
    for li in lines:
        if li.startswith("step"):
            chunks = li.split()
            # (step, t, dt, |e|)
            steps += [(int(chunks[1][:-1]), float(chunks[4][:-1]),
                       float(chunks[7][:-1]), float(chunks[10]))]
        if li.startswith("Major kernels total time"):
            perf["Major kernels total time"] = float(li.split(":")[1].strip())
        if li.startswith("Major kernels total rate"):
            perf["Major kernels total rate"] = float(li.split(":")[1].strip())
    return (steps, perf)

# this test is number 2 in the verification table here: https://github.com/CEED/Laghos#verification-of-results

@rfm.simple_test
class LaghosTest3(hack.HackathonBase):
    # Where to run the binaries 'aws:c6gn' on Arm or 'aws:c5n' on Intel
    valid_systems = ['aws:c6gn']

    # Logging Variables
    log_team_name = 'Iman'
    log_app_name = 'laghos'
    log_test_name = 'test3'

    # Define Execution
    # Binary to run
    executable = 'laghos'
    # Command line options to pass (validation data come from here: https://github.com/CEED/Laghos )
    executable_opts = ["-p", "0", "-dim", "3", "-rs",
                       "1", "-tf", "0.75", "-pa", ">", "laghos.out"]
    # executable_opts = []
    # Where the output is written to
    logfile = 'laghos.out'
    # Store the output file (used for validation later)
    keep_files = [logfile]

    # Parameters - Compilers - Defined as their Spack specs (use spec or hash)

    if run_mode in [RunMode.DEBUG_RUN, RunMode.PROFILE_RUN, RunMode.MATH_RUN]:
        spec = parameter(['laghos@3.1 %arm'])
    elif run_mode == RunMode.CCOMP_RUN:
        spec = parameter(['laghos@3.1 %gcc /rpvemyc'])
    else:
        spec = parameter([
            'laghos@3.1 %arm',  # arm
            'laghos@3.1 %gcc /3a63qmj',  # gcc
            'laghos@3.1 %nvhpc',    # nvhpc
        ])

    # Parameters - MPI / Threads - Used for scaling studies

    if run_mode == RunMode.DEBUG_RUN:
        parallelism = parameter([{'nodes': 1, 'mpi': 32, 'omp': 1}])
    elif run_mode == RunMode.PROFILE_RUN:
        parallelism = parameter([{'nodes': 1, 'mpi': 1, 'omp': 1},  # for serial profiling
                                {'nodes': 1, 'mpi': 64, 'omp': 1}])  # for full node profiling
    elif run_mode == RunMode.CCOMP_RUN:
        parallelism = parameter([{'nodes': 1, 'mpi': 1, 'omp': 1}, ])
    elif run_mode == RunMode.SSCALING_RUN:
        parallelism = parameter([{'nodes': 1, 'mpi': 1, 'omp': 1},
                                 {'nodes': 1, 'mpi': 4, 'omp': 1},
                                 {'nodes': 1, 'mpi': 16, 'omp': 1},
                                 {'nodes': 1, 'mpi': 64, 'omp': 1}, ])
    elif run_mode == RunMode.MATH_RUN:
        parallelism = parameter([{'nodes': 1, 'mpi': 1, 'omp': 1}])
    else:
        parallelism = parameter([
            {'nodes': 1, 'mpi': 32, 'omp': 1},
            {'nodes': 2, 'mpi': 64, 'omp': 1},
            {'nodes': 2, 'mpi': 128, 'omp': 1},
            {'nodes': 4, 'mpi': 256, 'omp': 1},
        ])

    # Request exclusive nodes from slurm
    @run_before('run')
    def prepare_job(self):
        if EXCLUSIVE:
            self.job.options += ['--exclusive']
        # profile run
        if run_mode == RunMode.PROFILE_RUN:
            # note: arm chosen for profile run
            self.proffile = 'profile.csv'
            self.keep_files.append(self.proffile)
            self.modules.append('arm-forge')
            # self.job.launcher = LauncherWrapper(self.job.launcher,'map',['--profile','--output='+self.proffile])
            self.job.launcher = LauncherWrapper(self.job.launcher, 'map', [
                                                '--profile', '--export-functions='+self.proffile])

        if run_mode == RunMode.MATH_RUN:
            # Load perf-libs-tools-module
            self.modules.append('perf-libs-tools-git')

            # Make folder to save results to
            apl_dir = 'plt_out'
            # Create the folder in pre_run cmd
            self.prerun_cmds.append('mkdir {0}'.format(apl_dir))
            # Set the Fileroot to the new folder
            self.variables['ARMPL_SUMMARY_FILEROOT'] = '$PWD/{0}/'.format(
                apl_dir)
            # Tell reframe to keep the folder after cleanup
            self.keep_files.append(apl_dir)

            # Add the LD_PRELOAD to srun
            self.job.launcher.options = [
                '--export=ALL,LD_PRELOAD=libarmpl-summarylog.so']

            # Make summary file
            apl_file = '{0}_{1}_apl_summary.log'.format(
                self.log_app_name, self.log_test_name)
            # Run post process
            self.postrun_cmds.append(
                'process_summary.py {0}/*.apl > {1}'.format(apl_dir, apl_file))
            # Keep the summary file
            self.keep_files.append(apl_file)

    # Code validation & timing (simple perf)
    @run_before('sanity')
    def set_sanity_patterns(self):
        print("setting sanity patterns...")
        lines = []
        logfile = os.path.join(self.stagedir, self.logfile)
        with open(logfile, 'rt') as fd:
            lines = fd.readlines()
        steps, perf = parselog(lines)
        # step format: (step, t, dt, |e|)
        lstep = steps[-1]
        # Perform a bounded assert
        self.sanity_patterns = sn.all([sn.assert_eq(lstep[0], 1041), sn.assert_reference(
            lstep[2], 	0.000121, -0.1, 0.1), sn.assert_reference(lstep[3], 3.3909635545e+03
, -0.1, 0.1)])
        # Performance Testing - FOM Total Time units 's'
        # We dont set an expected value
        # format is (value, tolerance low, tolerance high, unit)
        self.reference = {
            '*': {'Major kernels total time': (0, None, None, 's'),
                  'Major kernels total rate': (0, None, None, 'Mdofs x steps / s'),
                  }
        }
        for k in perf.keys():
            perf[k] = sn.defer(perf[k])
        self.perf_patterns = perf
