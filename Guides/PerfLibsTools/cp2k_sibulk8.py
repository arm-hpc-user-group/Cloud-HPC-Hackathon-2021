import reframe as rfm
import reframe.utility.sanity as sn
import hackathon as hack

@rfm.simple_test
class CP2K_Test(hack.HackathonBase):
    # Where to run the binaries
    valid_systems = ['aws:c6gn'] #, 'aws:c6gn'] 

    # Logging Variables
    log_team_name = 'TeamArm'
    log_app_name = 'CP2k'
    log_test_name = 'Si_Bulk8'

    # Define test case
    # In this case we download the file from GitHub and write as clover.in - the expected input file
    prerun_cmds = ['wget https://www.cp2k.org/_media/static_calculation.tgz', 
                   'tar xf static_calculation.tgz', 
                   'cp static_calculation/sample_output_with_smearing/BASIS_SET .',
                   'cp static_calculation/sample_output_with_smearing/GTH_POTENTIALS .',
                   'cp static_calculation/sample_output_with_smearing/Si_bulk8.inp .'
                   ]

    # Define Execution
    # Binary to run
    executable = 'cp2k.popt'

    # Where the output is written to
    logfile = 'Si_bulk8.out'

    # Command line options to pass
    executable_opts = ['-o', logfile, 'Si_bulk8.inp']

    # Store the output file (used for validation later)
    keep_files = [logfile]


    # Parameters - Compilers - Defined as their Spack specs (use spec or hash)
    spec = parameter([
        'cp2k%gcc smm=blas ^openblas ^fftw',     
        'cp2k%gcc smm=blas ^armpl',     
    ])

    # Parameters - MPI / Threads - Used for scaling studies
    parallelism = parameter([
        { 'nodes' : 1, 'mpi' : 1, 'omp' : 1},
        { 'nodes' : 1, 'mpi' : 2, 'omp' : 1},
        { 'nodes' : 1, 'mpi' : 4, 'omp' : 1},
    ])

    # Profiling
    @run_before('run')
    def perf_libs_tools(self):

        # Load perf-libs-tools-module
        self.modules.append('perf-libs-tools-git')

        # Make folder to save results to 
        apl_dir = 'plt_out'
        # Create the folder in pre_run cmd
        self.prerun_cmds.append('mkdir {0}'.format(apl_dir))
        # Set the Fileroot to the new folder
        self.variables['ARMPL_SUMMARY_FILEROOT'] = '$PWD/{0}/'.format(apl_dir)
        # Tell reframe to keep the folder after cleanup
        self.keep_files.append(apl_dir)

        # Add the LD_PRELOAD to srun
        self.job.launcher.options = ['--export=ALL,LD_PRELOAD=libarmpl-summarylog.so']
        
        # Make summary file
        apl_file = '{0}_{1}_apl_summary.log'.format(self.log_app_name, self.log_test_name)
        # Run post process
        self.postrun_cmds.append('process_summary.py {0}/*.apl > {1}'.format(apl_dir, apl_file))
        # Keep the summary file
        self.keep_files.append(apl_file)


    # Code validation
    @run_before('sanity')
    def set_sanity_patterns(self):

       # Use the logfile for validation testing and performance 

       #  ENERGY| Total FORCE_EVAL ( QS ) energy [a.u.]:              -31.297887031709706
       sol_regex = r'\sENERGY\| Total FORCE_EVAL \( QS \) energy \[a\.u\.\]:*\s+(\S+)'
       # Validate for Energy (1) 
       energy = sn.extractsingle(sol_regex, self.logfile, 1, float)
       
       # expected = -31.29788703173
       expected_lower = -31.29788704
       expected_upper = -31.29788702
       
       # Perform a bounded assert
       self.sanity_patterns = sn.assert_bounded(energy, expected_lower, expected_upper)

       # Performance Testing - FOM Total Time units 's'
       # We dont set an expected value
       self.reference = {
          '*': {'CP2K Time': (0, None, None, 's'),}
       }

       # CP2K prints a time summary at the end return the 'CP2K' line entry
       #  SUBROUTINE                       CALLS  ASD         SELF TIME        TOTAL TIME
       #                                MAXIMUM       AVERAGE  MAXIMUM  AVERAGE  MAXIMUM
       # CP2K                                 1  1.0    0.003    0.004    6.129    6.129
       pref_regex = r'\sCP2K\s+1\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)'

       self.perf_patterns = { 
               'CP2K Time': sn.extractsingle(pref_regex,self.logfile, 4, float),
       }
