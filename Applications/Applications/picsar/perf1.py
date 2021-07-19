import reframe as rfm
import reframe.utility.sanity as sn
import hackathon as hack
import os
from PyLoadArrayPicsar import *
from reframe.core.launchers import LauncherWrapper
from shutil import copyfile

@rfm.simple_test
class PICSARtest(hack.HackathonBase):
    # Where to run the binaries 'aws:c6gn' on Arm or 'aws:c5n' on Intel
    valid_systems = ['aws:c6gn']

    # Logging Variables
    log_team_name = 'ElkNet'
    log_app_name = 'PICSAR'
    log_test_name = 'PICSAR-PERF1'

    # Define test case
    input_name = 'perf1'
    input_dir = os.path.dirname(__file__) + '/benchmarks/' + input_name
    inputfile = input_dir + '/input/' + input_name + '.pixr'

    # Define Execution
    # Binary to run
    executable = 'picsar'

    # Parameters - Compilers - Defined as their Spack specs (use spec or hash)
    spec = parameter([
        'picsar%gcc@10.3.0',      # PICSAR with the GCC compiler
        'picsar%arm@21.0.0.879',  # PICSAR with the Arm compiler
        'picsar%nvhpc@21.2'       # PICSAR with the NVIDIA compiler
    ])

    # Parameters - MPI / Threads - Used for scaling studies
    parallelism = parameter([
        {'nodes': 1, 'mpi': 1, 'omp': 1},
        {'nodes': 1, 'mpi': 1, 'omp': 2},
        {'nodes': 1, 'mpi': 1, 'omp': 4},
        {'nodes': 1, 'mpi': 1, 'omp': 8},
        {'nodes': 1, 'mpi': 1, 'omp': 16},
        {'nodes': 1, 'mpi': 1, 'omp': 32},
        {'nodes': 1, 'mpi': 1, 'omp': 64},
    ])

    # Request exclusive nodes from slurm
    @run_before('run')
    def prepare_job(self):
        # prepend time to srun
        self.job.launcher = LauncherWrapper(self.job.launcher, 'time', ['-p'])

        self.job.options += ['--exclusive']

        # Copy the input file and change its name
        copyfile(self.inputfile, self.stagedir + '/input_file.pixr')
        # Create the needed output directory
        os.mkdir(self.stagedir + '/RESULTS')

    # Code validation
    @run_before('sanity')
    def set_sanity_patterns(self):
        # Validate the output
        results_path = self.stagedir + '/RESULTS'

        #### CHECK ENERGY BALANCE ###
        # Kinetic energy
        t,kinE = read_picsar_temporal_diags(results_path + '/kinE')
        # Opening of the ezfield
        t,ezE = read_picsar_temporal_diags(results_path + '/ezE')
        # Opening of the eyfield
        t,eyE = read_picsar_temporal_diags(results_path + '/eyE')
        # Opening of the exfield
        t,exE = read_picsar_temporal_diags(results_path + '/exE')
        # Opening of the exfield
        t,bzE = read_picsar_temporal_diags(results_path + '/bzE')
        # Opening of the exfield
        t,byE = read_picsar_temporal_diags(results_path + '/byE')
        # Opening of the exfield
        t,bxE = read_picsar_temporal_diags(results_path + '/bxE')

        total_energy = sum(kinE,axis=0) + ezE + exE + eyE + bzE + bxE + byE

        min_totalE = min(total_energy)
        max_totalE = max(total_energy)
        diffrel = (max_totalE - min_totalE)/max_totalE

        self.sanity_patterns = sn.assert_lt(diffrel, 1e-2, msg=None)

        # Performance Testing - FOM Total Time units 's'
        # We dont set an expected value
        self.reference = {
            '*': {'Total Time': (0, None, None, 's'), }
        }

        # Time prints the real time so extract it.
        pref_regex = r'\s*real\s+(\S+)'
        self.perf_patterns = {
            'Total Time': sn.extractsingle(pref_regex, self.stagedir + "/" + self.stderr, 1, float, item=-1)
        }
