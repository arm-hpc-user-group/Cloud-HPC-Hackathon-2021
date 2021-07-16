"""
Tests `gatk CountBases[Spark]` using public example data 

This tests one of the common GATK tools and both the GATK3 version and GATK4 (aka Spark-based) version.

This tests relies on publically accessible data for an example Illumina 2500 HiSeq run that is known to have 20K reads and 5000000 bases. 
"""
import re
import reframe as rfm
import reframe.utility.sanity as sn
import hackathon as hack

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
        'gatk@4.1.8.1%gcc@10.3.0',     # gatk CountBasesSparck with GCC compiler
        'gatk@4.1.8.1%arm@21.0.0.879', # gatk CountBasesSpark with ARM compiler
    ])


    parallelism = parameter([{ 'nodes' : 1, 'mpi' : 1, 'omp' : 1}])

    def __init__(self, log_test_name, bam_file, gatk_tool, expected_bases, perf_regex):
        self.log_test_name = log_test_name

        # CLI args to use the Spark version of read counting 
        self.executable_opts = [
             f'--java-options "-Xmx60G" {gatk_tool} -I {bam_file} &> gatk.out'
        ]

        self.bam_file = bam_file
        self.expected_bases = expected_bases
        self.perf_regex = perf_regex
        self.gatk_tool = gatk_tool

    @run_before('sanity')
    def set_sanity_patterns(self):

        # Use the logfile for validation testing and performance
        expected_count = sn.extractsingle(f'({self.expected_bases})', self.logfile, 1, float)

        self.sanity_patterns = sn.assert_eq(expected_count, self.expected_bases)

        # timing is taken from the code's self-reported numbers
        self.reference = {
            '*': {'Total Time': (0, None, None, 's'),}
        }

        total_time = sn.extractsingle(self.perf_regex, self.logfile, 1, float, item=-1)
        if 'Spark' not in self.gatk_tool:
            total_time *= 60
        self.perf_patterns = {
            'Total Time': total_time
        }


@rfm.simple_test
class GATKCountBasesSpark20kTest(GATKTest):
    def __init__(self):
        super().__init__(
                log_test_name="gatk_countbasesspark_hiseq_2500_20k",
                bam_file="/scratch/home/jayson/gatk-data/H06HDADXX130110.1.ATCACGAT.20k_reads.bam",
                gatk_tool="CountBasesSpark", 
                expected_bases=5000000,
                perf_regex=r'Job .* finished: .* took (\S+) s',
            )

@rfm.simple_test
class GATKCountBases20kTest(GATKTest):
    def __init__(self):
        super().__init__(
                log_test_name="gatk_countbases_hiseq_2500_20k",
                bam_file="/scratch/home/jayson/gatk-data/H06HDADXX130110.1.ATCACGAT.20k_reads.bam",
                gatk_tool="CountBases",
                expected_bases=5000000,
                perf_regex=r'Processed 20000 total reads in (\S+) minutes',
            )

@rfm.simple_test
class GATKCountBasesSpark1000GenomesLowCoverageTest(GATKTest):
    def __init__(self):
        super().__init__(
                log_test_name="gatk_countbasesspark_1000_genomes_low_coverage",
                bam_file="/scratch/home/jayson/gatk-data/HG00096.mapped.ILLUMINA.bwa.GBR.low_coverage.20120522.bam",
                gatk_tool="CountBasesSpark", 
                expected_bases=14506358900,
                perf_regex=r'Job .* finished: .* took (\S+) s',
            )

@rfm.simple_test
class GATKCountBases1000GenomesLowCoverageTest(GATKTest):
    def __init__(self):
        super().__init__(
                log_test_name="gatk_countbases_1000_genomes_low_coverage",
                bam_file="/scratch/home/jayson/gatk-data/HG00096.mapped.ILLUMINA.bwa.GBR.low_coverage.20120522.bam",
                gatk_tool="CountBases",
                expected_bases=14506358900,
                perf_regex=r'Processed 145063589 total reads in (\S+) minutes',
            )

@rfm.simple_test
class GATKCountBasesSpark1000GenomesHighCoverageTest(GATKTest):
    def __init__(self):
        super().__init__(
                log_test_name="gatk_countbasesspark_1000_genomes_high_coverage",
                bam_file="/scratch/home/jayson/gatk-data/HG00096.wgs.ILLUMINA.bwa.GBR.high_cov_pcr_free.20140203.bam",
                gatk_tool="CountBasesSpark", 
                expected_bases=161506906064,
                perf_regex=r'.*CountBasesSpark done. Elapsed time: (\S+) minutes.',
            )

@rfm.simple_test
class GATKCountBases1000GenomesHighCoverageTest(GATKTest):
    def __init__(self):
        super().__init__(
                log_test_name="gatk_countbases_1000_genomes_high_coverage",
                bam_file="/scratch/home/jayson/gatk-data/HG00096.wgs.ILLUMINA.bwa.GBR.high_cov_pcr_free.20140203.bam",
                gatk_tool="CountBases",
                expected_bases=161506906064,
                perf_regex=r'Processed 652944493 total reads in (\S+) minutes',
            )
