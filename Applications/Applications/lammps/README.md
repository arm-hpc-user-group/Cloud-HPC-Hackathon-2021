# LAMMPS 

**Description:** LAMMPS stands for Large-scale Atomic/Molecular Massively Parallel Simulator. This package uses patch releases, not stable release. See https://github.com/spack/spack/pull/5342 for a detailed discussion.

**URL:** http://lammps.sandia.gov/

**Team:** Master of puppets 

## Compilation

### Spack Package Modification

Details of any changes to the Spack recipe used.

Git commit hash of checkout for pacakage:

Pull request for Spack recipe changes:

### Building LAMMPS



#### Compiler 1

```
spack install lammps@20210310%gcc@10.3.0
```

```
$ spack spec -Il lammps@20210310%gcc@10.3.0

```

## Test Case 1

[ReFrame Benchmark 1](#)

```
../bin/reframe -c benchmark.py -r --performance-report
```

### Validation

Details of the validation for `Test Case 1`.


### ReFrame Output

```
==============================================================================
PERFORMANCE REPORT
------------------------------------------------------------------------------
[ReFrame Setup]
  version:           3.7.0-dev.3+34ee3d0b
  command:           '/software/reframe/bin/reframe --stage /scratch/home/jmiarons -c benchmark.py -r --performance-report'
  launched by:       jmiarons@ip-10-0-0-218
  working directory: '/home/jmiarons/lammps'
  settings file:     '/software/reframe/settings.py'
  check search path: '/home/jmiarons/lammps/benchmark.py'
  stage directory:   '/scratch/home/jmiarons'
  output directory:  '/home/jmiarons/lammps/output'

/home/jmiarons/lammps/benchmark.py:45: WARNING: using the @rfm.run_before decorator from the rfm module is deprecated; please use the built-in decorator @run_before instead.
    @rfm.run_before('run')

[==========] Running 6 check(s)
[==========] Started on Fri Jul 16 15:00:36 2021 

[----------] started processing LAMMPSTest_lammps_20210310__gcc_10_3_0___nodes___2___mpi___72___omp___1_ (LAMMPSTest_lammps_20210310__gcc_10_3_0___nodes___2___mpi___72___omp___1_)
[ RUN      ] LAMMPSTest_lammps_20210310__gcc_10_3_0___nodes___2___mpi___72___omp___1_ on aws:c5n using builtin
[----------] finished processing LAMMPS_logo_test_lammps_20210310__gcc_10_3_0_N_2_MPI_72_OMP_1 (LAMMPSTest_lammps_20210310__gcc_10_3_0___nodes___2___mpi___72___omp___1_)

[----------] started processing LAMMPSTest_lammps_20210310__gcc_10_3_0___nodes___4___mpi___108___omp___1_ (LAMMPSTest_lammps_20210310__gcc_10_3_0___nodes___4___mpi___108___omp___1_)
[ RUN      ] LAMMPSTest_lammps_20210310__gcc_10_3_0___nodes___4___mpi___108___omp___1_ on aws:c5n using builtin
[----------] finished processing LAMMPS_logo_test_lammps_20210310__gcc_10_3_0_N_4_MPI_108_OMP_1 (LAMMPSTest_lammps_20210310__gcc_10_3_0___nodes___4___mpi___108___omp___1_)

[----------] started processing LAMMPSTest_lammps_20210310__gcc_10_3_0___nodes___8___mpi___144___omp___1_ (LAMMPSTest_lammps_20210310__gcc_10_3_0___nodes___8___mpi___144___omp___1_)
[ RUN      ] LAMMPSTest_lammps_20210310__gcc_10_3_0___nodes___8___mpi___144___omp___1_ on aws:c5n using builtin
[----------] finished processing LAMMPS_logo_test_lammps_20210310__gcc_10_3_0_N_8_MPI_144_OMP_1 (LAMMPSTest_lammps_20210310__gcc_10_3_0___nodes___8___mpi___144___omp___1_)

[----------] started processing LAMMPSTest_lammps_20210310__nvhpc_21_2___nodes___2___mpi___72___omp___1_ (LAMMPSTest_lammps_20210310__nvhpc_21_2___nodes___2___mpi___72___omp___1_)
[ RUN      ] LAMMPSTest_lammps_20210310__nvhpc_21_2___nodes___2___mpi___72___omp___1_ on aws:c5n using builtin
[----------] finished processing LAMMPS_logo_test_lammps_20210310__nvhpc_21_2_N_2_MPI_72_OMP_1 (LAMMPSTest_lammps_20210310__nvhpc_21_2___nodes___2___mpi___72___omp___1_)

[----------] started processing LAMMPSTest_lammps_20210310__nvhpc_21_2___nodes___4___mpi___108___omp___1_ (LAMMPSTest_lammps_20210310__nvhpc_21_2___nodes___4___mpi___108___omp___1_)
[ RUN      ] LAMMPSTest_lammps_20210310__nvhpc_21_2___nodes___4___mpi___108___omp___1_ on aws:c5n using builtin
[----------] finished processing LAMMPS_logo_test_lammps_20210310__nvhpc_21_2_N_4_MPI_108_OMP_1 (LAMMPSTest_lammps_20210310__nvhpc_21_2___nodes___4___mpi___108___omp___1_)

[----------] started processing LAMMPSTest_lammps_20210310__nvhpc_21_2___nodes___8___mpi___144___omp___1_ (LAMMPSTest_lammps_20210310__nvhpc_21_2___nodes___8___mpi___144___omp___1_)
[ RUN      ] LAMMPSTest_lammps_20210310__nvhpc_21_2___nodes___8___mpi___144___omp___1_ on aws:c5n using builtin
[----------] finished processing LAMMPS_logo_test_lammps_20210310__nvhpc_21_2_N_8_MPI_144_OMP_1 (LAMMPSTest_lammps_20210310__nvhpc_21_2___nodes___8___mpi___144___omp___1_)

[----------] waiting for spawned checks to finish
[       OK ] (1/6) LAMMPS_logo_test_lammps_20210310__gcc_10_3_0_N_4_MPI_108_OMP_1 on aws:c5n using builtin [compile: 0.005s run: 378.085s total: 378.108s]
[       OK ] (2/6) LAMMPS_logo_test_lammps_20210310__gcc_10_3_0_N_2_MPI_72_OMP_1 on aws:c5n using builtin [compile: 0.006s run: 632.677s total: 632.700s]
[       OK ] (3/6) LAMMPS_logo_test_lammps_20210310__nvhpc_21_2_N_2_MPI_72_OMP_1 on aws:c5n using builtin [compile: 0.004s run: 681.050s total: 681.070s]
[       OK ] (4/6) LAMMPS_logo_test_lammps_20210310__nvhpc_21_2_N_4_MPI_108_OMP_1 on aws:c5n using builtin [compile: 0.004s run: 773.576s total: 773.596s]
[       OK ] (5/6) LAMMPS_logo_test_lammps_20210310__gcc_10_3_0_N_8_MPI_144_OMP_1 on aws:c5n using builtin [compile: 0.006s run: 996.833s total: 996.855s]
[       OK ] (6/6) LAMMPS_logo_test_lammps_20210310__nvhpc_21_2_N_8_MPI_144_OMP_1 on aws:c5n using builtin [compile: 0.006s run: 1218.031s total: 1218.054s]
[----------] all spawned checks have finished

[  PASSED  ] Ran 6/6 test case(s) from 6 check(s) (0 failure(s), 0 skipped)
[==========] Finished on Fri Jul 16 15:20:56 2021  
------------------------------------------------------------------------------
```

### On-node Compiler Comparison

Performance comparison of two compilers.
Compiler 2: nvhpc@21.2

| Cores | GCC 10.3   | NVHPC 21.2 |
|-------|------------|------------|
| 1     | 1343       | 1338       |
| 2     | 1385       | 1380       |
| 4     | 1427       | 1426       |
| 8     | 1670       | 1668       |
| 16    | 2057       | 2026       |
| 32    | 2818       | 2762       |
| 64    | 0029       | 0029       |


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

Compiler 2: nvhpc@21.2

| Cores | GCC 10.3   | NVHPC 21.2 |
|-------|------------|------------|
| 1     | 1343       | 1338       |
| 2     | 1385       | 1380       |
| 4     | 1427       | 1426       |
| 8     | 1670       | 1668       |
| 16    | 2057       | 2026       |
| 32    | 2818       | 2762       |
| 64    | 0029       | 0029       |

### Off-Node Scaling Study

Off-node scaling study comparing C6g and C6gn instances.

| Nodes | Cores | C6g | C6gn |
|-------|-------|-----|------|
| 1     | 8     | -   | 1670 |
| 1     | 16    | -   | 2057 |
| 1     | 32    | -   | 2818 |
| 1     | 64    | -   | 0029 |
| 2     | 128   | -   | 0015 |
| 4     | 256   | -   | 0008 |
| 8     | 512   | -   | 0004 |


### On-Node Architecture Comparison

On-node scaling study for two architectures.

| Cores | C6gn (Aarch64) | C5n (X86) |
|-------|----------------|-----------|
| 1     | 1343           | 860       |
| 2     | 1385           | 742       |
| 4     | 1427           | 717       |
| 8     | 1670           | 839       |
| 16    | 2057           | 877       |
| 32    | 2818           | 963       |
| 64    | 0029           | 1246      |


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

The version using gcc was the easiest one and we did not face any trouble. For the nvhpc comipler we had to compile cmake and ffmpeg with gcc in order to get a binary, otherwise spack could not compile those two dependencies mentioned before. For the ARM compiler we could not generate a binary because we had trouble compiling the kim-api dependency using arm because there is a known bug in this version when compiling fortran code. We tried compiling lammps without kim-api but spack was still using kim-api even though we modified the cmake option in the package.py file.

### Performance Summary

It is awkward the times we achieved because with a whole node or more the time in ARM cluster is ridicoulisly low like 5 seconds and in the intel cluster it takes some minutes. We could not run any profiler to see why this is happening. If we follow the numbers we got the best option to run lammps is using gcc compiler and run with the max amount of nodes possible in an ARM cluster.

### Optimisation Summary

No optimization made :(
