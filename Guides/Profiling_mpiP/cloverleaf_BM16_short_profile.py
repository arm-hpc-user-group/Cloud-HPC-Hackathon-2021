import reframe as rfm
import reframe.utility.sanity as sn
import hackathon as hack
from reframe.core.launchers import LauncherWrapper
import os
import csv

@rfm.simple_test
class CloverLeafTest(hack.HackathonBase):
    # Where to run the binaries
    valid_systems = ['aws:c6gn'] 

    # Logging Variables
    log_team_name = 'TeamArm'
    log_app_name = 'CloverLeaf'
    log_test_name = 'BM16_short_profile'
    log_test_type = 'profile'

    # Define test case
    prerun_cmds = ['wget -O clover.in https://raw.githubusercontent.com/UK-MAC/CloverLeaf_ref/master/InputDecks/clover_bm16_short.in']

    # Define Execution
    executable = 'clover_leaf'
    executable_opts = []

    logfile = 'clover.out'
    keep_files.append(logfile)

    # Parameters - Compilers
    spec = parameter([
        'cloverleaf@1.1 %arm@21.0.0.879'
    ])

    # Parameters - MPI / Threads
    parallelism = parameter([
        { 'nodes' : 1, 'mpi' : 64, 'omp' : 1},
    ])

    @run_before('sanity')
    def set_sanity_patterns(self):
       # Validation at step 87 (BM_short)
       # Regex - Volume   Mass   Density   Pressure   Internal Energy   Kinetic Energy   Total Energy
       sol_regex = r'\s+step:\s+87\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)'

       # Validate for kinetic energy (6) = 0.3075
       kinetic_energy = sn.extractsingle(sol_regex, self.logfile, 6, float)
       self.sanity_patterns = sn.assert_bounded(kinetic_energy, 0.30745, 0.30755)

       # Performance Testing
       self.reference = {
          '*': {'Total Time': (0, None, None, 's'),}
       }

       # Extract wall clock values
       pref_regex = r'\s+Wall clock\s+(\S+)'

       # Use last wall clock
       self.perf_patterns = { 
               'Total Time': sn.extractsingle(pref_regex, self.logfile, 1, float, item=-1)
       }


    # Profiling
    @run_before('run')
    def preload_mpiP(self):
        # Load mpiP module
        self.modules.append('mpip')

        # Store output in a folder
        mpip_output = 'mpip_output'
        self.prerun_cmds.append('mkdir "%s"' % mpip_output)
        # Configure mpiP
        self.variables['MPIP'] = '"-f %s"' % mpip_output
        # Tell reframe to keep the folder after cleanup
        self.keep_files.append(mpip_output)

        # Add the LD_PRELOAD to srun
        self.job.launcher.options = ['--export=ALL,LD_PRELOAD=libmpiP.so']
        
