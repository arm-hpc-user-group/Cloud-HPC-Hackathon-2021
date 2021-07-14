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
    log_test_name = 'BM16_short_hotspot'
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
       perf_regex = r'\s+Wall clock\s+(\S+)'

       # Use last wall clock
       self.perf_patterns = { 
               'Total Time': sn.extractsingle(perf_regex, self.logfile, 1, float, item=-1)
       }

    # Before we run, we want to add MAP to the launcher
    # But we want to export the functions list to a csv file
    @run_before('run')
    def set_profiler(self):
      self.proffile = 'prof.csv'
      self.keep_files.append(self.proffile)
      self.modules.append('arm-forge@21.0')
      self.job.launcher = LauncherWrapper(self.job.launcher, 'map',
                   ['--profile', '--export-functions='+self.proffile])


    # Now we can retrieve the csv file and parse it for the top 10 functions
    # We log them to the `hot_spots` variable
    # This then gets logged by ReFrame
    @run_before('sanity')
    def get_prof_data(self):
        self.hot_spots = []
        file_path = os.path.join(self.stagedir, self.proffile)
        with open(file_path, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            next(reader, None) # Skip Header
            for index, row in zip(range(10), reader):
               self.hot_spots.append(
                       {
                           "position" : index, 
                           "name" : row[7], 
                           "percent" : row[2], 
                           "mpi_percent" : row[4]
                        })

