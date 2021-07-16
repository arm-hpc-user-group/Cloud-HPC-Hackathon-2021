# PICSAR 

**Description:** PICSAR is a high performance library of optimized versions of the key functionalities of the PIC loop.

**URL:** https://picsar.net

**Team:** ElkNet

## Compilation

picsar depends on MPI and FFTT:

```
$ spack info picsar

MakefilePackage:   picsar

Description:
    PICSAR is a high performance library of optimized versions of the key
    functionalities of the PIC loop.

Homepage: https://picsar.net

Externally Detectable: 
    False

Tags: 
    None

Preferred version:  
    develop    [git] https://bitbucket.org/berkeleylab/picsar.git on branch master

Safe versions:  
    develop    [git] https://bitbucket.org/berkeleylab/picsar.git on branch master

Variants:
    Name [Default]         Allowed values    Description
    ===================    ==============    =============================================

    debug [off]            on, off           Debug mode
    library [off]          on, off           Create static and dynamic library
    map [off]              on, off           Allinea Map profiling
    prod [on]              on, off           Production mode (without FFTW)
    prod_spectral [off]    on, off           Production mode with spectral solver and FFTW
    sde [off]              on, off           sde profiling
    vtune [off]            on, off           Vtune profiling

Installation Phases:
    edit    build    install

Build Dependencies:
    fftw  mpi

Link Dependencies:
    fftw  mpi

Run Dependencies:
    None

Virtual Packages: 
    None
```

### Spack Package Modification

We had the following error when compiling with GCC 10.3.0 in both the x86 and the ARM cluster:
```
     25    
     26      304 |               bztile, .FALSE., l_lower_order_in_v_in, LVEC_fieldgathe,                &
     27          |                      1
     28    ......
     29     1092 |                 bztile , l4symtry_in, l_lower_order_in_v_in, lvect,                   &
     30          |                         2
  >> 31    Error: Type mismatch between actual argument at (1) and actual argument at (2) (LOGICAL(4)/LOGICAL(8)).
     32    src/particle_pushers/particle_pusher_manager_3d.F90:318:23:
     33    
     34      318 |               bztile , .FALSE., l_lower_order_in_v_in, lvec_fieldgathe,               &
     35          |                       1
     36    ......
     37     1104 |                 bztile , l4symtry_in, l_lower_order_in_v_in, lvect,                   &
     38          |                         2
  >> 39    Error: Type mismatch between actual argument at (1) and actual argument at (2) (LOGICAL(4)/LOGICAL(8)).
  >> 40    make: *** [src/particle_pushers/particle_pusher_manager_3d.o] Error 1
```

It seems that it is caused due to some changes in GCC v10. To circumvent the error, we have used the flag "-fallow-argument-mismatch". We have opened an [issue](https://github.com/ECP-WarpX/picsar/issues/24) in the picsar repository.

New additions to the spack package.py:

```
+ if '%gcc' in self.spec:
+     targets.append('FARGS=-g -fbounds-check -O3 -fopenmp -JModules -fallow-argument-mismatch')
```

We also had some problems when compiling with nvhpc:

```
==> Error: ProcessError: Command exited with status 2:
    'make' 'FC=/scratch/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/openmpi-4.1.0-lmaoy5tql4ymankvskpqsplxlig5wzvy/bin/mpif90' 'CC=/scratch/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/openmpi-4.1.0-lmaoy5tql4ymankvskpqsplxlig5wzvy/bin/mpicc' 'COMP=user' 'FARGS=-g -O3 -fopenmp' 'MODE = prod' 'SYS = default'

1 error found in build log:
     222    
     223    6 warnings generated.
     224    /scratch/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/openmpi-4.1.0-lmaoy5tql4ymankvskpqsplxlig5wzvy/bin/mpif90 -g -O3 -fopenmp -c -o src/diags/diags.o 
            src/diags/diags.F90
     225    F90-W-0547-OpenMP feature, SAFELEN, not yet implemented in this version of the compiler. (src/diags/diags.F90: 900)
     226    F90-F-0155-DO loop expected after COLLAPSE (src/diags/diags.F90: 908)
     227    F90/aarch64 Linux FlangArm F90  - 1.5 2017-05-01: compilation aborted
  >> 228    make: *** [src/diags/diags.o] Error 1
```

OpenMP directive SAFELEN it is not implemented in nvhpc.

spack develop picsar@develop



Git commit hash of checkout for pacakage:

Pull request for Spack recipe changes:

### Building PICSAR



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
