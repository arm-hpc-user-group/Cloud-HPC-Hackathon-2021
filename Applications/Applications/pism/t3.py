import reframe as rfm
import reframe.utility.sanity as sn
import hackathon as hack
from reframe.core.launchers import LauncherWrapper
import os
import enum

EXCLUSIVE = True
PROFMAP = False

@enum.unique
class RunMode(enum.IntEnum):
    DEBUG_RUN = 0
    HSPOT_RUN = 1
    SSCALING_RUN = 2
    MATH_RUN = 3
    CCOMP_RUN = 4    # this run is to compare compiler flag tunings

run_mode = RunMode.SSCALING_RUN

def parselog(lines):
    perf = dict()
    # lines = lines[-7:]
    # (material conservation, radiation conservation, emission energy)
    rel_err = 1.0
    T = 0
    for i,li in enumerate(lines):
        if "relmaxETA" in li:
            rel_err = float(lines[i+1].split()[-1].strip())
            continue
        if li.startswith('real'):
            T = float(li.split(":")[1])
    veri = rel_err
    perf["Total time"] = T
    return (veri, perf)

# tests are as described by maintainers here: https://www.lanl.gov/projects/crossroads/_assets/docs/ssi/summary-branson.pdf
@rfm.simple_test
class PismTest3(hack.HackathonBase):
    # Where to run the binaries 'aws:c6gn' on Arm or 'aws:c5n' on Intel
    valid_systems = ['aws:c6gn']

    # Logging Variables
    log_team_name = 'Iman'
    log_app_name = 'pism'
    log_test_name = f'test3_{run_mode}{"P" if PROFMAP else ""}'

    # Define Execution
    # Binary to run
    executable = '/usr/bin/time'
    logfile = 'pismv.out'
    executable_opts = ['-f','"real:%e"','pismv','-test', 'D', '-Mx', '61','-Mz','11',
    '-y','25000','&>', logfile]
    # Store the output file (used for validation later)
    keep_files = [logfile]

    # Parameters - Compilers - Defined as their Spack specs (use spec or hash)
    if run_mode in [RunMode.DEBUG_RUN,  RunMode.MATH_RUN, RunMode.HSPOT_RUN]:
        spec = parameter(['pism@1.1.4 %gcc'])
    elif run_mode == RunMode.CCOMP_RUN:
        spec = parameter(['pism@1.1.4 %gcc /NEW'],)
    else:
        spec = parameter([
            'pism@1.1.4 %arm',  # arm
            'pism@1.1.4 %gcc /cijv4kn',  # gcc
            'pism@1.1.4 %nvhpc',    # nvhpc
        ])

    # Parameters - MPI / Threads - Used for scaling studies

    if run_mode == RunMode.DEBUG_RUN:
        parallelism = parameter([{'nodes': 1, 'mpi': 1, 'omp': 1}])
    elif run_mode == RunMode.HSPOT_RUN:
        parallelism = parameter([{'nodes': 1, 'mpi': 1, 'omp': 1},  # for serial profiling
                                {'nodes': 1, 'mpi': 64, 'omp': 1}])  # for full node profiling
    elif run_mode == RunMode.CCOMP_RUN:
        parallelism = parameter([{'nodes': 1, 'mpi': 1, 'omp': 1}])
    elif run_mode == RunMode.SSCALING_RUN:
        parallelism = parameter([{'nodes': 1, 'mpi': 1, 'omp': 1},
                                 {'nodes': 1, 'mpi': 4, 'omp': 1},
                                 {'nodes': 1, 'mpi': 16, 'omp': 1},
                                 {'nodes': 1, 'mpi': 64, 'omp': 1}, ])
    elif run_mode == RunMode.MATH_RUN:
        parallelism = parameter([{'nodes': 1, 'mpi': 1, 'omp': 1}])

    # Request exclusive nodes from slurm
    @run_before('run')
    def prepare_job(self):
        if EXCLUSIVE:
            self.job.options += ['--exclusive']
        
        if PROFMAP and run_mode != RunMode.HSPOT_RUN:
            self.proffile = 'profile.map'
            self.keep_files.append(self.proffile)
            self.modules.append('arm-forge')
            self.job.launcher = LauncherWrapper(self.job.launcher,'map',['--profile','--output='+self.proffile])
  
        # profile run to find hotspots
        if run_mode == RunMode.HSPOT_RUN:
            # note: arm chosen for profile run
            self.proffile = 'profile.csv'
            self.keep_files.append(self.proffile)
            self.modules.append('arm-forge')
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
            self.variables['ARMPL_SUMMARY_FILEROOT'] = '$PWD/{0}/'.format(apl_dir)
            # Tell reframe to keep the folder after cleanup
            self.keep_files.append(apl_dir)

            # Add the LD_PRELOAD to srun
            self.job.launcher.options = ['--export=ALL,LD_PRELOAD=libarmpl-summarylog.so']

            # Make summary file
            apl_file = '{0}_{1}_apl_summary.log'.format(self.log_app_name, self.log_test_name)
            # Run post process
            self.postrun_cmds.append('process_summary.py {0}/*.apl > {1}'.format(apl_dir, apl_file))
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
        # veri: (material conservation, radiation conservation, emission energy)
        rel_err, perf = parselog(lines)

        # Perform a error check
        self.sanity_patterns = sn.assert_lt(rel_err,0.15)
        # Performance Testing - FOM Total Time units 's'
        # We dont set an expected value
        # format is (value, tolerance low, tolerance high, unit)
        self.reference = {
            '*': {'Total time': (0, None, None, 's'),
                  }
        }
        for k in perf.keys():
            perf[k] = sn.defer(perf[k])
        self.perf_patterns = perf
