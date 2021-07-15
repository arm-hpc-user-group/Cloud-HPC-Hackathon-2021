import reframe as rfm
import reframe.utility.sanity as sn
import hackathon as hack

@rfm.simple_test
class CosmoFlowTest(hack.HackathonBase):
    # Where to run the binaries 'aws:c6gn' on Arm or 'aws:c5n' on Intel
    valid_systems = ['aws:c6gn']

    # Logging Variables
    log_team_name = 'SGHackers'
    log_app_name = 'cosmoflow'
    log_test_name = 'short_test'

    # Define test case
    # In this case we download the file from GitHub and write as clover.in - the expected input file
    
    prerun_cmds = ['cp -r /home/malaithannir/Cloud-HPC-Hackathon-2021/Applications/Applications/cosmoflow-benchmark/src src', 'spack load py-tensorflow-estimator%gcc@10.3.0', 'spack load py-wandb%gcc@10.3.0', 'spack load py-promise%gcc@10.3.0', 'spack load py-setuptools%gcc@10.3.0', 'spack load py-pathtools', 'spack load cosmoflow-benchmark%gcc@10.3.0/oz44zmc']
    

    # Define Execution
    # Binary to run
    executable = f'time python3 src/train.py > output'
    # Command line options to pass executable_opts is parametrised
    #executable_opts = ['configs/cosmo.yaml']

    # Where the output is written to
    logfile = 'output'
    # Store the output file (used for validation later)
    keep_files = [logfile]

    exec_opts = parameter(["src/cosmo.yaml",])

    # Parameters - Compilers - Defined as their Spack specs (use spec or hash)
    spec = parameter([
        '^cosmoflow-benchmark/oz44zmc %gcc@10.3.0'     # CloverLeaf with the GCC compiler
     #   'minixyce %arm'     # CloverLeaf with the GCC compiler
#        'cloverleaf@1.1 %arm@21.0.0.879', # CloverLeaf with the Arm compiler
#        'cloverleaf@1.1 %nvhpc@21.2'      # CloverLeaf with the NVIDIA compiler
    ])

    # Parameters - MPI / Threads - Used for scaling studies
    parallelism = parameter([
        #{ 'nodes' : 1, 'mpi' : 64, 'omp' : 1},
        # { 'nodes' : 1, 'mpi' : 32, 'omp' : 1},
        # { 'nodes' : 1, 'mpi' : 16, 'omp' : 1},
         { 'nodes' : 1, 'mpi' : 4, 'omp' : 8},
        # { 'nodes' : 2, 'mpi' : 128, 'omp' : 1},
        # { 'nodes' : 4, 'mpi' : 256, 'omp' : 1},
        # { 'nodes' : 8, 'mpi' : 512, 'omp' : 1},
    ])
 

    @run_before('run')
    def set_executable_opts(self):
        self.executable_opts = [self.exec_opts]

    # Code validation
    @run_before('sanity')
    def set_sanity_patterns(self):

       # Use the logfile for validation testing and performance

       # Validation at step 87 (BM_short)
       # Regex - Volume   Mass   Density   Pressure   Internal Energy   Kinetic Energy   Total Energy
       # sol_regex = r'\s+step:\s+87\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)'
       # Validate for kinetic energy (6)
       # result = sn.extractsingle(sol_regex, self.logfile, 6, float)

       expected = 0.3075
       expected_lower = 0.30745
       expected_upper = 0.30755

       # Perform a bounded assert
       self.sanity_patterns = sn.assert_bounded(expected, expected_lower, expected_upper)

       # Performance Testing - FOM Total Time units 's'
       # We dont set an expected value
       self.reference = {
          '*': {'Total Time': (1.2, None, None, 's'),}
       }


       # CloverLeaf prints the 'Wall clock' every timestep - so extract all lines matching the regex
       #pref_regex = r'\s+Total Simulation Time:\s+(\S+)'
       #self.perf_patterns = {
       #     'Total Time': sn.extractsingle(pref_regex, self.logfile, 1, float, item=-1)
       #}


