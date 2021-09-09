import reframe as rfm
import reframe.utility.sanity as sn
import hackathon as hack


@rfm.simple_test
class STARTest(hack.HackathonBase):
    dprefix = variable(str)
    input_fq = variable(str)
    output = variable(str)

    dprefix = '/home/lisanhu/data'
    input_fq = dprefix + '/hg38-1k-500.fastq '
    output = 'Aligned.sortedByCoord.out.bam'

    test_name = 'star-hg38-1k-500'

    # Where to run the binaries 'aws:c6gn' on Arm or 'aws:c5n' on Intel
    valid_systems = ['aws:c5n']
    # Logging Variables
    log_team_name = 'BlueHPCHens'
    log_app_name = 'STAR'
    log_test_name = test_name

    # Define test case
    # Generates the initial data for the flecSPH test run
    prerun_cmds = [
        "/home/lisanhu/STAR/source/STAR --runMode genomeGenerate --genomeFastaFiles /home/lisanhu/data/hg38.fa"]

    # Define Execution
    # Binary to run
    executable = '/home/lisanhu/STAR/source/STAR'

    # Command line options to pass
    executable_opts = ['--genomeDir ' + dprefix + '/GenomeDir --readFilesIn ' +
                       input_fq + ' --outSAMtype BAM 		ortedByCoordinate']

    # Where the output is written to
    logfile = 'star.log'

    # results = 'scalar_reductions.dat'
    # Store the output file (used for validation later)
    keep_files = [output]

    spec = parameter([
        'star%gcc@10.3.0',     # FlecSPH with the GCC compiler
        #      'flecsph%arm@21.0.0.879', # FlecSPH with the Arm compiler
        # 'flecsph%nvhpc@21.2'      # FlecSPH with the NVIDIA compiler
         ])
    # Parameters - MPI / Threads - Used for scaling studies
    parallelism = parameter([
        {'nodes': 1, 'mpi': 1, 'omp': 1},
        {'nodes': 1, 'mpi': 1, 'omp': 2},
        {'nodes': 1, 'mpi': 1, 'omp': 4},
        {'nodes': 1, 'mpi': 1, 'omp': 8},
        {'nodes': 1, 'mpi': 1, 'omp': 16},
        {'nodes': 1, 'mpi': 1, 'omp': 32},
    ])

    # Request exclusive nodes from slurm

    @run_before('run')
    def prepare_job(self):
        self.job.options += ['--exclusive']
        self.job.launcher.options = ['/usr/bin/time -v']
        # self.job.launcher.options = ['/usr/bin/time -f "%e"']

    # Code validation
    @run_before('sanity')
    def set_sanity_patterns(self):
        validation_regex = r'finished succesfully'
        pref_regex = r'ss):\s(\S+)'
        # Perform a bounded assert for the three types of energy
        # self.sanity_patterns = sn.all([
        # 	sn.assert_found(validation_regex, self.stdout, msg="STAR Application never returned completion statement")
        # ])
        self.sanity_patterns = sn.assert_found(
            validation_regex, self.stdout, msg="STAR Application never returned completion statement")
        # Performance Testing - FOM Total Time units 's'
        # We dont set an expected value
        self.reference = {
            '*': {'Total Time': (0, None, None, 's'), }
        }
        # with open(self.stderr, 'rb') as f:
        #     for line in f:
        #         pass
        # last_line = line
        self.perf_patterns = {
            'Total Time': sn.extractsingle(pref_regex, self.stderr, 1, convert_to_seconds)
            # 'Total Time': last_line
        }


@rfm.simple_test
class Second(STARTest):
    dprefix = '/home/lisanhu/data'
    input_fq = dprefix + '/hg38-2k-500.fastq '
    output = dprefix + '/Aligned.sortedByCoord.out.bam'
    test_name = 'star-hg38-2k-500'


@rfm.simple_test
class Third(STARTest):
    dprefix = '/home/lisanhu/data'
    input_fq = dprefix + '/hg38-4k-500.fastq '
    output = dprefix + '/Aligned.sortedByCoord.out.bam'
    test_name = 'star-hg38-4k-500'
