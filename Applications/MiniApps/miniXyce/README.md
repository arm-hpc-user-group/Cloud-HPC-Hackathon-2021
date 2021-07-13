# miniXyce 

**Description:** Portable proxy of some of the key capabilities in the electrical modeling Xyce

**URL:** https://github.com/Mantevo/miniXyc 

**Team:**  

## Compilation

### Spack Package Modification

Details of any changes to the Spack recipe used.

Git commit hash of checkout for pacakage:

Pull request for Spack recipe changes:

### Building miniXyce



#### Compiler 1

```
spack install <app>%<compiler1>
```

```
$ spack spec -Il <app>%<compiler1>

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
MiniXyce_short_test_minixyce__gcc_10_3_0_N_1_MPI_64_OMP_1
- aws:c6gn
   - builtin
      * num_tasks: 64
      * Total Time: 39.7227 s
------------------------------------------------------------------------------
MiniXyce_short_test_minixyce__gcc_10_3_0_N_1_MPI_32_OMP_1
   - builtin
      * num_tasks: 32
      * Total Time: 69.0703 s
------------------------------------------------------------------------------
MiniXyce_short_test_minixyce__gcc_10_3_0_N_1_MPI_16_OMP_1
   - builtin
      * num_tasks: 16
      * Total Time: 153.912 s
------------------------------------------------------------------------------
MiniXyce_short_test_minixyce__gcc_10_3_0_N_1_MPI_8_OMP_1
   - builtin
      * num_tasks: 8
      * Total Time: 359.213 s
------------------------------------------------------------------------------
MiniXyce_short_test_minixyce__gcc_10_3_0_N_1_MPI_4_OMP_1
   - builtin
      * num_tasks: 4
      * Total Time: 848.906 s
------------------------------------------------------------------------------
MiniXyce_short_test_minixyce__gcc_10_3_0_N_1_MPI_2_OMP_1
   - builtin
      * num_tasks: 2
      * Total Time: 310.014 s
------------------------------------------------------------------------------
MiniXyce_short_test_minixyce__arm_N_1_MPI_64_OMP_1
   - builtin
      * num_tasks: 64
      * Total Time: 45.7333 s
------------------------------------------------------------------------------
MiniXyce_short_test_minixyce__arm_N_1_MPI_32_OMP_1
   - builtin
      * num_tasks: 32
      * Total Time: 68.6743 s
------------------------------------------------------------------------------
MiniXyce_short_test_minixyce__arm_N_1_MPI_16_OMP_1
   - builtin
      * num_tasks: 16
      * Total Time: 164.17 s
------------------------------------------------------------------------------
MiniXyce_short_test_minixyce__arm_N_1_MPI_8_OMP_1
   - builtin
      * num_tasks: 8
      * Total Time: 422.918 s
------------------------------------------------------------------------------
MiniXyce_short_test_minixyce__arm_N_1_MPI_4_OMP_1
   - builtin
      * num_tasks: 4
      * Total Time: 840.92 s
------------------------------------------------------------------------------
MiniXyce_short_test_minixyce__arm_N_1_MPI_2_OMP_1
   - builtin
      * num_tasks: 2
      * Total Time: 358.462 s
------------------------------------------------------------------------------

```

### On-node Compiler Comparison

Performance comparison of two compilers.

| Cores | GCC@10.3.0 |  ARM@20.0  |
|-------|------------|------------|
|   2   |  310.014s  |  358.462s  |
|-------|------------|------------|
|   4   |  848.906s  |  840.92s   |
|-------|------------|------------|
|   8   |  359.213s  |  422.918s  |
|-------|------------|------------|
|  16   |  153.912s  |  164.17s   |
|-------|------------|------------|
|  32   |  69.0703s  |  68.6743s  |
|-------|------------|------------|
|  64   |  39.7227s  |  45.7333s  |


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
