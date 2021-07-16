import reframe as rfm
import reframe.utility.sanity as sn
import hackathon as hack
from reframe.core.launchers import LauncherWrapper
import os
import csv

@rfm.simple_test
class MiniAeroTest(hack.HackathonBase):
    # Where to run the binaries 'aws:c6gn' on Arm or 'aws:c5n' on Intel
    valid_systems = ['aws:c6gn']

    # Logging Variables
    log_team_name = 'TeamJoe'
    log_app_name = 'miniAero'
    log_test_name = 'fine-ramp'
    log_test_type = 'profile'

    # Define test case
    # In this case we download the file from GitHub and write as clover.in - the expected input file
    prerun_cmds = ['wget -O miniaero.inp https://raw.githubusercontent.com/ghe-asu/miniAero/develop/kokkos/tests/Fine_Ramp_Parallel/miniaero.inp']
    # Define Execution
    # Binary to run
    executable = 'miniAero.mpi'
    # Command line options to pass
    executable_opts = []

    logfile = 'results.0'
    keep_files = [logfile]


    # Parameters - Compilers - Defined as their Spack specs (use spec or hash)
    spec = parameter([
        'miniaero@v1.0.1 %gcc@10.3.0',     # miniAero with the GCC compiler
        'miniaero@v1.0.1/qdrynal',
        'miniaero@v1.0.1/pgcn3wa',
    ])

    # Parameters - MPI / Threads - Used for scaling studies
    parallelism = parameter([
        { 'nodes' : 1, 'mpi' : 1, 'omp' : 1},
        { 'nodes' : 1, 'mpi' : 2, 'omp' : 1},
        { 'nodes' : 1, 'mpi' : 4, 'omp' : 1},
        { 'nodes' : 1, 'mpi' : 8, 'omp' : 1},
        { 'nodes' : 1, 'mpi' : 16, 'omp' : 1},
        { 'nodes' : 1, 'mpi' : 32, 'omp' : 1},
        { 'nodes' : 1, 'mpi' : 64, 'omp' : 1},
    ])


    # Code validation
    @run_before('sanity')
    def set_sanity_patterns(self):

       # Performance Testing - FOM Total Time units 's'
       # We dont set an expected value
       self.reference = {
          '*': {'Total Time': (0, None, None, 's'),}
       }

       cell_regex = r'\s+0.0078125\s+0.140625\s+0.625\s+0.5805\s+503.96\s+(\S+)\s+(\S+)\s+(\S+)'
       energy = sn.extractsingle(cell_regex, self.logfile, 1, float)
       expected_lower = -1e-6
       expected_upper = 1e-6

       # Perform an end of calculation assert
       self.sanity_patterns = sn.assert_bounded(energy, expected_lower, expected_upper)

       pref_regex = r'...\s+Total elapsed time:\s+(\S+)'
       self.perf_patterns = {
               'Total Time': sn.extractsingle(pref_regex, self.stdout, 1, float, item=-1)
       }

    # Here we modify the launcher to use the MAP profiler, and generate a `profile.map` file
    # We tell ReFrame to stage this file back too
    @run_before('run')
    def set_profiler(self):
      self.proffile = 'profile.map'
      self.keep_files.append(self.proffile)
  
      self.modules.append('arm-forge@21.0')
   
      self.job.launcher = LauncherWrapper(self.job.launcher, 'map',
                                            ['--profile', '--output='+self.proffile])

    # Before we run, we want to add MAP to the launcher
    # But we want to export the functions list to a csv file
    @run_before('run')
    def set_profiler(self):
      self.proffile = 'prof.csv'
      self.keep_files.append(self.proffile)
      self.modules.append('arm-forge@21.0')
      self.job.launcher = LauncherWrapper(self.job.launcher, 'map',
                   ['--profile', '--export-functions='+self.proffile])



    # Here we modify the launcher to use the MAP profiler, and generate a `profile.map` file
    # We tell ReFrame to stage this file back too
    @run_before('run')
    def set_profiler(self):
      self.proffile = 'profile.map'
      self.keep_files.append(self.proffile)
  
      self.modules.append('arm-forge@21.0')
   
      self.job.launcher = LauncherWrapper(self.job.launcher, 'map',
                                            ['--profile', '--output='+self.proffile])
