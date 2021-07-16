# ExaML 

**Description:** Exascale Maximum Likelihood (ExaML) code for phylogenetic inference using MPI. This code implements the popular RAxML search algorithm for maximum likelihood based inference of phylogenetic trees.

**URL:** https://github.com/stamatak/ExaML

**Team:**  

## Compilation

### Spack Package Modification

Details of any changes to the Spack recipe used.

Git commit hash of checkout for pacakage:

Pull request for Spack recipe changes:

### Building ExaML



#### Compiler 1: gcc@10.3.0

```
spack install examl%gcc
```

```
[+]  fso2lc3  examl@3.0.22%gcc@10.3.0+mpi dev_path=/scratch/home/cz5/examl/examl arch=linux-amzn2-graviton2
[+]  zvamksn      ^openmpi@4.1.0%gcc@10.3.0~atomics~cuda~cxx~cxx_exceptions+gpfs~internal-hwloc~java~legacylaunchers~lustre~memchecker+pmi~singularity~sqlite3+static~thread_multiple+vt+wrapper-rpath fabrics=ofi patches=60ce20bc14d98c572ef7883b9fcd254c3f232c2f3a13377480f96466169ac4c8 schedulers=slurm arch=linux-amzn2-graviton2
[+]  cukmqbg          ^hwloc@2.5.0%gcc@10.3.0~cairo~cuda~gl~libudev+libxml2~netloc~nvml+pci+shared arch=linux-amzn2-graviton2
[+]  asgtk6a              ^libpciaccess@0.16%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  z2uysov                  ^libtool@2.4.6%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  ebhjpix                      ^m4@1.4.18%gcc@10.3.0+sigsegv patches=3877ab548f88597ab2327a2230ee048d2d07ace1062efe81fc92e91b7f39cd00,fc9b61654a3ba1a8d6cd78ce087e7c96366c290bc8d2c299f09828d793b853c8 arch=linux-amzn2-graviton2
[+]  ltbv6bk                          ^libsigsegv@2.13%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  s4pw7zm                  ^pkgconf@1.7.4%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  4xr3hhh                  ^util-macros@1.19.3%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  iyhm3wi              ^libxml2@2.9.10%gcc@10.3.0~python arch=linux-amzn2-graviton2
[+]  y5ei3cm                  ^libiconv@1.16%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  ye3kcvv                  ^xz@5.2.5%gcc@10.3.0~pic libs=shared,static arch=linux-amzn2-graviton2
[+]  qepjcvj                  ^zlib@1.2.11%gcc@10.3.0+optimize+pic+shared arch=linux-amzn2-graviton2
[+]  iwzirqc              ^ncurses@6.2%gcc@10.3.0~symlinks+termlib abi=none arch=linux-amzn2-graviton2
[+]  tadxrfp          ^libevent@2.1.12%gcc@10.3.0+openssl arch=linux-amzn2-graviton2
[+]  5i3lgfb              ^openssl@1.1.1k%gcc@10.3.0~docs+systemcerts arch=linux-amzn2-graviton2
[+]  4m7exgb                  ^perl@5.32.1%gcc@10.3.0+cpanm+shared+threads arch=linux-amzn2-graviton2
[+]  y42m6yr                      ^berkeley-db@18.1.40%gcc@10.3.0+cxx~docs+stl patches=b231fcc4d5cff05e5c3a4814f6a5af0e9a966428dc2176540d2c05aff41de522 arch=linux-amzn2-graviton2
[+]  rqrpmap                      ^bzip2@1.0.8%gcc@10.3.0~debug~pic+shared arch=linux-amzn2-graviton2
[+]  2w7bert                          ^diffutils@3.7%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  wjwqncx                      ^gdbm@1.19%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  3zy7kxk                          ^readline@8.1%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  72f5gvk          ^libfabric@1.11.1-aws%gcc@10.3.0~debug~kdreg fabrics=sockets,tcp,udp arch=linux-amzn2-graviton2
[+]  mhav5gn          ^numactl@2.0.14%gcc@10.3.0 patches=4e1d78cbbb85de625bad28705e748856033eaafab92a66dffd383a3d7e00cc94,62fc8a8bf7665a60e8f4c93ebbd535647cebf74198f7afafec4c085a8825c006 arch=linux-amzn2-graviton2
[+]  jkuhz64              ^autoconf@2.69%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  xb2w5nc              ^automake@1.16.3%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  wturp6c          ^openssh@8.5p1%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  ivotdt7              ^libedit@3.1-20210216%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  wqpuvmh          ^slurm@20-02-4-1%gcc@10.3.0~gtk~hdf5~hwloc~mariadb~pmix+readline~restd sysconfdir=PREFIX/etc arch=linux-amzn2-graviton2
```

#### Compiler 2: arm@21.0.0.879

```
spack install examl%arm
```

```
[+]  gm6uysl  examl@3.0.22%arm@21.0.0.879+mpi dev_path=/scratch/home/cz5/examl-arm/examl arch=linux-amzn2-graviton2
[+]  huifkle      ^openmpi@4.1.0%arm@21.0.0.879~atomics~cuda~cxx~cxx_exceptions+gpfs~internal-hwloc~java~legacylaunchers~lustre~memchecker+pmi~singularity~sqlite3+static~thread_multiple+vt+wrapper-rpath fabrics=ofi patches=60ce20bc14d98c572ef7883b9fcd254c3f232c2f3a13377480f96466169ac4c8 schedulers=slurm arch=linux-amzn2-graviton2
[+]  xsh5tug          ^hwloc@2.5.0%arm@21.0.0.879~cairo~cuda~gl~libudev+libxml2~netloc~nvml+pci+shared arch=linux-amzn2-graviton2
[+]  heo5xlh              ^libpciaccess@0.16%arm@21.0.0.879 arch=linux-amzn2-graviton2
[+]  xcqslvj                  ^libtool@2.4.6%arm@21.0.0.879 arch=linux-amzn2-graviton2
[+]  guhrr3n                      ^m4@1.4.18%arm@21.0.0.879+sigsegv patches=3877ab548f88597ab2327a2230ee048d2d07ace1062efe81fc92e91b7f39cd00,fc9b61654a3ba1a8d6cd78ce087e7c96366c290bc8d2c299f09828d793b853c8 arch=linux-amzn2-graviton2
[+]  q27ybb5                          ^libsigsegv@2.13%arm@21.0.0.879 arch=linux-amzn2-graviton2
[+]  s6jl232                  ^pkgconf@1.7.4%arm@21.0.0.879 arch=linux-amzn2-graviton2
[+]  6eey55q                  ^util-macros@1.19.3%arm@21.0.0.879 arch=linux-amzn2-graviton2
[+]  7og6524              ^libxml2@2.9.10%arm@21.0.0.879~python arch=linux-amzn2-graviton2
[+]  4fpawwk                  ^libiconv@1.16%arm@21.0.0.879 arch=linux-amzn2-graviton2
[+]  3uhexv5                  ^xz@5.2.5%arm@21.0.0.879~pic libs=shared,static arch=linux-amzn2-graviton2
[+]  kfhtmo3                  ^zlib@1.2.11%arm@21.0.0.879+optimize+pic+shared arch=linux-amzn2-graviton2
[+]  5fshnbc              ^ncurses@6.2%arm@21.0.0.879~symlinks+termlib abi=none arch=linux-amzn2-graviton2
[+]  hj5l7x5          ^libevent@2.1.12%arm@21.0.0.879+openssl arch=linux-amzn2-graviton2
[+]  b6rhpqo              ^openssl@1.1.1k%arm@21.0.0.879~docs+systemcerts arch=linux-amzn2-graviton2
[+]  aoyzxyq                  ^perl@5.32.1%arm@21.0.0.879+cpanm+shared+threads arch=linux-amzn2-graviton2
[+]  rd3hv7n                      ^berkeley-db@18.1.40%arm@21.0.0.879+cxx~docs+stl patches=b231fcc4d5cff05e5c3a4814f6a5af0e9a966428dc2176540d2c05aff41de522 arch=linux-amzn2-graviton2
[+]  qaavobd                      ^bzip2@1.0.8%arm@21.0.0.879~debug~pic+shared arch=linux-amzn2-graviton2
[+]  qchmimy                          ^diffutils@3.7%arm@21.0.0.879 arch=linux-amzn2-graviton2
[+]  jbenr5m                      ^gdbm@1.19%arm@21.0.0.879 arch=linux-amzn2-graviton2
[+]  7fjq32x                          ^readline@8.1%arm@21.0.0.879 arch=linux-amzn2-graviton2
[+]  v75lszn          ^libfabric@1.11.1-aws%arm@21.0.0.879~debug~kdreg fabrics=sockets,tcp,udp arch=linux-amzn2-graviton2
[+]  325gh7i          ^numactl@2.0.14%arm@21.0.0.879 patches=4e1d78cbbb85de625bad28705e748856033eaafab92a66dffd383a3d7e00cc94,62fc8a8bf7665a60e8f4c93ebbd535647cebf74198f7afafec4c085a8825c006 arch=linux-amzn2-graviton2
[+]  mbkv7qv              ^autoconf@2.69%arm@21.0.0.879 arch=linux-amzn2-graviton2
[+]  toijtok              ^automake@1.16.3%arm@21.0.0.879 arch=linux-amzn2-graviton2
[+]  7cmi2lb          ^openssh@8.5p1%arm@21.0.0.879 arch=linux-amzn2-graviton2
[+]  qytqrqe              ^libedit@3.1-20210216%arm@21.0.0.879 arch=linux-amzn2-graviton2
[+]  uxllonc          ^slurm@20-02-4-1%arm@21.0.0.879~gtk~hdf5~hwloc~mariadb~pmix+readline~restd sysconfdir=PREFIX/etc arch=linux-amzn2-graviton2
```
#### Compiler 3: nvhpc

We haven't yet successfully build ExaML on nvhpc.

Reason:

ExaML uses a lot of Intel intrinsics. To build it on ARM, we need to use sse2neon. However, this technique is not supported by nvhpc.

## Test Case 1

> examl -t /home/peize/examl-test/case1/49.tree -m PSR -s /home/peize/examl-test/case1/49.unpartitioned.binary -n T1

[ReFrame Benchmark 1](#)

```
../bin/reframe -c benchmark.py -r --performance-report
```

### Validation

Details of the validation for `Test Case 1`.


### ReFrame Output

#### GCC compiler on aarch64 c6gn

```
==============================================================================
PERFORMANCE REPORT
------------------------------------------------------------------------------
ExaML_case1_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_1_OMP_1
- aws:c6gn
   - builtin
      * num_tasks: 1
      * Total Time: 8.206136 s
------------------------------------------------------------------------------
ExaML_case1_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_2_OMP_1
   - builtin
      * num_tasks: 2
      * Total Time: 6.26856 s
------------------------------------------------------------------------------
ExaML_case1_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_4_OMP_1
   - builtin
      * num_tasks: 4
      * Total Time: 6.533407 s
------------------------------------------------------------------------------
ExaML_case1_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_8_OMP_1
   - builtin
      * num_tasks: 8
      * Total Time: 7.698577 s
------------------------------------------------------------------------------
ExaML_case1_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_16_OMP_1
   - builtin
      * num_tasks: 16
      * Total Time: 9.4256 s
------------------------------------------------------------------------------
ExaML_case1_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_32_OMP_1
   - builtin
      * num_tasks: 32
      * Total Time: 11.153909 s
------------------------------------------------------------------------------
ExaML_case1_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_64_OMP_1
   - builtin
      * num_tasks: 64
      * Total Time: 14.792326 s
------------------------------------------------------------------------------
ExaML_case1_gcc_examl_3_0_22_gcc_10_3_0_N_2_MPI_128_OMP_1
   - builtin
      * num_tasks: 128
      * Total Time: 38.992808 s
------------------------------------------------------------------------------
ExaML_case1_gcc_examl_3_0_22_gcc_10_3_0_N_4_MPI_256_OMP_1
   - builtin
      * num_tasks: 256
      * Total Time: 55.726266 s
------------------------------------------------------------------------------
```

#### ARM compiler on aarch64 c6gn

```
==============================================================================
PERFORMANCE REPORT
------------------------------------------------------------------------------
ExaML_case1_arm_examl_3_0_22_arm_21_0_0_879_N_1_MPI_1_OMP_1
- aws:c6gn
   - builtin
      * num_tasks: 1
      * Total Time: 8.3541 s
------------------------------------------------------------------------------
ExaML_case1_arm_examl_3_0_22_arm_21_0_0_879_N_1_MPI_2_OMP_1
   - builtin
      * num_tasks: 2
      * Total Time: 6.207255 s
------------------------------------------------------------------------------
ExaML_case1_arm_examl_3_0_22_arm_21_0_0_879_N_1_MPI_4_OMP_1
   - builtin
      * num_tasks: 4
      * Total Time: 6.312409 s
------------------------------------------------------------------------------
ExaML_case1_arm_examl_3_0_22_arm_21_0_0_879_N_1_MPI_8_OMP_1
   - builtin
      * num_tasks: 8
      * Total Time: 7.812155 s
------------------------------------------------------------------------------
ExaML_case1_arm_examl_3_0_22_arm_21_0_0_879_N_1_MPI_16_OMP_1
   - builtin
      * num_tasks: 16
      * Total Time: 9.898919 s
------------------------------------------------------------------------------
ExaML_case1_arm_examl_3_0_22_arm_21_0_0_879_N_1_MPI_32_OMP_1
   - builtin
      * num_tasks: 32
      * Total Time: 13.136745 s
------------------------------------------------------------------------------
ExaML_case1_arm_examl_3_0_22_arm_21_0_0_879_N_1_MPI_64_OMP_1
   - builtin
      * num_tasks: 64
      * Total Time: 16.193352 s
------------------------------------------------------------------------------
ExaML_case1_arm_examl_3_0_22_arm_21_0_0_879_N_2_MPI_128_OMP_1
   - builtin
      * num_tasks: 128
      * Total Time: 48.722489 s
------------------------------------------------------------------------------
ExaML_case1_arm_examl_3_0_22_arm_21_0_0_879_N_4_MPI_256_OMP_1
   - builtin
      * num_tasks: 256
      * Total Time: 70.327222 s
------------------------------------------------------------------------------
```

#### GCC compiler on x86 c5n

```
==============================================================================
PERFORMANCE REPORT
------------------------------------------------------------------------------
ExaML_case1_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_1_OMP_1
- aws:c5n
   - builtin
      * num_tasks: 1
      * Total Time: 10.29801 s
------------------------------------------------------------------------------
ExaML_case1_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_2_OMP_1
   - builtin
      * num_tasks: 2
      * Total Time: 8.69561 s
------------------------------------------------------------------------------
ExaML_case1_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_4_OMP_1
   - builtin
      * num_tasks: 4
      * Total Time: 8.311922 s
------------------------------------------------------------------------------
ExaML_case1_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_8_OMP_1
   - builtin
      * num_tasks: 8
      * Total Time: 9.335008 s
------------------------------------------------------------------------------
ExaML_case1_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_16_OMP_1
   - builtin
      * num_tasks: 16
      * Total Time: 11.231569 s
------------------------------------------------------------------------------
ExaML_case1_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_32_OMP_1
   - builtin
      * num_tasks: 32
      * Total Time: 15.254454 s
------------------------------------------------------------------------------
ExaML_case1_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_64_OMP_1
   - builtin
      * num_tasks: 64
      * Total Time: 19.561287 s
------------------------------------------------------------------------------
ExaML_case1_gcc_examl_3_0_22_gcc_10_3_0_N_2_MPI_128_OMP_1
   - builtin
      * num_tasks: 128
      * Total Time: 51.807964 s
------------------------------------------------------------------------------
ExaML_case1_gcc_examl_3_0_22_gcc_10_3_0_N_4_MPI_256_OMP_1
   - builtin
      * num_tasks: 256
      * Total Time: 66.533237 s
------------------------------------------------------------------------------
```

### Strong Scaling (on&off-node, 1-4 nodes) and Compiler Comparison

This includes results of tasks: P1, P3, P6

| Cores(MPI rank) | GCC | ARM |
|-------|------------|------------|
|  1     |  8.21   | 8.35|
|  2     |  6.27    | 6.21|
|  4     |  6.53    | 6.31|
|  8     |  7.70    | 7.81|
|  16    |  9.43     | 9.90 |
|  32    |  11.15     | 13.14 |
|  64    |  14.79     | 16.19 |
|  128   |  38.99     | 48.72	|
|  256   |  55.73	 | 70.33	|


### Serial Hot-spot Profile

List of top-10 functions / code locations from a serial profile. Use GCC compiler.

Profiling command used:
```
map --profile srun -N 1 -n 1 examl -t /home/peize/examl-test/case1/49.tree -m PSR -s /home/peize/examl-test/case1/49.unpartitioned.binary -n T1
```

| Position | Routine                | Time (%) |
| -------- | ---------------------- | -------- |
| 1        | newviewGTRCAT          | 36.8%    |
| 2        | execCore               | 24.3%    |
| 3        | exp                    | 11.2%    |
| 4        | __exp_finite           | 7.8%     |
| 5        | makenewzIterative      | 3.3%     |
| 6        | MPI_Allreduce          | 3.3%     |
| 7        | __log_finite           | 3.1%     |
| 8        | newviewIterative       | 2.7%     |
| 9        | log                    | 2.0%     |
| 10       | evaluatePartialGeneric | 1.6%     |


### Full Node Hot-spot Profile

List of top-10 functions / code locations from a serial profile. Use GCC compiler.

Profiling command used:
```
map --profile srun -N 1 -n 64 examl -t /home/peize/examl-test/case1/49.tree -m PSR -s /home/peize/examl-test/case1/49.unpartitioned.binary -n T1
```

| Position | Routine          | Tims (%) | MPI (%) |
| -------- | ---------------- | -------- | ------- |
| 1        | MPI_Allreduce    | 93.6%    | 93.6%   |
| 2        | exp              | 2.2%     |         |
| 3        | __exp_finite     | 1.7%     |         |
| 4        | newviewIterative | 0.6%     |         |
| 5        | MPI_Barrier      | 0.3%     | 0.3%    |
| 6        | newviewGTRCAT    | 0.2%     |         |
| 7        | execCore         | 0.2%     |         |
| 8        | __log_finite     | 0.1%     |         |
| 9        | topLevelMakenewz | <0.1%    | 88.6%   |
| 10       | saveSubtree      | <0.1%    |         |


### On-Node & Off-Node Architecture Comparison

On-Node & Off-Node scaling study for two architectures.

| Cores | C6gn (Aarch64) | C5n (X86) |
|-------|----------------|-----------|
| 1     |       8.21         |      10.30     |
| 2     |       6.27         |         8.70  |
| 4     |       6.53         |      8.31     |
| 8     |       7.70         |      9.34     |
| 16    |       9.43         |      11.23     |
| 32    |       11.15         |      15.25     |
| 64    |       14.79         |      19.56     |
| 128    |      38.99          |     51.81      |
| 256    |      55.73          |     66.53      |

## Test Case 2

> examl -t /home/peize/examl-test/case1/49.tree -m GAMMA -s /home/peize/examl-test/case1/49.unpartitioned.binary -n T1

[ReFrame Benchmark 1](#)

```
../bin/reframe -c benchmark.py -r --performance-report
```

### Validation

Details of the validation for `Test Case 1`.


### ReFrame Output

#### GCC compiler on aarch64 c6gn

```
==============================================================================
PERFORMANCE REPORT
------------------------------------------------------------------------------
ExaML_case2_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_1_OMP_1
- aws:c6gn
   - builtin
      * num_tasks: 1
      * Total Time: 18.705801 s
------------------------------------------------------------------------------
ExaML_case2_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_2_OMP_1
   - builtin
      * num_tasks: 2
      * Total Time: 11.11089 s
------------------------------------------------------------------------------
ExaML_case2_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_4_OMP_1
   - builtin
      * num_tasks: 4
      * Total Time: 8.815214 s
------------------------------------------------------------------------------
ExaML_case2_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_8_OMP_1
   - builtin
      * num_tasks: 8
      * Total Time: 8.999906 s
------------------------------------------------------------------------------
ExaML_case2_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_16_OMP_1
   - builtin
      * num_tasks: 16
      * Total Time: 10.470279 s
------------------------------------------------------------------------------
ExaML_case2_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_32_OMP_1
   - builtin
      * num_tasks: 32
      * Total Time: 12.440436 s
------------------------------------------------------------------------------
ExaML_case2_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_64_OMP_1
   - builtin
      * num_tasks: 64
      * Total Time: 17.292035 s
------------------------------------------------------------------------------
ExaML_case2_gcc_examl_3_0_22_gcc_10_3_0_N_2_MPI_128_OMP_1
   - builtin
      * num_tasks: 128
      * Total Time: 49.663453 s
------------------------------------------------------------------------------
ExaML_case2_gcc_examl_3_0_22_gcc_10_3_0_N_4_MPI_256_OMP_1
   - builtin
      * num_tasks: 256
      * Total Time: 73.42773 s
------------------------------------------------------------------------------
```

#### ARM compiler on aarch64 c6gn

```
==============================================================================
PERFORMANCE REPORT
------------------------------------------------------------------------------
ExaML_case2_arm_examl_3_0_22_arm_21_0_0_879_N_1_MPI_1_OMP_1
- aws:c6gn
   - builtin
      * num_tasks: 1
      * Total Time: 19.32975 s
------------------------------------------------------------------------------
ExaML_case2_arm_examl_3_0_22_arm_21_0_0_879_N_1_MPI_2_OMP_1
   - builtin
      * num_tasks: 2
      * Total Time: 11.336217 s
------------------------------------------------------------------------------
ExaML_case2_arm_examl_3_0_22_arm_21_0_0_879_N_1_MPI_4_OMP_1
   - builtin
      * num_tasks: 4
      * Total Time: 8.706697 s
------------------------------------------------------------------------------
ExaML_case2_arm_examl_3_0_22_arm_21_0_0_879_N_1_MPI_8_OMP_1
   - builtin
      * num_tasks: 8
      * Total Time: 8.847904 s
------------------------------------------------------------------------------
ExaML_case2_arm_examl_3_0_22_arm_21_0_0_879_N_1_MPI_16_OMP_1
   - builtin
      * num_tasks: 16
      * Total Time: 10.632513 s
------------------------------------------------------------------------------
ExaML_case2_arm_examl_3_0_22_arm_21_0_0_879_N_1_MPI_32_OMP_1
   - builtin
      * num_tasks: 32
      * Total Time: 11.91183 s
------------------------------------------------------------------------------
ExaML_case2_arm_examl_3_0_22_arm_21_0_0_879_N_1_MPI_64_OMP_1
   - builtin
      * num_tasks: 64
      * Total Time: 16.395895 s
------------------------------------------------------------------------------
ExaML_case2_arm_examl_3_0_22_arm_21_0_0_879_N_2_MPI_128_OMP_1
   - builtin
      * num_tasks: 128
      * Total Time: 50.075047 s
------------------------------------------------------------------------------
ExaML_case2_arm_examl_3_0_22_arm_21_0_0_879_N_4_MPI_256_OMP_1
   - builtin
      * num_tasks: 256
      * Total Time: 71.162784 s
------------------------------------------------------------------------------
```

#### GCC compiler on x86 c5n

```
==============================================================================
PERFORMANCE REPORT
------------------------------------------------------------------------------
ExaML_case2_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_1_OMP_1
- aws:c5n
   - builtin
      * num_tasks: 1
      * Total Time: 20.770661 s
------------------------------------------------------------------------------
ExaML_case2_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_2_OMP_1
   - builtin
      * num_tasks: 2
      * Total Time: 15.57556 s
------------------------------------------------------------------------------
ExaML_case2_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_4_OMP_1
   - builtin
      * num_tasks: 4
      * Total Time: 10.884692 s
------------------------------------------------------------------------------
ExaML_case2_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_8_OMP_1
   - builtin
      * num_tasks: 8
      * Total Time: 10.716423 s
------------------------------------------------------------------------------
ExaML_case2_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_16_OMP_1
   - builtin
      * num_tasks: 16
      * Total Time: 12.784417 s
------------------------------------------------------------------------------
ExaML_case2_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_32_OMP_1
   - builtin
      * num_tasks: 32
      * Total Time: 16.821747 s
------------------------------------------------------------------------------
ExaML_case2_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_64_OMP_1
   - builtin
      * num_tasks: 64
      * Total Time: 22.248651 s
------------------------------------------------------------------------------
ExaML_case2_gcc_examl_3_0_22_gcc_10_3_0_N_2_MPI_128_OMP_1
   - builtin
      * num_tasks: 128
      * Total Time: 51.58473 s
------------------------------------------------------------------------------
ExaML_case2_gcc_examl_3_0_22_gcc_10_3_0_N_4_MPI_256_OMP_1
   - builtin
      * num_tasks: 256
      * Total Time: 81.924382 s
------------------------------------------------------------------------------
```

### Strong Scaling (on&off-node, 1-4 nodes) and Compiler Comparison

This includes results of tasks: P2, P3, P6

| Cores(MPI rank) | GCC | ARM |
|-------|------------|------------|
|  1     |  18.71   | 19.33|
|  2     |  11.11    | 11.34|
|  4     |  8.82    | 8.71|
|  8     |  9.00    | 8.85|
|  16    |  10.47     | 10.63 |
|  32    |  12.44     | 11.91 |
|  64    |  17.29     | 16.40 |
|  128   |  49.66     | 50.08	|
|  256   |  73.43	 | 71.16	|


### Serial Hot-spot Profile

List of top-10 functions / code locations from a serial profile. Use GCC compiler.

Profiling command used:

```
map --profile srun -N 1 -n 1 examl -t /home/peize/examl-test/case1/49.tree -m GAMMA -s /home/peize/examl-test/case1/49.unpartitioned.binary -n T1
```

| Position | Routine                 | Time (%) |
| -------- | ----------------------- | -------- |
| 1        | newviewGTRGAMMA         | 61.2%    |
| 2        | coreGTRGAMMA            | 24.4%    |
| 3        | makenewzIterative       | 4.0%     |
| 4        | MPI_Allreduce           | 3.7%     |
| 5        | __log_finite            | 1.6%     |
| 6        | exp                     | 1.1%     |
| 7        | __exp_finite            | 1.1%     |
| 8        | evaluateIterative       | 0.7%     |
| 9        | log                     | 0.4%     |
| 10       | \_\_GI\_\_IO_file_fopen | 0.3%     |


### Full Node Hot-spot Profile

List of top-10 functions / code locations from a serial profile. Use GCC compiler.

Profiling command used:

```
map --profile srun -N 1 -n 64 examl -t /home/peize/examl-test/case1/49.tree -m GAMMA -s /home/peize/examl-test/case1/49.unpartitioned.binary -n T1
```

| Position | Routine                 | Time (%) | MPI (%) |
| -------- | ----------------------- | -------- | ------- |
| 1        | newviewGTRGAMMA         | 61.2%    |         |
| 2        | coreGTRGAMMA            | 24.4%    |         |
| 3        | makenewzIterative       | 4.0%     |         |
| 4        | MPI_Allreduce           | 3.7%     | 3.7%    |
| 5        | __log_finite            | 1.6%     |         |
| 6        | exp                     | 1.1%     |         |
| 7        | __exp_finite            | 1.1%     |         |
| 8        | evaluateIterative       | 0.7%     |         |
| 9        | log                     | 0.4%     |         |
| 10       | \_\_GI\_\_IO_file_fopen | 0.3%     |         |


### On-Node & Off-Node Architecture Comparison

On-Node & Off-Node scaling study for two architectures.

| Cores | C6gn (Aarch64) | C5n (X86) |
| ----- | -------------- | --------- |
| 1     |       18.71         |    20.77       |
| 2     |       11.11         |    15.58       |
| 4     |       8.82         |    10.88       |
| 8     |       9.00         |    10.72       |
| 16    |       10.47         |    12.78       |
| 32    |       12.44         |    16.82       |
| 64    |       17.29         |    22.25       |
| 128    |      49.66          |   51.58        |
| 256    |      73.43          |   81.92        |

## Test Case 3

> examl -t /home/peize/examl-test/case2/140.tree -m PSR -s /home/peize/examl-test/case2/140.unpartitioned.binary -n T1

[ReFrame Benchmark 1](#)

```
../bin/reframe -c benchmark.py -r --performance-report
```

### Validation

Details of the validation for `Test Case 1`.


### ReFrame Output

#### GCC compiler on aarch64 c6gn

```
==============================================================================
PERFORMANCE REPORT
------------------------------------------------------------------------------
ExaML_case3_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_1_OMP_1
- aws:c6gn
   - builtin
      * num_tasks: 1
      * Total Time: 852.061624 s
------------------------------------------------------------------------------
ExaML_case3_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_2_OMP_1
   - builtin
      * num_tasks: 2
      * Total Time: 460.389792 s
------------------------------------------------------------------------------
ExaML_case3_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_4_OMP_1
   - builtin
      * num_tasks: 4
      * Total Time: 273.466533 s
------------------------------------------------------------------------------
ExaML_case3_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_8_OMP_1
   - builtin
      * num_tasks: 8
      * Total Time: 188.462236 s
------------------------------------------------------------------------------
ExaML_case3_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_16_OMP_1
   - builtin
      * num_tasks: 16
      * Total Time: 153.156592 s
------------------------------------------------------------------------------
ExaML_case3_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_32_OMP_1
   - builtin
      * num_tasks: 32
      * Total Time: 144.639644 s
------------------------------------------------------------------------------
ExaML_case3_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_64_OMP_1
   - builtin
      * num_tasks: 64
      * Total Time: 164.994314 s
------------------------------------------------------------------------------
ExaML_case3_gcc_examl_3_0_22_gcc_10_3_0_N_2_MPI_128_OMP_1
   - builtin
      * num_tasks: 128
      * Total Time: 348.725791 s
------------------------------------------------------------------------------
ExaML_case3_gcc_examl_3_0_22_gcc_10_3_0_N_4_MPI_256_OMP_1
   - builtin
      * num_tasks: 256
      * Total Time: 469.439062 s
------------------------------------------------------------------------------
```

#### ARM compiler on aarch64 c6gn

```
==============================================================================
PERFORMANCE REPORT
------------------------------------------------------------------------------
ExaML_case3_arm_examl_3_0_22_arm_21_0_0_879_N_1_MPI_1_OMP_1
- aws:c6gn
   - builtin
      * num_tasks: 1
      * Total Time: 1031.85876 s
------------------------------------------------------------------------------
ExaML_case3_arm_examl_3_0_22_arm_21_0_0_879_N_1_MPI_2_OMP_1
   - builtin
      * num_tasks: 2
      * Total Time: 538.28273 s
------------------------------------------------------------------------------
ExaML_case3_arm_examl_3_0_22_arm_21_0_0_879_N_1_MPI_4_OMP_1
   - builtin
      * num_tasks: 4
      * Total Time: 301.012165 s
------------------------------------------------------------------------------
ExaML_case3_arm_examl_3_0_22_arm_21_0_0_879_N_1_MPI_8_OMP_1
   - builtin
      * num_tasks: 8
      * Total Time: 189.691921 s
------------------------------------------------------------------------------
ExaML_case3_arm_examl_3_0_22_arm_21_0_0_879_N_1_MPI_16_OMP_1
   - builtin
      * num_tasks: 16
      * Total Time: 141.049704 s
------------------------------------------------------------------------------
ExaML_case3_arm_examl_3_0_22_arm_21_0_0_879_N_1_MPI_32_OMP_1
   - builtin
      * num_tasks: 32
      * Total Time: 122.590224 s
------------------------------------------------------------------------------
ExaML_case3_arm_examl_3_0_22_arm_21_0_0_879_N_1_MPI_64_OMP_1
   - builtin
      * num_tasks: 64
      * Total Time: 140.632196 s
------------------------------------------------------------------------------
ExaML_case3_arm_examl_3_0_22_arm_21_0_0_879_N_2_MPI_128_OMP_1
   - builtin
      * num_tasks: 128
      * Total Time: 329.231369 s
------------------------------------------------------------------------------
ExaML_case3_arm_examl_3_0_22_arm_21_0_0_879_N_4_MPI_256_OMP_1
   - builtin
      * num_tasks: 256
      * Total Time: 453.203107 s
------------------------------------------------------------------------------
```

#### GCC compiler on x86 c5n

```
==============================================================================
PERFORMANCE REPORT
------------------------------------------------------------------------------
ExaML_case3_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_1_OMP_1
- aws:c5n
   - builtin
      * num_tasks: 1
      * Total Time: 1108.00019 s
------------------------------------------------------------------------------
ExaML_case3_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_2_OMP_1
   - builtin
      * num_tasks: 2
      * Total Time: 580.099378 s
------------------------------------------------------------------------------
ExaML_case3_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_4_OMP_1
   - builtin
      * num_tasks: 4
      * Total Time: 348.781388 s
------------------------------------------------------------------------------
ExaML_case3_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_8_OMP_1
   - builtin
      * num_tasks: 8
      * Total Time: 240.919849 s
------------------------------------------------------------------------------
ExaML_case3_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_16_OMP_1
   - builtin
      * num_tasks: 16
      * Total Time: 195.841886 s
------------------------------------------------------------------------------
ExaML_case3_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_32_OMP_1
   - builtin
      * num_tasks: 32
      * Total Time: 188.016304 s
------------------------------------------------------------------------------
ExaML_case3_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_64_OMP_1
   - builtin
      * num_tasks: 64
      * Total Time: 204.525357 s
------------------------------------------------------------------------------
ExaML_case3_gcc_examl_3_0_22_gcc_10_3_0_N_2_MPI_128_OMP_1
   - builtin
      * num_tasks: 128
      * Total Time: 380.165379 s
------------------------------------------------------------------------------
ExaML_case3_gcc_examl_3_0_22_gcc_10_3_0_N_4_MPI_256_OMP_1
   - builtin
      * num_tasks: 256
      * Total Time: 383.982744 s
------------------------------------------------------------------------------
```

### Strong Scaling (on&off-node, 1-4 nodes) and Compiler Comparison

This includes results of tasks: P2, P3, P6

| Cores(MPI rank) | GCC | ARM |
|-------|------------|------------|
|  1     |  852.06   | 1031.86|
|  2     |  460.39    | 538.28|
|  4     |  273.47    | 301.01|
|  8     |  188.46    | 189.69|
|  16    |  153.16     | 141.05 |
|  32    |  144.64     | 122.59 |
|  64    |  164.99     | 140.63 |
|  128   |  348.73     | 329.23	|
|  256   |  469.44	 | 453.20	|


### Serial Hot-spot Profile

List of top-10 functions / code locations from a serial profile. Use GCC compiler.

Profiling command used:

```
map --profile srun -N 1 -n 1 examl -t /home/peize/examl-test/case2/140.tree -m PSR -s /home/peize/examl-test/case2/140.unpartitioned.binary -n T1
```

| Position | Routine                   | Time (%) |
| -------- | ------------------------- | -------- |
| 1        | newviewIterative          | 85.0%    |
| 2        | coreGTRCATPROT            | 7.3%     |
| 3        | exp                       | 3.1%     |
| 4        | makenewzIterative         | 1.7%     |
| 5        | __exp_finite              | 0.9%     |
| 6        | __log_finite              | 0.7%     |
| 7        | evaluatePartialGTRCATPROT | 0.5%     |
| 8        | free                      | 0.2%     |
| 9        | getxnode                  | 0.2%     |
| 10       | exp@plt                   | 0.1%     |


### Full Node Hot-spot Profile

List of top-10 functions / code locations from a serial profile. Use GCC compiler.

Profiling command used:

```
map --profile srun -N 1 -n 64 examl -t /home/peize/examl-test/case2/140.tree -m PSR -s /home/peize/examl-test/case2/140.unpartitioned.binary -n T1
```

| Position | Routine           | Time (%) | MPI (%) |
| -------- | ----------------- | -------- | ------- |
| 1        | MPI_Allreduce     | 70.2%    | 70.2%   |
| 2        | newviewIterative  | 12.0%    |         |
| 3        | exp               | 8.9%     |         |
| 4        | __exp_finite      | 6.5%     |         |
| 5        | coreGTRCATPROT    | 0.7%     |         |
| 6        | MPI_Barrier       | 0.3%     | 0.3%    |
| 7        | exp@plt           | 0.2%     |         |
| 8        | makenewzIterative | 0.2%     |         |
| 9        | __log_finite      | 0.2%     |         |
| 10       | malloc            | <0.1%    |         |


### On-Node Architecture Comparison

On-node scaling study for two architectures.

| Cores | C6gn (Aarch64) | C5n (X86) |
| ----- | -------------- | --------- |
| 1     |        852.06        |    1108.00       |
| 2     |        460.39        |    580.10       |
| 4     |        273.47        |    348.78       |
| 8     |        188.46        |    240.92       |
| 16    |        153.16        |    195.84       |
| 32    |        144.64        |    188.02       |
| 64    |        164.99        |    204.53       |
| 128    |       348.73         |   380.17        |
| 256    |       469.44         |   383.98        |

## Test Case 4

> examl -t /home/peize/examl-test/case2/140.tree -m GAMMA -s /home/peize/examl-test/case2/140.unpartitioned.binary -n T1

[ReFrame Benchmark 1](#)

```
../bin/reframe -c benchmark.py -r --performance-report
```

### Validation

Details of the validation for `Test Case 1`.


### ReFrame Output

#### GCC compiler on aarch64 c6gn

```
==============================================================================
PERFORMANCE REPORT
------------------------------------------------------------------------------
ExaML_case4_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_1_OMP_1
- aws:c6gn
   - builtin
      * num_tasks: 1
      * Total Time: 1675.11952 s
------------------------------------------------------------------------------
ExaML_case4_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_2_OMP_1
   - builtin
      * num_tasks: 2
      * Total Time: 856.515937 s
------------------------------------------------------------------------------
ExaML_case4_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_4_OMP_1
   - builtin
      * num_tasks: 4
      * Total Time: 444.694121 s
------------------------------------------------------------------------------
ExaML_case4_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_8_OMP_1
   - builtin
      * num_tasks: 8
      * Total Time: 248.167222 s
------------------------------------------------------------------------------
ExaML_case4_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_16_OMP_1
   - builtin
      * num_tasks: 16
      * Total Time: 156.176348 s
------------------------------------------------------------------------------
ExaML_case4_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_32_OMP_1
   - builtin
      * num_tasks: 32
      * Total Time: 116.126191 s
------------------------------------------------------------------------------
ExaML_case4_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_64_OMP_1
   - builtin
      * num_tasks: 64
      * Total Time: 117.506095 s
------------------------------------------------------------------------------
ExaML_case4_gcc_examl_3_0_22_gcc_10_3_0_N_2_MPI_128_OMP_1
   - builtin
      * num_tasks: 128
      * Total Time: 255.33368 s
------------------------------------------------------------------------------
ExaML_case4_gcc_examl_3_0_22_gcc_10_3_0_N_4_MPI_256_OMP_1
   - builtin
      * num_tasks: 256
      * Total Time: 337.595941 s
------------------------------------------------------------------------------
```

#### ARM compiler on aarch64 c6gn

```
==============================================================================
PERFORMANCE REPORT
------------------------------------------------------------------------------
ExaML_case4_arm_examl_3_0_22_arm_21_0_0_879_N_1_MPI_1_OMP_1
- aws:c6gn
   - builtin
      * num_tasks: 1
      * Total Time: 2047.356005 s
------------------------------------------------------------------------------
ExaML_case4_arm_examl_3_0_22_arm_21_0_0_879_N_1_MPI_2_OMP_1
   - builtin
      * num_tasks: 2
      * Total Time: 1039.04339 s
------------------------------------------------------------------------------
ExaML_case4_arm_examl_3_0_22_arm_21_0_0_879_N_1_MPI_4_OMP_1
   - builtin
      * num_tasks: 4
      * Total Time: 538.27324 s
------------------------------------------------------------------------------
ExaML_case4_arm_examl_3_0_22_arm_21_0_0_879_N_1_MPI_8_OMP_1
   - builtin
      * num_tasks: 8
      * Total Time: 293.502664 s
------------------------------------------------------------------------------
ExaML_case4_arm_examl_3_0_22_arm_21_0_0_879_N_1_MPI_16_OMP_1
   - builtin
      * num_tasks: 16
      * Total Time: 177.613992 s
------------------------------------------------------------------------------
ExaML_case4_arm_examl_3_0_22_arm_21_0_0_879_N_1_MPI_32_OMP_1
   - builtin
      * num_tasks: 32
      * Total Time: 124.450696 s
------------------------------------------------------------------------------
ExaML_case4_arm_examl_3_0_22_arm_21_0_0_879_N_1_MPI_64_OMP_1
   - builtin
      * num_tasks: 64
      * Total Time: 121.939978 s
------------------------------------------------------------------------------
ExaML_case4_arm_examl_3_0_22_arm_21_0_0_879_N_2_MPI_128_OMP_1
   - builtin
      * num_tasks: 128
      * Total Time: 235.258422 s
------------------------------------------------------------------------------
ExaML_case4_arm_examl_3_0_22_arm_21_0_0_879_N_4_MPI_256_OMP_1
   - builtin
      * num_tasks: 256
      * Total Time: 307.640001 s
------------------------------------------------------------------------------
```

#### GCC compiler on x86 c5n

```
==============================================================================
PERFORMANCE REPORT
------------------------------------------------------------------------------
ExaML_case4_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_1_OMP_1
- aws:c5n
   - builtin
      * num_tasks: 1
      * Total Time: 1679.379162 s
------------------------------------------------------------------------------
ExaML_case4_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_2_OMP_1
   - builtin
      * num_tasks: 2
      * Total Time: 1077.734474 s
------------------------------------------------------------------------------
ExaML_case4_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_4_OMP_1
   - builtin
      * num_tasks: 4
      * Total Time: 565.515572 s
------------------------------------------------------------------------------
ExaML_case4_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_8_OMP_1
   - builtin
      * num_tasks: 8
      * Total Time: 307.250027 s
------------------------------------------------------------------------------
ExaML_case4_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_16_OMP_1
   - builtin
      * num_tasks: 16
      * Total Time: 194.581353 s
------------------------------------------------------------------------------
ExaML_case4_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_32_OMP_1
   - builtin
      * num_tasks: 32
      * Total Time: 143.07804 s
------------------------------------------------------------------------------
ExaML_case4_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_64_OMP_1
   - builtin
      * num_tasks: 64
      * Total Time: 143.571914 s
------------------------------------------------------------------------------
ExaML_case4_gcc_examl_3_0_22_gcc_10_3_0_N_2_MPI_128_OMP_1
   - builtin
      * num_tasks: 128
      * Total Time: 291.438198 s
------------------------------------------------------------------------------
ExaML_case4_gcc_examl_3_0_22_gcc_10_3_0_N_4_MPI_256_OMP_1
   - builtin
      * num_tasks: 256
      * Total Time: 354.191831 s
------------------------------------------------------------------------------
```

### Strong Scaling (on&off-node, 1-4 nodes) and Compiler Comparison

This includes results of tasks: P2, P3, P6

| Cores(MPI rank) | GCC | ARM |
|-------|------------|------------|
|  1     |  1675.12   | 2047.36|
|  2     |  856.52    | 1039.04|
|  4     |  444.69    | 538.27|
|  8     |  248.17    | 293.50|
|  16    |  156.18     | 177.61 |
|  32    |  116.13     | 124.45 |
|  64    |  117.51     | 121.94 |
|  128   |  255.33     | 235.26	|
|  256   |  337.60	 | 307.64	|


### Serial Hot-spot Profile

List of top-10 functions / code locations from a serial profile. Use GCC compiler.

Profiling command used:

```
map --profile srun -N 1 -n 1 examl -t /home/peize/examl-test/case2/140.tree -m GAMMA -s /home/peize/examl-test/case2/140.unpartitioned.binary -n T1
```

| Position | Routine              | Time (%) |
| -------- | -------------------- | -------- |
| 1        | newviewGTRGAMMAPROT  | 89.5%    |
| 2        | coreGTRGAMMAPROT     | 7.7%     |
| 3        | makenewzIterative    | 1.3%     |
| 4        | __log_finite         | 0.5%     |
| 5        | __exp_finite         | 0.4%     |
| 6        | exp                  | 0.2%     |
| 7        | MPI_Allreduce        | 0.2%     |
| 8        | MPI_Finalize         | 0.1%     |
| 9        | computeTraversalInfo | 0.1%     |
| 10       | main                 | <0.1%    |


### Full Node Hot-spot Profile

List of top-10 functions / code locations from a serial profile. Use GCC compiler.

Profiling command used:

```
map --profile srun -N 1 -n 64 examl -t /home/peize/examl-test/case2/140.tree -m GAMMA -s /home/peize/examl-test/case2/140.unpartitioned.binary -n T1
```

| Position | Routine             | Time (%) | MPI (%) |
| -------- | ------------------- | -------- | ------- |
| 1        | MPI_Allreduce       | 72.8%    | 72.8%   |
| 2        | newviewGTRGAMMAPROT | 18.3%    |         |
| 3        | exp                 | 2.2%     |         |
| 4        | newviewIterative    | 1.8%     |         |
| 5        | __exp_finite        | 1.7%     |         |
| 6        | coreGTRGAMMAPROT    | 1.5%     |         |
| 7        | makenewzIterative   | 0.4%     |         |
| 8        | MPI_Barrier         | 0.3%     | 0.3%    |
| 9        | __log_finite        | 0.2%     |         |
| 10       | malloc              | <0.1%    |         |



### On-Node Architecture Comparison

On-node scaling study for two architectures.

| Cores | C6gn (Aarch64) | C5n (X86) |
| ----- | -------------- | --------- |
|  1     |  1675.12   | 1679.38  |
|  2     |  856.52    | 1077.73  |
|  4     |  444.69    | 565.52   |
|  8     |  248.17    | 307.25 |
|  16    |  156.18     | 194.58        |
|  32    |  116.13     |  143.08 |
|  64    |  117.51     | 143.57  |
|  128   |  255.33     | 291.44	|
|  256   |  337.60	 | 354.19 	|


## 

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
