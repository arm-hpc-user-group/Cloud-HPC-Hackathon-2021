# tinker 

**Description:** The Tinker molecular modeling software is a complete and general package for molecular mechanics and dynamics, with some special features for biopolymers.

**URL:** https://dasher.wustl.edu/tinker/

**Team:** dogecointothemoon

Tinker combines lost of some executable file, due to time limit, we only gave one test case of the `dynamic ice`. The Tinker is supported by the OpenMP, but the default version in Spack doesn't support that. So, we spent a lot of time on finding how to add the OpenMP to the spack package, and we made it finally! The program will run about **4 time faster with 8 threads**. We think it is a very impressive result, and maybe can be merged into the spack.

## Compilation

### Spack Package Modification

Adding OpenMP support to tinker is tricky, as what the original package did is using a patch file of cmake. And we patched the patch file to add the openmp support.

+
diff --git a/var/spack/repos/builtin/packages/tinker/tinker-8.7.1-cmake.patch b/var/spack/repos/builtin/packages/tinker/tinker-8.7.1-cmake.patch
index e07d05a7dc..96747a9bf1 100644
--- a/var/spack/repos/builtin/packages/tinker/tinker-8.7.1-cmake.patch
+++ b/var/spack/repos/builtin/packages/tinker/tinker-8.7.1-cmake.patch
@@ -1,19 +1,9 @@
-From c31e54353cf587c83c823544849226840fdb26da Mon Sep 17 00:00:00 2001
-From: Christoph Junghans <junghans@votca.org>
-Date: Sat, 23 Nov 2019 19:40:58 -0700
-Subject: [PATCH] add initial version of CMake build system
-
----
- source/CMakeLists.txt | 94 +++++++++++++++++++++++++++++++++++++++++++
- 1 file changed, 94 insertions(+)
- create mode 100644 source/CMakeLists.txt
-
 diff --git a/source/CMakeLists.txt b/source/CMakeLists.txt
 new file mode 100644
-index 0000000..c1f9831
+index 00000000..830c3e2b
 --- /dev/null
 +++ b/source/CMakeLists.txt
-@@ -0,0 +1,94 @@
+@@ -0,0 +1,99 @@
 +cmake_minimum_required(VERSION 3.10)
 +
 +project(tinker VERSION 8.7.1 LANGUAGES Fortran)
@@ -22,7 +12,11 @@ index 0000000..c1f9831
 +find_package(PkgConfig REQUIRED)
 +pkg_check_modules(FFTW3 REQUIRED IMPORTED_TARGET fftw3)
 +
-+add_library(tinker
++find_package(OpenMP)
++set(CMAKE_Fortran_FLAGS "${CMAKE_Fortran_FLAGS} -fopenmp")
++
++
++add_library(tinker
 +            action.f active.f align.f analysis.f analyz.f angang.f angbnd.f
 +            angles.f angpot.f angtor.f argue.f ascii.f atmlst.f atomid.f atoms.f
 +            attach.f baoab.f basefile.f bath.f beeman.f bicubic.f bitor.f bitors.f
@@ -105,9 +99,7 @@ index 0000000..c1f9831
 +        testpol testrot testvir timer timerot torsfit valence vibbig
 +        vibrate vibrot xtalfit xtalmin xyzedit xyzint xyzmol2 xyzpdb)
 +        add_executable(${_BIN}.x ${_BIN}.f)
-+        target_link_libraries(${_BIN}.x tinker PkgConfig::FFTW3)
++        target_link_libraries(${_BIN}.x tinker PkgConfig::FFTW3 OpenMP::OpenMP_Fortran m fftw3_omp)
 +        install(TARGETS ${_BIN}.x DESTINATION ${CMAKE_INSTALL_BINDIR})
 +endforeach()
---
-2.23.0
-

the git commit hash for Spack is HEAD(64f31c4)

### Building tinker

We must built the fftw(enabled with OpenMP) first if we want to parallize the tinker, as tinker depends on fftw.

#### GCC

```
$ spack install fftw%gcc10.3.0+openmp
```

You can see below now the fftw is `+mpi+openmp` while the original version is `+mpi~openmp`

```
$ spack spec -Il fftw/edegbs3
[+]  fftw@3.3.9%gcc@10.3.0+mpi+openmp~pfft_patches precision=double,float arch=linux-amzn2-graviton2
[+]      ^openmpi@4.1.0%gcc@10.3.0~atomics~cuda~cxx~cxx_exceptions+gpfs~internal-hwloc~java~legacylaunchers~lustre~memchecker+pmi~singularity~sqlite3+static~thread_multiple+vt+wrapper-rpath fabrics=ofi patches=60ce20bc14d98c572ef7883b9fcd254c3f232c2f3a13377480f96466169ac4c8 schedulers=slurm arch=linux-amzn2-graviton2
[+]          ^hwloc@2.5.0%gcc@10.3.0~cairo~cuda~gl~libudev+libxml2~netloc~nvml+pci+shared arch=linux-amzn2-graviton2
[+]              ^libpciaccess@0.16%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]              ^libxml2@2.9.10%gcc@10.3.0~python arch=linux-amzn2-graviton2
[+]                  ^libiconv@1.16%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]                  ^xz@5.2.5%gcc@10.3.0~pic libs=shared,static arch=linux-amzn2-graviton2
[+]                  ^zlib@1.2.11%gcc@10.3.0+optimize+pic+shared arch=linux-amzn2-graviton2
[+]              ^ncurses@6.2%gcc@10.3.0~symlinks+termlib abi=none arch=linux-amzn2-graviton2
[+]          ^libevent@2.1.12%gcc@10.3.0+openssl arch=linux-amzn2-graviton2
[+]              ^openssl@1.1.1k%gcc@10.3.0~docs+systemcerts arch=linux-amzn2-graviton2
[+]          ^libfabric@1.11.1-aws%gcc@10.3.0~debug~kdreg fabrics=sockets,tcp,udp arch=linux-amzn2-graviton2
[+]          ^numactl@2.0.14%gcc@10.3.0 patches=4e1d78cbbb85de625bad28705e748856033eaafab92a66dffd383a3d7e00cc94,62fc8a8bf7665a60e8f4c93ebbd535647cebf74198f7afafec4c085a8825c006 arch=linux-amzn2-graviton2
[+]          ^openssh@8.5p1%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]              ^libedit@3.1-20210216%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]          ^slurm@20-02-4-1%gcc@10.3.0~gtk~hdf5~hwloc~mariadb~pmix+readline~restd sysconfdir=PREFIX/etc arch=linux-amzn2-graviton2

Concretized
--------------------------------
[+]  edegbs3  fftw@3.3.9%gcc@10.3.0+mpi+openmp~pfft_patches precision=double,float arch=linux-amzn2-graviton2
[+]  zvamksn      ^openmpi@4.1.0%gcc@10.3.0~atomics~cuda~cxx~cxx_exceptions+gpfs~internal-hwloc~java~legacylaunchers~lustre~memchecker+pmi~singularity~sqlite3+static~thread_multiple+vt+wrapper-rpath fabrics=ofi patches=60ce20bc14d98c572ef7883b9fcd254c3f232c2f3a13377480f96466169ac4c8 schedulers=slurm arch=linux-amzn2-graviton2
[+]  cukmqbg          ^hwloc@2.5.0%gcc@10.3.0~cairo~cuda~gl~libudev+libxml2~netloc~nvml+pci+shared arch=linux-amzn2-graviton2
[+]  asgtk6a              ^libpciaccess@0.16%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  iyhm3wi              ^libxml2@2.9.10%gcc@10.3.0~python arch=linux-amzn2-graviton2
[+]  y5ei3cm                  ^libiconv@1.16%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  ye3kcvv                  ^xz@5.2.5%gcc@10.3.0~pic libs=shared,static arch=linux-amzn2-graviton2
[+]  qepjcvj                  ^zlib@1.2.11%gcc@10.3.0+optimize+pic+shared arch=linux-amzn2-graviton2
[+]  iwzirqc              ^ncurses@6.2%gcc@10.3.0~symlinks+termlib abi=none arch=linux-amzn2-graviton2
[+]  tadxrfp          ^libevent@2.1.12%gcc@10.3.0+openssl arch=linux-amzn2-graviton2
[+]  5i3lgfb              ^openssl@1.1.1k%gcc@10.3.0~docs+systemcerts arch=linux-amzn2-graviton2
[+]  72f5gvk          ^libfabric@1.11.1-aws%gcc@10.3.0~debug~kdreg fabrics=sockets,tcp,udp arch=linux-amzn2-graviton2
[+]  mhav5gn          ^numactl@2.0.14%gcc@10.3.0 patches=4e1d78cbbb85de625bad28705e748856033eaafab92a66dffd383a3d7e00cc94,62fc8a8bf7665a60e8f4c93ebbd535647cebf74198f7afafec4c085a8825c006 arch=linux-amzn2-graviton2
[+]  wturp6c          ^openssh@8.5p1%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  ivotdt7              ^libedit@3.1-20210216%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  wqpuvmh          ^slurm@20-02-4-1%gcc@10.3.0~gtk~hdf5~hwloc~mariadb~pmix+readline~restd sysconfdir=PREFIX/etc arch=linux-amzn2-graviton2
```

``` $ spack install tinker%gcc/dqija4h ```

``` $ spack spec -Il tinker%gcc/dqija4h 

[+]  tinker@8.7.1%gcc@10.3.0~ipo build_type=RelWithDebInfo patches=9121550598380fcac2929b9e0530c52ffd3466ff05654e80dbaa46b92566ac86 arch=linux-amzn2-graviton2
[+]      ^fftw@3.3.9%gcc@10.3.0+mpi+openmp~pfft_patches precision=double,float arch=linux-amzn2-graviton2
[+]          ^openmpi@4.1.0%gcc@10.3.0~atomics~cuda~cxx~cxx_exceptions+gpfs~internal-hwloc~java~legacylaunchers~lustre~memchecker+pmi~singularity~sqlite3+static~thread_multiple+vt+wrapper-rpath fabrics=ofi patches=60ce20bc14d98c572ef7883b9fcd254c3f232c2f3a13377480f96466169ac4c8 schedulers=slurm arch=linux-amzn2-graviton2
[+]              ^hwloc@2.5.0%gcc@10.3.0~cairo~cuda~gl~libudev+libxml2~netloc~nvml+pci+shared arch=linux-amzn2-graviton2
[+]                  ^libpciaccess@0.16%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]                  ^libxml2@2.9.10%gcc@10.3.0~python arch=linux-amzn2-graviton2
[+]                      ^libiconv@1.16%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]                      ^xz@5.2.5%gcc@10.3.0~pic libs=shared,static arch=linux-amzn2-graviton2
[+]                      ^zlib@1.2.11%gcc@10.3.0+optimize+pic+shared arch=linux-amzn2-graviton2
[+]                  ^ncurses@6.2%gcc@10.3.0~symlinks+termlib abi=none arch=linux-amzn2-graviton2
[+]              ^libevent@2.1.12%gcc@10.3.0+openssl arch=linux-amzn2-graviton2
[+]                  ^openssl@1.1.1k%gcc@10.3.0~docs+systemcerts arch=linux-amzn2-graviton2
[+]              ^libfabric@1.11.1-aws%gcc@10.3.0~debug~kdreg fabrics=sockets,tcp,udp arch=linux-amzn2-graviton2
[+]              ^numactl@2.0.14%gcc@10.3.0 patches=4e1d78cbbb85de625bad28705e748856033eaafab92a66dffd383a3d7e00cc94,62fc8a8bf7665a60e8f4c93ebbd535647cebf74198f7afafec4c085a8825c006 arch=linux-amzn2-graviton2
[+]              ^openssh@8.5p1%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]                  ^libedit@3.1-20210216%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]              ^slurm@20-02-4-1%gcc@10.3.0~gtk~hdf5~hwloc~mariadb~pmix+readline~restd sysconfdir=PREFIX/etc arch=linux-amzn2-graviton2

Concretized
--------------------------------
[+]  dqija4h  tinker@8.7.1%gcc@10.3.0~ipo build_type=RelWithDebInfo patches=9121550598380fcac2929b9e0530c52ffd3466ff05654e80dbaa46b92566ac86 arch=linux-amzn2-graviton2
[+]  edegbs3      ^fftw@3.3.9%gcc@10.3.0+mpi+openmp~pfft_patches precision=double,float arch=linux-amzn2-graviton2
[+]  zvamksn          ^openmpi@4.1.0%gcc@10.3.0~atomics~cuda~cxx~cxx_exceptions+gpfs~internal-hwloc~java~legacylaunchers~lustre~memchecker+pmi~singularity~sqlite3+static~thread_multiple+vt+wrapper-rpath fabrics=ofi patches=60ce20bc14d98c572ef7883b9fcd254c3f232c2f3a13377480f96466169ac4c8 schedulers=slurm arch=linux-amzn2-graviton2
[+]  cukmqbg              ^hwloc@2.5.0%gcc@10.3.0~cairo~cuda~gl~libudev+libxml2~netloc~nvml+pci+shared arch=linux-amzn2-graviton2
[+]  asgtk6a                  ^libpciaccess@0.16%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  iyhm3wi                  ^libxml2@2.9.10%gcc@10.3.0~python arch=linux-amzn2-graviton2
[+]  y5ei3cm                      ^libiconv@1.16%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  ye3kcvv                      ^xz@5.2.5%gcc@10.3.0~pic libs=shared,static arch=linux-amzn2-graviton2
[+]  qepjcvj                      ^zlib@1.2.11%gcc@10.3.0+optimize+pic+shared arch=linux-amzn2-graviton2
[+]  iwzirqc                  ^ncurses@6.2%gcc@10.3.0~symlinks+termlib abi=none arch=linux-amzn2-graviton2
[+]  tadxrfp              ^libevent@2.1.12%gcc@10.3.0+openssl arch=linux-amzn2-graviton2
[+]  5i3lgfb                  ^openssl@1.1.1k%gcc@10.3.0~docs+systemcerts arch=linux-amzn2-graviton2
[+]  72f5gvk              ^libfabric@1.11.1-aws%gcc@10.3.0~debug~kdreg fabrics=sockets,tcp,udp arch=linux-amzn2-graviton2
[+]  mhav5gn              ^numactl@2.0.14%gcc@10.3.0 patches=4e1d78cbbb85de625bad28705e748856033eaafab92a66dffd383a3d7e00cc94,62fc8a8bf7665a60e8f4c93ebbd535647cebf74198f7afafec4c085a8825c006 arch=linux-amzn2-graviton2
[+]  wturp6c              ^openssh@8.5p1%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  ivotdt7                  ^libedit@3.1-20210216%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  wqpuvmh              ^slurm@20-02-4-1%gcc@10.3.0~gtk~hdf5~hwloc~mariadb~pmix+readline~restd sysconfdir=PREFIX/etc arch=linux-amzn2-graviton2

```

#### ARM

``` spack install fftw%arm+openmp ```

``` spack spec -Il fftw%arm/mnfafv2 
[+]  fftw@3.3.9%arm@21.0.0.879+mpi+openmp~pfft_patches precision=double,float arch=linux-amzn2-aarch64
[+]      ^openmpi@4.1.0%arm@21.0.0.879~atomics~cuda~cxx~cxx_exceptions+gpfs~internal-hwloc~java~legacylaunchers~lustre~memchecker+pmi~singularity~sqlite3+static~thread_multiple+vt+wrapper-rpath fabrics=ofi patches=60ce20bc14d98c572ef7883b9fcd254c3f232c2f3a13377480f96466169ac4c8 schedulers=slurm arch=linux-amzn2-aarch64
[+]          ^hwloc@2.5.0%arm@21.0.0.879~cairo~cuda~gl~libudev+libxml2~netloc~nvml+pci+shared arch=linux-amzn2-aarch64
[+]              ^libpciaccess@0.16%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]              ^libxml2@2.9.10%arm@21.0.0.879~python arch=linux-amzn2-aarch64
[+]                  ^libiconv@1.16%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]                  ^xz@5.2.5%arm@21.0.0.879~pic libs=shared,static arch=linux-amzn2-aarch64
[+]                  ^zlib@1.2.11%arm@21.0.0.879+optimize+pic+shared arch=linux-amzn2-aarch64
[+]              ^ncurses@6.2%arm@21.0.0.879~symlinks+termlib abi=none arch=linux-amzn2-aarch64
[+]          ^libevent@2.1.12%arm@21.0.0.879+openssl arch=linux-amzn2-aarch64
[+]              ^openssl@1.1.1k%arm@21.0.0.879~docs+systemcerts arch=linux-amzn2-aarch64
[+]          ^libfabric@1.11.1-aws%arm@21.0.0.879~debug~kdreg fabrics=sockets,tcp,udp arch=linux-amzn2-aarch64
[+]          ^numactl@2.0.14%arm@21.0.0.879 patches=4e1d78cbbb85de625bad28705e748856033eaafab92a66dffd383a3d7e00cc94,62fc8a8bf7665a60e8f4c93ebbd535647cebf74198f7afafec4c085a8825c006 arch=linux-amzn2-aarch64
[+]          ^openssh@8.5p1%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]              ^libedit@3.1-20210216%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]          ^slurm@20-02-4-1%arm@21.0.0.879~gtk~hdf5~hwloc~mariadb~pmix+readline~restd sysconfdir=PREFIX/etc arch=linux-amzn2-aarch64

Concretized
--------------------------------
[+]  mnfafv2  fftw@3.3.9%arm@21.0.0.879+mpi+openmp~pfft_patches precision=double,float arch=linux-amzn2-aarch64
[+]  lmaoy5t      ^openmpi@4.1.0%arm@21.0.0.879~atomics~cuda~cxx~cxx_exceptions+gpfs~internal-hwloc~java~legacylaunchers~lustre~memchecker+pmi~singularity~sqlite3+static~thread_multiple+vt+wrapper-rpath fabrics=ofi patches=60ce20bc14d98c572ef7883b9fcd254c3f232c2f3a13377480f96466169ac4c8 schedulers=slurm arch=linux-amzn2-aarch64
[+]  xl6anaa          ^hwloc@2.5.0%arm@21.0.0.879~cairo~cuda~gl~libudev+libxml2~netloc~nvml+pci+shared arch=linux-amzn2-aarch64
[+]  jueqz7p              ^libpciaccess@0.16%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  dypqz2i              ^libxml2@2.9.10%arm@21.0.0.879~python arch=linux-amzn2-aarch64
[+]  7vnthzn                  ^libiconv@1.16%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  zqsab4f                  ^xz@5.2.5%arm@21.0.0.879~pic libs=shared,static arch=linux-amzn2-aarch64
[+]  puuxvg2                  ^zlib@1.2.11%arm@21.0.0.879+optimize+pic+shared arch=linux-amzn2-aarch64
[+]  uhtqtlb              ^ncurses@6.2%arm@21.0.0.879~symlinks+termlib abi=none arch=linux-amzn2-aarch64
[+]  gonqskn          ^libevent@2.1.12%arm@21.0.0.879+openssl arch=linux-amzn2-aarch64
[+]  vc3waha              ^openssl@1.1.1k%arm@21.0.0.879~docs+systemcerts arch=linux-amzn2-aarch64
[+]  qdn27nh          ^libfabric@1.11.1-aws%arm@21.0.0.879~debug~kdreg fabrics=sockets,tcp,udp arch=linux-amzn2-aarch64
[+]  mv2g7r5          ^numactl@2.0.14%arm@21.0.0.879 patches=4e1d78cbbb85de625bad28705e748856033eaafab92a66dffd383a3d7e00cc94,62fc8a8bf7665a60e8f4c93ebbd535647cebf74198f7afafec4c085a8825c006 arch=linux-amzn2-aarch64
[+]  6vvthuo          ^openssh@8.5p1%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  xe4evc4              ^libedit@3.1-20210216%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  x5xehti          ^slurm@20-02-4-1%arm@21.0.0.879~gtk~hdf5~hwloc~mariadb~pmix+readline~restd sysconfdir=PREFIX/etc arch=linux-amzn2-aarch64
```

```spack install tinker%arm ^fftw/mnfafv2```

``` spack spec -Il tinker%arm/ynitub 
[+]  tinker@8.7.1%arm@21.0.0.879~ipo build_type=RelWithDebInfo patches=9121550598380fcac2929b9e0530c52ffd3466ff05654e80dbaa46b92566ac86 arch=linux-amzn2-aarch64
[+]      ^fftw@3.3.9%arm@21.0.0.879+mpi+openmp~pfft_patches precision=double,float arch=linux-amzn2-aarch64
[+]          ^openmpi@4.1.0%arm@21.0.0.879~atomics~cuda~cxx~cxx_exceptions+gpfs~internal-hwloc~java~legacylaunchers~lustre~memchecker+pmi~singularity~sqlite3+static~thread_multiple+vt+wrapper-rpath fabrics=ofi patches=60ce20bc14d98c572ef7883b9fcd254c3f232c2f3a13377480f96466169ac4c8 schedulers=slurm arch=linux-amzn2-aarch64
[+]              ^hwloc@2.5.0%arm@21.0.0.879~cairo~cuda~gl~libudev+libxml2~netloc~nvml+pci+shared arch=linux-amzn2-aarch64
[+]                  ^libpciaccess@0.16%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]                  ^libxml2@2.9.10%arm@21.0.0.879~python arch=linux-amzn2-aarch64
[+]                      ^libiconv@1.16%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]                      ^xz@5.2.5%arm@21.0.0.879~pic libs=shared,static arch=linux-amzn2-aarch64
[+]                      ^zlib@1.2.11%arm@21.0.0.879+optimize+pic+shared arch=linux-amzn2-aarch64
[+]                  ^ncurses@6.2%arm@21.0.0.879~symlinks+termlib abi=none arch=linux-amzn2-aarch64
[+]              ^libevent@2.1.12%arm@21.0.0.879+openssl arch=linux-amzn2-aarch64
[+]                  ^openssl@1.1.1k%arm@21.0.0.879~docs+systemcerts arch=linux-amzn2-aarch64
[+]              ^libfabric@1.11.1-aws%arm@21.0.0.879~debug~kdreg fabrics=sockets,tcp,udp arch=linux-amzn2-aarch64
[+]              ^numactl@2.0.14%arm@21.0.0.879 patches=4e1d78cbbb85de625bad28705e748856033eaafab92a66dffd383a3d7e00cc94,62fc8a8bf7665a60e8f4c93ebbd535647cebf74198f7afafec4c085a8825c006 arch=linux-amzn2-aarch64
[+]              ^openssh@8.5p1%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]                  ^libedit@3.1-20210216%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]              ^slurm@20-02-4-1%arm@21.0.0.879~gtk~hdf5~hwloc~mariadb~pmix+readline~restd sysconfdir=PREFIX/etc arch=linux-amzn2-aarch64

Concretized
--------------------------------
[+]  ynitubh  tinker@8.7.1%arm@21.0.0.879~ipo build_type=RelWithDebInfo patches=9121550598380fcac2929b9e0530c52ffd3466ff05654e80dbaa46b92566ac86 arch=linux-amzn2-aarch64
[+]  mnfafv2      ^fftw@3.3.9%arm@21.0.0.879+mpi+openmp~pfft_patches precision=double,float arch=linux-amzn2-aarch64
[+]  lmaoy5t          ^openmpi@4.1.0%arm@21.0.0.879~atomics~cuda~cxx~cxx_exceptions+gpfs~internal-hwloc~java~legacylaunchers~lustre~memchecker+pmi~singularity~sqlite3+static~thread_multiple+vt+wrapper-rpath fabrics=ofi patches=60ce20bc14d98c572ef7883b9fcd254c3f232c2f3a13377480f96466169ac4c8 schedulers=slurm arch=linux-amzn2-aarch64
[+]  xl6anaa              ^hwloc@2.5.0%arm@21.0.0.879~cairo~cuda~gl~libudev+libxml2~netloc~nvml+pci+shared arch=linux-amzn2-aarch64
[+]  jueqz7p                  ^libpciaccess@0.16%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  dypqz2i                  ^libxml2@2.9.10%arm@21.0.0.879~python arch=linux-amzn2-aarch64
[+]  7vnthzn                      ^libiconv@1.16%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  zqsab4f                      ^xz@5.2.5%arm@21.0.0.879~pic libs=shared,static arch=linux-amzn2-aarch64
[+]  puuxvg2                      ^zlib@1.2.11%arm@21.0.0.879+optimize+pic+shared arch=linux-amzn2-aarch64
[+]  uhtqtlb                  ^ncurses@6.2%arm@21.0.0.879~symlinks+termlib abi=none arch=linux-amzn2-aarch64
[+]  gonqskn              ^libevent@2.1.12%arm@21.0.0.879+openssl arch=linux-amzn2-aarch64
[+]  vc3waha                  ^openssl@1.1.1k%arm@21.0.0.879~docs+systemcerts arch=linux-amzn2-aarch64
[+]  qdn27nh              ^libfabric@1.11.1-aws%arm@21.0.0.879~debug~kdreg fabrics=sockets,tcp,udp arch=linux-amzn2-aarch64
[+]  mv2g7r5              ^numactl@2.0.14%arm@21.0.0.879 patches=4e1d78cbbb85de625bad28705e748856033eaafab92a66dffd383a3d7e00cc94,62fc8a8bf7665a60e8f4c93ebbd535647cebf74198f7afafec4c085a8825c006 arch=linux-amzn2-aarch64
[+]  6vvthuo              ^openssh@8.5p1%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  xe4evc4                  ^libedit@3.1-20210216%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  x5xehti              ^slurm@20-02-4-1%arm@21.0.0.879~gtk~hdf5~hwloc~mariadb~pmix+readline~restd sysconfdir=PREFIX/etc arch=linux-amzn2-aarch64

```

####NVHPC

nvhpc doens't has the variant openmpi, so we used gcc(enabled openmp) version of the fftw.

``` spack install tinker%nvhpc ^cmake%gcc ^fftw/edegbs3 ```

``` spack spec -Il tinker/qszz7b5 ```

[+]  tinker@8.7.1%nvhpc@21.2~ipo build_type=RelWithDebInfo patches=9121550598380fcac2929b9e0530c52ffd3466ff05654e80dbaa46b92566ac86 arch=linux-amzn2-graviton2
[+]      ^fftw@3.3.9%gcc@10.3.0+mpi+openmp~pfft_patches precision=double,float arch=linux-amzn2-graviton2
[+]          ^openmpi@4.1.0%gcc@10.3.0~atomics~cuda~cxx~cxx_exceptions+gpfs~internal-hwloc~java~legacylaunchers~lustre~memchecker+pmi~singularity~sqlite3+static~thread_multiple+vt+wrapper-rpath fabrics=ofi patches=60ce20bc14d98c572ef7883b9fcd254c3f232c2f3a13377480f96466169ac4c8 schedulers=slurm arch=linux-amzn2-graviton2
[+]              ^hwloc@2.5.0%gcc@10.3.0~cairo~cuda~gl~libudev+libxml2~netloc~nvml+pci+shared arch=linux-amzn2-graviton2
[+]                  ^libpciaccess@0.16%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]                  ^libxml2@2.9.10%gcc@10.3.0~python arch=linux-amzn2-graviton2
[+]                      ^libiconv@1.16%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]                      ^xz@5.2.5%gcc@10.3.0~pic libs=shared,static arch=linux-amzn2-graviton2
[+]                      ^zlib@1.2.11%gcc@10.3.0+optimize+pic+shared arch=linux-amzn2-graviton2
[+]                  ^ncurses@6.2%gcc@10.3.0~symlinks+termlib abi=none arch=linux-amzn2-graviton2
[+]              ^libevent@2.1.12%gcc@10.3.0+openssl arch=linux-amzn2-graviton2
[+]                  ^openssl@1.1.1k%gcc@10.3.0~docs+systemcerts arch=linux-amzn2-graviton2
[+]              ^libfabric@1.11.1-aws%gcc@10.3.0~debug~kdreg fabrics=sockets,tcp,udp arch=linux-amzn2-graviton2
[+]              ^numactl@2.0.14%gcc@10.3.0 patches=4e1d78cbbb85de625bad28705e748856033eaafab92a66dffd383a3d7e00cc94,62fc8a8bf7665a60e8f4c93ebbd535647cebf74198f7afafec4c085a8825c006 arch=linux-amzn2-graviton2
[+]              ^openssh@8.5p1%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]                  ^libedit@3.1-20210216%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]              ^slurm@20-02-4-1%gcc@10.3.0~gtk~hdf5~hwloc~mariadb~pmix+readline~restd sysconfdir=PREFIX/etc arch=linux-amzn2-graviton2

Concretized
--------------------------------
[+]  qszz7b5  tinker@8.7.1%nvhpc@21.2~ipo build_type=RelWithDebInfo patches=9121550598380fcac2929b9e0530c52ffd3466ff05654e80dbaa46b92566ac86 arch=linux-amzn2-graviton2
[+]  edegbs3      ^fftw@3.3.9%gcc@10.3.0+mpi+openmp~pfft_patches precision=double,float arch=linux-amzn2-graviton2
[+]  zvamksn          ^openmpi@4.1.0%gcc@10.3.0~atomics~cuda~cxx~cxx_exceptions+gpfs~internal-hwloc~java~legacylaunchers~lustre~memchecker+pmi~singularity~sqlite3+static~thread_multiple+vt+wrapper-rpath fabrics=ofi patches=60ce20bc14d98c572ef7883b9fcd254c3f232c2f3a13377480f96466169ac4c8 schedulers=slurm arch=linux-amzn2-graviton2
[+]  cukmqbg              ^hwloc@2.5.0%gcc@10.3.0~cairo~cuda~gl~libudev+libxml2~netloc~nvml+pci+shared arch=linux-amzn2-graviton2
[+]  asgtk6a                  ^libpciaccess@0.16%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  iyhm3wi                  ^libxml2@2.9.10%gcc@10.3.0~python arch=linux-amzn2-graviton2
[+]  y5ei3cm                      ^libiconv@1.16%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  ye3kcvv                      ^xz@5.2.5%gcc@10.3.0~pic libs=shared,static arch=linux-amzn2-graviton2
[+]  qepjcvj                      ^zlib@1.2.11%gcc@10.3.0+optimize+pic+shared arch=linux-amzn2-graviton2
[+]  iwzirqc                  ^ncurses@6.2%gcc@10.3.0~symlinks+termlib abi=none arch=linux-amzn2-graviton2
[+]  tadxrfp              ^libevent@2.1.12%gcc@10.3.0+openssl arch=linux-amzn2-graviton2
[+]  5i3lgfb                  ^openssl@1.1.1k%gcc@10.3.0~docs+systemcerts arch=linux-amzn2-graviton2
[+]  72f5gvk              ^libfabric@1.11.1-aws%gcc@10.3.0~debug~kdreg fabrics=sockets,tcp,udp arch=linux-amzn2-graviton2
[+]  mhav5gn              ^numactl@2.0.14%gcc@10.3.0 patches=4e1d78cbbb85de625bad28705e748856033eaafab92a66dffd383a3d7e00cc94,62fc8a8bf7665a60e8f4c93ebbd535647cebf74198f7afafec4c085a8825c006 arch=linux-amzn2-graviton2
[+]  wturp6c              ^openssh@8.5p1%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  ivotdt7                  ^libedit@3.1-20210216%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  wqpuvmh              ^slurm@20-02-4-1%gcc@10.3.0~gtk~hdf5~hwloc~mariadb~pmix+readline~restd sysconfdir=PREFIX/etc arch=linux-amzn2-graviton2

```

## Ice test

```
reframe --stage /scratch/home/${USER} -v -c test_ice.py -r --performance-report
```

### ReFrame Output

```
tinker_ice_tinker_8_7_1_gcc_10_3_0_dqija4h_N_1_MPI_1_OMP_1
- aws:c6gn
   - builtin
      * num_tasks: 1
      * Total Time: 29.43 s
------------------------------------------------------------------------------
tinker_ice_tinker_8_7_1_gcc_10_3_0_dqija4h_N_1_MPI_1_OMP_2
   - builtin
      * num_tasks: 1
      * Total Time: 18.61 s
------------------------------------------------------------------------------
tinker_ice_tinker_8_7_1_gcc_10_3_0_dqija4h_N_1_MPI_1_OMP_4
   - builtin
      * num_tasks: 1
      * Total Time: 12.8 s
------------------------------------------------------------------------------
tinker_ice_tinker_8_7_1_gcc_10_3_0_dqija4h_N_1_MPI_1_OMP_8
   - builtin
      * num_tasks: 1
      * Total Time: 8.15 s
------------------------------------------------------------------------------
tinker_ice_tinker_8_7_1_gcc_10_3_0_oxk2q3c_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Total Time: 29.33 s
------------------------------------------------------------------------------
tinker_ice_tinker_8_7_1_gcc_10_3_0_oxk2q3c_N_1_MPI_1_OMP_2
   - builtin
      * num_tasks: 1
      * Total Time: 29.29 s
------------------------------------------------------------------------------
tinker_ice_tinker_8_7_1_gcc_10_3_0_oxk2q3c_N_1_MPI_1_OMP_4
   - builtin
      * num_tasks: 1
      * Total Time: 29.37 s
------------------------------------------------------------------------------
tinker_ice_tinker_8_7_1_gcc_10_3_0_oxk2q3c_N_1_MPI_1_OMP_8
   - builtin
      * num_tasks: 1
      * Total Time: 29.33 s
------------------------------------------------------------------------------
tinker_ice_tinker_8_7_1_arm_21_0_0_879_ynitubh_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Total Time: 28.64 s
------------------------------------------------------------------------------
tinker_ice_tinker_8_7_1_arm_21_0_0_879_ynitubh_N_1_MPI_1_OMP_2
   - builtin
      * num_tasks: 1
      * Total Time: 16.82 s
------------------------------------------------------------------------------
tinker_ice_tinker_8_7_1_arm_21_0_0_879_ynitubh_N_1_MPI_1_OMP_4
   - builtin
      * num_tasks: 1
      * Total Time: 10.29 s
------------------------------------------------------------------------------
tinker_ice_tinker_8_7_1_arm_21_0_0_879_ynitubh_N_1_MPI_1_OMP_8
   - builtin
      * num_tasks: 1
      * Total Time: 6.93 s
------------------------------------------------------------------------------
tinker_ice_tinker_8_7_1_nvhpc_21_2_qszz7b5_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Total Time: 29.3 s
------------------------------------------------------------------------------
tinker_ice_tinker_8_7_1_nvhpc_21_2_qszz7b5_N_1_MPI_1_OMP_2
   - builtin
      * num_tasks: 1
      * Total Time: 29.23 s
------------------------------------------------------------------------------
tinker_ice_tinker_8_7_1_nvhpc_21_2_qszz7b5_N_1_MPI_1_OMP_4
   - builtin
      * num_tasks: 1
      * Total Time: 29.2 s
------------------------------------------------------------------------------
tinker_ice_tinker_8_7_1_nvhpc_21_2_qszz7b5_N_1_MPI_1_OMP_8
   - builtin
      * num_tasks: 1
      * Total Time: 29.24 s
------------------------------------------------------------------------------
```

### Strong Scaling Study

As Tinker only support the OpenMP, so we only do the one node scaliabily tests. GCC and ARM compilers have relatively good scalability, while the NVHPC seems still keep the same.

| Cores | GCC | ARM | NVHPC |	 GCC default|
|-------|------------|------------|------------|------------|
| 1     |  29.43     | 28.64      | 29.3	   |	29.29	|
| 2     |  18.61     | 16.82      | 29.23	   |	29.37	|
| 4     |  12.8     | 10.29      | 29.2	   |	29.33	|
| 8     |  8.15      | 6.93       | 29.24	   |	29.33	|

## Optimisation

Details of steps taken to optimise performance of the application.
Please document work with compiler flags, maths libraries, system libraries, code optimisations, etc.

#### Performance Regression(4 times faster with 8 threads!!!)

I can't tell the exact the compiler as the package using cmake, but what I did is 1. Add the OpenMP support 2. Add other linker like -lm and -lfftw3_omp. You can see this in the first section "package modification"

| Cores | Original | Enabled with openmp|
|-------|----------------|-----------|
| 1     |    29.29       |  29.43         |
| 2     |    29.37       |  18.61         |
| 4     |    29.33       |  12.84         |
| 8     |    29.33       |  8.15          |

We have tried the 16 cores and more, but we figured out that with 8 threads the package runs fastest, so we don't display other configuration.
8.15 / 29.33 is about 0.278, so the program runs about x4 faster, we are very excited to see that!

## Report

### Compilation Summary

1. Compile the fftw with openmp support
2. Modify the patch file
3. Compile the tinker with the fftw(with openmp)

### Performance Summary

As you can see in the Peformance Regression part, the program runs faster when threads below 8, but when adding more threads, the program doesn't become faster(or even slower), We guess the reason is the overhead between the threads. 

We use the pre command in the reframe to copy some input data ; otherwise the input data can't be found. 

### Optimisation Summary

To be honest, we didn't change a lot of code to support the openmp. However, it takes up more than 10 hours to get the right configuration. The first thing is fftw is not enabled with openmp in the default package, but tinker depends on the fftw, so you must recompile the fftw with openmp. Second thing is changing the cmakelist, the problem is the cmakelist given by tinker is by a patch file, it brought us a lot of trouble to patch the "patch file".
