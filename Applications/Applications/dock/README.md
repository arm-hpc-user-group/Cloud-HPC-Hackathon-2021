# DOCK 

**Description:** DOCK is a molecular docking program used in drug discovery. This program, given a protein binding site and a small molecule, tries to predict the correct binding mode of the small molecule in the binding site, and the associated binding energy.

**URL:** http://dock.compbio.ucsf.edu/DOCK_6/index.htm

**Team:**  

## Compilation

### Spack Package Modification

Details of any changes to the Spack recipe used.

Git commit hash of checkout for pacakage:

Pull request for Spack recipe changes:

### Building DOCK



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
#### Test Case 1
| Cores | gcc | arm | nvhpc |
|-------|------------|------------|------------|
| 8     | 5.4           | 4.76 s           | 5.23 s |
| 16    | 4.23 s           | 4.21 s           | 5.31 s |
| 32    | 4.69 s           | 4.68 s           | 5.2 s |
| 64    | 5.72 s           | 5.73 s           | 6.22 s |

#### Test Case 2
| Cores | gcc | arm | nvhpc |
|-------|------------|------------|------------|
| 8     | 380.47 s           | 379.55 s            | 452.45 s |
| 16    | 180.85 s           | 180.51 s           | 215.18 s |
| 32    | 91.7 s           | 92.02 s           | 108.98 s |
| 64    | 49.32 s           | 49.34 s           | 57.51 s |

#### Test Case 3
| Cores | gcc | arm | nvhpc |
|-------|------------|------------|------------|
| 8     | 147.27 s           | 149.21 s           | 176.54 s |
| 16    | 72.2 s           | 72.8 s           | 86.12 s |
| 32    | 38.57 s           | 38.68 s           | 47.17 s |
| 64    | 24.9 s           | 24.65 s           | 29.07 s |

#### Test Case 4
| Cores | gcc | arm | nvhpc |
|-------|------------|------------|------------|
| 8     | 624.82 s           | 640.2 s           | 774.42 s |
| 16    | 298.95 s           | 306.58 s           | 367.14 s |
| 32    | 149.42 s           | 152.75 s           | 184.17 s |
| 64    | 84.8 s           | 87.79 s           | 104.57 s |


### Off-Node Scaling Study

#### Test Case 1
| Nodes | Cores | arm | gcc | nvhpc
|-------|-------|-----|------|------|
| 1     | 32    |     |      |      |
| 1     | 64    |     |      |      |
| 2     | 128   | 5.42 s    | 5.17 s     |      |
| 4     | 256   |     | 243.27 s     |      |

#### Test Case 2
| Nodes | Cores | arm | gcc | nvhpc
|-------|-------|-----|------|------|
| 1     | 32    |     |      |      |
| 1     | 64    |     |      |      |
| 2     | 128   | 46.78 s    | 47.87 s     |      |
| 4     | 256   |     | 165.37 s     |      |

#### Test Case 3
| Nodes | Cores | arm | gcc | nvhpc
|-------|-------|-----|------|------|
| 1     | 32    |     |      |      |
| 1     | 64    |     |      |      |
| 2     | 128   | 143.06 s    | 263.83 s    |      |
| 4     | 256   |     | 262.33 s     |      |

#### Test Case 4
| Nodes | Cores | arm | gcc | nvhpc
|-------|-------|-----|------|------|
| 1     | 32    |     |      |      |
| 1     | 64    |     |      |      |
| 2     | 128   | 318.1 s    | 190.17 s     |      |
| 4     | 256   |     | 207.26 s     |      |


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
