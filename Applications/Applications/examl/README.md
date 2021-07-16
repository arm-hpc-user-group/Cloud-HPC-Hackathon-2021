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
      * Total Time: 8.0 s
------------------------------------------------------------------------------
ExaML_case1_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_2_OMP_1
   - builtin
      * num_tasks: 2
      * Total Time: 6.0 s
------------------------------------------------------------------------------
ExaML_case1_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_4_OMP_1
   - builtin
      * num_tasks: 4
      * Total Time: 5.0 s
------------------------------------------------------------------------------
ExaML_case1_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_8_OMP_1
   - builtin
      * num_tasks: 8
      * Total Time: 7.0 s
------------------------------------------------------------------------------
ExaML_case1_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_16_OMP_1
   - builtin
      * num_tasks: 16
      * Total Time: 8.0 s
------------------------------------------------------------------------------
ExaML_case1_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_32_OMP_1
   - builtin
      * num_tasks: 32
      * Total Time: 10.0 s
------------------------------------------------------------------------------
ExaML_case1_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_64_OMP_1
   - builtin
      * num_tasks: 64
      * Total Time: 15.0 s
------------------------------------------------------------------------------
ExaML_case1_gcc_examl_3_0_22_gcc_10_3_0_N_2_MPI_128_OMP_1
   - builtin
      * num_tasks: 128
      * Total Time: 33.0 s
------------------------------------------------------------------------------
ExaML_case1_gcc_examl_3_0_22_gcc_10_3_0_N_4_MPI_256_OMP_1
   - builtin
      * num_tasks: 256
      * Total Time: 54.0 s
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
      * Total Time: 8.0 s
------------------------------------------------------------------------------
ExaML_case1_arm_examl_3_0_22_arm_21_0_0_879_N_1_MPI_2_OMP_1
   - builtin
      * num_tasks: 2
      * Total Time: 6.0 s
------------------------------------------------------------------------------
ExaML_case1_arm_examl_3_0_22_arm_21_0_0_879_N_1_MPI_4_OMP_1
   - builtin
      * num_tasks: 4
      * Total Time: 6.0 s
------------------------------------------------------------------------------
ExaML_case1_arm_examl_3_0_22_arm_21_0_0_879_N_1_MPI_8_OMP_1
   - builtin
      * num_tasks: 8
      * Total Time: 8.0 s
------------------------------------------------------------------------------
ExaML_case1_arm_examl_3_0_22_arm_21_0_0_879_N_1_MPI_16_OMP_1
   - builtin
      * num_tasks: 16
      * Total Time: 10.0 s
------------------------------------------------------------------------------
ExaML_case1_arm_examl_3_0_22_arm_21_0_0_879_N_1_MPI_32_OMP_1
   - builtin
      * num_tasks: 32
      * Total Time: 12.0 s
------------------------------------------------------------------------------
ExaML_case1_arm_examl_3_0_22_arm_21_0_0_879_N_1_MPI_64_OMP_1
   - builtin
      * num_tasks: 64
      * Total Time: 16.0 s
------------------------------------------------------------------------------
ExaML_case1_arm_examl_3_0_22_arm_21_0_0_879_N_2_MPI_128_OMP_1
   - builtin
      * num_tasks: 128
      * Total Time: 44.0 s
------------------------------------------------------------------------------
ExaML_case1_arm_examl_3_0_22_arm_21_0_0_879_N_4_MPI_256_OMP_1
   - builtin
      * num_tasks: 256
      * Total Time: 57.0 s
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
      * Total Time: 10.0 s
------------------------------------------------------------------------------
ExaML_case1_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_2_OMP_1
   - builtin
      * num_tasks: 2
      * Total Time: 8.0 s
------------------------------------------------------------------------------
ExaML_case1_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_4_OMP_1
   - builtin
      * num_tasks: 4
      * Total Time: 8.0 s
------------------------------------------------------------------------------
ExaML_case1_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_8_OMP_1
   - builtin
      * num_tasks: 8
      * Total Time: 9.0 s
------------------------------------------------------------------------------
ExaML_case1_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_16_OMP_1
   - builtin
      * num_tasks: 16
      * Total Time: 11.0 s
------------------------------------------------------------------------------
ExaML_case1_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_32_OMP_1
   - builtin
      * num_tasks: 32
      * Total Time: 15.0 s
------------------------------------------------------------------------------
ExaML_case1_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_64_OMP_1
   - builtin
      * num_tasks: 64
      * Total Time: 19.0 s
------------------------------------------------------------------------------
ExaML_case1_gcc_examl_3_0_22_gcc_10_3_0_N_2_MPI_128_OMP_1
   - builtin
      * num_tasks: 128
      * Total Time: 51.0 s
------------------------------------------------------------------------------
ExaML_case1_gcc_examl_3_0_22_gcc_10_3_0_N_4_MPI_256_OMP_1
   - builtin
      * num_tasks: 256
      * Total Time: 54.0 s
------------------------------------------------------------------------------
```

### On-node Compiler Comparison

Performance comparison of two compilers.

| Cores | Compiler 1 | Compiler 2 |
|-------|------------|------------|
|       |            |            |


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
It says case1 below, actually it's case2. I forgot to change the name.
==============================================================================
PERFORMANCE REPORT
------------------------------------------------------------------------------
ExaML_case1_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_1_OMP_1
- aws:c6gn
   - builtin
      * num_tasks: 1
      * Total Time: 18.0 s
------------------------------------------------------------------------------
ExaML_case1_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_2_OMP_1
   - builtin
      * num_tasks: 2
      * Total Time: 10.0 s
------------------------------------------------------------------------------
ExaML_case1_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_4_OMP_1
   - builtin
      * num_tasks: 4
      * Total Time: 8.0 s
------------------------------------------------------------------------------
ExaML_case1_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_8_OMP_1
   - builtin
      * num_tasks: 8
      * Total Time: 8.0 s
------------------------------------------------------------------------------
ExaML_case1_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_16_OMP_1
   - builtin
      * num_tasks: 16
      * Total Time: 10.0 s
------------------------------------------------------------------------------
ExaML_case1_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_32_OMP_1
   - builtin
      * num_tasks: 32
      * Total Time: 12.0 s
------------------------------------------------------------------------------
ExaML_case1_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_64_OMP_1
   - builtin
      * num_tasks: 64
      * Total Time: 17.0 s
------------------------------------------------------------------------------
ExaML_case1_gcc_examl_3_0_22_gcc_10_3_0_N_2_MPI_128_OMP_1
   - builtin
      * num_tasks: 128
      * Total Time: 50.0 s
------------------------------------------------------------------------------
ExaML_case1_gcc_examl_3_0_22_gcc_10_3_0_N_4_MPI_256_OMP_1
   - builtin
      * num_tasks: 256
      * Total Time: 64.0 s
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
      * Total Time: 19.0 s
------------------------------------------------------------------------------
ExaML_case2_arm_examl_3_0_22_arm_21_0_0_879_N_1_MPI_2_OMP_1
   - builtin
      * num_tasks: 2
      * Total Time: 11.0 s
------------------------------------------------------------------------------
ExaML_case2_arm_examl_3_0_22_arm_21_0_0_879_N_1_MPI_4_OMP_1
   - builtin
      * num_tasks: 4
      * Total Time: 9.0 s
------------------------------------------------------------------------------
ExaML_case2_arm_examl_3_0_22_arm_21_0_0_879_N_1_MPI_8_OMP_1
   - builtin
      * num_tasks: 8
      * Total Time: 9.0 s
------------------------------------------------------------------------------
ExaML_case2_arm_examl_3_0_22_arm_21_0_0_879_N_1_MPI_16_OMP_1
   - builtin
      * num_tasks: 16
      * Total Time: 10.0 s
------------------------------------------------------------------------------
ExaML_case2_arm_examl_3_0_22_arm_21_0_0_879_N_1_MPI_32_OMP_1
   - builtin
      * num_tasks: 32
      * Total Time: 12.0 s
------------------------------------------------------------------------------
ExaML_case2_arm_examl_3_0_22_arm_21_0_0_879_N_1_MPI_64_OMP_1
   - builtin
      * num_tasks: 64
      * Total Time: 16.0 s
------------------------------------------------------------------------------
ExaML_case2_arm_examl_3_0_22_arm_21_0_0_879_N_2_MPI_128_OMP_1
   - builtin
      * num_tasks: 128
      * Total Time: 45.0 s
------------------------------------------------------------------------------
ExaML_case2_arm_examl_3_0_22_arm_21_0_0_879_N_4_MPI_256_OMP_1
   - builtin
      * num_tasks: 256
      * Total Time: 69.0 s
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
      * Total Time: 21.0 s
------------------------------------------------------------------------------
ExaML_case2_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_2_OMP_1
   - builtin
      * num_tasks: 2
      * Total Time: 15.0 s
------------------------------------------------------------------------------
ExaML_case2_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_4_OMP_1
   - builtin
      * num_tasks: 4
      * Total Time: 10.0 s
------------------------------------------------------------------------------
ExaML_case2_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_8_OMP_1
   - builtin
      * num_tasks: 8
      * Total Time: 10.0 s
------------------------------------------------------------------------------
ExaML_case2_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_16_OMP_1
   - builtin
      * num_tasks: 16
      * Total Time: 12.0 s
------------------------------------------------------------------------------
ExaML_case2_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_32_OMP_1
   - builtin
      * num_tasks: 32
      * Total Time: 16.0 s
------------------------------------------------------------------------------
ExaML_case2_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_64_OMP_1
   - builtin
      * num_tasks: 64
      * Total Time: 22.0 s
------------------------------------------------------------------------------
ExaML_case2_gcc_examl_3_0_22_gcc_10_3_0_N_2_MPI_128_OMP_1
   - builtin
      * num_tasks: 128
      * Total Time: 92.0 s
------------------------------------------------------------------------------
ExaML_case2_gcc_examl_3_0_22_gcc_10_3_0_N_4_MPI_256_OMP_1
   - builtin
      * num_tasks: 256
      * Total Time: 63.0 s
------------------------------------------------------------------------------
```

### On-node Compiler Comparison

Performance comparison of two compilers.

| Cores | Compiler 1 | Compiler 2 |
| ----- | ---------- | ---------- |
|       |            |            |


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

### Strong Scaling Study

On-node scaling study for two compilers.

| Cores | Compiler 1 | Compiler 2 |
| ----- | ---------- | ---------- |
| 1     |            |            |
| 2     |            |            |
| 4     |            |            |
| 8     |            |            |
| 16    |            |            |
| 32    |            |            |
| 64    |            |            |


### Off-Node Scaling Study

Off-node scaling study comparing C6g and C6gn instances.

| Nodes | Cores | C6g  | C6gn |
| ----- | ----- | ---- | ---- |
| 1     | 8     |      |      |
| 1     | 16    |      |      |
| 1     | 32    |      |      |
| 1     | 64    |      |      |
| 2     | 128   |      |      |
| 4     | 256   |      |      |
| 8     | 512   |      |      |


### On-Node Architecture Comparison

On-node scaling study for two architectures.

| Cores | C6gn (Aarch64) | C5n (X86) |
| ----- | -------------- | --------- |
| 1     |                |           |
| 2     |                |           |
| 4     |                |           |
| 8     |                |           |
| 16    |                |           |
| 32    |                |           |
| 64    |                |           |

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
It says case1 below, actually it's case2. I forgot to change the name.
==============================================================================
PERFORMANCE REPORT
------------------------------------------------------------------------------
ExaML_case1_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_1_OMP_1
- aws:c6gn
   - builtin
      * num_tasks: 1
      * Total Time: 845.0 s
------------------------------------------------------------------------------
ExaML_case1_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_2_OMP_1
   - builtin
      * num_tasks: 2
      * Total Time: 455.0 s
------------------------------------------------------------------------------
ExaML_case1_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_4_OMP_1
   - builtin
      * num_tasks: 4
      * Total Time: 270.0 s
------------------------------------------------------------------------------
ExaML_case1_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_8_OMP_1
   - builtin
      * num_tasks: 8
      * Total Time: 184.0 s
------------------------------------------------------------------------------
ExaML_case1_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_16_OMP_1
   - builtin
      * num_tasks: 16
      * Total Time: 151.0 s
------------------------------------------------------------------------------
ExaML_case1_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_32_OMP_1
   - builtin
      * num_tasks: 32
      * Total Time: 141.0 s
------------------------------------------------------------------------------
ExaML_case1_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_64_OMP_1
   - builtin
      * num_tasks: 64
      * Total Time: 160.0 s
------------------------------------------------------------------------------
ExaML_case1_gcc_examl_3_0_22_gcc_10_3_0_N_2_MPI_128_OMP_1
   - builtin
      * num_tasks: 128
      * Total Time: 361.0 s
------------------------------------------------------------------------------
ExaML_case1_gcc_examl_3_0_22_gcc_10_3_0_N_4_MPI_256_OMP_1
   - builtin
      * num_tasks: 256
      * Total Time: 458.0 s
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
      * Total Time: 1032.0 s
------------------------------------------------------------------------------
ExaML_case3_arm_examl_3_0_22_arm_21_0_0_879_N_1_MPI_2_OMP_1
   - builtin
      * num_tasks: 2
      * Total Time: 538.0 s
------------------------------------------------------------------------------
ExaML_case3_arm_examl_3_0_22_arm_21_0_0_879_N_1_MPI_4_OMP_1
   - builtin
      * num_tasks: 4
      * Total Time: 299.0 s
------------------------------------------------------------------------------
ExaML_case3_arm_examl_3_0_22_arm_21_0_0_879_N_1_MPI_8_OMP_1
   - builtin
      * num_tasks: 8
      * Total Time: 190.0 s
------------------------------------------------------------------------------
ExaML_case3_arm_examl_3_0_22_arm_21_0_0_879_N_1_MPI_16_OMP_1
   - builtin
      * num_tasks: 16
      * Total Time: 141.0 s
------------------------------------------------------------------------------
ExaML_case3_arm_examl_3_0_22_arm_21_0_0_879_N_1_MPI_32_OMP_1
   - builtin
      * num_tasks: 32
      * Total Time: 125.0 s
------------------------------------------------------------------------------
ExaML_case3_arm_examl_3_0_22_arm_21_0_0_879_N_1_MPI_64_OMP_1
   - builtin
      * num_tasks: 64
      * Total Time: 141.0 s
------------------------------------------------------------------------------
ExaML_case3_arm_examl_3_0_22_arm_21_0_0_879_N_2_MPI_128_OMP_1
   - builtin
      * num_tasks: 128
      * Total Time: 304.0 s
------------------------------------------------------------------------------
ExaML_case3_arm_examl_3_0_22_arm_21_0_0_879_N_4_MPI_256_OMP_1
   - builtin
      * num_tasks: 256
      * Total Time: 393.0 s
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
      * Total Time: 1110.0 s
------------------------------------------------------------------------------
ExaML_case3_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_2_OMP_1
   - builtin
      * num_tasks: 2
      * Total Time: 579.0 s
------------------------------------------------------------------------------
ExaML_case3_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_4_OMP_1
   - builtin
      * num_tasks: 4
      * Total Time: 367.0 s
------------------------------------------------------------------------------
ExaML_case3_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_8_OMP_1
   - builtin
      * num_tasks: 8
      * Total Time: 240.0 s
------------------------------------------------------------------------------
ExaML_case3_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_16_OMP_1
   - builtin
      * num_tasks: 16
      * Total Time: 197.0 s
------------------------------------------------------------------------------
ExaML_case3_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_32_OMP_1
   - builtin
      * num_tasks: 32
      * Total Time: 186.0 s
------------------------------------------------------------------------------
ExaML_case3_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_64_OMP_1
   - builtin
      * num_tasks: 64
      * Total Time: 201.0 s
------------------------------------------------------------------------------
ExaML_case3_gcc_examl_3_0_22_gcc_10_3_0_N_2_MPI_128_OMP_1
   - builtin
      * num_tasks: 128
      * Total Time: 420.0 s
------------------------------------------------------------------------------
ExaML_case3_gcc_examl_3_0_22_gcc_10_3_0_N_4_MPI_256_OMP_1
   - builtin
      * num_tasks: 256
      * Total Time: 592.0 s
------------------------------------------------------------------------------
```

### On-node Compiler Comparison

Performance comparison of two compilers.

| Cores | Compiler 1 | Compiler 2 |
| ----- | ---------- | ---------- |
|       |            |            |


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

### Strong Scaling Study

On-node scaling study for two compilers.

| Cores | Compiler 1 | Compiler 2 |
| ----- | ---------- | ---------- |
| 1     |            |            |
| 2     |            |            |
| 4     |            |            |
| 8     |            |            |
| 16    |            |            |
| 32    |            |            |
| 64    |            |            |


### Off-Node Scaling Study

Off-node scaling study comparing C6g and C6gn instances.

| Nodes | Cores | C6g  | C6gn |
| ----- | ----- | ---- | ---- |
| 1     | 8     |      |      |
| 1     | 16    |      |      |
| 1     | 32    |      |      |
| 1     | 64    |      |      |
| 2     | 128   |      |      |
| 4     | 256   |      |      |
| 8     | 512   |      |      |


### On-Node Architecture Comparison

On-node scaling study for two architectures.

| Cores | C6gn (Aarch64) | C5n (X86) |
| ----- | -------------- | --------- |
| 1     |                |           |
| 2     |                |           |
| 4     |                |           |
| 8     |                |           |
| 16    |                |           |
| 32    |                |           |
| 64    |                |           |

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
It says case1 below, actually it's case2. I forgot to change the name.
==============================================================================
PERFORMANCE REPORT
------------------------------------------------------------------------------
ExaML_case1_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_1_OMP_1
- aws:c6gn
   - builtin
      * num_tasks: 1
      * Total Time: 1673.0 s
------------------------------------------------------------------------------
ExaML_case1_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_2_OMP_1
   - builtin
      * num_tasks: 2
      * Total Time: 856.0 s
------------------------------------------------------------------------------
ExaML_case1_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_4_OMP_1
   - builtin
      * num_tasks: 4
      * Total Time: 444.0 s
------------------------------------------------------------------------------
ExaML_case1_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_8_OMP_1
   - builtin
      * num_tasks: 8
      * Total Time: 248.0 s
------------------------------------------------------------------------------
ExaML_case1_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_16_OMP_1
   - builtin
      * num_tasks: 16
      * Total Time: 158.0 s
------------------------------------------------------------------------------
ExaML_case1_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_32_OMP_1
   - builtin
      * num_tasks: 32
      * Total Time: 118.0 s
------------------------------------------------------------------------------
ExaML_case1_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_64_OMP_1
   - builtin
      * num_tasks: 64
      * Total Time: 115.0 s
------------------------------------------------------------------------------
ExaML_case1_gcc_examl_3_0_22_gcc_10_3_0_N_2_MPI_128_OMP_1
   - builtin
      * num_tasks: 128
      * Total Time: 222.0 s
------------------------------------------------------------------------------
ExaML_case1_gcc_examl_3_0_22_gcc_10_3_0_N_4_MPI_256_OMP_1
   - builtin
      * num_tasks: 256
      * Total Time: 296.0 s
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
      * Total Time: 2044.0 s
------------------------------------------------------------------------------
ExaML_case4_arm_examl_3_0_22_arm_21_0_0_879_N_1_MPI_2_OMP_1
   - builtin
      * num_tasks: 2
      * Total Time: 1039.0 s
------------------------------------------------------------------------------
ExaML_case4_arm_examl_3_0_22_arm_21_0_0_879_N_1_MPI_4_OMP_1
   - builtin
      * num_tasks: 4
      * Total Time: 537.0 s
------------------------------------------------------------------------------
ExaML_case4_arm_examl_3_0_22_arm_21_0_0_879_N_1_MPI_8_OMP_1
   - builtin
      * num_tasks: 8
      * Total Time: 293.0 s
------------------------------------------------------------------------------
ExaML_case4_arm_examl_3_0_22_arm_21_0_0_879_N_1_MPI_16_OMP_1
   - builtin
      * num_tasks: 16
      * Total Time: 177.0 s
------------------------------------------------------------------------------
ExaML_case4_arm_examl_3_0_22_arm_21_0_0_879_N_1_MPI_32_OMP_1
   - builtin
      * num_tasks: 32
      * Total Time: 126.0 s
------------------------------------------------------------------------------
ExaML_case4_arm_examl_3_0_22_arm_21_0_0_879_N_1_MPI_64_OMP_1
   - builtin
      * num_tasks: 64
      * Total Time: 122.0 s
------------------------------------------------------------------------------
ExaML_case4_arm_examl_3_0_22_arm_21_0_0_879_N_2_MPI_128_OMP_1
   - builtin
      * num_tasks: 128
      * Total Time: 235.0 s
------------------------------------------------------------------------------
ExaML_case4_arm_examl_3_0_22_arm_21_0_0_879_N_4_MPI_256_OMP_1
   - builtin
      * num_tasks: 256
      * Total Time: 291.0 s
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
      * Total Time: 1685.0 s
------------------------------------------------------------------------------
ExaML_case4_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_2_OMP_1
   - builtin
      * num_tasks: 2
      * Total Time: 1088.0 s
------------------------------------------------------------------------------
ExaML_case4_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_4_OMP_1
   - builtin
      * num_tasks: 4
      * Total Time: 569.0 s
------------------------------------------------------------------------------
ExaML_case4_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_8_OMP_1
   - builtin
      * num_tasks: 8
      * Total Time: 300.0 s
------------------------------------------------------------------------------
ExaML_case4_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_16_OMP_1
   - builtin
      * num_tasks: 16
      * Total Time: 195.0 s
------------------------------------------------------------------------------
ExaML_case4_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_32_OMP_1
   - builtin
      * num_tasks: 32
      * Total Time: 143.0 s
------------------------------------------------------------------------------
ExaML_case4_gcc_examl_3_0_22_gcc_10_3_0_N_1_MPI_64_OMP_1
   - builtin
      * num_tasks: 64
      * Total Time: 135.0 s
------------------------------------------------------------------------------
ExaML_case4_gcc_examl_3_0_22_gcc_10_3_0_N_2_MPI_128_OMP_1
   - builtin
      * num_tasks: 128
      * Total Time: 441.0 s
------------------------------------------------------------------------------
ExaML_case4_gcc_examl_3_0_22_gcc_10_3_0_N_4_MPI_256_OMP_1
   - builtin
      * num_tasks: 256
      * Total Time: 301.0 s
------------------------------------------------------------------------------
```

### On-node Compiler Comparison

Performance comparison of two compilers.

| Cores | Compiler 1 | Compiler 2 |
| ----- | ---------- | ---------- |
|       |            |            |


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

### Strong Scaling Study

On-node scaling study for two compilers.

| Cores | Compiler 1 | Compiler 2 |
| ----- | ---------- | ---------- |
| 1     |            |            |
| 2     |            |            |
| 4     |            |            |
| 8     |            |            |
| 16    |            |            |
| 32    |            |            |
| 64    |            |            |


### Off-Node Scaling Study

Off-node scaling study comparing C6g and C6gn instances.

| Nodes | Cores | C6g  | C6gn |
| ----- | ----- | ---- | ---- |
| 1     | 8     |      |      |
| 1     | 16    |      |      |
| 1     | 32    |      |      |
| 1     | 64    |      |      |
| 2     | 128   |      |      |
| 4     | 256   |      |      |
| 8     | 512   |      |      |


### On-Node Architecture Comparison

On-node scaling study for two architectures.

| Cores | C6gn (Aarch64) | C5n (X86) |
| ----- | -------------- | --------- |
| 1     |                |           |
| 2     |                |           |
| 4     |                |           |
| 8     |                |           |
| 16    |                |           |
| 32    |                |           |
| 64    |                |           |


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
