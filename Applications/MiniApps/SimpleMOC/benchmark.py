import reframe as rfm
import reframe.utility.sanity as sn
import hackathon as hack


def convert_to_seconds(time):
    time_list = time.split(":")
    minutes = float(time_list[0])
    seconds = minutes * 60 + float(time_list[1])
    return seconds

@rfm.simple_test
class SimpleMOCTest4(hack.HackathonBase):
    # Where to run the binaries 'aws:c6gn' on Arm or 'aws:c5n' on Intel
    valid_systems = ['aws:c6gn']

    # Logging Variables
    log_team_name = 'BlueHPCHens'
    log_app_name = 'SimpleMOC'
    log_test_name = 'SimpleMOC_Test_Run_3'

    # Define test case
    # Generates the initial data for the flecSPH test run
    prerun_cmds = []

    # Define Execution
    # Binary to run
    executable = 'SimpleMOC'
    # Command line options to pass
    executable_opts = []
    # Where the output is written to
    logfile = './simpleMoc.log'
    #results = 'nothing'

    # Store the output file (used for validation later)
    keep_files = [logfile]


    # Parameters - Compilers - Defined as their Spack specs (use spec or hash)
    spec = parameter([
        'simplemoc@4%gcc@10.3.0',     # FlecSPH with the GCC compiler
        'simplemoc@4%arm', # FlecSPH with the Arm compiler
        'simplemoc@4%nvhpc'      # FlecSPH with the NVIDIA compiler
    ])

    # Parameters - MPI / Threads - Used for scaling studies
    parallelism = parameter([
        { 'nodes' : 1, 'mpi' : 1, 'omp' : 1},
        { 'nodes' : 1, 'mpi' : 1, 'omp' : 2},
        { 'nodes' : 1, 'mpi' : 1, 'omp' : 4},
        { 'nodes' : 1, 'mpi' : 1, 'omp' : 8},
        { 'nodes' : 1, 'mpi' : 1, 'omp' : 16},
        { 'nodes' : 1, 'mpi' : 1, 'omp' : 32},
        # intel machine has 18 cores, dual socket, so can't do 64 ranks
        { 'nodes' : 1, 'mpi' : 1, 'omp' : 64},
    ])

    # Request exclusive nodes from slurm
    @run_before('run')
    def prepare_job(self):
       self.job.options += ['--exclusive']
       self.executable_opts += ['-t', str(self.parallelism['omp']), '-s']
       #self.job.launcher.options = ['/usr/bin/time -v']
       #self.job.launcher.options = ['/usr/bin/time -f "%e"']
    # Code validation
    @run_before('sanity')
    def set_sanity_patterns(self):

       # Use the logfile for validation testing and performance

       # Validation at step 5000 (sod_test1_n10000)
       # 1:iteration 2:time 3:timestep 4:total_mass  5:total_energy 6:kinetic_energy 7:internal_energy 8:mom_x
       sol_regex = r'Renormalizing Flux Complete.'

       #gets kinetic_energy values from scalar_reductions.dat
       #generated_ke = sn.extractsingle(sol_regex, self.results, 5, conv = float)
       #generated_ie = sn.extractsingle(sol_regex, self.results, 6, conv = float)
       #generated_te = sn.extractsingle(sol_regex, self.results, 4, conv = float)


       # List of expected energy values
       #expected_ke = 5.667058383110e-01
       #expected_ie = 5.434194251698e+00
       #expected_te = 6.000900090009e+00

       # boundaries for the energy results (currently expected - 0.01 < expected < expected + 0.01)
       #boundary_threshold = 0.01

       #lower_ke = expected_ke - boundary_threshold
       #upper_ke = expected_ke + boundary_threshold
       #lower_ie = expected_ie - boundary_threshold
       #upper_ie = expected_ie + boundary_threshold
       #lower_te = expected_te - boundary_threshold
       #upper_te = expected_te + boundary_threshold

       # Perform a bounded assert for the three types of energy
       self.sanity_patterns = sn.all([
           #sn.assert_bounded(generated_ke, lower_ke, upper_ke, "Kinetic Energy assertion fails, value out of bounds"),
           #sn.assert_bounded(generated_ie, lower_ie, upper_ie, "Internal Energy assertion fails, value out of bounds"),
           #sn.assert_bounded(generated_te, lower_te, upper_te, "Total Energy assertion fails, value out of bounds")
           sn.assert_found(sol_regex, self.stdout, msg="SimpleMOC Application never returned competion statement")
           ])
       # Performance Testing - FOM Total Time units 's'
       # We dont set an expected value
       self.reference = {
          '*': {'Total Time': (0, None, None, 's'),}
       }

       # CloverLeaf prints the 'Wall clock' every timestep - so extract all lines matching the regex
       #pref_regex = r'\s+Wall clock\s+(\S+)'
       pref_regex = r'Total Time:                   (\S+) sec'
       #with open(self.stdout, 'rb') as f:
       #    for line in f:
       #        pass
       #    last_line = line
       self.perf_patterns = {
               'Total Time': sn.extractsingle(pref_regex, self.stdout, 1, float)
              #'Total Time': last_line
       }
