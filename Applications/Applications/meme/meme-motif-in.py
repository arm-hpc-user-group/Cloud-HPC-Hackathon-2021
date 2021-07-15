import os
import sys

import reframe as rfm
import reframe.utility.sanity as sn
import reframe.utility.udeps as udeps
import hackathon as hack


@rfm.simple_test
class MemeMotifInT1(hack.HackathonBase):
    # Where to run the binaries 'aws:c6gn' on Arm or 'aws:c5n' on Intel
    valid_systems = ['aws:c6gn']

    # Logging Variables
    log_team_name = 'TeamEPCC'
    log_app_name = 'meme'
    log_test_name = 'meme'

    prerun_cmds = [
        # inputs
        'wget https://raw.githubusercontent.com/rj-jesus/Cloud-HPC-Hackathon-2021/app/meme/Applications/Applications/meme/inputs/Klf1-200-100-shuffled.py2.fa',
        'wget https://raw.githubusercontent.com/rj-jesus/Cloud-HPC-Hackathon-2021/app/meme/Applications/Applications/meme/inputs/Klf1-200-100.fa',
        'wget https://raw.githubusercontent.com/rj-jesus/Cloud-HPC-Hackathon-2021/app/meme/Applications/Applications/meme/inputs/Puf3p-20.s',
        'wget https://raw.githubusercontent.com/rj-jesus/Cloud-HPC-Hackathon-2021/app/meme/Applications/Applications/meme/inputs/Puf3p.s',
        'wget https://raw.githubusercontent.com/rj-jesus/Cloud-HPC-Hackathon-2021/app/meme/Applications/Applications/meme/inputs/crp0.s',
        'wget https://raw.githubusercontent.com/rj-jesus/Cloud-HPC-Hackathon-2021/app/meme/Applications/Applications/meme/inputs/extended_dna.alph',
        'wget https://raw.githubusercontent.com/rj-jesus/Cloud-HPC-Hackathon-2021/app/meme/Applications/Applications/meme/inputs/lipocalin.s',
        # scripts
        'wget https://raw.githubusercontent.com/rj-jesus/Cloud-HPC-Hackathon-2021/app/meme/Applications/Applications/meme/motif-in.test.sh',
        # outputs
        'mkdir -p results',
    ]

    # Define Execution
    my_test = 'T1'
    executable = 'streme'
    executable_opts = [
            '-oc', 'results/motif.streme.klf1', '-verbosity', '1', '-nmotifs', '2', '-p', 'Klf1-200-100.fa', '-n', 'Klf1-200-100-shuffled.py2.fa'
        ]

    # Parameters - Compilers - Defined as their Spack specs (use spec or hash)
    spec = parameter([
        #'meme/csigtg7',     # Meme with the Arm compiler
        'meme%arm ^perl@5.32.1'
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

    postrun_cmds = [
        f'bash motif-in.test.sh {my_test}'
    ]

    # Code validation
    @run_before('sanity')
    def set_sanity_patterns(self):
        pass_regex = r'^PASS$'
        m = sn.len(sn.findall(pass_regex, self.stdout))
        self.sanity_patterns = sn.assert_eq(m, 3)


@rfm.simple_test
class MemeMotifInT2(hack.HackathonBase):
    # Where to run the binaries 'aws:c6gn' on Arm or 'aws:c5n' on Intel
    valid_systems = ['aws:c6gn']

    # Logging Variables
    log_team_name = 'TeamEPCC'
    log_app_name = 'meme'
    log_test_name = 'meme'

    prerun_cmds = [
        # inputs
        'wget https://raw.githubusercontent.com/rj-jesus/Cloud-HPC-Hackathon-2021/app/meme/Applications/Applications/meme/inputs/Klf1-200-100-shuffled.py2.fa',
        'wget https://raw.githubusercontent.com/rj-jesus/Cloud-HPC-Hackathon-2021/app/meme/Applications/Applications/meme/inputs/Klf1-200-100.fa',
        'wget https://raw.githubusercontent.com/rj-jesus/Cloud-HPC-Hackathon-2021/app/meme/Applications/Applications/meme/inputs/Puf3p-20.s',
        'wget https://raw.githubusercontent.com/rj-jesus/Cloud-HPC-Hackathon-2021/app/meme/Applications/Applications/meme/inputs/Puf3p.s',
        'wget https://raw.githubusercontent.com/rj-jesus/Cloud-HPC-Hackathon-2021/app/meme/Applications/Applications/meme/inputs/crp0.s',
        'wget https://raw.githubusercontent.com/rj-jesus/Cloud-HPC-Hackathon-2021/app/meme/Applications/Applications/meme/inputs/extended_dna.alph',
        'wget https://raw.githubusercontent.com/rj-jesus/Cloud-HPC-Hackathon-2021/app/meme/Applications/Applications/meme/inputs/lipocalin.s',
        # scripts
        'wget https://raw.githubusercontent.com/rj-jesus/Cloud-HPC-Hackathon-2021/app/meme/Applications/Applications/meme/motif-in.test.sh',
        # outputs
        'mkdir -p results',
    ]

    # Define Execution
    my_test = 'T2'
    executable = 'streme'
    executable_opts = [
            '-oc', 'results/motif.streme.klf1.extdna', '-verbosity', '1', '-alph', 'extended_dna.alph', '-nmotifs', '2', '-p', 'Klf1-200-100.fa', '-n', 'Klf1-200-100-shuffled.py2.fa'
        ]

    # Parameters - Compilers - Defined as their Spack specs (use spec or hash)
    spec = parameter([
        #'meme/csigtg7',     # Meme with the Arm compiler
        'meme%arm ^perl@5.32.1'
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

    postrun_cmds = [
        f'bash motif-in.test.sh {my_test}'
    ]

    # Code validation
    @run_before('sanity')
    def set_sanity_patterns(self):
        pass_regex = r'^PASS$'
        m = sn.len(sn.findall(pass_regex, self.stdout))
        self.sanity_patterns = sn.assert_eq(m, 3)
