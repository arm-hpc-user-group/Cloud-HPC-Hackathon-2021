import reframe as rfm
import reframe.utility.sanity as sn
import hackathon as hack


@rfm.simple_test
class MemeMemeTest(hack.HackathonBase):
    # Where to run the binaries 'aws:c6gn' on Arm or 'aws:c5n' on Intel
    valid_systems = ['aws:c6gn']

    # Logging Variables
    log_team_name = 'TeamEPCC'
    log_app_name = 'meme'
    log_test_name = 'meme'

    # Define test case
    # In this case we download the file from GitHub and write as clover.in - the expected input file
    prerun_cmds = [
            'wget https://raw.githubusercontent.com/rj-jesus/Cloud-HPC-Hackathon-2021/app/meme/Applications/Applications/meme/inputs/Klf1-200-100.fa',
            'wget https://raw.githubusercontent.com/rj-jesus/Cloud-HPC-Hackathon-2021/app/meme/Applications/Applications/meme/inputs/Klf1-200-100-shuffled.py2.fa',
            ]

    # Define Execution
    # Binary to run
    executable = 'streme'
    # Command line options to pass
    executable_opts = [
            '-oc', 'results/motif.streme.klf1', '-verbosity', '1', '-nmotifs', '2', '-p', 'Klf1-200-100.fa', '-n', 'Klf1-200-100-shuffled.py2.fa'
            ]
    # Where the output is written to
    logfile = 'motif.streme.out'
    # Store the output file
    keep_files = [logfile]

    # Parameters - Compilers - Defined as their Spack specs (use spec or hash)
    spec = parameter([
        'meme%arm ^perl@5.32.1',     # Meme with the Arm compiler
    ])

    # Parameters - MPI / Threads - Used for scaling studies
    parallelism = parameter([
        { 'nodes' : 1, 'mpi' : 1, 'omp' : 1},
        #{ 'nodes' : 1, 'mpi' : 2, 'omp' : 1},
        #{ 'nodes' : 1, 'mpi' : 4, 'omp' : 1},
        #{ 'nodes' : 1, 'mpi' : 8, 'omp' : 1},
        #{ 'nodes' : 1, 'mpi' : 16, 'omp' : 1},
        #{ 'nodes' : 1, 'mpi' : 32, 'omp' : 1},
        #{ 'nodes' : 1, 'mpi' : 64, 'omp' : 1},
    ])


    # Code validation
    @run_before('sanity')
    def set_sanity_patterns(self):
        return

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
