import reframe as rfm
import reframe.utility.sanity as sn
import hackathon as hack
from reframe.core.launchers import LauncherWrapper
import os
import csv

@rfm.simple_test
class CloverLeafTest(hack.HackathonBase):
    # Where to run the binaries
    valid_systems = ['aws:c6g'] #, 'aws:c6gn'] 

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
        { 'nodes' : 1, 'mpi' : 32, 'omp' : 1},
        { 'nodes' : 1, 'mpi' : 64, 'omp' : 1},
    ])

    @rfm.run_before('sanity')
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
       times = sn.extractall(pref_regex,self.logfile, 1, float)

       # Use last wall clock
       self.perf_patterns = { 
               'Total Time':  times[sn.count(times) -1],
       }



    @rfm.run_before('run')
    def set_profiler(self):
      self.proffile = 'profile.map'
      self.keep_files.append(self.proffile)
  
      self.modules.append('arm-forge@21.0')
   
      self.job.launcher = LauncherWrapper(self.job.launcher, 'map',
                                            ['--profile', '--outfile='+self.proffile])


