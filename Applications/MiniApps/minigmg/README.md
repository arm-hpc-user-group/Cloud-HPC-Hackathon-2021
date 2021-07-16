# miniGMG 

**Description:** miniGMG is a compact benchmark for understanding the performance challenges associated with geometric multigrid solvers found in applications built from AMR MG frameworks like CHOMBO or BoxLib when running on modern multi- and manycore-based supercomputers. It includes both productive reference examples as well as highly-optimized implementations for CPUs and GPUs. It is sufficiently general that it has been used to evaluate a broad range of research topics including PGAS programming models and algorithmic tradeoffs inherit in multigrid. miniGMG was developed under the CACHE Joint Math-CS Institute. Note, miniGMG code has been supersceded by HPGMG.

**URL:** http://crd.lbl.gov/departments/computer-science/PAR/research/previous-projects/miniGMG/

**Team:**  WolfPack

## Compilation

### Spack Package Modification

Details of any changes to the Spack recipe used.

We add a new dependent package since we apply our arm/simde optimizations to this application, and add the corresponding `simde` variant. For other compiler optimization flags, we add a variant `opt` to enable all of them.

Git commit hash of checkout for pacakage:

https://github.com/spack/spack/pull/24926/commits/949b7a644c6677fa6ccf824099b2ec32688000ba

https://github.com/spack/spack/commit/2f3d651b1967050523919a881b883982d2351eeb

Pull request for Spack recipe changes:

https://github.com/spack/spack/pull/24926

### Building miniGMG

#### GCC 10.3.0

```
spack install -j 64 minigmg@local%gcc@10.3.0
```

```
$ spack spec -Il minigmg@local%gcc@10.3.0

 -   sstmxbz  minigmg@local%gcc@10.3.0~debug~opt~simde arch=linux-amzn2-graviton2
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

#### ARM 21.0.0.879

```
spack install -j 64 minigmg@local%arm
```

```
$ spack spec -Il minigmg@local%arm

 -   33ilsbt  minigmg@local%arm@21.0.0.879~debug~opt~simde arch=linux-amzn2-graviton2
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

#### NVHPC 21.2

```
spack install -j 64 minigmg@local%nvhpc
```

```
$ spack spec -Il minigmg@local%nvhpc

 -   fjnn2h7  minigmg@local%nvhpc@21.2~debug~opt~simde arch=linux-amzn2-graviton2
[+]  krxyvbc      ^openmpi@4.1.0%nvhpc@21.2~atomics~cuda~cxx~cxx_exceptions+gpfs~internal-hwloc~java~legacylaunchers~lustre~memchecker+pmi~singularity~sqlite3+static~thread_multiple+vt+wrapper-rpath fabrics=ofi patches=60ce20bc14d98c572ef7883b9fcd254c3f232c2f3a13377480f96466169ac4c8,fba0d3a784a9723338722b48024a22bb32f6a951db841a4e9f08930a93f41d7a schedulers=slurm arch=linux-amzn2-graviton2
[+]  jroqews          ^hwloc@2.5.0%nvhpc@21.2~cairo~cuda~gl~libudev+libxml2~netloc~nvml+pci+shared arch=linux-amzn2-graviton2
[+]  e4m4ued              ^libpciaccess@0.16%nvhpc@21.2 patches=6e08dc445ece06e9e8b1344397f2d3f169005703ddc0f2ae24f366cde78c7377 arch=linux-amzn2-graviton2
[+]  kk4ax3i                  ^libtool@2.4.6%nvhpc@21.2 arch=linux-amzn2-graviton2
[+]  6c4kz5g                      ^m4@1.4.18%nvhpc@21.2+sigsegv patches=3877ab548f88597ab2327a2230ee048d2d07ace1062efe81fc92e91b7f39cd00,5746cf51f45b405661c3edae7a78c33d41e54d83f635d16e2bf1f956dbfbf635,fc9b61654a3ba1a8d6cd78ce087e7c96366c290bc8d2c299f09828d793b853c8 arch=linux-amzn2-graviton2
[+]  pa6wm5j                          ^libsigsegv@2.13%nvhpc@21.2 arch=linux-amzn2-graviton2
[+]  vtiml6g                  ^pkgconf@1.7.4%nvhpc@21.2 arch=linux-amzn2-graviton2
[+]  4imdwuy                  ^util-macros@1.19.3%nvhpc@21.2 arch=linux-amzn2-graviton2
[+]  wo4l72s              ^libxml2@2.9.10%nvhpc@21.2~python patches=05ff238cf435825ef835c7ae39376b52dc83d8caf19e962f0766c841386a305a,10a88ad47f9797cf7cf2d7d07241f665a3b6d1f31fa026728c8c2ae93e1664e9 arch=linux-amzn2-graviton2
[+]  r7mmkdp                  ^libiconv@1.16%nvhpc@21.2 arch=linux-amzn2-graviton2
[+]  br733tn                  ^xz@5.2.5%nvhpc@21.2~pic libs=shared,static arch=linux-amzn2-graviton2
[+]  4js6ect                  ^zlib@1.2.11%nvhpc@21.2+optimize+pic+shared arch=linux-amzn2-graviton2
[+]  asgm7mt              ^ncurses@6.2%nvhpc@21.2~symlinks+termlib abi=none arch=linux-amzn2-graviton2
[+]  uttaumr          ^libevent@2.1.12%nvhpc@21.2+openssl arch=linux-amzn2-graviton2
[+]  j2qhi7h              ^openssl@1.1.1k%nvhpc@21.2~docs+systemcerts arch=linux-amzn2-graviton2
[+]  gn4fgp5                  ^perl@5.32.1%nvhpc@21.2+cpanm+shared+threads patches=21cf6a73cec16760f8de2e8895ace1299aff2d8e92dc581cd18f1d95a4503048 arch=linux-amzn2-graviton2
[+]  5uyf3k4                      ^berkeley-db@18.1.40%nvhpc@21.2+cxx~docs+stl patches=b231fcc4d5cff05e5c3a4814f6a5af0e9a966428dc2176540d2c05aff41de522 arch=linux-amzn2-graviton2
[+]  wsi7g3j                      ^bzip2@1.0.8%nvhpc@21.2~debug~pic+shared arch=linux-amzn2-graviton2
[+]  s4mb5no                          ^diffutils@3.7%nvhpc@21.2 patches=6e42dc243f17aab29fd167f060f5bc1f08813e03368eb301b43c95d4b1386681 arch=linux-amzn2-graviton2
[+]  m2wdbeo                      ^gdbm@1.19%nvhpc@21.2 arch=linux-amzn2-graviton2
[+]  zori3wf                          ^readline@8.1%nvhpc@21.2 arch=linux-amzn2-graviton2
[+]  xl6zavq          ^libfabric@1.11.1-aws%nvhpc@21.2~debug~kdreg fabrics=sockets,tcp,udp arch=linux-amzn2-graviton2
[+]  5yq4tpw          ^numactl@2.0.14%nvhpc@21.2 patches=4e1d78cbbb85de625bad28705e748856033eaafab92a66dffd383a3d7e00cc94,62fc8a8bf7665a60e8f4c93ebbd535647cebf74198f7afafec4c085a8825c006 arch=linux-amzn2-graviton2
[+]  fo57byt              ^autoconf@2.69%nvhpc@21.2 arch=linux-amzn2-graviton2
[+]  gmd4264              ^automake@1.16.3%nvhpc@21.2 arch=linux-amzn2-graviton2
[+]  cl3ohqo          ^openssh@8.5p1%nvhpc@21.2 arch=linux-amzn2-graviton2
[+]  yvqpq74              ^libedit@3.1-20210216%nvhpc@21.2 arch=linux-amzn2-graviton2
[+]  zehhooy          ^slurm@20-02-4-1%nvhpc@21.2~gtk~hdf5~hwloc~mariadb~pmix+readline~restd sysconfdir=PREFIX/etc arch=linux-amzn2-graviton2
```

## Test Case 1

[ReFrame Benchmark 1](reframe_scripts/benchmark_v_test1_gcc.py)

```
reframe -c benchmark_v_test1_gcc.py -v -r --performance-report --keep-stage-files
```

## Test Case 2

[ReFrame Benchmark 2](reframe_scripts/benchmark_v_test2_gcc.py)

```
reframe -c benchmark_v_test2_gcc.py -v -r --performance-report --keep-stage-files
```

## Test Case 3

[ReFrame Benchmark 3](reframe_scripts/benchmark_v_test3_gcc.py)

```
reframe -c benchmark_v_test3_gcc.py -v -r --performance-report --keep-stage-files
```

## Test Case 4

[ReFrame Benchmark 4](reframe_scripts/benchmark_v_test4_gcc.py)

```
reframe -c benchmark_v_test4_gcc.py -v -r --performance-report --keep-stage-files
```

### Validation

miniGMG reduces the norm until it is less than 1e-15. If the norm is still greater than 1e-15 after `maxVCycles` v-cycles, the program will ends with incorrect results. So we check if all the norms produced by last v-cycles are less than 1e-15.  
#### Test Case 1
arm script:   
[ReFrame Benchmark](reframe_scripts/benchmark_v_test1_arm.py)    
gcc script:   
[ReFrame Benchmark](reframe_scripts/benchmark_v_test1_gcc.py)  

#### Test Case 2
arm script:   
[ReFrame Benchmark](reframe_scripts/benchmark_v_test2_arm.py)    
gcc script:   
[ReFrame Benchmark](reframe_scripts/benchmark_v_test2_gcc.py)  

#### Test Case 3
arm script:   
[ReFrame Benchmark](reframe_scripts/benchmark_v_test3_arm.py)    
gcc script:   
[ReFrame Benchmark](reframe_scripts/benchmark_v_test3_gcc.py)  

#### Test Case 4
arm script:   
[ReFrame Benchmark](reframe_scripts/benchmark_v_test4_arm.py)    
gcc script:   
[ReFrame Benchmark](reframe_scripts/benchmark_v_test4_gcc.py)  


### ReFrame Output

```
==============================================================================
PERFORMANCE REPORT
------------------------------------------------------------------------------
miniGMG_minigmg_on_node_test2_gcc_minigmg_local_gcc_10_3_0_N_1_MPI_1_OMP_1
- aws:c6gn
   - builtin
      * num_tasks: 1
      * Total Time: 127.3 s
------------------------------------------------------------------------------
miniGMG_minigmg_on_node_test2_gcc_minigmg_local_gcc_10_3_0_N_1_MPI_1_OMP_2
   - builtin
      * num_tasks: 1
      * Total Time: 84.14 s
------------------------------------------------------------------------------
miniGMG_minigmg_on_node_test2_gcc_minigmg_local_gcc_10_3_0_N_1_MPI_1_OMP_4
   - builtin
      * num_tasks: 1
      * Total Time: 52.06 s
------------------------------------------------------------------------------
miniGMG_minigmg_on_node_test2_gcc_minigmg_local_gcc_10_3_0_N_1_MPI_1_OMP_8
   - builtin
      * num_tasks: 1
      * Total Time: 41.18 s
------------------------------------------------------------------------------
miniGMG_minigmg_on_node_test2_gcc_minigmg_local_gcc_10_3_0_N_1_MPI_1_OMP_16
   - builtin
      * num_tasks: 1
      * Total Time: 51.58 s
------------------------------------------------------------------------------
miniGMG_minigmg_on_node_test2_gcc_minigmg_local_gcc_10_3_0_N_1_MPI_1_OMP_32
   - builtin
      * num_tasks: 1
      * Total Time: 82.87 s
------------------------------------------------------------------------------
miniGMG_minigmg_on_node_test2_gcc_minigmg_local_gcc_10_3_0_N_1_MPI_1_OMP_64
   - builtin
      * num_tasks: 1
      * Total Time: 131.02 s
------------------------------------------------------------------------------
miniGMG_minigmg_on_node_test2_arm_minigmg_local_arm_21_0_0_879_N_1_MPI_1_OMP_1
- aws:c6gn
   - builtin
      * num_tasks: 1
      * Total Time: 124.5 s
------------------------------------------------------------------------------
miniGMG_minigmg_on_node_test2_arm_minigmg_local_arm_21_0_0_879_N_1_MPI_1_OMP_2
   - builtin
      * num_tasks: 1
      * Total Time: 83.3 s
------------------------------------------------------------------------------
miniGMG_minigmg_on_node_test2_arm_minigmg_local_arm_21_0_0_879_N_1_MPI_1_OMP_4
   - builtin
      * num_tasks: 1
      * Total Time: 52.5 s
------------------------------------------------------------------------------
miniGMG_minigmg_on_node_test2_arm_minigmg_local_arm_21_0_0_879_N_1_MPI_1_OMP_8
   - builtin
      * num_tasks: 1
      * Total Time: 35.18 s
------------------------------------------------------------------------------
miniGMG_minigmg_on_node_test2_arm_minigmg_local_arm_21_0_0_879_N_1_MPI_1_OMP_16
   - builtin
      * num_tasks: 1
      * Total Time: 25.2 s
------------------------------------------------------------------------------
miniGMG_minigmg_on_node_test2_arm_minigmg_local_arm_21_0_0_879_N_1_MPI_1_OMP_32
   - builtin
      * num_tasks: 1
      * Total Time: 18.27 s
------------------------------------------------------------------------------
miniGMG_minigmg_on_node_test2_arm_minigmg_local_arm_21_0_0_879_N_1_MPI_1_OMP_64
   - builtin
      * num_tasks: 1
      * Total Time: 11.56 s
------------------------------------------------------------------------------
```

### On-node Compiler Comparison

Performance comparison of two compilers.
#### Test Case 1
arm script:   
[ReFrame Benchmark](reframe_scripts/benchmark_onnode_test1_arm.py)    
gcc script:   
[ReFrame Benchmark](reframe_scripts/benchmark_onnode_test1_gcc.py)  
| Cores | arm | gcc |
|-------|------------|------------|
| 8     | 4.35 s           | 6.31 s           |
| 16    | 3.58 s           | 7.81 s           |
| 32    | 3.71 s           | 11.39 s           |
| 64    | 3.91 s           | 18.33 s           |

#### Test Case 2
arm script:   
[ReFrame Benchmark](reframe_scripts/benchmark_onnode_test2_arm.py)    
gcc script:   
[ReFrame Benchmark](reframe_scripts/benchmark_onnode_test2_gcc.py)   
| Cores | arm | gcc |
|-------|------------|------------|
| 8     | 35.18 s           | 41.18 s           |
| 16    | 25.2 s           | 51.58 s           |
| 32    | 18.27 s           | 82.87 s           |
| 64    | 11.56 s           | 131.02 s           |

#### Test Case 3
arm script:   
[ReFrame Benchmark](reframe_scripts/benchmark_onnode_test3_arm.py)    
gcc script:   
[ReFrame Benchmark](reframe_scripts/benchmark_onnode_test3_gcc.py) 
| Cores | arm | gcc |
|-------|------------|------------|
| 8     | 273.77 s           | 314.23 s           |
| 16    | 199.31 s           | 418.16 s           |
| 32    | 134.02 s           | 686.54 s           |
| 64    | 81.45 s           | 1097.58 s           |

#### Test Case 4
arm script:   
[ReFrame Benchmark](reframe_scripts/benchmark_onnode_test4_arm.py)    
gcc script:   
[ReFrame Benchmark](reframe_scripts/benchmark_onnode_test4_gcc.py)  
| Cores | arm | gcc |
|-------|------------|------------|
| 8     | 535.99 s           | 789.04 s           |
| 16    | 520.7 s           | 1048.72 s           |
| 32    | 375.39 s           | 1906.81 s           |
| 64    | 269.4 s           | 2499.68 s           |


### Serial Hot-spot Profile

List of top-10 functions / code locations from a serial profile.

#### Test Case 1  
Profiling script:  
[ReFrame Benchmark](reframe_scripts/benchmark_p4_test1_gcc.py)  
![st1](pictures/st1.png)

#### Test Case 2
Profiling script:  
[ReFrame Benchmark](reframe_scripts/benchmark_p4_test2_gcc.py)  
![st2](pictures/st2.png)

#### Test Case 3
Profiling script:  
[ReFrame Benchmark](reframe_scripts/benchmark_p4_test3_gcc.py)  
![st3](pictures/st3.png)

#### Test Case 4
Profiling script:  
[ReFrame Benchmark](reframe_scripts/benchmark_p4_test4_gcc.py)  
![st4](pictures/st4.png)

### Full Node Hot-spot Profile

List of top-10 functions / code locations from a full node profile.

#### gcc
#### Test Case 1  
Profiling script:  
[ReFrame Benchmark](reframe_scripts/benchmark_p5_test1_gcc.py)  
![w1g](pictures/w1g.png)

#### Test Case 2
Profiling script:  
[ReFrame Benchmark](reframe_scripts/benchmark_p5_test2_gcc.py)  
![w2g](pictures/w2g.png)

#### Test Case 3
Profiling script:  
[ReFrame Benchmark](reframe_scripts/benchmark_p5_test3_gcc.py)  
![w3g](pictures/w3g.png)

#### Test Case 4
HPCToolkit  
![w4g](pictures/w4g.png)

#### arm
#### Test Case 1  
Profiling script:  
[ReFrame Benchmark](reframe_scripts/benchmark_p5_test1_arm.py)  
![w1a](pictures/w1a.png)

#### Test Case 2
Profiling script:  
[ReFrame Benchmark](reframe_scripts/benchmark_p5_test2_arm.py)  
![w2a](pictures/w2a.png)

#### Test Case 3
Profiling script:  
[ReFrame Benchmark](reframe_scripts/benchmark_p5_test3_arm.py)  
![w3a](pictures/w3a.png)

#### Test Case 4
Profiling script:  
[ReFrame Benchmark](reframe_scripts/benchmark_p5_test4_arm.py)  
![w4a](pictures/w4a.png)

### Strong Scaling Study
#### On-node scaling study for two compilers:

#### Test Case 1
arm script:   
[ReFrame Benchmark](reframe_scripts/benchmark_onnode_test1_arm.py)    
gcc script:   
[ReFrame Benchmark](reframe_scripts/benchmark_onnode_test1_gcc.py)    
| Cores | arm | gcc |
|-------|------------|------------|
| 8     | 4.35 s           | 6.31 s           |
| 16    | 3.58 s           | 7.81 s           |
| 32    | 3.71 s           | 11.39 s           |
| 64    | 3.91 s           | 19.33 s           |

#### Test Case 2
arm script:   
[ReFrame Benchmark](reframe_scripts/benchmark_onnode_test2_arm.py)    
gcc script:   
[ReFrame Benchmark](reframe_scripts/benchmark_onnode_test2_gcc.py)    
| Cores | arm | gcc |
|-------|------------|------------|
| 8     | 35.18 s           | 41.18 s           |
| 16    | 25.2 s           | 51.58 s           |
| 32    | 18.27 s           | 82.87 s           |
| 64    | 11.56 s           | 131.02 s           |

#### Test Case 3
arm script:   
[ReFrame Benchmark](reframe_scripts/benchmark_onnode_test3_arm.py)    
gcc script:   
[ReFrame Benchmark](reframe_scripts/benchmark_onnode_test3_gcc.py)    
| Cores | arm | gcc |
|-------|------------|------------|
| 8     | 273.77 s           | 314.23 s           |
| 16    | 199.31 s           | 418.16 s           |
| 32    | 134.02 s           | 686.54 s           |
| 64    | 81.45 s           | 1097.58 s           |

#### Test Case 4
arm script:   
[ReFrame Benchmark](reframe_scripts/benchmark_onnode_test4_arm.py)    
gcc script:   
[ReFrame Benchmark](reframe_scripts/benchmark_onnode_test4_gcc.py)    
| Cores | arm | gcc |
|-------|------------|------------|
| 8     | 535.99 s           | 789.04 s            |
| 16    | 520.7 s           | 1048.72 s          |
| 32    | 375.39 s           | 1906.81 s           |
| 64    | 269.4 s           | 2499.68 s           |

#### Off-node scaling study for two compilers:
#### Test Case 1
arm script:  
[ReFrame Benchmark 1](reframe_scripts/benchmark_offnode1_test1_arm.py)  
[ReFrame Benchmark 2](reframe_scripts/benchmark_offnode2_test1_arm.py)  
gcc script:  
[ReFrame Benchmark 1](reframe_scripts/benchmark_offnode1_test1_gcc.py)  
[ReFrame Benchmark 2](reframe_scripts/benchmark_offnode1_test1_gcc.py)  

| Nodes | Cores | arm |  gcc |
|-------|-------|------------|------------|
| 1     | 32    | 4.35 s	           |  11.39 s   |
| 1     | 64    | 3.58 s           | 19.33 s    |
| 2     | 128   | 60.24 s           | 11.34 s    |
| 4     | 256   | 63.33 s           | 7.67 s    |

#### Test Case 2
arm script:  
[ReFrame Benchmark 1](reframe_scripts/benchmark_offnode1_test2_arm.py)  
[ReFrame Benchmark 2](reframe_scripts/benchmark_offnode2_test2_arm.py)  
gcc script:  
[ReFrame Benchmark 1](reframe_scripts/benchmark_offnode1_test2_gcc.py)  
[ReFrame Benchmark 2](reframe_scripts/benchmark_offnode1_test2_gcc.py)  

| Nodes | Cores | arm |  gcc |
|-------|-------|------------|------------|
| 1     | 32    | 35.18 s	           | 41.18 s    |
| 1     | 64    | 25.2 s           | 51.58 s    |
| 2     | 128   | 7.67 s           | 68.77 s    |
| 4     | 256   | 66.17 s           | 37.38 s     |

#### Test Case 3
arm script:  
[ReFrame Benchmark 1](reframe_scripts/benchmark_offnode1_test3_arm.py)  
[ReFrame Benchmark 2](reframe_scripts/benchmark_offnode2_test3_arm.py)  
gcc script:  
[ReFrame Benchmark 1](reframe_scripts/benchmark_offnode1_test3_gcc.py)  
[ReFrame Benchmark 2](reframe_scripts/benchmark_offnode1_test3_gcc.py)  

| Nodes | Cores | arm |  gcc |
|-------|-------|------------|------------|
| 1     | 32    | 273.77 s	           | 314.23 s    |
| 1     | 64    | 199.31 s           | 418.16 s    |
| 2     | 128   | 46.77 s           | 559.38 s    |
| 4     | 256   | 29.05 s          | 283.53 s     |

#### Test Case 4
arm script:  
[ReFrame Benchmark 1](reframe_scripts/benchmark_offnode1_test4_arm.py)  
[ReFrame Benchmark 2](reframe_scripts/benchmark_offnode2_test4_arm.py)  
gcc script:  
[ReFrame Benchmark 1](reframe_scripts/benchmark_offnode1_test4_gcc.py)  
[ReFrame Benchmark 2](reframe_scripts/benchmark_offnode1_test4_gcc.py)  
| Nodes | Cores | arm |  gcc |
|-------|-------|------------|------------|
| 1     | 32    | 535.99 s 	           | 789.04 s    |
| 1     | 64    | 520.7 s           | 1048.72 s   |
| 2     | 128   | 147.97 s          | 1879.59 s    |
| 4     | 256   | 82.66 s           | 942.39 s     |

### On-Node Architecture Comparison

On-node scaling study for two architectures.  
Compiler: gcc
#### Test Case 1
X86 script:  
[ReFrame Benchmark](reframe_scripts/benchmark_onnode_test1_gcc_x86.py)  
| Cores | C6gn (ARM) | C5n (X86) |
|-------|------------|-----------|
| 8     | 6.31 s           | 19.91 s   |
| 16    | 7.81 s           | 22.06 s   |
| 32    | 11.39 s           | 30.28 s   |
| 64    | 19.33 s           | 46.11 s   |

#### Test Case 2
X86 script:  
[ReFrame Benchmark](reframe_scripts/benchmark_onnode_test2_gcc_x86.py)  
| Cores | C6gn (ARM) | C5n (X86) |
|-------|------------|-----------|
| 8     | 41.18 s           | 72.85 s   |
| 16    | 51.58 s           | 84.45 s   |
| 32    | 82.87 s           | 142.46 s  |
| 64    | 131.02 s           | 252.93 s  |

#### Test Case 3
X86 script:  
[ReFrame Benchmark](reframe_scripts/benchmark_onnode_test3_gcc_x86.py)  
| Cores | C6gn (ARM) | C5n (X86) |
|-------|------------|-----------|
| 8     | 314.23 s           | 543.84 s  |
| 16    | 418.16 s           | 640.72 s  |
| 32    | 686.54 s           | 1087.96 s |
| 64    | 1097.58 s           | 2025.36 s |

#### Test Case 4
X86 script:  
[ReFrame Benchmark](reframe_scripts/benchmark_onnode_test4_gcc_x86.py)  
| Cores | C6gn (ARM) | C5n (X86) |
|-------|------------|-----------|
| 8     | 789.04 s           | 1305.74 s |
| 16    | 1048.72 s           | 1915.15 s |
| 32    | 1906.81 s           | 3563.73 s |
| 64    | 2499.68 s           | 7220.35 s |

### Off-Node Architecture Comparison

Off-node scaling study for two architectures.
Compiler: gcc
#### Test Case 1
X86 script:  
[ReFrame Benchmark](reframe_scripts/benchmark_offnode1_test1_gcc_x86.py)  
[ReFrame Benchmark](reframe_scripts/benchmark_offnode2_test1_gcc_x86.py)  
| Nodes | Cores | C6gn (ARM) |  C5n (X86) |
|-------|-------|------------|------------|
| 1     | 32    | 11.39 s	           | 30.28 s    |
| 1     | 64    | 19.33 s           | 46.11 s    |
| 2     | 128   | 11.34 s           | 33.52 s    |
| 4     | 256   | 7.67 s           | 26.4 s     |

#### Test Case 2
X86 script:  
[ReFrame Benchmark](reframe_scripts/benchmark_offnode1_test2_gcc_x86.py)  
[ReFrame Benchmark](reframe_scripts/benchmark_offnode2_test2_gcc_x86.py)  
| Nodes | Cores | C6gn (ARM) |  C5n (X86) |
|-------|-------|------------|------------|
| 1     | 32    | 82.87 s           | 142.46 s   |
| 1     | 64    | 131.02 s           | 252.93 s   |
| 2     | 128   | 68.77 s           | 141.92 s   |
| 4     | 256   | 37.38 s           | 82.26 s    |

#### Test Case 3
X86 script:  
[ReFrame Benchmark](reframe_scripts/benchmark_offnode1_test3_gcc_x86.py)  
[ReFrame Benchmark](reframe_scripts/benchmark_offnode2_test3_gcc_x86.py)  
| Nodes | Cores | C6gn (ARM) |  C5n (X86) |
|-------|-------|------------|------------|
| 1     | 32    | 686.54 s           | 1087.96 s  |
| 1     | 64    | 1097.58 s           | 2025.36 s  |
| 2     | 128   | 559.38 s           | 1027.75 s  |
| 4     | 256   | 283.53 s          | 526.23 s   |

#### Test Case 4
X86 script:  
[ReFrame Benchmark](reframe_scripts/benchmark_offnode1_test4_gcc_x86.py)  
[ReFrame Benchmark](reframe_scripts/benchmark_offnode2_test4_gcc_x86.py)  
| Nodes | Cores | C6gn (ARM) |  C5n (X86) |
|-------|-------|------------|------------|
| 1     | 32    | 1906.81 s           | 3563.73 s  |
| 1     | 64    | 2499.68 s           | 7220.35 s  |
| 2     | 128   | 1879.59 s           | 3421.94 s  |
| 4     | 256   | 942.39 s           | 1732.57 s  |

## Optimisation

Details of steps taken to optimise performance of the application.
Please document work with compiler flags, maths libraries, system libraries, code optimisations, etc.

### Compiler Flag Tuning

Compiler flags before:
```
CFLAGS= -O3 -fopenmp  -lm -Daarch64 -D__MPI -D__COLLABORATIVE_THREADING=6 -D__TEST_MG_CONVERGENCE -D__PRINT_NORM -D__USE_BICGSTAB 
FFLAGS=
```

Compiler flags after:
```
CFLAGS= -O3 -Ofast -fopenmp -lm -Daarch64 -D__MPI -D__TEST_MG_CONVERGENCE -D__PREFETCH_NEXT_PLANE_FROM_DRAM -D__FUSION_RESIDUAL_RESTRICTION -D__PRINT_NORM -D__USE_BICGSTAB 
FFLAGS=
```

#### Compiler Flag Performance

The following table is based on gcc@10.3.0 with Test Case 3.

| Cores | Original Flags | New Flags |
| ----- | -------------- | --------- |
| 1     | 1060.55            |1030.97   |
| 2     | 643.84        |    619.43       |
| 4     | 401.97      |          371.58 |
| 8     | 314.23    |          270.56 |
| 16    | 418.16 |           146.35|
| 32    | 686.54|           105.15|
| 64    | 1097.58 |           74.81|

### Performance Regression

How fast can you make the code?

The following table is based on gcc@10.3.0 with Test Case 3.


| Cores | Original  | Optimization |
| ----- | -------------- | --------- |
| 1     | 1060.55            |720.42   |
| 2     | 643.84        |    349.17      |
| 4     | 401.97      |          233.63 |
| 8     | 314.23    |          144.44|
| 16    | 418.16 |           91.6|
| 32    | 686.54|           64.02|
| 64    | 1097.58 |           46.04|

#### 


Use all of the above aproaches and any others to make the code as fast as possible.
Demonstrate your gains by providing a scaling study for your test case, demonstrating the performance before and after.



## Report

### Compilation Summary

Porting miniGMG to ARM needs some adaptation of the code. We changed the rdtsc() function in the timer.x86.c from x86 assemblies to aarch64 assemblies to ensure the success of the compilation. Furthermore, our compilation enables both OpenMP and MPI. We found some issues in both Spack and nvhpc compiler. For Spack, it does not give a special build option for graviton2, but only a general aarch64 option; we added a graviton2 option in Spack and submitted to archspec-json. For nvhpc, we found it produces wrong code for OpenMP programs when running with more than 1 thread, while nvhpc works correctly for sequential and MPI (with no threads) programs. Given the short time frame, we didn’t pinpoint the exact bug in nvhpc code genration, but it inspires to investigate its OpenMP implementation and checks whether it exactly follows the OpenMP standard.

### Performance Summary

We have observed very interesting performance insights in miniGMG. When there are 4 cores or less, ARM21 and GCC have comparable performanc
e. However, ARM21 gives much better performance over GCC when the execution scales to 8 and more cores. Moreover, ARM server gives much bet
ter performance than Intel server.


### Optimisation Summary

We have tested multiple optimization strategies, which includes: (1) using SIMD instructions on aarch64 (Neon), (2) using -Ofast (especially using fast math library), (3) enabling algorithm optimization (residual operator fusion), (4) using active waiting policy for OpenMP threads.
