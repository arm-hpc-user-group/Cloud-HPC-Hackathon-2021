# FleCSPH 

**Description:** FleCSPH is a multi-physics compact application that exercises FleCSI parallel data structures for tree-based particle methods. In particular, FleCSPH implements a smoothed-particle hydrodynamics (SPH) solver for the solution of Lagrangian problems in astrophysics and cosmology. FleCSPH includes support for gravitational forces using the fast multipole method (FMM).

**URL:** http://flecsi.lanl.com

**Team:** BlueHPCHens  

## Compilation

### Spack Package Modification

Details of any changes to the Spack recipe used.

Git commit hash of checkout for pacakage:

Pull request for Spack recipe changes: https://github.com/mferrato/spack/commit/2687874dc6e6d86a78ed405ebd8adaa941229489

** Had to edit Spack package for FleCSPH **

** Update 5/16: PR was merged into Spack **

### Building FleCSPH

#### Compiler 1: GCC

```
$ mkdir flecsph-devel
$ cd flecsph-devel
$ spack env create -d .
$ spack env activate .
$ spack install flecsph%gcc@10.3.0
$ spack load flecsph
```

```
$ echo $PATH  # check path to gcc-10.3.0/flecsph-***/bin
```
cd into gcc-10.3.0/flecsph-***/bin
Binaries to run FleCSPH will be in this `bin` folder

#### Compiler 2: NVHPC

```
$ mkdir flecsph-devel
$ cd flecsph-devel
$ spack env create -d .
$ spack env activate .
$ spack develop flecsph@master     # puts a copy of the application src in current dir
$ spack concretize -f
$EDITOR flecsph/include/physics/eos/eos.h  # edit this file
```
*** Delete Line 422: "template<>"

```
spack install flecsph%nvhpc ^cmake%gcc ^python%gcc ^perl@5.30.3 ^boost%gcc ^m4%gcc ^pfunit%gcc 
spack load flecsph
```
```
$ echo $PATH  # check path to nvhpc-*/flecsph-***/bin
```
cd into nvhpc-*/flecsph-***/bin
Binaries to run FleCSPH will be in this `bin` folder

## Test Case 1

https://github.com/laristra/flecsph/wiki/1D-Sod-shock-tubes

Generates test data
```
mpirun -np 1 ./sodtube_1d_generator sod_test1_n10000.par
```


[ReFrame Benchmark 1](#)

```
../bin/reframe -c benchmark.py -r --performance-report
```

### Validation

Details of the validation for `Test Case 1`.

We were not sure which energy value would be relevant so we used Kinetic, Internal, and Total energy values at the end of 5000 iterations. We then used a boundary threshold of 0.01 to check for errors in the outputs of the 3 energy values.


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

We had to make a change (documented in the steps above) to get the application to run on NVHPC.

### Performance Summary

Details of lessons from analysing the performance of the application.


### Optimisation Summary

Details of lessons from performance optimising the application.
