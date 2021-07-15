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
iniXyce_short_test_minixyce__gcc_10_3_0_N_1_MPI_8_OMP_1
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

```
==============================================================================
PERFORMANCE REPORT
------------------------------------------------------------------------------
MiniXyce_short_test_minixyce__gcc_10_3_0_N_1_MPI_64_OMP_1
- aws:c6gn
   - builtin
      * num_tasks: 64
      * Total Time: 52.2978 s
------------------------------------------------------------------------------
MiniXyce_short_test_minixyce__gcc_10_3_0_N_1_MPI_32_OMP_1
   - builtin
      * num_tasks: 32
      * Total Time: 85.407 s
------------------------------------------------------------------------------
MiniXyce_short_test_minixyce__gcc_10_3_0_N_1_MPI_16_OMP_1
   - builtin
      * num_tasks: 16
      * Total Time: 184.024 s
------------------------------------------------------------------------------
MiniXyce_short_test_minixyce__gcc_10_3_0_N_1_MPI_8_OMP_1
   - builtin
      * num_tasks: 8
      * Total Time: 476.893 s
------------------------------------------------------------------------------
MiniXyce_short_test_minixyce__gcc_10_3_0_N_1_MPI_4_OMP_1
   - builtin
      * num_tasks: 4
      * Total Time: 934.919 s
------------------------------------------------------------------------------
MiniXyce_short_test_minixyce__gcc_10_3_0_N_1_MPI_2_OMP_1
   - builtin
      * num_tasks: 2
      * Total Time: 498.911 s
------------------------------------------------------------------------------
MiniXyce_short_test_minixyce__gcc_10_3_0_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Total Time: 111.029 s
------------------------------------------------------------------------------
MiniXyce_short_test_minixyce__arm_N_1_MPI_64_OMP_1
   - builtin
      * num_tasks: 64
      * Total Time: 39.9701 s
------------------------------------------------------------------------------
MiniXyce_short_test_minixyce__arm_N_1_MPI_32_OMP_1
   - builtin
      * num_tasks: 32
      * Total Time: 54.2542 s
------------------------------------------------------------------------------
MiniXyce_short_test_minixyce__arm_N_1_MPI_16_OMP_1
   - builtin
      * num_tasks: 16
      * Total Time: 136.656 s
------------------------------------------------------------------------------
MiniXyce_short_test_minixyce__arm_N_1_MPI_8_OMP_1
   - builtin
      * num_tasks: 8
      * Total Time: 368.376 s
------------------------------------------------------------------------------
MiniXyce_short_test_minixyce__arm_N_1_MPI_4_OMP_1
   - builtin
      * num_tasks: 4
      * Total Time: 732.316 s
------------------------------------------------------------------------------
MiniXyce_short_test_minixyce__arm_N_1_MPI_2_OMP_1
   - builtin
      * num_tasks: 2
      * Total Time: 284.202 s
------------------------------------------------------------------------------
MiniXyce_short_test_minixyce__arm_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Total Time: 16.5698 s
------------------------------------------------------------------------------
MiniXyce_short_test_minixyce__nvhpc_N_1_MPI_64_OMP_1
   - builtin
      * num_tasks: 64
      * Total Time: 51.5188 s
------------------------------------------------------------------------------
MiniXyce_short_test_minixyce__nvhpc_N_1_MPI_32_OMP_1
   - builtin
      * num_tasks: 32
      * Total Time: 80.6583 s
------------------------------------------------------------------------------
MiniXyce_short_test_minixyce__nvhpc_N_1_MPI_16_OMP_1
   - builtin
      * num_tasks: 16
      * Total Time: 176.202 s
------------------------------------------------------------------------------
MiniXyce_short_test_minixyce__nvhpc_N_1_MPI_8_OMP_1
   - builtin
      * num_tasks: 8
      * Total Time: 523.669 s
------------------------------------------------------------------------------
MiniXyce_short_test_minixyce__nvhpc_N_1_MPI_4_OMP_1
   - builtin
      * num_tasks: 4
      * Total Time: 948.424 s
------------------------------------------------------------------------------
MiniXyce_short_test_minixyce__nvhpc_N_1_MPI_2_OMP_1
   - builtin
      * num_tasks: 2
      * Total Time: 513.17 s
------------------------------------------------------------------------------
MiniXyce_short_test_minixyce__nvhpc_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Total Time: 105.56 s
------------------------------------------------------------------------------

```

### On-node Compiler Comparison

Performance comparison of two compilers.

| Cores | GCC@10.3.0 |  ARM@20.0  |  NVHPC
|   2   |  310.014s  |  358.462s  | 349.158 
|   4   |  848.906s  |  840.92s   | 786.762 
|   8   |  359.213s  |  422.918s  | 389.469
|  16   |  153.912s  |  164.17s   | 155.474
|  32   |  69.0703s  |  68.6743s  | 71.611 
|  64   |  39.7227s  |  45.7333s  | 44.378


### Serial Hot-spot Profile

List of top-10 functions / code locations from a serial profile.

Profiling command used:
```
:map -profile /opt/amazon/openmpi/bin/mpiexec --np 1 miniXyce.x --circuit tests/cir6.net --t_start 0 --pf tests/default_params.txt

```

| Position | Routine | Time (s) | Time (%) |
|----------|---------|----------|----------|
| 1        |  mX_matrix_utils::gmres(mX_matrix_utils::distributed_sparse_matrix*, std::vector<double, std::allocator<double       |          |     33.8%     |
| 2        |   mX_matrix_utils::sparse_matrix_vector_product(mX_matrix_utils::distributed_sparse_matrix*, std::vector<double, std::allocator<double      |          |   12.1%       |
| 3        |  __aarch64_swp4_rel       |          |   8.2%       |
| 4        |  __printf_fp_l       |          |   4.9"%       |
| 5        |  hack_digit       |          |    4.5%      |
| 6        |    malloc     |          |     3.9%     |
| 7        |    _int_malloc     |          |  3.6%        |
| 8        |  _int_free       |          |   3.5%       |
| 9        |  malloc_consolidate       |          |  3.1%        |
| 10       |  __aarch64_cas4_acq       |          |   3.1%       |


### Full Node Hot-spot Profile

List of top-10 functions / code locations from a full node profile.

Profiling command used:
```
:map -profile /opt/amazon/openmpi/bin/mpiexec --np 64 miniXyce.x --circuit tests/cir6.net --t_start 0 --pf tests/default_params.txt
```

| Position | Routine | Time (s) | Time (%) | MPI (%) |
|----------|---------|----------|----------|---------|
| 1        |  MPI_Allreduce       |          |          |   94.7%      |
| 2        | MPI_Recv        |          |          |   4.1%      |
| 3        | MPI_Send        |          |          |    0.7%     |
| 4        |  std::_Rb_tree<int, std::pair<int const, double>, std::_Select1st<std::pair<int const, double       |          |          |   <0.1%      |
| 5        |    std::vector<double, std::allocator<double..     |          |          |      <0.1%   |
| 6        |   __gnu_cxx::__aligned_membuf<std::pair<int const, double      |          |          |  <0.1%       |
| 7        |  mX_matrix_utils::gmres(mX_matrix_utils::distributed_sparse_matrix*, std::vector<double, std::allocator<double       |          |          |      <0.1%   |
| 8        |  std::less<int>::operator()(int const&, int const&) const       |          |          |      <0.1%   |
| 9        |   mX_matrix_utils::sparse_matrix_vector_product(mX_matrix_utils::distributed_sparse_matrix*, std::vector<double, std::allocator<double      |          |          |       <0.1%  |
| 10       |  std::_Select1st<std::pair<int const, double       |          |          |        <0.1% |

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
| 1     | 8     |     |363.83|
| 1     | 16    |     |136.99|
| 1     | 32    |     |61.952|
| 1     | 64    |     |38.711|
| 2     | 128   |     |66.053|
| 4     | 256   |     |53.526|
| 8     | 512   |     |38.311|


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
CFLAGS=" "
FFLAGS=" "
```

Compiler flags after:
```
CFLAGS=-O3 -march=native -funroll-loops -mtune=cortex-a76
FFLAGS=-O3 -march=native -funroll-loops -mtune=cortex-a76
```

#### Compiler Flag Performance

We didn't observe any significant performance improvement by adding the new flags.

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
