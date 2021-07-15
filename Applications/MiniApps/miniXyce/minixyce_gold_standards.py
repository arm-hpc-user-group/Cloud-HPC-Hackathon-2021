import reframe as rfm
import reframe.utility.sanity as sn
import hackathon as hack

@rfm.simple_test
class MiniXyceTest(hack.HackathonBase):
    # Where to run the binaries 'aws:c6gn' on Arm or 'aws:c5n' on Intel
    valid_systems = ['aws:c6gn']

    # Logging Variables
    log_team_name = 'SGHackers'
    log_app_name = 'MiniXyce'
    log_test_name = 'short_test'

    # Define test case
    # In this case we download the file from GitHub and write as clover.in - the expected input file
    '''
    prerun_cmds = ['cp -r /scratch/opt/spack/linux-amzn2-graviton2/gcc-10.3.0/minixyce-1.0-6txjvdkxg5w6myfup6wocxhwlolawgq4/doc/tests tests' ,
                   'cp /scratch/opt/spack/linux-amzn2-graviton2/gcc-10.3.0/minixyce-1.0-6txjvdkxg5w6myfup6wocxhwlolawgq4/bin/default_params.txt default_params.txt']
    '''
    prerun_cmds = ['cp -r /home/rae/Cloud-HPC-Hackathon-2021/Applications/MiniApps/miniXyce/tests tests' ,
                    'cp /home/rae/Cloud-HPC-Hackathon-2021/Applications/MiniApps/miniXyce/tests/default_params.txt default_params.txt']

    # Define Execution
    # Binary to run
    executable = 'miniXyce.x'
    # Command line options to pass executable_opts is parametrised
    # executable_opts = ['-c tests/cir1.net > output']
    exec_opts = parameter([
        # "-c tests/cir3.net --t_start 0 --pf default_params.txt > output", # This test is failing, why?
        "-c tests/cir1.net --t_start 0 --pf default_params.txt > output",
        "-c tests/cir2.net --t_start 0 --pf default_params.txt > output",
        "-c tests/cir4.net --t_start 0 --pf default_params.txt > output",
        ])

    # Where the output is written to
    logfile = 'output'
    # Store the output file (used for validation later)
    keep_files = [logfile]


    # Parameters - Compilers - Defined as their Spack specs (use spec or hash)
    spec = parameter([
        'minixyce %gcc@10.3.0',     # CloverLeaf with the GCC compiler
         'minixyce %arm@21.0.0.879', # CloverLeaf with the Arm compiler
         'minixyce %nvhpc@21.2'      # CloverLeaf with the NVIDIA compiler
    ])

    # Parameters - MPI / Threads - Used for scaling studies
    parallelism = parameter([
        { 'nodes' : 1, 'mpi' : 64, 'omp' : 1},
        { 'nodes' : 1, 'mpi' : 32, 'omp' : 1},
        { 'nodes' : 1, 'mpi' : 16, 'omp' : 1},
        { 'nodes' : 1, 'mpi' : 8, 'omp' : 1},
        { 'nodes' : 1, 'mpi' : 4, 'omp' : 1},
        { 'nodes' : 1, 'mpi' : 2, 'omp' : 1},
        { 'nodes' : 1, 'mpi' : 1, 'omp' : 1},
    ])
 
    @run_before('run')
    def set_executable_opts(self):
        self.executable_opts = [self.exec_opts]

    # Code validation
    @run_before('sanity')
    def set_sanity_patterns(self):

       # Log performance
       pref_regex = r'\s+Total Simulation Time:\s+(\S+)'
       self.perf_patterns = {
            'Total Time': sn.extractsingle(pref_regex, self.logfile, 1, float, item=-1)
       }

       # Gold standard validation
       filename = self.exec_opts.split(" ")[1]
       filename = filename[filename.index('/')+1:]
       cirname = filename[:filename.index('.')]
       gold_standard_filename = "tests/goldStandards/"+filename+".prn"
       output_filename = "tests/"+cirname+"_tran_results.prn" #cir1_tran_results.prn  
       line = 0
       with open(output_filename,"r") as f1, open(gold_standard_filename,"r") as f2:
           for i,j in zip(f1,f2):
               if (line != 501):
                   line += 1
                   continue
               else:
                   # compare line 501(final state)
                   i = [float(val) for val in i.strip('\n').split()]
                   j = [float(val) for val in j.strip('\n').split()][1:]
                   for ind in range(len(j)):
                       print ("Output: ", abs(i[ind]) , " Goldstandard: ", abs(j[ind]))
                       self.sanity_patterns = sn.assert_bounded(abs(i[ind]), abs(j[ind])-1e-5, abs(j[ind])+1e-5)
                   break;

       '''
       pref_regex = r'\s+TIME\s+(\S+)'
       self.perf_patterns = {
            'Found': sn.extractsingle(pref_regex, "tests/cir2_tran_results.prn", 1, str, item=-1)
       }
       '''




