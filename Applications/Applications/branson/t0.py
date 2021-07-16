import reframe as rfm
import reframe.utility.sanity as sn
import hackathon as hack
from reframe.core.launchers import LauncherWrapper
import os
import enum

EXCLUSIVE = True
PROFMAP = True

@enum.unique
class RunMode(enum.IntEnum):
    DEBUG_RUN = 0
    HSPOT_RUN = 1
    SSCALING_RUN = 2
    MATH_RUN = 3
    CCOMP_RUN = 4    # this run is to compare compiler flag tunings

run_mode = RunMode.DEBUG_RUN

def parselog(lines):
    perf = dict()
    # (material conservation, radiation conservation, emission energy)
    E_emi = 0
    M_con = 0
    R_con = 0
    T = 0
    for li in lines:
        if li.startswith("Material"):
            M_con = float(li.split(":")[1].strip())
            continue
        if li.startswith("Radiation"):
            R_con = float(li.split(":")[1].strip())
            continue
        if li.startswith("Emission"):
            E_emi = float(li.split(":")[1].split(",")[0].strip())
            continue
        if li.startswith("Total transport"):
            T = float(li.split(":")[1].strip())
    veri = (M_con,R_con,E_emi)
    perf["Total transport"] = T
    return (veri, perf)

# tests are as described by maintainers here: https://www.lanl.gov/projects/crossroads/_assets/docs/ssi/summary-branson.pdf
@rfm.simple_test
class BransonTest0(hack.HackathonBase):
    # Where to run the binaries 'aws:c6gn' on Arm or 'aws:c5n' on Intel
    valid_systems = ['aws:c6gn']

    # Logging Variables
    log_team_name = 'Iman'
    log_app_name = 'branson'
    log_test_name = f'test0_{run_mode}{"P" if PROFMAP else ""}'

    prerun_cmds = ['cp /home/iman/rfms/branson/proxy_small.xml ./branson.in']
    # Define Execution
    # Binary to run
    executable = 'BRANSON'
    logfile = 'branson.out'
    # Command line options to pass (validation data come from here: https://github.com/CEED/Laghos )
    executable_opts = ["./branson.in", ">", logfile]
    # Store the output file (used for validation later)
    keep_files = [logfile]

    # Parameters - Compilers - Defined as their Spack specs (use spec or hash)
    if run_mode in [RunMode.DEBUG_RUN,  RunMode.MATH_RUN, RunMode.HSPOT_RUN]:
        spec = parameter(['branson@0.82 %arm'])
    elif run_mode == RunMode.CCOMP_RUN:
        spec = parameter(['branson@0.82 %gcc /gsc3hlo','branson@3.1 %gcc /3a63qmj'],)
    else:
        spec = parameter([
            'branson@0.82 %arm',  # arm
            'branson@0.82 %gcc /gsc3hlo',  # gcc
            'branson@0.82 %nvhpc',    # nvhpc
        ])

    # Parameters - MPI / Threads - Used for scaling studies

    if run_mode == RunMode.DEBUG_RUN:
        parallelism = parameter([{'nodes': 1, 'mpi': 32, 'omp': 2}])
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
        veri, perf = parselog(lines)
        ratio0 = abs(veri[0]/veri[2])
        ratio1 = abs(veri[1]/veri[2])
        # Perform a bounded assert
        print(f"{ratio0} - {ratio1}")
        self.sanity_patterns = sn.all([sn.assert_bounded(
            ratio0, 1.0e-17, 1.0e-9), sn.assert_bounded(
            ratio1, 1.0e-17, 1.0e-9)])
        # Performance Testing - FOM Total Time units 's'
        # We dont set an expected value
        # format is (value, tolerance low, tolerance high, unit)
        self.reference = {
            '*': {'Total transport': (0, None, None, 's'),
                  }
        }
        for k in perf.keys():
            perf[k] = sn.defer(perf[k])
        self.perf_patterns = perf
