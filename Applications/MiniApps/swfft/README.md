# swfft 

**Description:** A stand-alone version of HACC's distributed-memory, pencil-decomposed, parallel 3D FFT.

**URL:** https://xgitlab.cels.anl.gov/hacc/SWFFT

**Team:**  

## Compilation

SWFFT depends on MPI and FFTT. TODO

### Spack Package Modification

Details of any changes to the Spack recipe used.

The existing Spack package does not set the correct output granularity for maximum performance, which is `DFFT_TIMING=0`.

```
# spack edit cloverleaf
# ...
          targets.append('DFFT_MPI_CC=%s' % spec['mpi'].mpicc)
          targets.append('DFFT_MPI_CXX=%s' % spec['mpi'].mpicxx)
          targets.append('DFFT_MPI_F90=%s' % spec['mpi'].mpifc)

+         targets.append('DFFT_MPI_CPPFLAGS=-DDFFT_TIMING=0')

          if self.spec.satisfies('%nvhpc'):
               # remove -Wno-deprecated -std=gnu99
-              targets.append('DFFT_MPI_CFLAGS=-g -O3 -Wall')
+              targets.append('DFFT_MPI_CFLAGS+=-g -O3 -Wall')
```

Git commit hash of checkout for pacakage: fe5c226d

Pull request for Spack recipe changes: TODO: What is this?

### Building SWFFT

#### GCC 10.3.0

```
spack install swfft@1.0%gcc@10.3.0
```

```
$ spack spec -Il swfft@1.0%gcc@10.3.0

[+]  estt4jj  swfft@1.0%gcc@10.3.0 patches=ef6d6c7a5e5b207fef33ba4713be9fe522cd32f8aa53781a9a4e7b063ee52729 arch=linux-amzn2-graviton2
[+]  cgb46v5      ^fftw@3.3.9%gcc@10.3.0+mpi~openmp~pfft_patches precision=double,float arch=linux-amzn2-graviton2
[+]  zvamksn          ^openmpi@4.1.0%gcc@10.3.0~atomics~cuda~cxx~cxx_exceptions+gpfs~internal-hwloc~java~legacylaunchers~lustre~memchecker+pmi~singularity~sqlite3+static~thread_multiple+vt+wrapper-rpath fabrics=ofi patches=60ce20bc14d98c572ef7883b9fcd254c3f232c2f3a13377480f96466169ac4c8 schedulers=slurm arch=linux-amzn2-graviton2
[+]  cukmqbg              ^hwloc@2.5.0%gcc@10.3.0~cairo~cuda~gl~libudev+libxml2~netloc~nvml+pci+shared arch=linux-amzn2-graviton2
[+]  asgtk6a                  ^libpciaccess@0.16%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  z2uysov                      ^libtool@2.4.6%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  ebhjpix                          ^m4@1.4.18%gcc@10.3.0+sigsegv patches=3877ab548f88597ab2327a2230ee048d2d07ace1062efe81fc92e91b7f39cd00,fc9b61654a3ba1a8d6cd78ce087e7c96366c290bc8d2c299f09828d793b853c8 arch=linux-amzn2-graviton2
[+]  ltbv6bk                              ^libsigsegv@2.13%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  s4pw7zm                      ^pkgconf@1.7.4%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  4xr3hhh                      ^util-macros@1.19.3%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  iyhm3wi                  ^libxml2@2.9.10%gcc@10.3.0~python arch=linux-amzn2-graviton2
[+]  y5ei3cm                      ^libiconv@1.16%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  ye3kcvv                      ^xz@5.2.5%gcc@10.3.0~pic libs=shared,static arch=linux-amzn2-graviton2
[+]  qepjcvj                      ^zlib@1.2.11%gcc@10.3.0+optimize+pic+shared arch=linux-amzn2-graviton2
[+]  iwzirqc                  ^ncurses@6.2%gcc@10.3.0~symlinks+termlib abi=none arch=linux-amzn2-graviton2
[+]  tadxrfp              ^libevent@2.1.12%gcc@10.3.0+openssl arch=linux-amzn2-graviton2
[+]  5i3lgfb                  ^openssl@1.1.1k%gcc@10.3.0~docs+systemcerts arch=linux-amzn2-graviton2
[+]  4m7exgb                      ^perl@5.32.1%gcc@10.3.0+cpanm+shared+threads arch=linux-amzn2-graviton2
[+]  y42m6yr                          ^berkeley-db@18.1.40%gcc@10.3.0+cxx~docs+stl patches=b231fcc4d5cff05e5c3a4814f6a5af0e9a966428dc2176540d2c05aff41de522 arch=linux-amzn2-graviton2
[+]  rqrpmap                          ^bzip2@1.0.8%gcc@10.3.0~debug~pic+shared arch=linux-amzn2-graviton2
[+]  2w7bert                              ^diffutils@3.7%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  wjwqncx                          ^gdbm@1.19%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  3zy7kxk                              ^readline@8.1%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  72f5gvk              ^libfabric@1.11.1-aws%gcc@10.3.0~debug~kdreg fabrics=sockets,tcp,udp arch=linux-amzn2-graviton2
[+]  mhav5gn              ^numactl@2.0.14%gcc@10.3.0 patches=4e1d78cbbb85de625bad28705e748856033eaafab92a66dffd383a3d7e00cc94,62fc8a8bf7665a60e8f4c93ebbd535647cebf74198f7afafec4c085a8825c006 arch=linux-amzn2-graviton2
[+]  jkuhz64                  ^autoconf@2.69%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  xb2w5nc                  ^automake@1.16.3%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  wturp6c              ^openssh@8.5p1%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  ivotdt7                  ^libedit@3.1-20210216%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  wqpuvmh              ^slurm@20-02-4-1%gcc@10.3.0~gtk~hdf5~hwloc~mariadb~pmix+readline~restd sysconfdir=PREFIX/etc arch=linux-amzn2-graviton2
```

#### ARM 21.0.0.879

```
spack install swfft@1.0%arm@21.0.0.879
```

```
$ spack spec -Il swfft@1.0%arm@21.0.0.879

[+]  q3vxhyi  swfft@1.0%arm@21.0.0.879 patches=ef6d6c7a5e5b207fef33ba4713be9fe522cd32f8aa53781a9a4e7b063ee52729 arch=linux-amzn2-aarch64
[+]  v7y2mew      ^fftw@3.3.9%arm@21.0.0.879+mpi~openmp~pfft_patches precision=double,float arch=linux-amzn2-aarch64
[+]  lmaoy5t          ^openmpi@4.1.0%arm@21.0.0.879~atomics~cuda~cxx~cxx_exceptions+gpfs~internal-hwloc~java~legacylaunchers~lustre~memchecker+pmi~singularity~sqlite3+static~thread_multiple+vt+wrapper-rpath fabrics=ofi patches=60ce20bc14d98c572ef7883b9fcd254c3f232c2f3a13377480f96466169ac4c8 schedulers=slurm arch=linux-amzn2-aarch64
[+]  xl6anaa              ^hwloc@2.5.0%arm@21.0.0.879~cairo~cuda~gl~libudev+libxml2~netloc~nvml+pci+shared arch=linux-amzn2-aarch64
[+]  jueqz7p                  ^libpciaccess@0.16%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  e4ssqx6                      ^libtool@2.4.6%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  i2jmeo4                          ^m4@1.4.18%arm@21.0.0.879+sigsegv patches=3877ab548f88597ab2327a2230ee048d2d07ace1062efe81fc92e91b7f39cd00,fc9b61654a3ba1a8d6cd78ce087e7c96366c290bc8d2c299f09828d793b853c8 arch=linux-amzn2-aarch64
[+]  6jhzlul                              ^libsigsegv@2.13%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  zpuzm23                      ^pkgconf@1.7.4%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  uwcxkin                      ^util-macros@1.19.3%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  dypqz2i                  ^libxml2@2.9.10%arm@21.0.0.879~python arch=linux-amzn2-aarch64
[+]  7vnthzn                      ^libiconv@1.16%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  zqsab4f                      ^xz@5.2.5%arm@21.0.0.879~pic libs=shared,static arch=linux-amzn2-aarch64
[+]  puuxvg2                      ^zlib@1.2.11%arm@21.0.0.879+optimize+pic+shared arch=linux-amzn2-aarch64
[+]  uhtqtlb                  ^ncurses@6.2%arm@21.0.0.879~symlinks+termlib abi=none arch=linux-amzn2-aarch64
[+]  gonqskn              ^libevent@2.1.12%arm@21.0.0.879+openssl arch=linux-amzn2-aarch64
[+]  vc3waha                  ^openssl@1.1.1k%arm@21.0.0.879~docs+systemcerts arch=linux-amzn2-aarch64
[+]  vv6txro                      ^perl@5.32.1%arm@21.0.0.879+cpanm+shared+threads arch=linux-amzn2-aarch64
[+]  33wiajj                          ^berkeley-db@18.1.40%arm@21.0.0.879+cxx~docs+stl patches=b231fcc4d5cff05e5c3a4814f6a5af0e9a966428dc2176540d2c05aff41de522 arch=linux-amzn2-aarch64
[+]  z4ybgri                          ^bzip2@1.0.8%arm@21.0.0.879~debug~pic+shared arch=linux-amzn2-aarch64
[+]  adtc6yc                              ^diffutils@3.7%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  645q4qj                          ^gdbm@1.19%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  3haw5gt                              ^readline@8.1%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  qdn27nh              ^libfabric@1.11.1-aws%arm@21.0.0.879~debug~kdreg fabrics=sockets,tcp,udp arch=linux-amzn2-aarch64
[+]  mv2g7r5              ^numactl@2.0.14%arm@21.0.0.879 patches=4e1d78cbbb85de625bad28705e748856033eaafab92a66dffd383a3d7e00cc94,62fc8a8bf7665a60e8f4c93ebbd535647cebf74198f7afafec4c085a8825c006 arch=linux-amzn2-aarch64
[+]  dcs645r                  ^autoconf@2.69%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  edezkz3                  ^automake@1.16.3%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  6vvthuo              ^openssh@8.5p1%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  xe4evc4                  ^libedit@3.1-20210216%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  x5xehti              ^slurm@20-02-4-1%arm@21.0.0.879~gtk~hdf5~hwloc~mariadb~pmix+readline~restd sysconfdir=PREFIX/etc arch=linux-amzn2-aarch64
```

#### NVHPC 21.2

```
spack install swfft@1.0%nvhpc@21.2
```

```
$ spack spec -Il swfft@1.0%nvhpc@21.2
```

## Test Case 1

[ReFrame Benchmark 1](#)

```
../bin/reframe -c benchmark.py -r --performance-report
```

### Validation

Details of the validation for `Test Case 1`.

The validation of the results consists in a comparison of the binary output, extracting the performance measurements and using the x86 output as the reference.


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
