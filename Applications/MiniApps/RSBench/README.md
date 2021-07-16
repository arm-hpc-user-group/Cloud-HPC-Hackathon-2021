# RSBench 

**Description:** A mini-app to represent the multipole resonance representation lookup cross section algorithm., C

**URL:** https://github.com/ANL-CESAR/RSBench

**Team:** Deepneuron purple

## Compilation

### Spack Package Modification

Details of any changes to the Spack recipe used.

Git commit hash of checkout for pacakage:

Pull request for Spack recipe changes:

### Building RSBench from source

1. cloned the RSBench repository
2. make sure a compiler is loaded, or specify it with `export CC=clang`
3. run `make`
4. to execute the program, run `./RSBench`

### Spack Package Modification

update to the latest, note we are only doing thread offloading variant
```
# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Rsbench(MakefilePackage):
    """# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Rsbench(MakefilePackage):
    """A mini-app to represent the multipole resonance representation lookup
       cross section algorithm."""

    homepage = "https://github.com/ANL-CESAR/RSBench"
    url = "https://github.com/ANL-CESAR/RSBench/archive/refs/tags/v12.tar.gz"

    version('12', sha256='2e437dbdaf7bf12bb9ade429d46a9e74fd519fc4686777a452770790d0546499')
    version('2',  sha256='1e97a38a863836e98cedc5cc669f8fdcaed905fafdc921d2bce32319b3e157ff')
    version('0',  sha256='95c06cf4cb6f396f9964d5e4b58a477bf9d7131cd39804480f1cb74e9310b271')

    tags = ['proxy-app']

    variant('openmp-threading', default=True,
            description='This is the "default" version of RSBench that is appropriate for serial and multicore CPU architectures. The method of parallelism is via the OpenMP threading model.')
    
    build_directory = 'openmp-threading'

    @property
    def build_targets(self):
        targets = []

        cflags = ''
        ldflags = '-lm'

        if self.compiler.name == 'gcc':
            cflags += '-std=gnu99 -ffast-math '
        elif self.compiler.name == 'intel':
            cflags += ' -xhost -ansi-alias -no-prec-div '
        elif self.compiler.name == 'pgi':
            cflags += ' -fastsse '
        # elif self.compiler.name == 'arm':
        #     cflags += ' -O3 '

        cflags += self.compiler.openmp_flag

        targets.append('CFLAGS={0}'.format(cflags))
        targets.append('LDFLAGS={0}'.format(ldflags))

        return targets

    def install(self, spec, prefix):
        mkdir(prefix.bin)
        install('openmp-threading/rsbench', prefix.bin)

```

#### GCC Compiler

```
$ spack install rsbench@12%gcc@10.3.0
==> Installing rsbench-12-6xsbxe54rtpbebgql3zh2i2romk5txfo
==> No binary for rsbench-12-6xsbxe54rtpbebgql3zh2i2romk5txfo found: installing from source
==> Using cached archive: /home/mh/.spack/cache/sources/_source-cache/archive/2e/2e437dbdaf7bf12bb9ade429d46a9e74fd519fc4686777a452770790d0546499.tar.gz
==> No patches needed for rsbench
==> rsbench: Executing phase: 'edit'
==> rsbench: Executing phase: 'build'
==> rsbench: Executing phase: 'install'
==> rsbench: Successfully installed rsbench-12-6xsbxe54rtpbebgql3zh2i2romk5txfo
  Fetch: 0.00s.  Build: 0.22s.  Total: 0.22s.
[+] /scratch/opt/spack/linux-amzn2-skylake_avx512/gcc-10.3.0/rsbench-12-6xsbxe54rtpbebgql3zh2i2romk5txfo
```

```
$ spack spec -Il rsbench@12%gcc@10.3.0
Input spec
--------------------------------
 -   rsbench@12%gcc@10.3.0

Concretized
--------------------------------
[+]  6xsbxe5  rsbench@12%gcc@10.3.0+openmp-threading arch=linux-amzn2-skylake_avx512

```

#### nvhpc Compiler
```
$ spack install rsbench@12%nvhpc@21.2
==> Installing rsbench-12-vnq4upk2uicztb3j2joscq2izmhmzwl6
==> No binary for rsbench-12-vnq4upk2uicztb3j2joscq2izmhmzwl6 found: installing from source
==> Using cached archive: /home/mh/.spack/cache/sources/_source-cache/archive/2e/2e437dbdaf7bf12bb9ade429d46a9e74fd519fc4686777a452770790d0546499.tar.gz
==> No patches needed for rsbench
==> rsbench: Executing phase: 'edit'
==> rsbench: Executing phase: 'build'
==> rsbench: Executing phase: 'install'
==> rsbench: Successfully installed rsbench-12-vnq4upk2uicztb3j2joscq2izmhmzwl6
  Fetch: 0.00s.  Build: 0.37s.  Total: 0.37s.
[+] /scratch/opt/spack/linux-amzn2-skylake_avx512/nvhpc-21.2/rsbench-12-vnq4upk2uicztb3j2joscq2izmhmzwl6
```

```
$ spack spec -Il rsbench@12%nvhpc@21.2
Input spec
--------------------------------
 -   rsbench@12%nvhpc@21.2

Concretized
--------------------------------
[+]  vnq4upk  rsbench@12%nvhpc@21.2+openmp-threading arch=linux-amzn2-skylake_avx512
```

## OpenMP Test Case

```
/software/reframe/bin/reframe -c /software/deepneuron-purple/rsbenchtest/rsbench_reframe.py -r --performance-report -v
```

reframe file
```
import reframe as rfm
import reframe.utility.sanity as sn
import hackathon as hack

@rfm.simple_test
class RSbenchTest(hack.HackathonBase):
    # Where to run the binaries 'aws:c6gn' on Arm or 'aws:c5n' on Intel
    valid_systems = ['aws:c6gn', 'aws:c5n']

    # Logging Variables
    log_team_name = 'DeepNeuron Purple'
    log_app_name = 'RSbench'
    log_test_name = 'openmp'

    # Define test case
    # In this case we download the file from GitHub and write as ---.in - the expected input file
    prerun_cmds = []

    # Define Execution
    # Binary to run
    executable = 'rsbench'
    # Command line options to pass
    executable_opts = []
    # Where the output is written to
    logfile = 'rsbench.out'
    # Store the output file (used for validation later)
    keep_files = [logfile]


    # Parameters - Compilers - Defined as their Spack specs (use spec or hash)
    spec = parameter([
        'rsbench@12% gcc@10.3.0',     #GCC compiler
        #'rsbench@1.1 %arm@21.0.0.879', #Intel compiler
        'rsbench@12% nvhpc@21.2'      #PGI compiler
    ])

    # Parameters - MPI / Threads - Used for scaling studies
    parallelism = parameter([
        # { 'nodes' : 1, 'mpi' : 1, 'omp' : 1}
        { 'nodes' : 1, 'mpi' : 1, 'omp' : 1},
        { 'nodes' : 1, 'mpi' : 1, 'omp' : 2},
        { 'nodes' : 1, 'mpi' : 1, 'omp' : 4},
        { 'nodes' : 1, 'mpi' : 1, 'omp' : 8},
	{ 'nodes' : 1, 'mpi' : 1, 'omp' : 16},
	{ 'nodes' : 1, 'mpi' : 1, 'omp' : 32},
	{ 'nodes' : 1, 'mpi' : 1, 'omp' : 64},
    ])


    # Code validation
    @run_before('sanity')
    def set_sanity_patterns(self):

       # Validation Testing
       self.sanity_patterns = sn.assert_found(
            r'Simulation Complete.', self.stdout)

       # Performance Testing - FOM Total Time units 's'
       # We dont set an expected value
       self.reference = {
          '*': {'Total Time': (0, None, None, 's'),}
       }

       # CloverLeaf prints the 'Wall clock' every timestep - so extract all lines matching the regex
       pref_regex = r'Runtime:\s+(\S+)'
       self.perf_patterns = {
               'Total Time': sn.extractsingle(pref_regex, self.stdout, 1, float, item=-1)
       }

```

### Validation

For this test case we checked the string "Simulation Complete." to verify that the calculation is completed.
However, this validation method is insufficient as the calculation result could be different.

Ideally, you should check "Verification checksum"
```
================================================================================
                                   SIMULATION
================================================================================
Beginning history based simulation...
Simulation Complete.
================================================================================
                                     RESULTS
================================================================================
Threads:               72
Runtime:               22.417 seconds
Lookups:               10,200,000
Lookups/s:             455,007
Verification checksum: 351485 (Valid)
================================================================================
```
### ReFrame Output

```
[  PASSED  ] Ran 14/14 test case(s) from 14 check(s) (0 failure(s), 0 skipped)
[==========] Finished on Fri Jul 16 11:16:02 2021 
==============================================================================
PERFORMANCE REPORT
------------------------------------------------------------------------------
RSbench_yusuke_rsbench_12__gcc_10_3_0_N_1_MPI_1_OMP_1
- aws:c5n
   - builtin
      * num_tasks: 1
      * Total Time: 1251.635 s
------------------------------------------------------------------------------
RSbench_yusuke_rsbench_12__gcc_10_3_0_N_1_MPI_1_OMP_2
   - builtin
      * num_tasks: 1
      * Total Time: 708.768 s
------------------------------------------------------------------------------
RSbench_yusuke_rsbench_12__gcc_10_3_0_N_1_MPI_1_OMP_4
   - builtin
      * num_tasks: 1
      * Total Time: 376.402 s
------------------------------------------------------------------------------
RSbench_yusuke_rsbench_12__gcc_10_3_0_N_1_MPI_1_OMP_8
   - builtin
      * num_tasks: 1
      * Total Time: 196.672 s
------------------------------------------------------------------------------
RSbench_yusuke_rsbench_12__gcc_10_3_0_N_1_MPI_1_OMP_16
   - builtin
      * num_tasks: 1
      * Total Time: 95.934 s
------------------------------------------------------------------------------
RSbench_yusuke_rsbench_12__gcc_10_3_0_N_1_MPI_1_OMP_32
   - builtin
      * num_tasks: 1
      * Total Time: 48.346 s
------------------------------------------------------------------------------
RSbench_yusuke_rsbench_12__gcc_10_3_0_N_1_MPI_1_OMP_64
   - builtin
      * num_tasks: 1
      * Total Time: 24.064 s
------------------------------------------------------------------------------
RSbench_yusuke_rsbench_12__nvhpc_21_2_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Total Time: 638.504 s
------------------------------------------------------------------------------
RSbench_yusuke_rsbench_12__nvhpc_21_2_N_1_MPI_1_OMP_2
   - builtin
      * num_tasks: 1
      * Total Time: 402.173 s
------------------------------------------------------------------------------
RSbench_yusuke_rsbench_12__nvhpc_21_2_N_1_MPI_1_OMP_4
   - builtin
      * num_tasks: 1
      * Total Time: 281.048 s
------------------------------------------------------------------------------
RSbench_yusuke_rsbench_12__nvhpc_21_2_N_1_MPI_1_OMP_8
   - builtin
      * num_tasks: 1
      * Total Time: 121.778 s
------------------------------------------------------------------------------
RSbench_yusuke_rsbench_12__nvhpc_21_2_N_1_MPI_1_OMP_16
   - builtin
      * num_tasks: 1
      * Total Time: 57.982 s
------------------------------------------------------------------------------
RSbench_yusuke_rsbench_12__nvhpc_21_2_N_1_MPI_1_OMP_32
   - builtin
      * num_tasks: 1
      * Total Time: 35.091 s
------------------------------------------------------------------------------
RSbench_yusuke_rsbench_12__nvhpc_21_2_N_1_MPI_1_OMP_64
   - builtin
      * num_tasks: 1
      * Total Time: 15.347 s
------------------------------------------------------------------------------
```

### On-node Compiler Comparison

Performance comparison of two compilers.

| Cores  | gcc | nvhpc |
|--------|------------|------------|
|  1     |   1088.4  |    634.105 |
|  2     |   748.998 |    396.431 |
|  4     |   382.686 |   276.921  |
|  8     |   191.75  |   116.096  |
|  16    |   95.004  |    64.305  |
|  32    |   48.059  |   30.314   |
|  64    |   24.066  |   15.317   |


### Serial Hot-spot Profile

List of top-10 functions / code locations from a serial profile.

Profiling command used:
```
:
```

| Position | Routine | Time (s) | Time (%) |
|----------|---------|----------|----------|
| 1        |         |          |          |
| 2        |         |          |          |
| 3        |         |          |          |
| 4        |         |          |          |
| 5        |         |          |          |
| 6        |         |          |          |
| 7        |         |          |          |
| 8        |         |          |          |
| 9        |         |          |          |
| 10       |         |          |          |


### Full Node Hot-spot Profile

List of top-10 functions / code locations from a full node profile.

Profiling command used:
```
:
```

| Position | Routine | Time (s) | Time (%) | MPI (%) |
|----------|---------|----------|----------|---------|
| 1        |         |          |          |         |
| 2        |         |          |          |         |
| 3        |         |          |          |         |
| 4        |         |          |          |         |
| 5        |         |          |          |         |
| 6        |         |          |          |         |
| 7        |         |          |          |         |
| 8        |         |          |          |         |
| 9        |         |          |          |         |
| 10       |         |          |          |         |

### Strong Scaling Study

On-node scaling study for two compilers.

| Cores | Compiler 1 | Compiler 2 |
|-------|------------|------------|
| 1     |            |            |
| 2     |            |            |
| 4     |            |            |
| 8     |            |            |
| 16    |            |            |
| 32    |            |            |
| 64    |            |            |


### Off-Node Scaling Study

Off-node scaling study comparing C6g and C6gn instances.

| Nodes | Cores | C6g | C6gn |
|-------|-------|-----|------|
| 1     | 8     |     |      |
| 1     | 16    |     |      |
| 1     | 32    |     |      |
| 1     | 64    |     |      |
| 2     | 128   |     |      |
| 4     | 256   |     |      |
| 8     | 512   |     |      |


### On-Node Architecture Comparison

On-node scaling study for two architectures.

| Cores | C6gn (Aarch64) | C5n (X86) |
|-------|----------------|-----------|
| 1     |                |           |
| 2     |                |           |
| 4     |                |           |
| 8     |                |           |
| 16    |                |           |
| 32    |                |           |
| 64    |                |           |


## Optimisation

Details of steps taken to optimise performance of the application.
Please document work with compiler flags, maths libraries, system libraries, code optimisations, etc.

### Compiler Flag Tuning

Compiler flags before:
```
CFLAGS=
FFLAGS=
```

Compiler flags after:
```
CFLAGS=
FFLAGS=
```

#### Compiler Flag Performance

| Cores | Original Flags | New Flags |
|-------|----------------|-----------|
| 1     |                |           |
| 2     |                |           |
| 4     |                |           |
| 8     |                |           |
| 16    |                |           |
| 32    |                |           |
| 64    |                |           |


### Maths Library Report

Report on use of maths library calls generated by (Perf Lib Tools)[https://github.com/ARM-software/perf-libs-tools].
Please attach the corresponding apl files.


### Maths Library Optimisation

Performance analysis of the use of different maths libraries.


| Cores | OpenBLAS | ArmPL | BLIS | 
|-------|----------|-------| ---- |
| 1     |          |       |      |
| 2     |          |       |      |
| 4     |          |       |      |
| 8     |          |       |      |
| 16    |          |       |      |
| 32    |          |       |      |
| 64    |          |       |      |


### Performance Regression

How fast can you make the code?

Use all of the above aproaches and any others to make the code as fast as possible.
Demonstrate your gains by providing a scaling study for your test case, demonstrating the performance before and after.



## Report

### Compilation Summary

Details of lessons from compiling the application.

### Performance Summary

Details of lessons from analysing the performance of the application.


### Optimisation Summary

Details of lessons from performance optimising the application.
