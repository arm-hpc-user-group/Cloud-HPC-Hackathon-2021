# miniGMG 

**Description:** miniGMG is a compact benchmark for understanding the performance challenges associated with geometric multigrid solvers found in applications built from AMR MG frameworks like CHOMBO or BoxLib when running on modern multi- and manycore-based supercomputers. It includes both productive reference examples as well as highly-optimized implementations for CPUs and GPUs. It is sufficiently general that it has been used to evaluate a broad range of research topics including PGAS programming models and algorithmic tradeoffs inherit in multigrid. miniGMG was developed under the CACHE Joint Math-CS Institute. Note, miniGMG code has been supersceded by HPGMG.

**URL:** http://crd.lbl.gov/departments/computer-science/PAR/research/previous-projects/miniGMG/

**Team:**  

## Compilation

### Spack Package Modification

Details of any changes to the Spack recipe used.

Git commit hash of checkout for pacakage:

Pull request for Spack recipe changes:

### Building miniGMG



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

## Test Case 2

[ReFrame Benchmark 2](#)

```
../bin/reframe -c benchmark.py -r --performance-report
```

## Test Case 3

[ReFrame Benchmark 3](#)

```
../bin/reframe -c benchmark.py -r --performance-report
```

## Test Case 4

[ReFrame Benchmark 4](#)

```
../bin/reframe -c benchmark.py -r --performance-report
```

### Validation

miniGMG reduces the norm until it is less than 1e-15. If the norm is still greater than 1e-15 after `maxVCycles` v-cycles, the program will ends with incorrect results. So we check if all the norms produced by last v-cycles are less than 1e-15.


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
| 1     |            |            |
| 2     |            |            |
| 4     |            |            |
| 8     |            |            |
| 16    |            |            |
| 32    |            |            |
| 64    |            |            |


### Serial Hot-spot Profile

List of top-10 functions / code locations from a serial profile.

#### Test Case 1  
Profiling script:  
[ReFrame Benchmark](#)

#### Test Case 2
Profiling script:  
[ReFrame Benchmark](#)

#### Test Case 3
Profiling script:  
[ReFrame Benchmark](#)

#### Test Case 4
Profiling script:  
[ReFrame Benchmark](#)

### Full Node Hot-spot Profile

List of top-10 functions / code locations from a full node profile.

#### Test Case 1  
Profiling script:  
[ReFrame Benchmark](#)

#### Test Case 2
Profiling script:  
[ReFrame Benchmark](#)

#### Test Case 3
Profiling script:  
[ReFrame Benchmark](#)

#### Test Case 4
Profiling script:  
[ReFrame Benchmark](#)

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

### On-Node Architecture Comparison

On-node scaling study for two architectures.

#### Test Case 1
X86 script:  
[ReFrame Benchmark](#)  
ARM script:  
[ReFrame Benchmark](#)  
Time: 
| Cores | C6gn (ARM) | C5n (X86) |
|-------|------------|-----------|
| 1     |            | 19.09 s   |
| 2     |            | 23.29 s   |
| 4     |            | 20.83 s   |
| 8     |            | 19.91 s   |
| 16    |            | 22.06 s   |
| 32    |            | 30.28 s   |
| 64    |            | 46.11 s   |

Number of v-cycles:
| Cores | C6gn (ARM) | C5n (X86) |
|-------|------------|-----------|
| 1     |            | 17        |
| 2     |            | 17        |
| 4     |            | 17        |
| 8     |            | 17        |
| 16    |            | 17        |
| 32    |            | 17        |
| 64    |            | 17        |

Total time in MGSolve:
| Cores | C6gn (ARM) | C5n (X86) |
|-------|------------|-----------|
| 1     |            | 3.763650 s|
| 2     |            | 4.905664 s|
| 4     |            | 4.455355 s|
| 8     |            | 4.296553 s|
| 16    |            | 4.856182 s|
| 32    |            | 6.893029 s|
| 64    |            | 10.553772 s         |

Total time of v-cycles:
| Cores | C6gn (ARM) | C5n (X86) |
|-------|------------|-----------|
| 1     |            | 3.757559 s          |
| 2     |            | 4.900422 s         |
| 4     |            | 4.451428 s         |
| 8     |            | 4.289725 s         |
| 16    |            | 4.844235 s         |
| 32    |            | 6.862862 s         |
| 64    |            | 10.490605 s         |

#### Test Case 2
X86 script:  
[ReFrame Benchmark](#)  
ARM script:  
[ReFrame Benchmark](#)  
Time:
| Cores | C6gn (ARM) | C5n (X86) |
|-------|------------|-----------|
| 1     |            | 164.75 s  |
| 2     |            | 128.39 s  |
| 4     |            | 85.88 s   |
| 8     |            | 72.85 s   |
| 16    |            | 84.45 s   |
| 32    |            | 142.46 s  |
| 64    |            | 252.93 s  |

Number of v-cycles:
| Cores | C6gn (ARM) | C5n (X86) |
|-------|------------|-----------|
| 1     |            | 17          |
| 2     |            | 17          |
| 4     |            | 17          |
| 8     |            | 17          |
| 16    |            | 17          |
| 32    |            | 17          |
| 64    |            | 17          |

Total time in MGSolve:
| Cores | C6gn (ARM) | C5n (X86) |
|-------|------------|-----------|
| 1     |            | 35.559029 s          |
| 2     |            | 28.587486 s          |
| 4     |            | 19.218630 s          |
| 8     |            | 16.626050 s          |
| 16    |            | 19.742723 s         |
| 32    |            | 34.154504 s          |
| 64    |            | 61.337021 s         |

Total time of v-cycles:
| Cores | C6gn (ARM) | C5n (X86) |
|-------|------------|-----------|
| 1     |            | 35.484981 s          |
| 2     |            | 28.539944 s          |
| 4     |            | 19.178477 s          |
| 8     |            | 16.565863 s          |
| 16    |            | 19.631998 s          |
| 32    |            | 33.908929 s          |
| 64    |            | 60.835770 s          |

#### Test Case 3
X86 script:  
[ReFrame Benchmark](#)  
ARM script:  
[ReFrame Benchmark](#)  
Time:
| Cores | C6gn (ARM) | C5n (X86) |
|-------|------------|-----------|
| 1     |            | 1335.42 s |
| 2     |            | 981.23 s  |
| 4     |            | 627.84 s  |
| 8     |            | 543.84 s  |
| 16    |            | 640.72 s  |
| 32    |            | 1087.96 s |
| 64    |            | 2025.36 s |

Number of v-cycles:
| Cores | C6gn (ARM) | C5n (X86) |
|-------|------------|-----------|
| 1     |            | 18          |
| 2     |            | 18          |
| 4     |            | 18          |
| 8     |            | 18          |
| 16    |            | 18          |
| 32    |            | 18          |
| 64    |            | 18          |

Total time in MGSolve:
| Cores | C6gn (ARM) | C5n (X86) |
|-------|------------|-----------|
| 1     |            | 290.789095 s          |
| 2     |            | 221.358545 s          |
| 4     |            | 143.249228 s          |
| 8     |            | 126.818601 s          |
| 16    |            | 152.875151 s          |
| 32    |            | 263.761818 s          |
| 64    |            | 494.900773 s          |

Total time of v-cycles:
| Cores | C6gn (ARM) | C5n (X86) |
|-------|------------|-----------|
| 1     |            | 290.245135 s          |
| 2     |            | 220.979693 s          |
| 4     |            | 142.892534 s          |
| 8     |            | 126.285004 s          |
| 16    |            | 151.944911 s          |
| 32    |            | 261.758187 s          |
| 64    |            | 490.806534 s          |

#### Test Case 4
X86 script:  
[ReFrame Benchmark](#)  
ARM script:  
[ReFrame Benchmark](#)  
Time:
| Cores | C6gn (ARM) | C5n (X86) |
|-------|------------|-----------|
| 1     |            | 4790.18 s |
| 2     |            | 3343.18 s |
| 4     |            | 1994.46 s |
| 8     |            | 1305.74 s |
| 16    |            | 1915.15 s |
| 32    |            | 3563.73 s |
| 64    |            | 7220.35 s |

Number of v-cycles:
| Cores | C6gn (ARM) | C5n (X86) |
|-------|------------|-----------|
| 1     |            | 18          |
| 2     |            | 18          |
| 4     |            | 18          |
| 8     |            | 18          |
| 16    |            | 18          |
| 32    |            | 18          |
| 64    |            | 18          |

Total time in MGSolve:
| Cores | C6gn (ARM) | C5n (X86) |
|-------|------------|-----------|
| 1     |            | 1051.882945 s          |
| 2     |            | 755.768008 s          |
| 4     |            | 452.718762 s          |
| 8     |            | 298.740681 s          |
| 16    |            | 455.145482 s          |
| 32    |            | 864.805499 s          |
| 64    |            | 1764.467881 s          |

Total time of v-cycles:
| Cores | C6gn (ARM) | C5n (X86) |
|-------|------------|-----------|
| 1     |            | 1050.009506 s          |
| 2     |            | 754.524528 s          |
| 4     |            | 451.749684 s          |
| 8     |            | 297.413569 s          |
| 16    |            | 452.217409 s          |
| 32    |            | 858.144534 s          |
| 64    |            | 1750.044089 s          |

### Off-Node Architecture Comparison

Off-node scaling study for two architectures.

#### Test Case 1
X86 script:  
[ReFrame Benchmark](#)  
ARM script:  
[ReFrame Benchmark](#)  
Time:
| Nodes | Cores | C6gn (ARM) |  C5n (X86) |
|-------|-------|------------|------------|
| 1     | 32    |            | 30.28 s    |
| 1     | 64    |            | 46.11 s    |
| 2     | 128   |            | 33.52 s    |
| 4     | 256   |            | 26.4 s     |

Number of v-cycles:
| Nodes | Cores | C6gn (ARM) |  C5n (X86) |
|-------|-------|------------|------------|
| 1     | 32    |            | 17    |
| 1     | 64    |            | 17   |
| 2     | 128   |            | 17   |
| 4     | 256   |            | 17     |

Total time in MGSolve:
| Nodes | Cores | C6gn (ARM) |  C5n (X86) |
|-------|-------|------------|------------|
| 1     | 32    |            | 6.893029 s    |
| 1     | 64    |            | 10.553772 s   |
| 2     | 128   |            | 7.432422 s   |
| 4     | 256   |            | 5.668103 s     |

Total time of v-cycles:
| Nodes | Cores | C6gn (ARM) |  C5n (X86) |
|-------|-------|------------|------------|
| 1     | 32    |            | 6.862862 s    |
| 1     | 64    |            | 10.490605 s   |
| 2     | 128   |            | 7.400493 s  |
| 4     | 256   |            | 5.654560 s     |

#### Test Case 2
X86 script:  
[ReFrame Benchmark](#)  
ARM script:  
[ReFrame Benchmark](#)  
Time:
| Nodes | Cores | C6gn (ARM) |  C5n (X86) |
|-------|-------|------------|------------|
| 1     | 32    |            | 142.46 s   |
| 1     | 64    |            | 252.93 s   |
| 2     | 128   |            | 141.92 s   |
| 4     | 256   |            | 82.26 s    |

Number of v-cycles:
| Nodes | Cores | C6gn (ARM) |  C5n (X86) |
|-------|-------|------------|------------|
| 1     | 32    |            | 17    |
| 1     | 64    |            | 17   |
| 2     | 128   |            | 17   |
| 4     | 256   |            | 17     |

Total time in MGSolve:
| Nodes | Cores | C6gn (ARM) |  C5n (X86) |
|-------|-------|------------|------------|
| 1     | 32    |            | 34.154504 s    |
| 1     | 64    |            | 61.337021 s   |
| 2     | 128   |            | 34.176679 s   |
| 4     | 256   |            | 19.599111 s     |

Total time of v-cycles:
| Nodes | Cores | C6gn (ARM) |  C5n (X86) |
|-------|-------|------------|------------|
| 1     | 32    |            | 33.908929 s    |
| 1     | 64    |            | 60.835770 s   |
| 2     | 128   |            | 33.919927 s   |
| 4     | 256   |            | 19.488011 s     |

#### Test Case 3
X86 script:  
[ReFrame Benchmark](#)  
ARM script:  
[ReFrame Benchmark](#)  
Time:
| Nodes | Cores | C6gn (ARM) |  C5n (X86) |
|-------|-------|------------|------------|
| 1     | 32    |            | 1087.96 s  |
| 1     | 64    |            | 2025.36 s  |
| 2     | 128   |            | 1027.75 s  |
| 4     | 256   |            | 526.23 s   |

Number of v-cycles:
| Nodes | Cores | C6gn (ARM) |  C5n (X86) |
|-------|-------|------------|------------|
| 1     | 32    |            | 18    |
| 1     | 64    |            | 18   |
| 2     | 128   |            | 18   |
| 4     | 256   |            | 18     |

Total time in MGSolve:
| Nodes | Cores | C6gn (ARM) |  C5n (X86) |
|-------|-------|------------|------------|
| 1     | 32    |            | 263.761818 s    |
| 1     | 64    |            | 494.900773 s   |
| 2     | 128   |            | 250.927827 s   |
| 4     | 256   |            | 127.999570 s     |

Total time of v-cycles:
| Nodes | Cores | C6gn (ARM) |  C5n (X86) |
|-------|-------|------------|------------|
| 1     | 32    |            | 261.758187 s    |
| 1     | 64    |            | 490.806534 s   |
| 2     | 128   |            | 248.893242 s   |
| 4     | 256   |            | 127.084274 s     |

#### Test Case 4
X86 script:  
[ReFrame Benchmark](#)  
ARM script:  
[ReFrame Benchmark](#)  
Time:
| Nodes | Cores | C6gn (ARM) |  C5n (X86) |
|-------|-------|------------|------------|
| 1     | 32    |            | 3563.73 s  |
| 1     | 64    |            | 7220.35 s  |
| 2     | 128   |            | 3421.94 s  |
| 4     | 256   |            | 1732.57 s  |

Number of v-cycles:
| Nodes | Cores | C6gn (ARM) |  C5n (X86) |
|-------|-------|------------|------------|
| 1     | 32    |            | 18    |
| 1     | 64    |            | 18   |
| 2     | 128   |            | 18   |
| 4     | 256   |            | 18     |

Total time in MGSolve:
| Nodes | Cores | C6gn (ARM) |  C5n (X86) |
|-------|-------|------------|------------|
| 1     | 32    |            | 864.805499 s    |
| 1     | 64    |            | 1764.467881 s   |
| 2     | 128   |            | 836.623473 s   |
| 4     | 256   |            | 423.034038 s     |

Total time of v-cycles:
| Nodes | Cores | C6gn (ARM) |  C5n (X86) |
|-------|-------|------------|------------|
| 1     | 32    |            | 858.144534 s    |
| 1     | 64    |            | 1750.044089 s   |
| 2     | 128   |            | 829.759071 s   |
| 4     | 256   |            | 419.650698 s     |

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
