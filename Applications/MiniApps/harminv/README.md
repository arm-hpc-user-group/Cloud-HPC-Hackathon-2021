# Harminv 

**Description:** Harminv is a free program (and accompanying library) to solve the problem of harmonic inversion - given a discrete-time, finite-length signal that consists of a sum of finitely-many sinusoids (possibly exponentially decaying) in a given bandwidth, it determines the frequencies, decay constants, amplitudes, and phases of those sinusoids.


**URL:** http://ab-initio.mit.edu/wiki/index.php/Harminv 

**Team:** QMLab 

## Compilation

### Spack Package Modification
No changes were needed to compile Harminv

### Building Harminv



#### Compiler 1

```
spack install harminv@1.4%gcc@10.3.0 
```

```
$ spack spec -Il harminv@1.4%gcc@10.3.0

```
```
Input spec
--------------------------------
 -   harminv@1.4%gcc@10.3.0

Concretized
--------------------------------
[+]  qlbsovg  harminv@1.4%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  rv7gj6u      ^openblas@0.3.15%gcc@10.3.0~bignuma~consistent_fpcsr~ilp64+locking+pic+shared threads=none arch=linux-amzn2-graviton2
[+]  4m7exgb          ^perl@5.32.1%gcc@10.3.0+cpanm+shared+threads arch=linux-amzn2-graviton2
[+]  y42m6yr              ^berkeley-db@18.1.40%gcc@10.3.0+cxx~docs+stl patches=b231fcc4d5cff05e5c3a4814f6a5af0e9a966428dc2176540d2c05aff41de522 arch=linux-amzn2-graviton2
[+]  rqrpmap              ^bzip2@1.0.8%gcc@10.3.0~debug~pic+shared arch=linux-amzn2-graviton2
[+]  2w7bert                  ^diffutils@3.7%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  y5ei3cm                      ^libiconv@1.16%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  wjwqncx              ^gdbm@1.19%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  3zy7kxk                  ^readline@8.1%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  iwzirqc                      ^ncurses@6.2%gcc@10.3.0~symlinks+termlib abi=none arch=linux-amzn2-graviton2
[+]  s4pw7zm                          ^pkgconf@1.7.4%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  qepjcvj              ^zlib@1.2.11%gcc@10.3.0+optimize+pic+shared arch=linux-amzn2-graviton2
```
#### Compiler 2
```
spack install harminv@1.4%arm@21.0.0.879
```

```
spack spec -Il harminv@1.4%arm@21.0.0.879
```

```
Input spec
--------------------------------
 -   harminv@1.4%arm@21.0.0.879

Concretized
--------------------------------
==> Warning: arm@21.0.0.879 cannot build optimized binaries for "graviton2". Using best target possible: "aarch64"
[+]  fx2jixh  harminv@1.4%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  cwuo4ek      ^openblas@0.3.15%arm@21.0.0.879~bignuma~consistent_fpcsr~ilp64+locking+pic+shared threads=none arch=linux-amzn2-aarch64
[+]  vv6txro          ^perl@5.32.1%arm@21.0.0.879+cpanm+shared+threads arch=linux-amzn2-aarch64
[+]  33wiajj              ^berkeley-db@18.1.40%arm@21.0.0.879+cxx~docs+stl patches=b231fcc4d5cff05e5c3a4814f6a5af0e9a966428dc2176540d2c05aff41de522 arch=linux-amzn2-aarch64
[+]  z4ybgri              ^bzip2@1.0.8%arm@21.0.0.879~debug~pic+shared arch=linux-amzn2-aarch64
[+]  adtc6yc                  ^diffutils@3.7%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  7vnthzn                      ^libiconv@1.16%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  645q4qj              ^gdbm@1.19%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  3haw5gt                  ^readline@8.1%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  uhtqtlb                      ^ncurses@6.2%arm@21.0.0.879~symlinks+termlib abi=none arch=linux-amzn2-aarch64
[+]  zpuzm23                          ^pkgconf@1.7.4%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  puuxvg2              ^zlib@1.2.11%arm@21.0.0.879+optimize+pic+shared arch=linux-amzn2-aarch64
```

## Test Case 1
Validation is done my comparing result regenreated on C6gn with C5n
to install on X86
```
spack install harminv@1.4%gcc@10.3.0 
```
```
$spack spec -Il harminv@1.4%gcc@10.3.0
```
```
Input spec
--------------------------------
 -   harminv@1.4%gcc@10.3.0

Concretized
--------------------------------
[+]  a36yf6c  harminv@1.4%gcc@10.3.0 arch=linux-amzn2-skylake_avx512
[+]  skexx3l      ^openblas@0.3.15%gcc@10.3.0~bignuma~consistent_fpcsr~ilp64+locking+pic+shared threads=none arch=linux-amzn2-skylake_avx512
[+]  fb3kjch          ^perl@5.32.1%gcc@10.3.0+cpanm+shared+threads arch=linux-amzn2-skylake_avx512
[+]  i5lbkjo              ^berkeley-db@18.1.40%gcc@10.3.0+cxx~docs+stl patches=b231fcc4d5cff05e5c3a4814f6a5af0e9a966428dc2176540d2c05aff41de522 arch=linux-amzn2-skylake_avx512
[+]  s36txvt              ^bzip2@1.0.8%gcc@10.3.0~debug~pic+shared arch=linux-amzn2-skylake_avx512
[+]  kjoplsl                  ^diffutils@3.7%gcc@10.3.0 arch=linux-amzn2-skylake_avx512
[+]  qmzfn6j                      ^libiconv@1.16%gcc@10.3.0 arch=linux-amzn2-skylake_avx512
[+]  fgwgsih              ^gdbm@1.19%gcc@10.3.0 arch=linux-amzn2-skylake_avx512
[+]  i35suwy                  ^readline@8.1%gcc@10.3.0 arch=linux-amzn2-skylake_avx512
[+]  xbybdoz                      ^ncurses@6.2%gcc@10.3.0~symlinks+termlib abi=none arch=linux-amzn2-skylake_avx512
[+]  i665ooz                          ^pkgconf@1.7.4%gcc@10.3.0 arch=linux-amzn2-skylake_avx512
[+]  q2x25kt              ^zlib@1.2.11%gcc@10.3.0+optimize+pic+shared arch=linux-amzn2-skylake_avx512
```

create an [input file](./x86/input.txt)
use command ```harminv -t 0.02 0-6250 <input.txt > harminv.out```
[reframe python file is used](./x86/reframe_validation.py)

[ReFrame Benchmark 1](#)

```
../bin/reframe -c benchmark.py -r --performance-report
```

for above input file both gcc and arm compiler version of harminv genereate the following outputfile
```
frequency, decay constant, Q, amplitude, phase, error
-7.24255, -8.198696e-02, -277.522, 9.6967, 0.617387, 3.756439e-04
-7.21708, 2.497940e-01, 90.7673, 448.229, -1.01601, 4.921908e-04
-7.15291, 4.496000e-02, 499.811, 11752.5, 0.886237, 1.904845e-06
-5.81166, -5.067082e-01, -36.0323, 38.1634, -2.444, 1.268257e-02
-5.02506, 2.669698e-02, 591.328, 8196.4, 0.960597, 1.133048e-04
-5.0155, 5.586238e-02, 282.062, 3629.56, 0.44016, 4.038701e-04
-4.83879, 7.200798e-01, 21.1109, 307.37, -0.53876, 2.441557e-03
-4.35149, 4.090887e-02, 334.173, 13779.7, 0.914174, 4.574732e-06
-4.31982, 5.896658e-02, 230.149, 17758.7, 0.68476, 4.418857e-06
-2.42392, -5.203076e-01, -14.6355, 64.5147, 0.0448755, 2.425428e-02
-1.70371, 4.347789e-02, 123.105, 12976.3, 0.61648, 2.272682e-06
-1.45155, 3.988270e-01, 11.434, 171.026, -1.1668, 2.773334e-03
-1.17061, 5.421554e-02, 67.8323, 15245.8, 0.626476, 3.531540e-06
-1.05749, -3.431828e-02, -96.8059, 25.4132, 2.88087, 2.110161e-03
0.330692, 3.992533e-02, 26.0211, 12766.7, 0.599104, 1.142644e-04
0.444489, 3.857638e-02, 36.1984, 12611.1, 0.558483, 3.323750e-05
0.505193, 1.516980e-01, 10.4623, 18.3136, 1.68094, 1.539671e-02
2.36235, 3.853256e-02, 192.604, 11973.8, 0.514951, 7.002382e-07
2.65695, 4.842720e-01, 17.2363, 94.341, 1.08883, 3.147858e-03
2.80995, -6.294260e-01, -14.025, 15.2935, -2.38326, 1.452004e-02
5.11537, 5.576936e-01, 28.8159, 84.3572, -0.313173, 9.872748e-03
5.41056, -2.910707e-02, -583.974, 228.561, 1.05248, 2.814381e-04
5.44827, 2.800150e-02, 611.262, 388.257, -2.55406, 1.606303e-04
5.60774, -2.665346e-02, -660.973, 4.95633, 0.0436863, 5.272788e-04
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
