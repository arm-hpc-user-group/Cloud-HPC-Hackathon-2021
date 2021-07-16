# CANDLE-benchmarks

**Description:** ECP-CANDLE Benchmarks

**URL:** https://github.com/ECP-CANDLE/Benchmarks

**Team:** DeepNeuron-Blue

## Compilation

```
candle-benchmarks%gcc +mpi ^openblas ^binutils+gold+ld  ^automake@1.15: ^py-scipy@1.6.3 ^py-gast@0.3.3 ^py-pybind11@2.6.2 ^openjdk@11: ^protobuf@:3.15
```

The latest version of candle-benchmarks depends on py-numba, which depends on llvm that needs binutils+gold. The external binutils is configured with ~gold therefore need to be rebuild.

Blas need to be provided in order to build py-torch, unfortunately, py-torch does not recognize armpl as a valid blas provider.

The latest py-scipy version depends on py-pythran, which in turn depends on `py-gast@0.4.0:0.4.999`, and py-tensorflow explictly requires `py-gast@0.3.3`. See thread in https://github.com/spack/spack/pull/24897.

Bazel does not like the default openjdk, See https://github.com/spack/spack/issues/14234

The latest protobuf does not build with tensorflow. Its likely an error from tensorflow code base. Specifically, protobuf removed error_message() method and replaced it with message() in Status class of `protobuf/src/google/stubs/status.h` from 3.16 onwards, however `tensorflow/tensorflow/core/kernels/example_parsing_ops.cc` is still trying to access `error_message()` methods all the way from v2 to latest.


### Spack Package Modification

We encountered several issues during the installation of candle-benchmarks. We had to refactor most parts of the package recipe as well as fixing a number of bugs in a few dependencies.

A list of pull requests:

* Candle-benchmarks: https://github.com/spack/spack/pull/24896
* CuDNN: https://github.com/spack/spack/pull/24882
* py-tensorflow: https://github.com/spack/spack/pull/24923

#### dependencies

The original recipe only has parts of dependencies specified in README file.

#### version

We applied git version scheme instead of using raw checksum, the origin recipe only has v0.1 and the updated recipe includs v0.1-master.

#### bug fix in recipe

* `+gpu` is an invalid boolean variant for py-theano package as appeared in candle-benchmarks script, which is correted to be `+cuda`.
* `+highgui` is flaged as conflicted with `imgproc`, therefore we removed `+highgui`, in addition, opencv either does not have `+python` or `+zlib` option.
* the expected arch argument in `cudnn` is set to `aarch64sbsa`, which does not align with spack convention.

### Building CANDLE-benchmarks



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
     ****
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
