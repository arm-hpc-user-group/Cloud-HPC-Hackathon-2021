"""
"strong scaling" test from CoMD's examples

This reframe test helps check that compiles of CoMD for HPC work correctly. It also enables comparison of different compilers. e.g. gcc vs arm on Graviton2 nodes.

Test logically scale up to 64 MPI and follow the test script from CoMD's website

  https://github.com/ECP-copa/CoMD/blob/master/examples/mpi-strongScaling.sh

```
#!/bin/sh

# Simple strong scaling study with eam potential and 256,000 atoms
mpirun -np 1  ../bin/CoMD-mpi -e -i 1 -j 1 -k 1 -x 40 -y 40 -z 40
mpirun -np 2  ../bin/CoMD-mpi -e -i 2 -j 1 -k 1 -x 40 -y 40 -z 40
mpirun -np 4  ../bin/CoMD-mpi -e -i 2 -j 2 -k 1 -x 40 -y 40 -z 40
mpirun -np 8  ../bin/CoMD-mpi -e -i 2 -j 2 -k 2 -x 40 -y 40 -z 40
mpirun -np 16 ../bin/CoMD-mpi -e -i 4 -j 2 -k 2 -x 40 -y 40 -z 40
```
"""
import reframe as rfm
import reframe.utility.sanity as sn
import hackathon as hack

class CoMDTest(hack.HackathonBase):
    # Where to run the binaries 'aws:c6gn' on Arm or 'aws:c5n' on Intel
    valid_systems = ['aws:c6gn', 'aws:c5n']

    # Logging Variables
    log_team_name = 'Falkners'
    log_app_name = 'CoMD'

    # Required potentials from CoMD's website
    prerun_cmds = [
        'mkdir ./pots',
        'wget -O ./pots/Cu_u6.eam https://raw.githubusercontent.com/ECP-copa/CoMD/master/pots/Cu_u6.eam'
    ]

    # Binary to run
    executable = 'CoMD-mpi'
    # Where the output is written to
    logfile = 'comd.out'
    # Store the output file (used for validation later)
    keep_files = [logfile]

    # Parameters - Compilers - Defined as their Spack specs (use spec or hash)
    # Only gcc on x86 but all three on ARM
    spec = parameter([
        'comd@1.1 %gcc@10.3.0',     # CoMD with the GCC compiler
        'comd@1.1 %arm@21.0.0.879', # CoMD with the Arm compiler
        'comd@1.1 %nvhpc@21.2'      # CoMD with the NVIDIA compiler
    ])

    def __init__(self, mpi, i, j, k):
        self.log_test_name = f'CoMD_strong_{mpi}'

        # CLI args. "strong" largely means more atoms with eam potential
        self.executable_opts = [f'&> comd.out -e -i {i} -j {j} -k {k} -x {i*40} -y {j*40} -z {k*40}']

        # Scale MPI to confirm that more work takes similar time 
        self.parallelism = { 'nodes' : 1, 'mpi' : mpi, 'omp' : 1}

    # Code validation
    @run_before('sanity')
    def set_sanity_patterns(self):

        # Use the logfile for validation testing and performance
        ratio_regex = r'\s+eFinal/eInitial\s+:\s+(\S+)'
        energy_ratio = sn.extractsingle(ratio_regex, self.logfile, 1, float)

        # bounds for the entergy ratio, which should end up approximately 1
        expected_lower = 0.99
        expected_upper = 1.01

        self.sanity_patterns = sn.assert_bounded(energy_ratio, expected_lower, expected_upper)

        # timing is taken from the code's self-reporting numbers
        self.reference = {
            '*': {'Total Time': (0, None, None, 's'),}
        }

        pref_regex = r'\s+total\s+1\s+(\S+)'
        self.perf_patterns = {
            'Total Time': sn.extractsingle(pref_regex, self.logfile, 1, float, item=-1)
        }

@rfm.simple_test
class CoMDTest1(CoMDTest):
    def __init__(self):
        super().__init__(mpi=1, i=1, j=1, k=1)

@rfm.simple_test
class CoMDTest2(CoMDTest):
    def __init__(self):
        super().__init__(mpi=2, i=2, j=1, k=1)

@rfm.simple_test
class CoMDTest4(CoMDTest):
    def __init__(self):
        super().__init__(mpi=4, i=2, j=2, k=1)

@rfm.simple_test
class CoMDTest8(CoMDTest):
    def __init__(self):
        super().__init__(mpi=8, i=2, j=2, k=2)

@rfm.simple_test
class CoMDTest16(CoMDTest):
    def __init__(self):
        super().__init__(mpi=16, i=4, j=2, k=2)

@rfm.simple_test
class CoMDTest32(CoMDTest):
    def __init__(self):
        super().__init__(mpi=32, i=4, j=4, k=2)

@rfm.simple_test
class CoMDTest64(CoMDTest):
    def __init__(self):
        super().__init__(mpi=64, i=4, j=4, k=4)

