import reframe as rfm
import reframe.utility.sanity as sn
import hackathon as hack

@rfm.simple_test
class NWChemTest(hack.HackathonBase):
    # Where to run the binaries 'aws:c6gn' on Arm or 'aws:c5n' on Intel
    valid_systems = ['aws:c6gn']

    # Logging Variables
    log_team_name = 'QMlab'
    log_app_name = 'harminv'
    log_test_name = 'harminv_validation'

    # Define test case
    # In this case we download the file from GitHub and write as clover.in - the expected input file
    prerun_cmds = ['wget -O input.txt https://raw.githubusercontent.com/PrakashQM/Cloud-HPC-Hackathon-2021/miniapp/harminv/Applications/MiniApps/harminv/input.txt'] 

    # Define Execution
    # Binary to run
    executable = 'harminv'
    # Command line options to pass
    executable_opts = [' -t 0.02 0-6250 <input.txt > harminv.out']
    # Where the output is written to
    logfile = 'harminv.out'
    # Store the output file (used for validation later)
    keep_files = [logfile]


    # Parameters - Compilers - Defined as their Spack specs (use spec or hash)
    spec = parameter([
        'harminv@1.4%arm@21.0.0.879',     # CloverLeaf with the GCC compiler
        'harminv@1.4%gcc@10.3.0', # CloverLeaf with the Arm compiler
#        'cloverleaf@1.1 %nvhpc@21.2'      # CloverLeaf with the NVIDIA compiler
    ])

    # Parameters - MPI / Threads - Used for scaling studies
    parallelism = parameter([
        { 'nodes' : 1, 'mpi' : 1, 'omp' : 1},
        { 'nodes' : 1, 'mpi' : 2, 'omp' : 1},
#        { 'nodes' : 1, 'mpi' : 4, 'omp' : 1},
#        { 'nodes' : 1, 'mpi' : 8, 'omp' : 1},
#        { 'nodes' : 1, 'mpi' : 16, 'omp' : 1},
#        { 'nodes' : 1, 'mpi' : 32, 'omp' : 1},
#        { 'nodes' : 1, 'mpi' : 64, 'omp' : 1},
    ])

    # Request exclusive nodes from slurm
    @rfm.run_before('run')
    def prepare_job(self):
       self.job.options += ['--exclusive']

    # Code validation
    @run_before('sanity')
    def set_sanity_patterns(self):

       # Use the logfile for validation testing and performance



       self.sanity_patterns = sn.assert_found(
            r'-7.24255, -8.198696e-02, -277.522, 9.6967, 0.617387, 3.756439e-04', 'harminv.out')

       # Performance Testing - FOM Total Time units 's'
       # We dont set an expected value
       self.reference = {
          '*': {'Total Time': (0, None, None, 's'),}
       }

