import reframe as rfm
import reframe.utility.sanity as sn
import hackathon as hack

@rfm.simple_test
class NWChemTest(hack.HackathonBase):
    # Where to run the binaries 'aws:c6gn' on Arm or 'aws:c5n' on Intel
    valid_systems = ['aws:c6gn']

    # Logging Variables
    log_team_name = 'QMlab'
    log_app_name = 'NWChem'
    log_test_name = 'nwchem_short_exclusive'

    # Define test case
    # In this case we download the file from GitHub and write as clover.in - the expected input file
    prerun_cmds = ['wget -O nwchem.nw https://raw.githubusercontent.com/nwchemgit/nwchem/master/QA/tests/h2o-bhlyp/h2o-bhlyp.nw'] 

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
        'nwchem@7.0.2 %arm@21.0.0.879', # CloverLeaf with the Arm compiler
#        'cloverleaf@1.1 %nvhpc@21.2'      # CloverLeaf with the NVIDIA compiler
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

    # Request exclusive nodes from slurm
    @rfm.run_before('run')
    def prepare_job(self):
       self.job.options += ['--exclusive']

    # Code validation
    @run_before('sanity')
    def set_sanity_patterns(self):

       # Use the logfile for validation testing and performance

       # Validation at step 87 (BM_short)
       # Regex - Volume   Mass   Density   Pressure   Internal Energy   Kinetic Energy   Total Energy
       sol_regex = r'\s+Total DFT energy =\s+(\S+)'
       # Validate for kinetic energy (6)
       kinetic_energy = sn.extractsingle(sol_regex, 'nwchem.out',1,float)

       # expected = -76.42192374510
       expected_lower = float(-76.42190000000)
       expected_upper = float(-76.52192376000)       

       # Perform a bounded assert
       #self.sanity_patterns = sn.assert_bounded(kinetic_energy, expected_lower, expected_upper)
       #self.sanity_patterns = sn.assert_eq(kinetic_energy, -76.421923745064)
       self.sanity_patterns=   sn.assert_reference(kinetic_energy,-76.421923745064, lower_thres=-0.0004, upper_thres=0.0004, msg=None)

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

