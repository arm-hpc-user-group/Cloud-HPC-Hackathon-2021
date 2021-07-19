import os

os.environ['FI_EFA_FORK_SAFE'] = '1'

import reframe as rfm
import reframe.utility.sanity as sn
import hackathon as hack
from reframe.core.launchers import LauncherWrapper
import os
import csv

@rfm.simple_test
class PICSARliteTest(hack.HackathonBase):

    # Where to run the binaries 'aws:c6gn' on Arm or 'aws:c5n' on Intel
    valid_systems = ['aws:c5n' if os.uname().machine == 'x86_64' else 'aws:c6gn']

    # Logging Variables
    log_team_name = 'TeamEPCC'
    log_app_name = 'PICSARlite'
    log_test_name = 'test'
    #log_test_type = 'profile'

    # Define test case
    # In this case we download the file from GitHub and write as picsarlite.in - the expected input file
    prerun_cmds = [
        'wget --quiet -O picsarlite.in https://raw.githubusercontent.com/ECP-WarpX/picsar/348830b444c65ca305aa3f89cd72fef7c65abd7d/examples/example_decks_fortran/test.pixr',
        'touch prof.csv',
    ]

    # Define Execution
    # Binary to run
    executable = 'picsar'
    # Command line options to pass
    executable_opts = ["picsarlite.in"]
    # Where the output is written to
    logfile = 'picsarlite.out'
    # Store the output file (used for validation later)
    keep_files = [logfile]

    # Parameters - Compilers - Defined as their Spack specs (use spec or hash)
    spec = parameter([
            'picsarlite/x4t2nz4', #'picsarlite@0.1%gcc@10.3.0',
            'picsarlite@0.1%arm@21.0.0.879', 
            'picsarlite@0.1%nvhpc@21.2'      
    ])

    # Parameters - MPI / Threads - Used for scaling studies
    my_parallelism = [
            { 'nodes' : 1, 'mpi' : 1, 'omp' : 64},
            { 'nodes' : 1, 'mpi' : 1, 'omp' : 32},
            { 'nodes' : 1, 'mpi' : 1, 'omp' : 16},
            { 'nodes' : 1, 'mpi' : 1, 'omp' : 8},
            { 'nodes' : 1, 'mpi' : 1, 'omp' : 4},
            { 'nodes' : 1, 'mpi' : 1, 'omp' : 2},
            { 'nodes' : 1, 'mpi' : 1, 'omp' : 1},
            #
            { 'nodes' : 1, 'mpi' : 2, 'omp' : 1},
            { 'nodes' : 1, 'mpi' : 4, 'omp' : 1},
            { 'nodes' : 1, 'mpi' : 8, 'omp' : 1},
            { 'nodes' : 1, 'mpi' : 16, 'omp' : 1},
            { 'nodes' : 1, 'mpi' : 32, 'omp' : 1},
            { 'nodes' : 1, 'mpi' : 64, 'omp' : 1},
            #
            { 'nodes' : 1, 'mpi' : 2, 'omp' : 32},
            { 'nodes' : 1, 'mpi' : 4, 'omp' : 16},
            { 'nodes' : 1, 'mpi' : 8, 'omp' : 8},
            { 'nodes' : 1, 'mpi' : 16, 'omp' : 4},
            { 'nodes' : 1, 'mpi' : 32, 'omp' : 2},
            #
            { 'nodes' : 2, 'mpi' : 32, 'omp' : 4},
            { 'nodes' : 4, 'mpi' : 64, 'omp' : 4},
            { 'nodes' : 8, 'mpi' : 128, 'omp' : 4},
    ] if 'aws:c6gn' in valid_systems else [
            { 'nodes' : 1, 'mpi' : 1, 'omp' : 72},
            { 'nodes' : 1, 'mpi' : 1, 'omp' : 36},
            { 'nodes' : 1, 'mpi' : 1, 'omp' : 18},
            { 'nodes' : 1, 'mpi' : 1, 'omp' : 9},
            { 'nodes' : 1, 'mpi' : 1, 'omp' : 3},
            { 'nodes' : 1, 'mpi' : 1, 'omp' : 1},
            #
            { 'nodes' : 1, 'mpi' : 1, 'omp' : 1},
            { 'nodes' : 1, 'mpi' : 3, 'omp' : 1},
            { 'nodes' : 1, 'mpi' : 9, 'omp' : 1},
            { 'nodes' : 1, 'mpi' : 18, 'omp' : 1},
            { 'nodes' : 1, 'mpi' : 36, 'omp' : 1},
            { 'nodes' : 1, 'mpi' : 72, 'omp' : 1},
            # 
            { 'nodes' : 1, 'mpi' : 2, 'omp' : 36},
            { 'nodes' : 1, 'mpi' : 4, 'omp' : 18},
            { 'nodes' : 1, 'mpi' : 8, 'omp' : 9},
            { 'nodes' : 1, 'mpi' : 9, 'omp' : 8},
            { 'nodes' : 1, 'mpi' : 18, 'omp' : 4},
            { 'nodes' : 1, 'mpi' : 36, 'omp' : 2},
            #
            { 'nodes' : 2, 'mpi' : 16, 'omp' : 9},
            { 'nodes' : 4, 'mpi' : 32, 'omp' : 9},
            { 'nodes' : 8, 'mpi' : 64, 'omp' : 9},
    ]

    parallelism = parameter(my_parallelism)

    @run_before('run')
    def prepare_job(self):
        self.job.options += ['--exclusive']

    @run_before('sanity')
    def set_sanity_patterns(self):
        # simple check: make sure to find 21x "Fields dump in", indicating 21 iterations
        num_messages = sn.len(sn.findall(r'\s+Fields\s+dump\s+in\s+', self.stdout)) 
        self.sanity_patterns = sn.assert_eq(num_messages, 21)

        # Performance Testing
        # We dont set an expected value
        self.reference = {
           '*': {'Total runtime': (0, None, None, 's'),}
        }

        # Total runtime
        perf_regex = r'Total\s+runtime\s+on\s+\d+\s+CPUS\s+=\s+(\S+)'
        self.perf_patterns = {
                'Total runtime': sn.extractsingle(perf_regex, self.stderr, 1, float, item=-1)
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
