# ExaSP2

**Description:** Proxy-app, reference implementation of typical linear algebra algorithms and workloads for a quantum molecular dynamics (QMD) electronic structure code. The algorithm is based on a recursive second-order Fermi-Operator expansion method (SP2) and is tailored for density functional based tight-binding calculations of material systems. The SP2 algorithm variants are part of the Los Alamos Transferable Tight-binding for Energetics (LATTE) code, based on a matrix expansion of the Fermi operator in a recursive series of generalized matrix-matrix multiplications. It is created and maintained by Co-Design Center for Particle Applications (CoPA). The code is intended to serve as a vehicle for co-design by allowing others to extend and/or reimplement as needed to test performance of new architectures, programming models, etc.

**URL:** https://github.com/ECP-copa/ExaSP2

**Team:**

## Compilation

### Spack Package Modification

Details of any changes to the Spack recipe used.

Git commit hash of checkout for pacakage:

Pull request for Spack recipe changes:

### Building ExaSP2

#### Compiler NVHPC v21.2 x86_64
```
spack install python@3.8.11
spack install cmake@3.20.4
spack external find cmake
spack external find python

spack add exasp2%nvhpc
spack install
```
#### Compiler NVHPC v21.2 AARCH64
```
spack install python@3.8.11
spack install cmake@3.20.4
spack external find cmake
spack external find python

spack add exasp2%nvhpc
spack install
```
#### Compiler GCC v10.3 x86_64

```
spack install exasp2%gcc@10.3 ^openmpi
```

```
$ spack spec -Il exasp2%gcc@10.3.0 ^openmpi
Input spec
--------------------------------
 -   exasp2%gcc@10.3.0
 -       ^openmpi

Concretized
--------------------------------
[+]  4i67huk  exasp2@1.0%gcc@10.3.0+mpi arch=linux-amzn2-skylake_avx512
[+]  rt6uajc      ^bml@1.3.1%gcc@10.3.0~ipo+mpi+shared build_type=RelWithDebInfo arch=linux-amzn2-skylake_avx512
 -   gozuirv          ^cmake@3.20.5%gcc@10.3.0~doc+ncurses+openssl+ownlibs~qt build_type=Release arch=linux-amzn2-skylake_avx512
[+]  xbybdoz              ^ncurses@6.2%gcc@10.3.0~symlinks+termlib abi=none arch=linux-amzn2-skylake_avx512
 -   i665ooz                  ^pkgconf@1.7.4%gcc@10.3.0 arch=linux-amzn2-skylake_avx512
[+]  larjnul              ^openssl@1.1.1k%gcc@10.3.0~docs+systemcerts arch=linux-amzn2-skylake_avx512
 -   fb3kjch                  ^perl@5.32.1%gcc@10.3.0+cpanm+shared+threads arch=linux-amzn2-skylake_avx512
 -   i5lbkjo                      ^berkeley-db@18.1.40%gcc@10.3.0+cxx~docs+stl patches=b231fcc4d5cff05e5c3a4814f6a5af0e9a966428dc2176540d2c05aff41de522 arch=linux-amzn2-skylake_avx512
 -   s36txvt                      ^bzip2@1.0.8%gcc@10.3.0~debug~pic+shared arch=linux-amzn2-skylake_avx512
 -   kjoplsl                          ^diffutils@3.7%gcc@10.3.0 arch=linux-amzn2-skylake_avx512
[+]  qmzfn6j                              ^libiconv@1.16%gcc@10.3.0 arch=linux-amzn2-skylake_avx512
 -   fgwgsih                      ^gdbm@1.19%gcc@10.3.0 arch=linux-amzn2-skylake_avx512
 -   i35suwy                          ^readline@8.1%gcc@10.3.0 arch=linux-amzn2-skylake_avx512
[+]  q2x25kt                      ^zlib@1.2.11%gcc@10.3.0+optimize+pic+shared arch=linux-amzn2-skylake_avx512
[+]  skexx3l          ^openblas@0.3.15%gcc@10.3.0~bignuma~consistent_fpcsr~ilp64+locking+pic+shared threads=none arch=linux-amzn2-skylake_avx512
[+]  pmn26hx          ^openmpi@4.1.0%gcc@10.3.0~atomics~cuda~cxx~cxx_exceptions+gpfs~internal-hwloc~java~legacylaunchers~lustre~memchecker+pmi~singularity~sqlite3+static~thread_multiple+vt+wrapper-rpath fabrics=ofi patches=60ce20bc14d98c572ef7883b9fcd254c3f232c2f3a13377480f96466169ac4c8 schedulers=slurm arch=linux-amzn2-skylake_avx512
[+]  xkz726a              ^hwloc@2.5.0%gcc@10.3.0~cairo~cuda~gl~libudev+libxml2~netloc~nvml+pci+shared arch=linux-amzn2-skylake_avx512
[+]  a4nq5nh                  ^libpciaccess@0.16%gcc@10.3.0 arch=linux-amzn2-skylake_avx512
 -   ya47eic                      ^libtool@2.4.6%gcc@10.3.0 arch=linux-amzn2-skylake_avx512
 -   6y53od3                          ^m4@1.4.18%gcc@10.3.0+sigsegv patches=3877ab548f88597ab2327a2230ee048d2d07ace1062efe81fc92e91b7f39cd00,fc9b61654a3ba1a8d6cd78ce087e7c96366c290bc8d2c299f09828d793b853c8 arch=linux-amzn2-skylake_avx512
 -   5qpmdxk                              ^libsigsegv@2.13%gcc@10.3.0 arch=linux-amzn2-skylake_avx512
 -   4fouma3                      ^util-macros@1.19.3%gcc@10.3.0 arch=linux-amzn2-skylake_avx512
[+]  mztzlil                  ^libxml2@2.9.10%gcc@10.3.0~python arch=linux-amzn2-skylake_avx512
[+]  p7yqdpr                      ^xz@5.2.5%gcc@10.3.0~pic libs=shared,static arch=linux-amzn2-skylake_avx512
[+]  rt2yj4o              ^libevent@2.1.12%gcc@10.3.0+openssl arch=linux-amzn2-skylake_avx512
[+]  aodqozx              ^libfabric@1.11.1-aws%gcc@10.3.0~debug~kdreg fabrics=sockets,tcp,udp arch=linux-amzn2-skylake_avx512
[+]  uqxtsju              ^numactl@2.0.14%gcc@10.3.0 patches=4e1d78cbbb85de625bad28705e748856033eaafab92a66dffd383a3d7e00cc94,62fc8a8bf7665a60e8f4c93ebbd535647cebf74198f7afafec4c085a8825c006 arch=linux-amzn2-skylake_avx512
 -   qx56ujy                  ^autoconf@2.69%gcc@10.3.0 arch=linux-amzn2-skylake_avx512
 -   xveamuz                  ^automake@1.16.3%gcc@10.3.0 arch=linux-amzn2-skylake_avx512
[+]  7t25qrr              ^openssh@8.5p1%gcc@10.3.0 arch=linux-amzn2-skylake_avx512
[+]  7523zhe                  ^libedit@3.1-20210216%gcc@10.3.0 arch=linux-amzn2-skylake_avx512
[+]  724okpi              ^slurm@20-02-4-1%gcc@10.3.0~gtk~hdf5~hwloc~mariadb~pmix+readline~restd sysconfdir=PREFIX/etc arch=linux-amzn2-skylake_avx512
 -   p7mkxd4          ^python@3.8.11%gcc@10.3.0+bz2+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tix~tkinter~ucs4+uuid+zlib patches=0d98e93189bc278fbc37a50ed7f183bd8aaf249a8e1670a465f0db6bb4f8cf87 arch=linux-amzn2-skylake_avx512
 -   256y6qy              ^expat@2.4.1%gcc@10.3.0+libbsd arch=linux-amzn2-skylake_avx512
 -   mxgrkle                  ^libbsd@0.11.3%gcc@10.3.0 arch=linux-amzn2-skylake_avx512
 -   aehweer                      ^libmd@1.0.3%gcc@10.3.0 arch=linux-amzn2-skylake_avx512
 -   vfg4fms              ^gettext@0.21%gcc@10.3.0+bzip2+curses+git~libunistring+libxml2+tar+xz arch=linux-amzn2-skylake_avx512
 -   fajl3kg                  ^tar@1.34%gcc@10.3.0 arch=linux-amzn2-skylake_avx512
 -   vv3r7pc              ^libffi@3.3%gcc@10.3.0 patches=26f26c6f29a7ce9bf370ad3ab2610f99365b4bdd7b82e7c31df41a3370d685c0 arch=linux-amzn2-skylake_avx512
 -   6ox5zyb              ^sqlite@3.35.5%gcc@10.3.0+column_metadata+fts~functions~rtree arch=linux-amzn2-skylake_avx512
 -   uzq2g5d              ^util-linux-uuid@2.36.2%gcc@10.3.0 arch=linux-amzn2-skylake_avx512

```

#### Compiler GCC v10.3 AARCH64

```
spack install exasp2%gcc@10.3.0 ^openmpi
```

```
$ spack spec -Il exasp2
Input spec
--------------------------------
 -   exasp2

Concretized
--------------------------------
[+]  wocdwe5  exasp2@1.0%gcc@10.3.0+mpi arch=linux-amzn2-graviton2
[+]  4p22aej      ^bml@1.3.1%gcc@10.3.0~ipo+mpi+shared build_type=RelWithDebInfo arch=linux-amzn2-graviton2
[+]  m7325ee          ^cmake@3.20.5%gcc@10.3.0~doc+ncurses+openssl+ownlibs~qt build_type=Release arch=linux-amzn2-graviton2
[+]  iwzirqc              ^ncurses@6.2%gcc@10.3.0~symlinks+termlib abi=none arch=linux-amzn2-graviton2
[+]  s4pw7zm                  ^pkgconf@1.7.4%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  5i3lgfb              ^openssl@1.1.1k%gcc@10.3.0~docs+systemcerts arch=linux-amzn2-graviton2
[+]  ijjxlug                  ^perl@5.34.0%gcc@10.3.0+cpanm+shared+threads arch=linux-amzn2-graviton2
[+]  y42m6yr                      ^berkeley-db@18.1.40%gcc@10.3.0+cxx~docs+stl patches=b231fcc4d5cff05e5c3a4814f6a5af0e9a966428dc2176540d2c05aff41de522 arch=linux-amzn2-graviton2
[+]  rqrpmap                      ^bzip2@1.0.8%gcc@10.3.0~debug~pic+shared arch=linux-amzn2-graviton2
[+]  2w7bert                          ^diffutils@3.7%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  y5ei3cm                              ^libiconv@1.16%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  wjwqncx                      ^gdbm@1.19%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  3zy7kxk                          ^readline@8.1%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  qepjcvj                      ^zlib@1.2.11%gcc@10.3.0+optimize+pic+shared arch=linux-amzn2-graviton2
[+]  rv7gj6u          ^openblas@0.3.15%gcc@10.3.0~bignuma~consistent_fpcsr~ilp64+locking+pic+shared threads=none arch=linux-amzn2-graviton2
[+]  l7oony6          ^openmpi@4.1.1%gcc@10.3.0~atomics~cuda~cxx~cxx_exceptions+gpfs~internal-hwloc~java~legacylaunchers~lustre~memchecker~pmi~singularity~sqlite3+static~thread_multiple+vt+wrapper-rpath fabrics=none schedulers=none arch=linux-amzn2-graviton2
[+]  cukmqbg              ^hwloc@2.5.0%gcc@10.3.0~cairo~cuda~gl~libudev+libxml2~netloc~nvml+pci+shared arch=linux-amzn2-graviton2
[+]  asgtk6a                  ^libpciaccess@0.16%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  z2uysov                      ^libtool@2.4.6%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  3mz7xyt                          ^m4@1.4.19%gcc@10.3.0+sigsegv arch=linux-amzn2-graviton2
[+]  ltbv6bk                              ^libsigsegv@2.13%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  4xr3hhh                      ^util-macros@1.19.3%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  iyhm3wi                  ^libxml2@2.9.10%gcc@10.3.0~python arch=linux-amzn2-graviton2
[+]  ye3kcvv                      ^xz@5.2.5%gcc@10.3.0~pic libs=shared,static arch=linux-amzn2-graviton2
[+]  tadxrfp              ^libevent@2.1.12%gcc@10.3.0+openssl arch=linux-amzn2-graviton2
[+]  mhav5gn              ^numactl@2.0.14%gcc@10.3.0 patches=4e1d78cbbb85de625bad28705e748856033eaafab92a66dffd383a3d7e00cc94,62fc8a8bf7665a60e8f4c93ebbd535647cebf74198f7afafec4c085a8825c006 arch=linux-amzn2-graviton2
[+]  gignjm7                  ^autoconf@2.69%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  h3qfzfb                  ^automake@1.16.3%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  wturp6c              ^openssh@8.5p1%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  ivotdt7                  ^libedit@3.1-20210216%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  62czasr          ^python@3.8.11%gcc@10.3.0+bz2+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tix~tkinter~ucs4+uuid+zlib patches=0d98e93189bc278fbc37a50ed7f183bd8aaf249a8e1670a465f0db6bb4f8cf87 arch=linux-amzn2-graviton2
[+]  ychdz7l              ^expat@2.4.1%gcc@10.3.0+libbsd arch=linux-amzn2-graviton2
[+]  ourxkez                  ^libbsd@0.11.3%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  nssrqfc                      ^libmd@1.0.3%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  fqlpcsl              ^gettext@0.21%gcc@10.3.0+bzip2+curses+git~libunistring+libxml2+tar+xz arch=linux-amzn2-graviton2
[+]  v6cutkh                  ^tar@1.34%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  35cffos              ^libffi@3.3%gcc@10.3.0 patches=26f26c6f29a7ce9bf370ad3ab2610f99365b4bdd7b82e7c31df41a3370d685c0 arch=linux-amzn2-graviton2
[+]  2q753q6              ^sqlite@3.35.5%gcc@10.3.0+column_metadata+fts~functions~rtree arch=linux-amzn2-graviton2
[+]  2non7qx              ^util-linux-uuid@2.36.2%gcc@10.3.0 arch=linux-amzn2-graviton2
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
