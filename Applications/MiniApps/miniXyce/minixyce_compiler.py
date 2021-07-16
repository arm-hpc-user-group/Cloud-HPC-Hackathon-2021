import reframe as rfm
import reframe.utility.sanity as sn
import hackathon as hack

@rfm.simple_test
class MiniXyceTest(hack.HackathonBase):
    # Where to run the binaries 'aws:c6gn' on Arm or 'aws:c5n' on Intel
    valid_systems = ['aws:c6gn']

    # Logging Variables
    log_team_name = 'SGHackers'
    log_app_name = 'MiniXyce'
    log_test_name = 'short_test'

    # Define test case
    # In this case we download the file from GitHub and write as clover.in - the expected input file
    '''
    prerun_cmds = ['cp -r /scratch/opt/spack/linux-amzn2-graviton2/gcc-10.3.0/minixyce-1.0-6txjvdkxg5w6myfup6wocxhwlolawgq4/doc/tests tests' ,
                   'cp /scratch/opt/spack/linux-amzn2-graviton2/gcc-10.3.0/minixyce-1.0-6txjvdkxg5w6myfup6wocxhwlolawgq4/bin/default_params.txt default_params.txt']
    '''
    prerun_cmds = ['cp -r /home/rae/Cloud-HPC-Hackathon-2021/Applications/MiniApps/miniXyce/tests tests' ,
                    'cp /home/rae/Cloud-HPC-Hackathon-2021/Applications/MiniApps/miniXyce/tests/default_params.txt default_params.txt']

    # Define Execution
    # Binary to run
    executable = 'miniXyce.x'
    # Command line options to pass executable_opts is parametrised
    # executable_opts = ['-c tests/cir1.net > output']
    exec_opts = parameter([
        #"-c tests/cir1.net --t_start 0 --pf default_params.txt > output",
        #"-c tests/cir2.net > output",
        #"-c tests/cir3.net > output",
        #"-c tests/cir4.net > output",
        #"-c tests/cir5.net > output"
        "-c tests/cir6.net --t_start 0 --pf default_params.txt > output",
        ])

    # Where the output is written to
    logfile = 'output'
    # Store the output file (used for validation later)
    keep_files = [logfile]


    # Parameters - Compilers - Defined as their Spack specs (use spec or hash)
    spec = parameter([
        'minixyce %gcc@10.3.0' ,     # CloverLeaf with the GCC compiler
        'minixyce %arm',     # CloverLeaf with the GCC compiler
        'minixyce %nvhpc',     # CloverLeaf with the GCC compiler
#        'cloverleaf@1.1 %arm@21.0.0.879', # CloverLeaf with the Arm compiler
#        'cloverleaf@1.1 %nvhpc@21.2'      # CloverLeaf with the NVIDIA compiler
    ])

    # Parameters - MPI / Threads - Used for scaling studies
    parallelism = parameter([
        { 'nodes' : 1, 'mpi' : 64, 'omp' : 1},
         { 'nodes' : 1, 'mpi' : 32, 'omp' : 1},
         { 'nodes' : 1, 'mpi' : 16, 'omp' : 1},
         { 'nodes' : 1, 'mpi' : 8, 'omp' : 1},
         { 'nodes' : 1, 'mpi' : 4, 'omp' : 1},
         { 'nodes' : 1, 'mpi' : 2, 'omp' : 1},
         { 'nodes' : 1, 'mpi' : 1, 'omp' : 1},
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

       # Basic sanity checks
       '''
         5 Circuit_attributes:
     Number_of_devices: 6
     Resistors_(R): 2
     Inductors_(L): 1
     Capacitors_(C): 1
     '''

       sol_regex = r'\s+Number_of_devices:\s+(\S+)'
       result = sn.extractsingle(sol_regex, self.logfile, 1, int)
       self.sanity_patterns = sn.assert_bounded(result, 15001, 15001)

       sol_regex = r'\s+Resistors_\(R\):\s+(\S+)'
       result = sn.extractsingle(sol_regex, self.logfile, 1, int)
       self.sanity_patterns = sn.assert_bounded(result, 5000, 5000)
       
       sol_regex = r'\s+Inductors_\(L\):\s+(\S+)'
       result = sn.extractsingle(sol_regex, self.logfile, 1, int)
       self.sanity_patterns = sn.assert_bounded(result, 5000, 5000)

       '''
       sol_regex = r'\s+Capacitors_\(C\):\s+(\S+)'
       result = sn.extractsingle(sol_regex, self.logfile, 1, int)
       self.sanity_patterns = sn.assert_bounded(result, 5000, 5000)
       '''


       # Performance Testing - FOM Total Time units 's'
       # We dont set an expected value
       self.reference = {
          '*': {'Total Time': (0, None, None, 's'),}
       }


       # CloverLeaf prints the 'Wall clock' every timestep - so extract all lines matching the regex
       pref_regex = r'\s+Total Simulation Time:\s+(\S+)'
       self.perf_patterns = {
            'Total Time': sn.extractsingle(pref_regex, self.logfile, 1, float, item=-1)
       }


