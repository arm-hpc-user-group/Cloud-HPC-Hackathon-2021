#!/usr/bin/python
# -*- coding: utf-8 -*-
import reframe as rfm
import reframe.utility.sanity as sn
import hackathon as hack
from reframe.core.launchers import LauncherWrapper
import os
import enum

EXCLUSIVE = True
PROFMAP = False

# run with: reframe --stage /scratch/home/${USER} -c t0.py -r --performance-report --report-file report.txt
 
@enum.unique 
class RunMode(enum.IntEnum):
    DEBUG_RUN = 0
    HSPOT_RUN = 1
    SSCALING_RUN = 2
    MATH_RUN = 3
    CCOMP_RUN = 4  # this run is to compare compiler flag tunings

run_mode = RunMode.SSCALING_RUN

def parselog(lines):
    perf = dict()

    # 3 particle types: nu_e, nu_e_bar, nu_x
    # for each we track total count, escapees and absorbed

    totals = [0, 0, 0]
    esc = [0, 0, 0]
    abso = [0, 0, 0]
    MC = 0
    T = 1
    state = 0
    for li in lines:
        if 'particles' in li:
            totals[state] = int(li.split()[0].strip())
            continue
        if 'escapes' in li:
            esc[state] = int(li.split()[1].strip())
            continue
        if 'absorptions' in li:
            abso[state] = int(li.split()[2].strip())
            continue
        if 'nu_e' in li:
            state = 0
            continue
        if 'nu_e_bar' in li:
            state = 1
            continue
        if 'nu_x' in li:
            state = 2
            continue
        if li.startswith('Total number of MC steps'):
            MC = float(li.split(':')[1].strip())
        if li.startswith('real'):
            T = float(li.split(":")[1])
            # print(f"TTTTTTTTTTT:{T}")
    veri = [totals, esc, abso]
    perf['MC/s'] = MC/T
    perf['T'] = T
    return [veri, perf]


# tests are as described by maintainers here: https://www.lanl.gov/projects/crossroads/_assets/docs/ssi/summary-branson.pdf
@rfm.simple_test
class NutTest1(hack.HackathonBase):
    # Where to run the binaries 'aws:c6gn' on Arm or 'aws:c5n' on Intel
    valid_systems = ['aws:c6gn']
    # Logging Variables
    log_team_name = 'Iman'
    log_app_name = 'nut'
    log_test_name = f'test1_{run_mode}{"P" if PROFMAP else ""}'

    prerun_cmds = \
        ['wget -O nut.in https://raw.githubusercontent.com/lanl/NuT/master/test/data/p.2']

    # Define Execution
    # Binary to run
    # must do /usr/bin otherwise bash builtin time is called which sucks
    executable = '/usr/bin/time'
    logfile = 'nut.out'

    # Command line options to pass (validation data come from here: https://github.com/CEED/Laghos )
    # NOTE: notice how we do &> to redirect stderr and thus timing info to logfile as well
    executable_opts = ['-f','"real:%e"','bh-3','-n', '20000', '-i', 'nut.in', '&>', logfile]
    if run_mode == RunMode.HSPOT_RUN:
        executable = "bh-3"
        executable_opts = ['-n', '10000', '-i', 'nut.in', '>', logfile]
    # executable_opts = ['-v','bh-3','-n', '10000', '-i', 'nut.in', '&>', logfile]
    # Store the output file (used for validation later)

    keep_files = [logfile]

    # Parameters - Compilers - Defined as their Spack specs (use spec or hash)

    if run_mode in [RunMode.DEBUG_RUN, RunMode.MATH_RUN, RunMode.HSPOT_RUN]:
        spec = parameter(['nut@0.1.1 %arm'])
    elif run_mode == RunMode.CCOMP_RUN:
        spec = parameter(['nut@0.1.1 %gcc /NEW',
                         'nut@0.1.1 %gcc /ihypvrj'])
    else:
        spec = parameter(['nut@0.1.1 %arm', 'nut@0.1.1 %gcc /ihypvrj',
                         'nut@0.1.1 %nvhpc'])  # arm
                                               # gcc
                                               # nvhpc

    # Parameters - MPI / Threads - Used for scaling studies
    parallelism = parameter([{'nodes': 1, 'mpi': 1, 'omp': 1}])
    # if run_mode == RunMode.DEBUG_RUN:
    #     parallelism = parameter([{'nodes': 1, 'mpi': 32, 'omp': 1}])
    # elif run_mode == RunMode.HSPOT_RUN:
    #     parallelism = parameter([{'nodes': 1, 'mpi': 1, 'omp': 1},
    #                             {'nodes': 1, 'mpi': 64, 'omp': 1}])  # for serial profiling
    #                                                                  # for full node profiling
    # elif run_mode == RunMode.CCOMP_RUN:
    #     parallelism = parameter([{'nodes': 1, 'mpi': 1, 'omp': 1}])
    # elif run_mode == RunMode.SSCALING_RUN:
    #     parallelism = parameter([{'nodes': 1, 'mpi': 1, 'omp': 1},
    #                             {'nodes': 1, 'mpi': 4, 'omp': 1},
    #                             {'nodes': 1, 'mpi': 16, 'omp': 1},
    #                             {'nodes': 1, 'mpi': 64, 'omp': 1}])
    # elif run_mode == RunMode.MATH_RUN:
    #     parallelism = parameter([{'nodes': 1, 'mpi': 1, 'omp': 1}])

    # Request exclusive nodes from slurm

    @run_before('run')
    def prepare_job(self):
        if EXCLUSIVE:
            self.job.options += ['--exclusive']

        if PROFMAP and run_mode != RunMode.HSPOT_RUN:
            self.proffile = 'profile.map'
            self.keep_files.append(self.proffile)
            self.modules.append('arm-forge')
            self.job.launcher = LauncherWrapper(self.job.launcher, 'map'
                    , ['--profile', '--output=' + self.proffile])

        # profile run to find hotspots

        if run_mode == RunMode.HSPOT_RUN:

            # note: arm chosen for profile run

            self.proffile = 'profile.csv'
            self.keep_files.append(self.proffile)
            self.modules.append('arm-forge')
            self.job.launcher = LauncherWrapper(self.job.launcher, 'map'
                    , ['--profile', '--export-functions='
                    + self.proffile])

        if run_mode == RunMode.MATH_RUN:

            # Load perf-libs-tools-module

            self.modules.append('perf-libs-tools-git')

            # Make folder to save results to

            apl_dir = 'plt_out'

            # Create the folder in pre_run cmd

            self.prerun_cmds.append('mkdir {0}'.format(apl_dir))

            # Set the Fileroot to the new folder

            self.variables['ARMPL_SUMMARY_FILEROOT'] = \
                '$PWD/{0}/'.format(apl_dir)

            # Tell reframe to keep the folder after cleanup

            self.keep_files.append(apl_dir)

            # Add the LD_PRELOAD to srun

            self.job.launcher.options = \
                ['--export=ALL,LD_PRELOAD=libarmpl-summarylog.so']

            # Make summary file

            apl_file = \
                '{0}_{1}_apl_summary.log'.format(self.log_app_name,
                    self.log_test_name)

            # Run post process

            self.postrun_cmds.append('process_summary.py {0}/*.apl > {1}'.format(apl_dir,
                    apl_file))

            # Keep the summary file

            self.keep_files.append(apl_file)

    # Code validation & timing (simple perf)

    @run_before('sanity')
    def set_sanity_patterns(self):
        print('setting sanity patterns...')
        lines = []
        logfile = os.path.join(self.stagedir, self.logfile)
        with open(logfile, 'rt') as fd:
            lines = fd.readlines()

        # veri: totals, absorbed, escaped per each particle type
        # veri = [totals,esc,abso]
        # the number should be conserved: totals[i] = absorbed[i] + escaped[i]

        (veri, perf) = parselog(lines)

        # Perform a bounded assert

        self.sanity_patterns = sn.all([sn.assert_eq(veri[0][0],
                veri[1][0] + veri[2][0]), sn.assert_eq(veri[0][1],
                veri[1][1] + veri[2][1]), sn.assert_eq(veri[0][2],
                veri[1][2] + veri[2][2])])

        # Performance Testing - FOM Total Time units 's'
        # We dont set an expected value
        # format is (value, tolerance low, tolerance high, unit)

        self.reference = {'*': {'MC/s': (0, None, None, ''),
                                    'T':(0, None, None, 's')}}

        for k in perf.keys():
            perf[k] = sn.defer(perf[k])
        self.perf_patterns = perf
