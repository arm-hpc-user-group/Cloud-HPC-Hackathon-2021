import reframe as rfm
import reframe.utility.sanity as sn
import hackathon as hack

@rfm.simple_test
class QuantumEspressoTest(hack.HackathonBase):
    # Where to run the binaries 'aws:c6gn' on Arm or 'aws:c5n' on Intel
    valid_systems = ['aws:c6gn']

    # Logging Variables
    log_team_name = 'TeamPhoenix'
    log_app_name = 'Quantum Espresso'
    log_test_name = 'Test'

    # Define test case
    # In this case we download the file from GitHub and write as ausurf.in - the expected input file
    prerun_cmds = ['wget -O ausurf.in https://raw.githubusercontent.com/electronic-structure/benchmarks/master/Si63Ge-scf/pw.in']

    # Define Execution
    # Binary to run
    executable = 'quantum-espresso'
    # Command line options to pass
    executable_opts = []
    # Where the output is written to
    logfile = 'quantum-espresso.out'
    # Store the output file (used for validation later)
    keep_files = [logfile]


    # Parameters - Compilers - Defined as their Spack specs (use spec or hash)
    spec = parameter([
        'quantum-espresso@6.7 %gcc@10.3.0',     # with the GCC compiler
        'quantum-espresso@6.7 %arm@21.0.0.879', # with the Arm compiler
        'quantum-espresso@6.7 %nvhpc@21.2'      # with the NVIDIA compiler
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

    # https://github.com/QEF/benchmarks/blob/master/small-benchmarks/benchmark-results.txt


    # Code validation
    @run_before('sanity')
    def set_sanity_patterns(self):

       # Use the logfile for validation testing and performance

       # Validation at step 87 (BM_short)
       # Regex - Volume   Mass   Density   Pressure   Internal Energy   Kinetic Energy   Total Energy
       sol_regex = r'\s+step:\s+87\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)'
       # Validate for kinetic energy (6)
       kinetic_energy = sn.extractsingle(sol_regex, self.logfile, 6, float)

       # expected = 0.3075
       expected_lower = 0.30745
       expected_upper = 0.30755

       # Perform a bounded assert
       self.sanity_patterns = sn.assert_bounded(kinetic_energy, expected_lower, expected_upper)

       # Performance Testing - FOM Total Time units 's'
       # We dont set an expected value
       self.reference = {
          '*': {'Total Time': (0, None, None, 's'),}
       }

       # CloverLeaf prints the 'Wall clock' every timestep - so extract all lines matching the regex
       perf_regex = r'\s+Wall clock\s+(\S+)'
       self.perf_patterns = {
               'Total Time': sn.extractsingle(perf_regex, self.logfile, 1, float, item=-1)
       }
