# GATK 

**Description:** GATK (pronounced "Gee-ay-tee-kay", not "Gat-kay"), stands for GenomeAnalysisToolkit. It is a collection of command-line tools for analyzing high-throughput sequencing data with a primary focus on variant discovery. The tools can be used individually or chained together into complete workflows 

**URL:** https://software.broadinstitute.org/gatk/

**Team:** Falkners 

## Compilation

GATK has two requirements:
* [BWA](http://bio-bwa.sourceforge.net/)
* [SAMTools](http://samtools.sourceforge.net/)

It also relies on JDK 1.8+ to be installed.

### Spack Package Modification

Details of any changes to the Spack recipe used.

Git commit hash of checkout for pacakage:

Pull request for Spack recipe changes:

### Building GATK

GATK compiled fine with `gcc` on the x86 HPC and with both `gcc` and `arm` on the ARM HPC.

#### Compiler 1

`gcc` and `arm` compilers were used on the ARM HPC.
```
spack install gatk@4.1.8.1 %arm@21.0.0.879
spack install gatk@4.1.8.1 %gcc@10.3.0
```

`arm` dependencies used.

```
$ spack spec -Il gatk@4.1.8.1%arm@21.0.0.879

[+]  352aeok  gatk@4.1.8.1%arm@21.0.0.879~r arch=linux-amzn2-aarch64
[+]  pp2djek      ^openjdk@1.8.0_191-b12%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  jk7wv5q      ^python@3.8.11%arm@21.0.0.879+bz2+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tix~tkinter~ucs4+uuid+zlib patches=0d98e93189bc278fbc37a50ed7f183bd8aaf249a8e1670a465f0db6bb4f8cf87 arch=linux-amzn2-aarch64
[+]  z4ybgri          ^bzip2@1.0.8%arm@21.0.0.879~debug~pic+shared arch=linux-amzn2-aarch64
[+]  adtc6yc              ^diffutils@3.7%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  7vnthzn                  ^libiconv@1.16%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  oyfuwk3          ^expat@2.4.1%arm@21.0.0.879+libbsd arch=linux-amzn2-aarch64
[+]  5q4lmyg              ^libbsd@0.11.3%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  srfepw2                  ^libmd@1.0.3%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  645q4qj          ^gdbm@1.19%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  3haw5gt              ^readline@8.1%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  uhtqtlb                  ^ncurses@6.2%arm@21.0.0.879~symlinks+termlib abi=none arch=linux-amzn2-aarch64
[+]  zpuzm23                      ^pkgconf@1.7.4%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  rl3qj47          ^gettext@0.21%arm@21.0.0.879+bzip2+curses+git~libunistring+libxml2+tar+xz arch=linux-amzn2-aarch64
[+]  dypqz2i              ^libxml2@2.9.10%arm@21.0.0.879~python arch=linux-amzn2-aarch64
[+]  zqsab4f                  ^xz@5.2.5%arm@21.0.0.879~pic libs=shared,static arch=linux-amzn2-aarch64
[+]  puuxvg2                  ^zlib@1.2.11%arm@21.0.0.879+optimize+pic+shared arch=linux-amzn2-aarch64
[+]  fohku26              ^tar@1.34%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  far5l4e          ^libffi@3.3%arm@21.0.0.879 patches=26f26c6f29a7ce9bf370ad3ab2610f99365b4bdd7b82e7c31df41a3370d685c0 arch=linux-amzn2-aarch64
[+]  vc3waha          ^openssl@1.1.1k%arm@21.0.0.879~docs+systemcerts arch=linux-amzn2-aarch64
[+]  vv6txro              ^perl@5.32.1%arm@21.0.0.879+cpanm+shared+threads arch=linux-amzn2-aarch64
[+]  33wiajj                  ^berkeley-db@18.1.40%arm@21.0.0.879+cxx~docs+stl patches=b231fcc4d5cff05e5c3a4814f6a5af0e9a966428dc2176540d2c05aff41de522 arch=linux-amzn2-aarch64
[+]  zj3dbdy          ^sqlite@3.35.5%arm@21.0.0.879+column_metadata+fts~functions~rtree arch=linux-amzn2-aarch64
[+]  uflz3t5          ^util-linux-uuid@2.36.2%arm@21.0.0.879 arch=linux-amzn2-aarch64
```


`gcc` dependencies used.
[+]  dryvlws  gatk@4.1.8.1%gcc@10.3.0~r arch=linux-amzn2-graviton2
[+]  763lrfl      ^openjdk@1.8.0_191-b12%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  62czasr      ^python@3.8.11%gcc@10.3.0+bz2+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tix~tkinter~ucs4+uuid+zlib patches=0d98e93189bc278fbc37a50ed7f183bd8aaf249a8e1670a465f0db6bb4f8cf87 arch=linux-amzn2-graviton2
[+]  rqrpmap          ^bzip2@1.0.8%gcc@10.3.0~debug~pic+shared arch=linux-amzn2-graviton2
[+]  2w7bert              ^diffutils@3.7%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  y5ei3cm                  ^libiconv@1.16%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  ychdz7l          ^expat@2.4.1%gcc@10.3.0+libbsd arch=linux-amzn2-graviton2
[+]  ourxkez              ^libbsd@0.11.3%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  nssrqfc                  ^libmd@1.0.3%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  wjwqncx          ^gdbm@1.19%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  3zy7kxk              ^readline@8.1%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  iwzirqc                  ^ncurses@6.2%gcc@10.3.0~symlinks+termlib abi=none arch=linux-amzn2-graviton2
[+]  s4pw7zm                      ^pkgconf@1.7.4%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  fqlpcsl          ^gettext@0.21%gcc@10.3.0+bzip2+curses+git~libunistring+libxml2+tar+xz arch=linux-amzn2-graviton2
[+]  iyhm3wi              ^libxml2@2.9.10%gcc@10.3.0~python arch=linux-amzn2-graviton2
[+]  ye3kcvv                  ^xz@5.2.5%gcc@10.3.0~pic libs=shared,static arch=linux-amzn2-graviton2
[+]  qepjcvj                  ^zlib@1.2.11%gcc@10.3.0+optimize+pic+shared arch=linux-amzn2-graviton2
[+]  v6cutkh              ^tar@1.34%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  35cffos          ^libffi@3.3%gcc@10.3.0 patches=26f26c6f29a7ce9bf370ad3ab2610f99365b4bdd7b82e7c31df41a3370d685c0 arch=linux-amzn2-graviton2
[+]  5i3lgfb          ^openssl@1.1.1k%gcc@10.3.0~docs+systemcerts arch=linux-amzn2-graviton2
[+]  4m7exgb              ^perl@5.32.1%gcc@10.3.0+cpanm+shared+threads arch=linux-amzn2-graviton2
[+]  y42m6yr                  ^berkeley-db@18.1.40%gcc@10.3.0+cxx~docs+stl patches=b231fcc4d5cff05e5c3a4814f6a5af0e9a966428dc2176540d2c05aff41de522 arch=linux-amzn2-graviton2
[+]  2q753q6          ^sqlite@3.35.5%gcc@10.3.0+column_metadata+fts~functions~rtree arch=linux-amzn2-graviton2
[+]  2non7qx          ^util-linux-uuid@2.36.2%gcc@10.3.0 arch=linux-amzn2-graviton2```
```

#### Compiler 2

`gcc` was used on the x86 HPC.
```
spack install gatk@4.1.8.1 %gcc@10.3.0
```

x86 `gcc` dependencies used.
```
pack spec -Il gatk@4.1.8.1%gcc@10.3.0

gatk@4.1.8.1%gcc@10.3.0~r arch=linux-amzn2-skylake_avx512
    ^openjdk@1.8.0_265-b01%gcc@10.3.0 arch=linux-amzn2-skylake_avx512
    ^python@3.8.11%gcc@10.3.0+bz2+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tix~tkinter~ucs4+uuid+zlib patches=0d98e93189bc278fbc37a50ed7f183bd8aaf249a8e1670a465f0db6bb4f8cf87 arch=linux-amzn2-skylake_avx512
        ^bzip2@1.0.8%gcc@10.3.0~debug~pic+shared arch=linux-amzn2-skylake_avx512
            ^diffutils@3.7%gcc@10.3.0 arch=linux-amzn2-skylake_avx512
                ^libiconv@1.16%gcc@10.3.0 arch=linux-amzn2-skylake_avx512
        ^expat@2.4.1%gcc@10.3.0+libbsd arch=linux-amzn2-skylake_avx512
            ^libbsd@0.11.3%gcc@10.3.0 arch=linux-amzn2-skylake_avx512
                ^libmd@1.0.3%gcc@10.3.0 arch=linux-amzn2-skylake_avx512
        ^gdbm@1.19%gcc@10.3.0 arch=linux-amzn2-skylake_avx512
            ^readline@8.1%gcc@10.3.0 arch=linux-amzn2-skylake_avx512
                ^ncurses@6.2%gcc@10.3.0~symlinks+termlib abi=none arch=linux-amzn2-skylake_avx512
                    ^pkgconf@1.7.4%gcc@10.3.0 arch=linux-amzn2-skylake_avx512
        ^gettext@0.21%gcc@10.3.0+bzip2+curses+git~libunistring+libxml2+tar+xz arch=linux-amzn2-skylake_avx512
            ^libxml2@2.9.10%gcc@10.3.0~python arch=linux-amzn2-skylake_avx512
                ^xz@5.2.5%gcc@10.3.0~pic libs=shared,static arch=linux-amzn2-skylake_avx512
                ^zlib@1.2.11%gcc@10.3.0+optimize+pic+shared arch=linux-amzn2-skylake_avx512
            ^tar@1.34%gcc@10.3.0 arch=linux-amzn2-skylake_avx512
        ^libffi@3.3%gcc@10.3.0 patches=26f26c6f29a7ce9bf370ad3ab2610f99365b4bdd7b82e7c31df41a3370d685c0 arch=linux-amzn2-skylake_avx512
        ^openssl@1.1.1k%gcc@10.3.0~docs+systemcerts arch=linux-amzn2-skylake_avx512
            ^perl@5.32.1%gcc@10.3.0+cpanm+shared+threads arch=linux-amzn2-skylake_avx512
                ^berkeley-db@18.1.40%gcc@10.3.0+cxx~docs+stl patches=b231fcc4d5cff05e5c3a4814f6a5af0e9a966428dc2176540d2c05aff41de522 arch=linux-amzn2-skylake_avx512
        ^sqlite@3.35.5%gcc@10.3.0+column_metadata+fts~functions~rtree arch=linux-amzn2-skylake_avx512
        ^util-linux-uuid@2.36.2%gcc@10.3.0 arch=linux-amzn2-skylake_avx512
```


## Test Case 0

This confirms that GATK is working by doing a basic analysis of a BAM file. The BAM file will be downloaded, if it doesn't already exist.

```
reframe -c gatk_countbases.py -r --performance-report
```

### Validation

This is a public BAM file from an Illumina HiSeq 2500 and is known to have 20K reads and 5000000 bases in it.

Running GATK by hand (same commands) lets you inspect stats and work with this file. It is small enough that it should always process in a fraction of a second.

### ReFrame Output

ARM HPC output after `gcc` compile.
```
==============================================================================
PERFORMANCE REPORT
------------------------------------------------------------------------------
GATK_gatk_countbases_gatk_4_1_8_1_gcc_10_3_0_N_1_MPI_1_OMP_1
- aws:c6gn
   - builtin
      * num_tasks: 1
      * Total Time: 0.0 s
------------------------------------------------------------------------------
```

x86 HPC output after `gcc` compile.

```
==============================================================================
PERFORMANCE REPORT
------------------------------------------------------------------------------
GATK_gatk_countbases_gatk_4_1_8_1_gcc_10_3_0_N_1_MPI_1_OMP_1
- aws:c5n
   - builtin
      * num_tasks: 1
      * Total Time: 0.0 s
------------------------------------------------------------------------------
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
-----------------------------------------------------------------------------
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
