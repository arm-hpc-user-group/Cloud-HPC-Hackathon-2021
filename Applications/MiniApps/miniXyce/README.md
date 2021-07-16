# miniXyce 

**Description:** Portable proxy of some of the key capabilities in the electrical modeling Xyce

**URL:** https://github.com/Mantevo/miniXyc 

**Team:** SGHackers 

## Compilation

### Spack Package Modification

Details of any changes to the Spack recipe used.

Git commit hash of checkout for pacakage:

Pull request for Spack recipe changes:

### Building miniXyce

#### Compiler 1 - GCC

Note that this version of minixyce is built with clingo concretizer

```
spack install minixyce@gcc10.3.0 ^openmpi ^openblas
```

```
spack spec -Il minixyce@gcc10.3.0 ^openmpi ^openblas

 -   owz3zsf  minixyce@gcc10.3.0%gcc@10.3.0+mpi arch=linux-amzn2-graviton2
[+]  db6k6bv      ^openmpi@4.1.0%gcc@10.3.0~atomics~cuda~cxx~cxx_exceptions+gpfs~internal-hwloc~java~legacylaunchers~lustre+memchecker+pmi~singularity~sqlite3+static~thread_multiple+vt+wrapper-rpath fabrics=ofi patches=60ce20bc14d98c572ef7883b9fcd254c3f232c2f3a13377480f96466169ac4c8 schedulers=slurm arch=linux-amzn2-graviton2
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
[+]  naovedc          ^libfabric@1.11.1-aws%gcc@10.3.0~debug~kdreg fabrics=sockets,tcp,udp arch=linux-amzn2-graviton2
[+]  mhav5gn          ^numactl@2.0.14%gcc@10.3.0 patches=4e1d78cbbb85de625bad28705e748856033eaafab92a66dffd383a3d7e00cc94,62fc8a8bf7665a60e8f4c93ebbd535647cebf74198f7afafec4c085a8825c006 arch=linux-amzn2-graviton2
[+]  jkuhz64              ^autoconf@2.69%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  xb2w5nc              ^automake@1.16.3%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  wturp6c          ^openssh@8.5p1%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  ivotdt7              ^libedit@3.1-20210216%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  23tbh4p          ^slurm@20-02-4-1%gcc@10.3.0~gtk~hdf5~hwloc~mariadb~pmix+readline~restd sysconfdir=PREFIX/etc arch=linux-amzn2-graviton2
[+]  3rwukeq          ^valgrind@3.17.0%gcc@10.3.0+boost~mpi+only64bit+ubsan arch=linux-amzn2-graviton2
[+]  57hfd5g              ^boost@1.76.0%gcc@10.3.0+atomic+chrono~clanglibcpp~container~context~coroutine+date_time~debug+exception~fiber+filesystem+graph~icu+iostreams+locale+log+math~mpi+multithreaded+numpy~pic+program_options+python+random+regex+serialization+shared+signals~singlethreaded+system~taggedlayout+test+thread+timer~versionedlayout+wave cxxstd=98 patches=2ab6c72d03dec6a4ae20220a9dfd5c8c572c5294252155b85c6874d97c323199 visibility=hidden arch=linux-amzn2-graviton2
[+]  y4tgmgt                  ^py-numpy@1.21.0%gcc@10.3.0+blas+lapack patches=873745d7b547857fcfec9cae90b09c133b42a4f0c23b6c2d84cf37e2dd816604 arch=linux-amzn2-graviton2
[+]  rv7gj6u                      ^openblas@0.3.15%gcc@10.3.0~bignuma~consistent_fpcsr~ilp64+locking+pic+shared threads=none arch=linux-amzn2-graviton2
[+]  gck7f7b                      ^py-cython@0.29.22%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  s6xqcwm                          ^py-setuptools@50.3.2%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  62czasr                              ^python@3.8.11%gcc@10.3.0+bz2+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tix~tkinter~ucs4+uuid+zlib patches=0d98e93189bc278fbc37a50ed7f183bd8aaf249a8e1670a465f0db6bb4f8cf87 arch=linux-amzn2-graviton2
[+]  ychdz7l                                  ^expat@2.4.1%gcc@10.3.0+libbsd arch=linux-amzn2-graviton2
[+]  ourxkez                                      ^libbsd@0.11.3%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  nssrqfc                                          ^libmd@1.0.3%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  fqlpcsl                                  ^gettext@0.21%gcc@10.3.0+bzip2+curses+git~libunistring+libxml2+tar+xz arch=linux-amzn2-graviton2
[+]  v6cutkh                                      ^tar@1.34%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  35cffos                                  ^libffi@3.3%gcc@10.3.0 patches=26f26c6f29a7ce9bf370ad3ab2610f99365b4bdd7b82e7c31df41a3370d685c0 arch=linux-amzn2-graviton2
[+]  2q753q6                                  ^sqlite@3.35.5%gcc@10.3.0+column_metadata+fts~functions~rtree arch=linux-amzn2-graviton2
[+]  2non7qx                                  ^util-linux-uuid@2.36.2%gcc@10.3.0 arch=linux-amzn2-graviton2

```

#### Compiler 2 - arm

Note that this version of minixyce is built with default concretizer

```
spack install minixyce%arm@21.0.0.879 ^openmpi

```

```
spack spec -Il minixyce%arm@21.0.0.879 ^openmpi

[+]  lglv4qx  minixyce@1.0%arm@21.0.0.879+mpi arch=linux-amzn2-aarch64
[+]  lmaoy5t      ^openmpi@4.1.0%arm@21.0.0.879~atomics~cuda~cxx~cxx_exceptions+gpfs~internal-hwloc~java~legacylaunchers~lustre~memchecker+pmi~singularity~sqlite3+static~thread_multiple+vt+wrapper-rpath fabrics=ofi patches=60ce20bc14d98c572ef7883b9fcd254c3f232c2f3a13377480f96466169ac4c8 schedulers=slurm arch=linux-amzn2-aarch64
[+]  xl6anaa          ^hwloc@2.5.0%arm@21.0.0.879~cairo~cuda~gl~libudev+libxml2~netloc~nvml+pci+shared arch=linux-amzn2-aarch64
[+]  jueqz7p              ^libpciaccess@0.16%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  e4ssqx6                  ^libtool@2.4.6%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  i2jmeo4                      ^m4@1.4.18%arm@21.0.0.879+sigsegv patches=3877ab548f88597ab2327a2230ee048d2d07ace1062efe81fc92e91b7f39cd00,fc9b61654a3ba1a8d6cd78ce087e7c96366c290bc8d2c299f09828d793b853c8 arch=linux-amzn2-aarch64
[+]  6jhzlul                          ^libsigsegv@2.13%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  zpuzm23                  ^pkgconf@1.7.4%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  uwcxkin                  ^util-macros@1.19.3%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  dypqz2i              ^libxml2@2.9.10%arm@21.0.0.879~python arch=linux-amzn2-aarch64
[+]  7vnthzn                  ^libiconv@1.16%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  zqsab4f                  ^xz@5.2.5%arm@21.0.0.879~pic libs=shared,static arch=linux-amzn2-aarch64
[+]  puuxvg2                  ^zlib@1.2.11%arm@21.0.0.879+optimize+pic+shared arch=linux-amzn2-aarch64
[+]  uhtqtlb              ^ncurses@6.2%arm@21.0.0.879~symlinks+termlib abi=none arch=linux-amzn2-aarch64
[+]  gonqskn          ^libevent@2.1.12%arm@21.0.0.879+openssl arch=linux-amzn2-aarch64
[+]  vc3waha              ^openssl@1.1.1k%arm@21.0.0.879~docs+systemcerts arch=linux-amzn2-aarch64
[+]  vv6txro                  ^perl@5.32.1%arm@21.0.0.879+cpanm+shared+threads arch=linux-amzn2-aarch64
[+]  33wiajj                      ^berkeley-db@18.1.40%arm@21.0.0.879+cxx~docs+stl patches=b231fcc4d5cff05e5c3a4814f6a5af0e9a966428dc2176540d2c05aff41de522 arch=linux-amzn2-aarch64
[+]  z4ybgri                      ^bzip2@1.0.8%arm@21.0.0.879~debug~pic+shared arch=linux-amzn2-aarch64
[+]  adtc6yc                          ^diffutils@3.7%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  645q4qj                      ^gdbm@1.19%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  3haw5gt                          ^readline@8.1%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  qdn27nh          ^libfabric@1.11.1-aws%arm@21.0.0.879~debug~kdreg fabrics=sockets,tcp,udp arch=linux-amzn2-aarch64
[+]  mv2g7r5          ^numactl@2.0.14%arm@21.0.0.879 patches=4e1d78cbbb85de625bad28705e748856033eaafab92a66dffd383a3d7e00cc94,62fc8a8bf7665a60e8f4c93ebbd535647cebf74198f7afafec4c085a8825c006 arch=linux-amzn2-aarch64
[+]  dcs645r              ^autoconf@2.69%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  edezkz3              ^automake@1.16.3%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  6vvthuo          ^openssh@8.5p1%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  xe4evc4              ^libedit@3.1-20210216%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  x5xehti          ^slurm@20-02-4-1%arm@21.0.0.879~gtk~hdf5~hwloc~mariadb~pmix+readline~restd sysconfdir=PREFIX/etc arch=linux-amzn2-aarch64

```

#### Compiler 3

```
spack install minixyce%nvhpc@21.2 ^openmpi
```

```
spack spec -Il minixyce%nvhpc@21.2 ^openmpi

[+]  hgzlj2e  minixyce@1.0%nvhpc@21.2+mpi arch=linux-amzn2-graviton2
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
## Test Set 1

[ReFrame Benchmark 1](#)

```
reframe -c minixyce_compiler.py -r --performance-report -v

```

### Validation

This Test Set contains 21 tests in total.

Test Set 1 (minixyce_compiler.py) is for scaling analysis such as on-node and off-node analysis, as well as performance comparison across different compilers.
The input is a large circuit with 15000 electrical components. Basic sanity check is done to ensure the validity of benchmark. This includes checking for resistor/inductor/capacitor counts from the output dump.

For functional validation, see Test Set 2.


### ReFrame Output

Performance report for minixyce benchmark running 1,2,4,8,16,32 and 64 tasks, across gcc, arm and nvhpc compilers

```
==============================================================================
PERFORMANCE REPORT
------------------------------------------------------------------------------
MiniXyce_short_test_minixyce__gcc_10_3_0_N_1_MPI_64_OMP_1
- aws:c6gn
   - builtin
      * num_tasks: 64
      * Total Time: 52.2978 s
------------------------------------------------------------------------------
MiniXyce_short_test_minixyce__gcc_10_3_0_N_1_MPI_32_OMP_1
   - builtin
      * num_tasks: 32
      * Total Time: 85.407 s
------------------------------------------------------------------------------
MiniXyce_short_test_minixyce__gcc_10_3_0_N_1_MPI_16_OMP_1
   - builtin
      * num_tasks: 16
      * Total Time: 184.024 s
------------------------------------------------------------------------------
MiniXyce_short_test_minixyce__gcc_10_3_0_N_1_MPI_8_OMP_1
   - builtin
      * num_tasks: 8
      * Total Time: 476.893 s
------------------------------------------------------------------------------
MiniXyce_short_test_minixyce__gcc_10_3_0_N_1_MPI_4_OMP_1
   - builtin
      * num_tasks: 4
      * Total Time: 934.919 s
------------------------------------------------------------------------------
MiniXyce_short_test_minixyce__gcc_10_3_0_N_1_MPI_2_OMP_1
   - builtin
      * num_tasks: 2
      * Total Time: 498.911 s
------------------------------------------------------------------------------
MiniXyce_short_test_minixyce__gcc_10_3_0_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Total Time: 15.7698 s
------------------------------------------------------------------------------
MiniXyce_short_test_minixyce__arm_N_1_MPI_64_OMP_1
   - builtin
      * num_tasks: 64
      * Total Time: 39.9701 s
------------------------------------------------------------------------------
MiniXyce_short_test_minixyce__arm_N_1_MPI_32_OMP_1
   - builtin
      * num_tasks: 32
      * Total Time: 54.2542 s
------------------------------------------------------------------------------
MiniXyce_short_test_minixyce__arm_N_1_MPI_16_OMP_1
   - builtin
      * num_tasks: 16
      * Total Time: 136.656 s
------------------------------------------------------------------------------
MiniXyce_short_test_minixyce__arm_N_1_MPI_8_OMP_1
   - builtin
      * num_tasks: 8
      * Total Time: 368.376 s
------------------------------------------------------------------------------
MiniXyce_short_test_minixyce__arm_N_1_MPI_4_OMP_1
   - builtin
      * num_tasks: 4
      * Total Time: 732.316 s
------------------------------------------------------------------------------
MiniXyce_short_test_minixyce__arm_N_1_MPI_2_OMP_1
   - builtin
      * num_tasks: 2
      * Total Time: 284.202 s
------------------------------------------------------------------------------
MiniXyce_short_test_minixyce__arm_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Total Time: 16.5698 s
------------------------------------------------------------------------------
MiniXyce_short_test_minixyce__nvhpc_N_1_MPI_64_OMP_1
   - builtin
      * num_tasks: 64
      * Total Time: 51.5188 s
------------------------------------------------------------------------------
MiniXyce_short_test_minixyce__nvhpc_N_1_MPI_32_OMP_1
   - builtin
      * num_tasks: 32
      * Total Time: 80.6583 s
------------------------------------------------------------------------------
MiniXyce_short_test_minixyce__nvhpc_N_1_MPI_16_OMP_1
   - builtin
      * num_tasks: 16
      * Total Time: 176.202 s
------------------------------------------------------------------------------
MiniXyce_short_test_minixyce__nvhpc_N_1_MPI_8_OMP_1
   - builtin
      * num_tasks: 8
      * Total Time: 523.669 s
------------------------------------------------------------------------------
MiniXyce_short_test_minixyce__nvhpc_N_1_MPI_4_OMP_1
   - builtin
      * num_tasks: 4
      * Total Time: 948.424 s
------------------------------------------------------------------------------
MiniXyce_short_test_minixyce__nvhpc_N_1_MPI_2_OMP_1
   - builtin
      * num_tasks: 2
      * Total Time: 513.17 s
------------------------------------------------------------------------------
MiniXyce_short_test_minixyce__nvhpc_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Total Time: 15.6227 s
------------------------------------------------------------------------------


```


### On-node Compiler Comparison

Performance comparison of three compilers(in seconds).

| Cores | GCC@10.3.0 | ARM@20.0 | NVHPC   |
|-------|------------|----------|---------|
| 1     | 15.7698    | 16.5698  | 15.6227 |
| 2     | 498.911    | 284.202  | 513.17  |
| 4     | 932.919    | 732.316  | 948.424 |
| 8     | 476.893    | 386.378  | 523.699 |
| 16    | 184.024    | 136.656  | 176.202 |
| 32    | 85.407     | 54.2524  | 80.6583 |
| 64    | 52.2978    | 39.9701  | 51.5188 |



### Serial Hot-spot Profile

List of top-10 functions / code locations from a serial profile.


We used the arm-forge tool-chain to profile our applications.

Profiling command used:
```
:map -profile /opt/amazon/openmpi/bin/mpiexec --np 1 miniXyce.x --circuit tests/cir6.net --t_start 0 --pf tests/default_params.txt

```

| Position | Routine                                                                                                                              | Time (s) | Time (%) |
|----------|--------------------------------------------------------------------------------------------------------------------------------------|----------|----------|
| 1        | mX_matrix_utils::gmres(mX_matrix_utils::distributed_sparse_matrix*, std::vector<double, std::allocator<double                        |          | 33.8%    |
| 2        | mX_matrix_utils::sparse_matrix_vector_product(mX_matrix_utils::distributed_sparse_matrix*, std::vector<double, std::allocator<double |          | 12.1%    |
| 3        | __aarch64_swp4_rel                                                                                                                   |          | 8.2%     |
| 4        | __printf_fp_l                                                                                                                        |          | 4.9"%    |
| 5        | hack_digit                                                                                                                           |          | 4.5%     |
| 6        | malloc                                                                                                                               |          | 3.9%     |
| 7        | _int_malloc                                                                                                                          |          | 3.6%     |
| 8        | _int_free                                                                                                                            |          | 3.5%     |
| 9        | malloc_consolidate                                                                                                                   |          | 3.1%     |
| 10       | __aarch64_cas4_acq                                                                                                                   |          | 3.1%     |



### Full Node Hot-spot Profile

List of top-10 functions / code locations from a full node profile.

Profiling command used:
```
:map -profile /opt/amazon/openmpi/bin/mpiexec --np 64 miniXyce.x --circuit tests/cir6.net --t_start 0 --pf tests/default_params.txt
```

| Position | Routine                                                                                                                              | Time (s) | Time (%) | MPI (%) |
|----------|--------------------------------------------------------------------------------------------------------------------------------------|----------|----------|---------|
| 1        | MPI_Allreduce                                                                                                                        |          | 94.7%    | 94.7%   |
| 2        | MPI_Recv                                                                                                                             |          | 4.1%     | 4.1%    |
| 3        | MPI_Send                                                                                                                             |          | 0.7%     | 0.7%    |
| 4        | std::_Rb_tree<int, std::pair<int const, double>, std::_Select1st<std::pair<int const, double                                         |          | <0.1%    | 0       |
| 5        | std::vector<double, std::allocator<double..                                                                                          |          | <0.1%    | 0       |
| 6        | __gnu_cxx::__aligned_membuf<std::pair<int const, double                                                                              |          | <0.1%    | 0       |
| 7        | mX_matrix_utils::gmres(mX_matrix_utils::distributed_sparse_matrix*, std::vector<double, std::allocator<double                        |          | <0.1%    | 99.5%   |
| 8        | std::less<int>::operator()(int const&, int const&) const                                                                             |          | <0.1%    |         |
| 9        | mX_matrix_utils::sparse_matrix_vector_product(mX_matrix_utils::distributed_sparse_matrix*, std::vector<double, std::allocator<double |          | <0.1%    | 4.8%    |
| 10       | std::_Select1st<std::pair<int const, double                                                                                          |          | <0.1%    | <0.1%   |


### Strong Scaling Study

On-node scaling study for three compilers.

| Cores | GCC@10.3.0 | ARM@20.0 | NVHPC   |
|-------|------------|----------|---------|
| 1     | 15.7698    | 16.5698  | 15.6227 |
| 2     | 498.911    | 284.202  | 513.17  |
| 4     | 932.919    | 732.316  | 948.424 |
| 8     | 476.893    | 386.378  | 523.699 |
| 16    | 184.024    | 136.656  | 176.202 |
| 32    | 85.407     | 54.2524  | 80.6583 |
| 64    | 52.2978    | 39.9701  | 51.5188 |

### Off-Node Scaling Study

Off-node scaling study comparing C6g and C6gn instances.

| Nodes | Cores | C6g | C6gn |
|-------|-------|-----|------|
| 1     | 8     |     |363.83|
| 1     | 16    |     |136.99|
| 1     | 32    |     |61.952|
| 1     | 64    |     |38.711|
| 2     | 128   |     |66.053|
| 4     | 256   |     |53.526|
| 8     | 512   |     |38.311|


### On-Node Architecture Comparison

On-node scaling study for two architectures.

| Cores | C6gn (Aarch64) | C5n (X86) |
|-------|----------------|-----------|
| 1     | 15.7689        | 13.9867   |
| 2     | 498.911        | 407.504   |
| 4     | 932.919        | 951.857   |
| 8     | 476.893        | 544.264   |
| 16    | 184.024        | 204.829   |
| 32    | 85.407         | 86.7813   |
| 64    | 52.2978        | 54.0766   |

## Test Set 2

[ReFrame Benchmark 2](#)

```
reframe -c minixyce_gold_standards.py -r --performance-report -v

```

### Validation

This Test Set contains 63 tests in total.

Test Set 2 aims to ensure functional validity to prevent errors that could arise from flaws in implementing distributed software, as well as compilation bugs due to aggressive compiler optimisation (such as -Ofast)
This test integrates miniXyce's goldStandards benchmarks with 4 different circuits and their corresponding expected results that was provided by this repository.

A sample pass case looks like the following

```
[       OK ] ( 7/63) MiniXyce_short_test_minixyce__nvhpc_21_2_N_1_MPI_1_OMP_1 on aws:c6gn using builtin [compile: 0.006s run: 4.010s total: 261.839s]
==> timings: setup: 0.006s compile: 0.006s run: 4.010s sanity: 0.001s performance: 0.207s total: 261.839s
Output:  5e-06  Goldstandard:  5e-06
Output:  5.0  Goldstandard:  5.0
Output:  4.16666667  Goldstandard:  4.16666667
Output:  3.33333333  Goldstandard:  3.33333333
```

## Optimisation

Details of steps taken to optimise performance of the application.
Please document work with compiler flags, maths libraries, system libraries, code optimisations, etc.

### Compiler Flag Tuning

Compiler flags before:
```
CFLAGS=" "
FFLAGS=" "
```

Compiler flags after:
```
OMP_GNU=-fopenmp
CFLAGS=-Ofast -march=linux-amzn2-graviton2 -funroll-loops -mtune=cortex-a76
CXXFLAGS=-Ofast -march=linux-amzn2-graviton2 -funroll-loops -mtune=cortex-a76
```
or
```
OMP_GNU=-fopenmp
CFLAGS=-O3 -march=linux-amzn2-graviton2 -funroll-loops -mtune=cortex-a76
CXXFLAGS=-O3 -march=linux-amzn2-graviton2 -funroll-loops -mtune=cortex-a76
```
or for nvhpc:
```
OMP_NVHPC=-mp=multicore
FLAGS_NVHPC=-O3 -fast
CFLAGS_NVHPC=-O3 -fast
```

#### Compiler Flag Performance

We didn't observe any significant performance improvement by adding the new flags.

### Maths Library Report

### Maths Library Optimisation

minixyce does not depend on any math libraries.

### Performance Regression

We would really like to get SIMD instruction working with the code base, as there are some matrix operations that can be replaced using compiler intrinsics.
However, due to time constraint we could not get a bug-free version soon enough.

However, we have added some more straightforward optimizations, such as reserving capacity for std::vectors to avoid uncessary copies due to relocation.
The speedup is about 10% (15.5s to 14s). This is done by `spack fetch` followed by `spack stage`, then modify the code inplace and `spack install --dont-restage --keep-stage <miniapp>`\
to install.


## Report

### Compilation Summary

spack allows a fine granularity of managing packages by allowing mix and match of different dependency versions and built by different versions of compilers.\
Each package file has a set of constraints and the concretizer perform algorithms to find a valid set of combinations that satisft all the constraints.\
This definitely has it pros and cons. We appreciate the fact that spack tries to hide all the gruesome work of figuring out dependencies,\
and leave us a fool-proof way to install packages with a few lines of commands. However, there are definitely some catches:

1. As spack tries to hide all the details, it could be sometimes less flexible (at least for inexperience users) to make easy fixes to the build scripts directly.

2. When writing package files, the developer may not be able to take into account of all constraints, leading to incomplete builds that goes unreported.

3. spack tries to load packages by appending to the environment variable, it could lead to a second package environment overriding the path of the former package 

(such as 2 python paths). 

4. The clingo concretizer is undoubtly magical, but our experience is that it could sometimes introduce unnecessary and over-complicated builds, leading to 
an explosion of cached dependencies. In these cases the default concretizer that follows the greedy solution could be more favourable.


### Performance Summary

The empirical observation we have is that the performance trend follows a parabolic trend, with 8-core configuration having the higher overhead, which single-core and multi-core higher than 8 performs increasingly better. This lead us to suspect that mpi introduces more overhead than benefits. As the nature of the application\
performs small but numerous tasks, the overhead of message passing dominates and lead to worsening performance than single-core. \
By using arm-forge toolchain, we profiled the application and observed that MPI synchronization contribute to 94% of the total computation time. This \
suggests that this application is not suitable for mpi application, or can be much better optimized. (In fact, we suspect GPU could be a much better fit for this workload)


### Optimisation Summary

As explained in the previous section, we do not observe much performance benefits in turining on optimisation flags. \
We also did not manage to optimize code base by introducing compiler intrinsics specific to the current architecture. \
Some simple optimizations are made, such as reserving capacity for vectors and observed 10% speedup for large benchmarks, \
as this avoids overhead in relocation.
