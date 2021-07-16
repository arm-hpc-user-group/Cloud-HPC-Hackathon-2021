# CloverLeaf3D 

**Description:** 3D version of the CloverLeaf min-app

**URL:** http://uk-mac.github.io/CloverLeaf3D 

**Team:**  C-unMake

## Compilation

### Spack Package Modification

Default spack recipe is usable. However, optimisation flags is added. See [spack.patch](./spack.patch) and use `git apply spack.patch` for patching and pull request to official spack repo is pending.

Git commit hash of checkout for package: 7880dfd

Pull request for Spack recipe changes: s1913388:optimize_cloverleaf3d

### Building CloverLeaf3D



#### Compiler GCC

```shell
spack install cloverleaf3d@1.0%gcc@10.3.0^openmpi
```

```shell
$ spack spec -Il cloverleaf3d@1.0%gcc@10.3.0^openmpi
Input spec
--------------------------------
 -   cloverleaf3d@1.0%gcc@10.3.0
 -       ^openmpi

Concretized
--------------------------------
 -   edbssk4  cloverleaf3d@1.0%gcc@10.3.0~openacc~opencl arch=linux-amzn2-graviton2
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

#### Compiler ARM

```shell
$ spack install cloverleaf3d@1.0%arm@21.0.0.879^openmpi
```

```shell
$ spack spec -Il cloverleaf3d@1.0%arm@21.0.0.879^openmpi
Input spec
--------------------------------
 -   cloverleaf3d@1.0%arm@21.0.0.879
 -       ^openmpi

Concretized
--------------------------------
 -   k4yeqns  cloverleaf3d@1.0%arm@21.0.0.879~openacc~opencl arch=linux-amzn2-graviton2
 -   huifkle      ^openmpi@4.1.0%arm@21.0.0.879~atomics~cuda~cxx~cxx_exceptions+gpfs~internal-hwloc~java~legacylaunchers~lustre~memchecker+pmi~singularity~sqlite3+static~thread_multiple+vt+wrapper-rpath fabrics=ofi patches=60ce20bc14d98c572ef7883b9fcd254c3f232c2f3a13377480f96466169ac4c8 schedulers=slurm arch=linux-amzn2-graviton2
 -   xsh5tug          ^hwloc@2.5.0%arm@21.0.0.879~cairo~cuda~gl~libudev+libxml2~netloc~nvml+pci+shared arch=linux-amzn2-graviton2
 -   heo5xlh              ^libpciaccess@0.16%arm@21.0.0.879 arch=linux-amzn2-graviton2
 -   xcqslvj                  ^libtool@2.4.6%arm@21.0.0.879 arch=linux-amzn2-graviton2
 -   guhrr3n                      ^m4@1.4.18%arm@21.0.0.879+sigsegv patches=3877ab548f88597ab2327a2230ee048d2d07ace1062efe81fc92e91b7f39cd00,fc9b61654a3ba1a8d6cd78ce087e7c96366c290bc8d2c299f09828d793b853c8 arch=linux-amzn2-graviton2
 -   q27ybb5                          ^libsigsegv@2.13%arm@21.0.0.879 arch=linux-amzn2-graviton2
 -   s6jl232                  ^pkgconf@1.7.4%arm@21.0.0.879 arch=linux-amzn2-graviton2
 -   6eey55q                  ^util-macros@1.19.3%arm@21.0.0.879 arch=linux-amzn2-graviton2
 -   7og6524              ^libxml2@2.9.10%arm@21.0.0.879~python arch=linux-amzn2-graviton2
 -   4fpawwk                  ^libiconv@1.16%arm@21.0.0.879 arch=linux-amzn2-graviton2
 -   3uhexv5                  ^xz@5.2.5%arm@21.0.0.879~pic libs=shared,static arch=linux-amzn2-graviton2
 -   kfhtmo3                  ^zlib@1.2.11%arm@21.0.0.879+optimize+pic+shared arch=linux-amzn2-graviton2
 -   5fshnbc              ^ncurses@6.2%arm@21.0.0.879~symlinks+termlib abi=none arch=linux-amzn2-graviton2
 -   hj5l7x5          ^libevent@2.1.12%arm@21.0.0.879+openssl arch=linux-amzn2-graviton2
 -   b6rhpqo              ^openssl@1.1.1k%arm@21.0.0.879~docs+systemcerts arch=linux-amzn2-graviton2
 -   aoyzxyq                  ^perl@5.32.1%arm@21.0.0.879+cpanm+shared+threads arch=linux-amzn2-graviton2
 -   rd3hv7n                      ^berkeley-db@18.1.40%arm@21.0.0.879+cxx~docs+stl patches=b231fcc4d5cff05e5c3a4814f6a5af0e9a966428dc2176540d2c05aff41de522 arch=linux-amzn2-graviton2
 -   qaavobd                      ^bzip2@1.0.8%arm@21.0.0.879~debug~pic+shared arch=linux-amzn2-graviton2
 -   qchmimy                          ^diffutils@3.7%arm@21.0.0.879 arch=linux-amzn2-graviton2
 -   jbenr5m                      ^gdbm@1.19%arm@21.0.0.879 arch=linux-amzn2-graviton2
 -   7fjq32x                          ^readline@8.1%arm@21.0.0.879 arch=linux-amzn2-graviton2
 -   v75lszn          ^libfabric@1.11.1-aws%arm@21.0.0.879~debug~kdreg fabrics=sockets,tcp,udp arch=linux-amzn2-graviton2
 -   325gh7i          ^numactl@2.0.14%arm@21.0.0.879 patches=4e1d78cbbb85de625bad28705e748856033eaafab92a66dffd383a3d7e00cc94,62fc8a8bf7665a60e8f4c93ebbd535647cebf74198f7afafec4c085a8825c006 arch=linux-amzn2-graviton2
 -   mbkv7qv              ^autoconf@2.69%arm@21.0.0.879 arch=linux-amzn2-graviton2
 -   toijtok              ^automake@1.16.3%arm@21.0.0.879 arch=linux-amzn2-graviton2
 -   7cmi2lb          ^openssh@8.5p1%arm@21.0.0.879 arch=linux-amzn2-graviton2
 -   qytqrqe              ^libedit@3.1-20210216%arm@21.0.0.879 arch=linux-amzn2-graviton2
 -   uxllonc          ^slurm@20-02-4-1%arm@21.0.0.879~gtk~hdf5~hwloc~mariadb~pmix+readline~restd sysconfdir=PREFIX/etc arch=linux-amzn2-graviton2
```

#### Compiler NVHPC

```shell
$ spack install cloverleaf3d@1.0%nvhpc@21.2^openmpi
```

```shell
$ spack spec -Il cloverleaf3d@1.0%nvhpc@21.2^openmpi
Input spec
--------------------------------
 -   cloverleaf3d@1.0%nvhpc@21.2
 -       ^openmpi

Concretized
--------------------------------
 -   fqvfjl3  cloverleaf3d@1.0%nvhpc@21.2~openacc~opencl arch=linux-amzn2-graviton2
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

## Test Case

[ReFrame Benchmark](./cloverleaf_bm8_short_exclusive.py)

```
reframe -c cloverleaf_bm8_short_exclusive.py -r --performance-report
```

### Validation

For simplicity we just check for kinetic energy = 0.2093E+02 ± 0.00005E+02

### ReFrame Output

```
==============================================================================
PERFORMANCE REPORT
------------------------------------------------------------------------------
CloverLeaf3D_BM8_short_cloverleaf3d_1_0__gcc_10_3_0_N_1_MPI_1_OMP_1
- aws:c6gn
   - builtin
      * num_tasks: 1
      * Total Time: 350.75899600982666 s
------------------------------------------------------------------------------
CloverLeaf3D_BM8_short_cloverleaf3d_1_0__gcc_10_3_0_N_1_MPI_2_OMP_1
   - builtin
      * num_tasks: 2
      * Total Time: 229.4602301120758 s
------------------------------------------------------------------------------
CloverLeaf3D_BM8_short_cloverleaf3d_1_0__gcc_10_3_0_N_1_MPI_4_OMP_1
   - builtin
      * num_tasks: 4
      * Total Time: 129.30270504951477 s
------------------------------------------------------------------------------
CloverLeaf3D_BM8_short_cloverleaf3d_1_0__gcc_10_3_0_N_1_MPI_8_OMP_1
   - builtin
      * num_tasks: 8
      * Total Time: 82.30532383918762 s
------------------------------------------------------------------------------
CloverLeaf3D_BM8_short_cloverleaf3d_1_0__gcc_10_3_0_N_1_MPI_16_OMP_1
   - builtin
      * num_tasks: 16
      * Total Time: 57.14682698249817 s
------------------------------------------------------------------------------
CloverLeaf3D_BM8_short_cloverleaf3d_1_0__gcc_10_3_0_N_1_MPI_32_OMP_1
   - builtin
      * num_tasks: 32
      * Total Time: 34.57797288894653 s
------------------------------------------------------------------------------
CloverLeaf3D_BM8_short_cloverleaf3d_1_0__gcc_10_3_0_N_2_MPI_64_OMP_1
   - builtin
      * num_tasks: 64
      * Total Time: 16.07563591003418 s
------------------------------------------------------------------------------
CloverLeaf3D_BM8_short_cloverleaf3d_1_0__gcc_10_3_0_N_4_MPI_128_OMP_1
   - builtin
      * num_tasks: 128
      * Total Time: 11.487725019454956 s
------------------------------------------------------------------------------
CloverLeaf3D_BM8_short_cloverleaf3d_1_0__gcc_10_3_0_N_8_MPI_256_OMP_1
   - builtin
      * num_tasks: 256
      * Total Time: 4.155719041824341 s
------------------------------------------------------------------------------
CloverLeaf3D_BM8_short_cloverleaf3d_1_0__arm_21_0_0_879_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Total Time: 295.5387468338013 s
------------------------------------------------------------------------------
CloverLeaf3D_BM8_short_cloverleaf3d_1_0__arm_21_0_0_879_N_1_MPI_2_OMP_1
   - builtin
      * num_tasks: 2
      * Total Time: 166.374351978302 s
------------------------------------------------------------------------------
CloverLeaf3D_BM8_short_cloverleaf3d_1_0__arm_21_0_0_879_N_1_MPI_4_OMP_1
   - builtin
      * num_tasks: 4
      * Total Time: 103.238508939743 s
------------------------------------------------------------------------------
CloverLeaf3D_BM8_short_cloverleaf3d_1_0__arm_21_0_0_879_N_1_MPI_8_OMP_1
   - builtin
      * num_tasks: 8
      * Total Time: 62.71004486083984 s
------------------------------------------------------------------------------
CloverLeaf3D_BM8_short_cloverleaf3d_1_0__arm_21_0_0_879_N_1_MPI_16_OMP_1
   - builtin
      * num_tasks: 16
      * Total Time: 34.35910415649414 s
------------------------------------------------------------------------------
CloverLeaf3D_BM8_short_cloverleaf3d_1_0__arm_21_0_0_879_N_1_MPI_32_OMP_1
   - builtin
      * num_tasks: 32
      * Total Time: 19.40960788726807 s
------------------------------------------------------------------------------
CloverLeaf3D_BM8_short_cloverleaf3d_1_0__arm_21_0_0_879_N_2_MPI_64_OMP_1
   - builtin
      * num_tasks: 64
      * Total Time: 10.79916596412659 s
------------------------------------------------------------------------------
CloverLeaf3D_BM8_short_cloverleaf3d_1_0__arm_21_0_0_879_N_4_MPI_128_OMP_1
   - builtin
      * num_tasks: 128
      * Total Time: 5.783955097198486 s
------------------------------------------------------------------------------
CloverLeaf3D_BM8_short_cloverleaf3d_1_0__arm_21_0_0_879_N_8_MPI_256_OMP_1
   - builtin
      * num_tasks: 256
      * Total Time: 4.773585081100464 s
------------------------------------------------------------------------------
CloverLeaf3D_BM8_short_cloverleaf3d_1_0__nvhpc_21_2_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Total Time: 297.7256031036377 s
------------------------------------------------------------------------------
CloverLeaf3D_BM8_short_cloverleaf3d_1_0__nvhpc_21_2_N_1_MPI_2_OMP_1
   - builtin
      * num_tasks: 2
      * Total Time: 149.6047248840332 s
------------------------------------------------------------------------------
CloverLeaf3D_BM8_short_cloverleaf3d_1_0__nvhpc_21_2_N_1_MPI_4_OMP_1
   - builtin
      * num_tasks: 4
      * Total Time: 85.92013812065125 s
------------------------------------------------------------------------------
CloverLeaf3D_BM8_short_cloverleaf3d_1_0__nvhpc_21_2_N_1_MPI_8_OMP_1
   - builtin
      * num_tasks: 8
      * Total Time: 52.82903790473938 s
------------------------------------------------------------------------------
CloverLeaf3D_BM8_short_cloverleaf3d_1_0__nvhpc_21_2_N_1_MPI_16_OMP_1
   - builtin
      * num_tasks: 16
      * Total Time: 35.01609706878662 s
------------------------------------------------------------------------------
CloverLeaf3D_BM8_short_cloverleaf3d_1_0__nvhpc_21_2_N_1_MPI_32_OMP_1
   - builtin
      * num_tasks: 32
      * Total Time: 20.02013897895813 s
------------------------------------------------------------------------------
CloverLeaf3D_BM8_short_cloverleaf3d_1_0__nvhpc_21_2_N_2_MPI_64_OMP_1
   - builtin
      * num_tasks: 64
      * Total Time: 14.73618578910828 s
------------------------------------------------------------------------------
CloverLeaf3D_BM8_short_cloverleaf3d_1_0__nvhpc_21_2_N_4_MPI_128_OMP_1
   - builtin
      * num_tasks: 128
      * Total Time: 5.879961013793945 s
------------------------------------------------------------------------------
CloverLeaf3D_BM8_short_cloverleaf3d_1_0__nvhpc_21_2_N_8_MPI_256_OMP_1
   - builtin
      * num_tasks: 256
      * Total Time: 6.758138179779053 s
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

See [spack.patch](./spack.patch) and use `git apply spack.patch` for patching and pull request to official spack repo is pending.

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
