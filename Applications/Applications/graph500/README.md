# graph500 

**Description:** Graph500 reference implementations.

**URL:** https://graph500.org

**Team:** Master of puppets

## Compilation

### Spack Package Modification

Details of any changes to the Spack recipe used.

Git commit hash of checkout for pacakage:

Pull request for Spack recipe changes:

### Building graph500



#### Compiler 1
x86 machine:

```
spack install graph500@3.0.0%gcc@10.3.0
```

```
$ spack spec -Il graph500@3.0.0%gcc@10.3.0

```

## Test Case 1

[ReFrame Benchmark 1](benchmark.py)

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
  command:           '/software/reframe/bin/reframe -c benchmark.py -r --performance-report'
  launched by:       cbayona@ip-10-0-0-218
  working directory: '/home/cbayona/Cloud-HPC-Hackathon-2021/Applications/Applications/graph500'
  settings file:     '/software/reframe/settings.py'
  check search path: '/home/cbayona/Cloud-HPC-Hackathon-2021/Applications/Applications/graph500/benchmark.py'
  stage directory:   '/home/cbayona/Cloud-HPC-Hackathon-2021/Applications/Applications/graph500/stage'
  output directory:  '/home/cbayona/Cloud-HPC-Hackathon-2021/Applications/Applications/graph500/output'

[==========] Running 10 check(s)
[==========] Started on Fri Jul 16 13:27:07 2021 

[----------] started processing Graph500Test_graph500_3_0_0__gcc_10_3_0___nodes___1___mpi___1___omp___1_ (Graph500Test_graph500_3_0_0__gcc_10_3_0___nodes___1___mpi___1___omp___1_)
[ RUN      ] Graph500Test_graph500_3_0_0__gcc_10_3_0___nodes___1___mpi___1___omp___1_ on aws:c5n using builtin
[----------] finished processing G500_x86_scalab_graph500_3_0_0__gcc_10_3_0_N_1_MPI_1_OMP_1 (Graph500Test_graph500_3_0_0__gcc_10_3_0___nodes___1___mpi___1___omp___1_)

[----------] started processing Graph500Test_graph500_3_0_0__gcc_10_3_0___nodes___1___mpi___2___omp___1_ (Graph500Test_graph500_3_0_0__gcc_10_3_0___nodes___1___mpi___2___omp___1_)
[ RUN      ] Graph500Test_graph500_3_0_0__gcc_10_3_0___nodes___1___mpi___2___omp___1_ on aws:c5n using builtin
[----------] finished processing G500_x86_scalab_graph500_3_0_0__gcc_10_3_0_N_1_MPI_2_OMP_1 (Graph500Test_graph500_3_0_0__gcc_10_3_0___nodes___1___mpi___2___omp___1_)

[----------] started processing Graph500Test_graph500_3_0_0__gcc_10_3_0___nodes___1___mpi___4___omp___1_ (Graph500Test_graph500_3_0_0__gcc_10_3_0___nodes___1___mpi___4___omp___1_)
[ RUN      ] Graph500Test_graph500_3_0_0__gcc_10_3_0___nodes___1___mpi___4___omp___1_ on aws:c5n using builtin
[----------] finished processing G500_x86_scalab_graph500_3_0_0__gcc_10_3_0_N_1_MPI_4_OMP_1 (Graph500Test_graph500_3_0_0__gcc_10_3_0___nodes___1___mpi___4___omp___1_)

[----------] started processing Graph500Test_graph500_3_0_0__gcc_10_3_0___nodes___1___mpi___8___omp___1_ (Graph500Test_graph500_3_0_0__gcc_10_3_0___nodes___1___mpi___8___omp___1_)
[ RUN      ] Graph500Test_graph500_3_0_0__gcc_10_3_0___nodes___1___mpi___8___omp___1_ on aws:c5n using builtin
[----------] finished processing G500_x86_scalab_graph500_3_0_0__gcc_10_3_0_N_1_MPI_8_OMP_1 (Graph500Test_graph500_3_0_0__gcc_10_3_0___nodes___1___mpi___8___omp___1_)

[----------] started processing Graph500Test_graph500_3_0_0__gcc_10_3_0___nodes___1___mpi___16___omp___1_ (Graph500Test_graph500_3_0_0__gcc_10_3_0___nodes___1___mpi___16___omp___1_)
[ RUN      ] Graph500Test_graph500_3_0_0__gcc_10_3_0___nodes___1___mpi___16___omp___1_ on aws:c5n using builtin
[----------] finished processing G500_x86_scalab_graph500_3_0_0__gcc_10_3_0_N_1_MPI_16_OMP_1 (Graph500Test_graph500_3_0_0__gcc_10_3_0___nodes___1___mpi___16___omp___1_)

[----------] started processing Graph500Test_graph500_3_0_0__gcc_10_3_0___nodes___1___mpi___32___omp___1_ (Graph500Test_graph500_3_0_0__gcc_10_3_0___nodes___1___mpi___32___omp___1_)
[ RUN      ] Graph500Test_graph500_3_0_0__gcc_10_3_0___nodes___1___mpi___32___omp___1_ on aws:c5n using builtin
[----------] finished processing G500_x86_scalab_graph500_3_0_0__gcc_10_3_0_N_1_MPI_32_OMP_1 (Graph500Test_graph500_3_0_0__gcc_10_3_0___nodes___1___mpi___32___omp___1_)

[----------] started processing Graph500Test_graph500_3_0_0__gcc_10_3_0___nodes___1___mpi___64___omp___1_ (Graph500Test_graph500_3_0_0__gcc_10_3_0___nodes___1___mpi___64___omp___1_)
[ RUN      ] Graph500Test_graph500_3_0_0__gcc_10_3_0___nodes___1___mpi___64___omp___1_ on aws:c5n using builtin
[----------] finished processing G500_x86_scalab_graph500_3_0_0__gcc_10_3_0_N_1_MPI_64_OMP_1 (Graph500Test_graph500_3_0_0__gcc_10_3_0___nodes___1___mpi___64___omp___1_)

[----------] started processing Graph500Test_graph500_3_0_0__gcc_10_3_0___nodes___2___mpi___128___omp___1_ (Graph500Test_graph500_3_0_0__gcc_10_3_0___nodes___2___mpi___128___omp___1_)
[ RUN      ] Graph500Test_graph500_3_0_0__gcc_10_3_0___nodes___2___mpi___128___omp___1_ on aws:c5n using builtin
[----------] finished processing G500_x86_scalab_graph500_3_0_0__gcc_10_3_0_N_2_MPI_128_OMP_1 (Graph500Test_graph500_3_0_0__gcc_10_3_0___nodes___2___mpi___128___omp___1_)

[----------] started processing Graph500Test_graph500_3_0_0__gcc_10_3_0___nodes___4___mpi___256___omp___1_ (Graph500Test_graph500_3_0_0__gcc_10_3_0___nodes___4___mpi___256___omp___1_)
[ RUN      ] Graph500Test_graph500_3_0_0__gcc_10_3_0___nodes___4___mpi___256___omp___1_ on aws:c5n using builtin
[     HOLD ] Graph500Test_graph500_3_0_0__gcc_10_3_0___nodes___4___mpi___256___omp___1_ on aws:c5n using builtin
[----------] finished processing Graph500Test_graph500_3_0_0__gcc_10_3_0___nodes___4___mpi___256___omp___1_ (Graph500Test_graph500_3_0_0__gcc_10_3_0___nodes___4___mpi___256___omp___1_)

[----------] started processing Graph500Test_graph500_3_0_0__gcc_10_3_0___nodes___8___mpi___512___omp___1_ (Graph500Test_graph500_3_0_0__gcc_10_3_0___nodes___8___mpi___512___omp___1_)
[ RUN      ] Graph500Test_graph500_3_0_0__gcc_10_3_0___nodes___8___mpi___512___omp___1_ on aws:c5n using builtin
[     HOLD ] Graph500Test_graph500_3_0_0__gcc_10_3_0___nodes___8___mpi___512___omp___1_ on aws:c5n using builtin
[----------] finished processing Graph500Test_graph500_3_0_0__gcc_10_3_0___nodes___8___mpi___512___omp___1_ (Graph500Test_graph500_3_0_0__gcc_10_3_0___nodes___8___mpi___512___omp___1_)

[----------] waiting for spawned checks to finish

[       OK ] ( 1/10) G500_x86_scalab_graph500_3_0_0__gcc_10_3_0_N_1_MPI_8_OMP_1 on aws:c5n using builtin [compile: 0.005s run: 56.925s total: 56.946s]
[       OK ] ( 2/10) G500_x86_scalab_graph500_3_0_0__gcc_10_3_0_N_1_MPI_4_OMP_1 on aws:c5n using builtin [compile: 0.005s run: 73.903s total: 73.924s]
[       OK ] ( 3/10) G500_x86_scalab_graph500_3_0_0__gcc_10_3_0_N_1_MPI_16_OMP_1 on aws:c5n using builtin [compile: 0.006s run: 73.883s total: 73.904s]
[       OK ] ( 4/10) G500_x86_scalab_graph500_3_0_0__gcc_10_3_0_N_1_MPI_32_OMP_1 on aws:c5n using builtin [compile: 0.005s run: 105.471s total: 105.492s]
[       OK ] ( 5/10) G500_x86_scalab_graph500_3_0_0__gcc_10_3_0_N_2_MPI_128_OMP_1 on aws:c5n using builtin [compile: 0.005s run: 105.662s total: 105.683s]
[       OK ] ( 6/10) G500_x86_scalab_graph500_3_0_0__gcc_10_3_0_N_1_MPI_2_OMP_1 on aws:c5n using builtin [compile: 0.005s run: 108.389s total: 108.410s]
[       OK ] ( 7/10) G500_x86_scalab_graph500_3_0_0__gcc_10_3_0_N_1_MPI_64_OMP_1 on aws:c5n using builtin [compile: 0.005s run: 107.678s total: 107.699s]
[       OK ] ( 8/10) G500_x86_scalab_graph500_3_0_0__gcc_10_3_0_N_4_MPI_256_OMP_1 on aws:c5n using builtin [compile: 0.005s run: 61.031s total: 133.238s]
[       OK ] ( 9/10) G500_x86_scalab_graph500_3_0_0__gcc_10_3_0_N_1_MPI_1_OMP_1 on aws:c5n using builtin [compile: 0.006s run: 135.541s total: 135.562s]
[       OK ] (10/10) G500_x86_scalab_graph500_3_0_0__gcc_10_3_0_N_8_MPI_512_OMP_1 on aws:c5n using builtin [compile: 0.006s run: 643.702s total: 699.067s]
[----------] all spawned checks have finished

[  PASSED  ] Ran 10/10 test case(s) from 10 check(s) (0 failure(s), 0 skipped)
[==========] Finished on Fri Jul 16 13:38:49 2021

------------------------------------------------------------------------------
```

### On-node Compiler Comparison

Performance comparison of two compilers.

| Cores | Compiler 1 | Compiler 2 |
|-------|------------|------------|
|       |            |            |


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

We were not able to extract the TEPS via the reframe script but we created another python script
to do the job: [TEPS extraction](extract_TEPS_graph500.py)

| Cores | Compiler 1  | Compiler 2 |
|-------|-------------|------------|
| 1     | 6.22528e+07 |            |
| 2     | 5.91513e+07 |            |
| 4     | 1.10096e+08 |            |
| 8     | 2.03358e+08 |            |
| 16    | 3.45317e+08 |            |
| 32    | 3.45195e+08 |            |
| 64    | 3.40478e+08 |            |
| 128   | 4.45355e+08 |            |
| 256   | 6.98172e+08 |            |
| 512   | 5.66846e+08 |            |


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
CFLAGS=-Drestrict=__restrict__ -O3 -DGRAPH_GENERATOR_MPI -DREUSE_CSR_FOR_VALIDATION -I../aml
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

Graph500 does not use any math library.

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
