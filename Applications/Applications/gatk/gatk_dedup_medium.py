"""
Tests `gatk BwaSpark` using public example data 

Performs a sequencing alignment of a 1000 genomes sample to human chromosome 1. This is an example of an expensive bioinformatics operation GATK is commonly used for.
"""
import reframe as rfm
import reframe.utility.sanity as sn
import hackathon as hack

@rfm.simple_test
class GATKTest(hack.HackathonBase):
    # Where to run the binaries 'aws:c6gn' on Arm or 'aws:c5n' on Intel
    valid_systems = ['aws:c6gn', 'aws:c5n']

    # Logging Variables
    log_team_name = 'Falkners'
    log_app_name = 'GATK'

    # no pre-run. Genomies files are big and already in scratch
    # see gatk_countbases...py for auto-downloads
    prerun_cmds = [
    ]

    # Binary to run
    executable = 'gatk'
    # Where the output is written to
    logfile = 'gatk.out'
    # Store the output file (used for validation later)
    keep_files = [logfile]

    # Parameters - Compilers - Defined as their Spack specs (use spec or hash)
    spec = parameter([
        'gatk@4.1.8.1%gcc@10.3.0',     # gatk CountReadsSparck with GCC compiler
        'gatk@4.1.8.1%arm@21.0.0.879', # gatk CountReadsSpark with ARM compiler
    ])

    log_test_name = f'gatk_dedup_medium'

    # CLI args to use the Spark version of read counting 
    executable_opts = [
        '--java-options "-Xmx60g" MarkDuplicatesSpark -I /scratch/home/jayson/gatk-data/HG00096.mapped.ILLUMINA.bwa.GBR.low_coverage.20120522.bam -O test.bam -M test_metrics.txt &> gatk.out'
    ]

    parallelism = parameter([
        #{ 'nodes' : 1, 'mpi' : 1, 'omp' : 1, 'extra-cmd': '0'},
        #{ 'nodes' : 1, 'mpi' : 1, 'omp' : 2, 'extra-cmd': '0-1'},
        #{ 'nodes' : 1, 'mpi' : 1, 'omp' : 4, 'extra-cmd': '0-3'},
        #{ 'nodes' : 1, 'mpi' : 1, 'omp' : 8, 'extra-cmd': '0-7'},
        #{ 'nodes' : 1, 'mpi' : 1, 'omp' : 16, 'extra-cmd': '0-15'},
        #{ 'nodes' : 1, 'mpi' : 1, 'omp' : 32, 'extra-cmd': '0-31'},
        #{ 'nodes' : 1, 'mpi' : 1, 'omp' : 35, 'extra-cmd': '0-35'},
        { 'nodes' : 1, 'mpi' : 1, 'omp' : 1, 'extra-cmd': '0'},
    ])

    @run_before('run')
    def set_config(self):
        pass
        # tried to get the JVM to respect a scaling test!
        #self.executable = f"taskset --cpu-list {self.parallelism['extra-cmd']} {self.executable}"
        #self.executable_opts.append(f"--spark-master local[{self.parallelism['omp']}] &> gatk.out")
        

    @run_before('sanity')
    def set_sanity_patterns(self):

        # Use the logfile for validation testing and performance
        expected_count_regex = r'(MarkDuplicatesSpark)'
        expected_count = sn.extractsingle(expected_count_regex, self.logfile, 1, str)

        self.sanity_patterns = sn.assert_eq(expected_count, 'MarkDuplicatesSpark') 

        # timing is taken from the code's self-reported numbers
        self.reference = {
            '*': {'Total Time': (0, None, None, 'm'),}
        }

        perf_regex = r'MarkDuplicatesSpark done. Elapsed time: (\S+) minutes'
        self.perf_patterns = {
            'Total Time': sn.extractsingle(perf_regex, self.logfile, 1, float, item=-1)
        }
