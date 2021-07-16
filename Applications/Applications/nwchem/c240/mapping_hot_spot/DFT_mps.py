import reframe as rfm
import reframe.utility.sanity as sn
import hackathon as hack
from reframe.core.launchers import LauncherWrapper
import os
import csv

@rfm.simple_test
class NWChemTest(hack.HackathonBase):
    # Where to run the binaries 'aws:c6gn' on Arm or 'aws:c5n' on Intel
    valid_systems = ['aws:c6gn']

    # Logging Variables
    log_team_name = 'QMlab'
    log_app_name = 'NWChem'
    log_test_name = 'NWchem_mps'
    log_test_type = 'profile'

    # Define test case
    # In this case we download the file from GitHub and write as clover.in - the expected input file
    prerun_cmds = ['wget -O nwchem.nw https://nwchemgit.github.io/c240_631gs.nw'] 

    # Define Execution
    # Binary to run
    executable = 'nwchem'
    # Command line options to pass
    executable_opts = ['nwchem.nw > nwchem.out']
    # Where the output is written to
    logfile = 'nwchem.out'
    # Store the output file (used for validation later)
    keep_files = [logfile]


    # Parameters - Compilers - Defined as their Spack specs (use spec or hash)
    spec = parameter([
        'nwchem@7.0.2 %gcc@10.3.0',     # CloverLeaf with the GCC compiler
#        'nwchem@7.0.2 %arm@21.0.0.879', # CloverLeaf with the Arm compiler
#        'cloverleaf@1.1 %nvhpc@21.2'      # CloverLeaf with the NVIDIA compiler
    ])

    # Parameters - MPI / Threads - Used for scaling studies
    parallelism = parameter([
        { 'nodes' : 2, 'mpi' : 128, 'omp' : 1},
    ])

    # Request exclusive nodes from slurm
    @rfm.run_before('run')
    def prepare_job(self):
       self.job.options += ['--exclusive']

    # Code validation
    @run_before('sanity')
    def set_sanity_patterns(self):

       # Use the logfile for validation testing and performance

       # Validation at step 87 (BM_short)
       sol_regex = r'\s+Total DFT energy =\s+(\S+)'
       # Validate for kinetic energy (6)
       kinetic_energy = sn.extractsingle(sol_regex, 'nwchem.out',1,float)

       # expected = -76.42192374510
       #expected_lower = float(-76.42190000000
       #expected_upper = float(-76.52192376000       

       # Perform a bounded assert
       #self.sanity_patterns = sn.assert_bounded(kinetic_energy, expected_lower, expected_upper)
       #self.sanity_patterns = sn.assert_eq(kinetic_energy, kinetic_energy)
       self.sanity_patterns=   sn.assert_reference(kinetic_energy,-9136.856741718977, lower_thres=-0.0004, upper_thres=0.0004, msg=None)

       # Performance Testing - FOM Total Time units 's'
       # We dont set an expected value
       self.reference = {
          '*': {'Total Time': (0, None, None, 's'),}
       }

       # CloverLeaf prints the 'Wall clock' every timestep - so extract all lines matching the regex
       pref_regex = r'\s+wall:\s+(\S+)+s'
       self.perf_patterns = {
               'Total Time': sn.extractsingle(pref_regex, self.logfile, 1, float, item=-1)
       }

    # Now we can retrieve the csv file and parse it for the top 10 functions
    # We log them to the `hot_spots` variable
    # This then gets logged by ReFrame
    @run_before('run')
    def set_profiler(self):
      self.proffile = 'prof.csv'
      self.keep_files.append(self.proffile)
      self.modules.append('arm-forge@21.0')
      self.job.launcher = LauncherWrapper(self.job.launcher, 'map',
                   ['--profile', '--export-functions='+self.proffile])

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
