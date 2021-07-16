# CoMD 

**Description:** CoMD is a reference implementation of classical molecular dynamics algorithms and workloads as used in materials science. It is created and maintained by The Exascale Co-Design Center for Materials in Extreme Environments (ExMatEx). The code is intended to serve as a vehicle for co-design by allowing others to extend and/or reimplement it as needed to test performance of new architectures, programming models, etc. New versions of CoMD will be released to incorporate the lessons learned from the co-design process.

**URL:** http://www.exmatex.org/comd.html

**Source-Code:** https://github.com/ECP-copa/CoMD

**Team:** Falkners

## Compilation

### Spack Package Modification

The default spack configuration works for MPI but won't compile for OMP. The below diff was used to enable OpenMP compilation on the ARM HPC and was used for the scaling test. A PR is linked below to fix these two issues in the spack config.

Two issues below:
* A copy of `Make.vanilla` would not happen in the `with ... or ...:` for the second thing, namely OpenMP
* `'spack_cc'` is incorrectly quoted, which prevents the variable from being evaluated to the correct compiler. Removing the quotes fixes this. 

```
diff --git a/var/spack/repos/builtin/packages/comd/package.py b/var/spack/repos/builtin/packages/comd/package.py
index 5ab3600f1f..9eaafb4733 100644
--- a/var/spack/repos/builtin/packages/comd/package.py
+++ b/var/spack/repos/builtin/packages/comd/package.py
@@ -36,14 +36,17 @@ class Comd(MakefilePackage):
     conflicts('+openmp', when='+mpi')

     def edit(self, spec, prefix):
-        with working_dir('src-mpi') or working_dir('src-openmp'):
+        with working_dir('src-openmp'):
+            copy('Makefile.vanilla', 'Makefile')
+        with working_dir('src-mpi'):
             copy('Makefile.vanilla', 'Makefile')

     @property
     def build_targets(self):
         targets = []
         cflags = ' -std=c99 '
-        optflags = ' -g -O5 '
+        optflags = ' -g -O5 -Ofast'
+
         clib = ' -lm '
         comd_variant = 'CoMD'
         cc = spack_cc
@@ -56,7 +59,7 @@ def build_targets(self):
                 comd_variant += '-mpi'
                 targets.append('CC = {0}'.format(self.spec['mpi'].mpicc))
             else:
-                targets.append('CC = {0}'.format('spack_cc'))
+                targets.append(f'CC = {spack_cc}')

         else:
             targets.append('--directory=src-mpi')
```

Git commit hash of checkout for pacakage: `667ab501996058b1f89f1763d1791befa455b1f8`

Pull request for Spack recipe changes: https://github.com/spack/spack/pull/24916

### Building COMD



#### Compiler 1: arm@21.0.0.879

```
spack install comd@1.1 %arm@21.0.0.879
```

```
$ spack spec -Il comd@1.1 %arm@21.0.0.879 

[+]  ehp56fd  comd@1.1%arm@21.0.0.879~graphs+mpi~openmp+precision arch=linux-amzn2-aarch64
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

#### Compiler 2: gcc@10.3.0

```
spack install comd@1.1 %gcc@10.3.0
```

```
$ spack spec -Il comd@1.1 %gcc@10.3.0
[+]  z3b2svr  comd@1.1%gcc@10.3.0~graphs+mpi~openmp+precision arch=linux-amzn2-graviton2
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

#### Compiler 3: nvhpc@21.2

```
spack install comd@1.1 %nvhpc@21.2
```

```
$ spack spec -Il comd@1.1 %nvhpc@21.2

[+]  az7mhit  comd@1.1%nvhpc@21.2~graphs+mpi~openmp+precision arch=linux-amzn2-graviton2
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

[ReFrame Benchmark 1](#)

```
reframe -c comd_weak.py -r --performance-report
```

### Validation

`Test Case 1` is a validation of the example "weak scaling" study data and based on the steps from the `mpi-weakScaling.sh` script in CoMD's repository. This test relies relies on the potentials from the `pots/Cu_u6.eam` file in the same GitHub repository.

See `comd_weak.py` for the reframe test that does all the downloads needed potential data and does scaling steps. 

Output from the test shows how well the MPI scales with work-load. It also provides a way to compare different compilers on the same architecture.

### ReFrame Output

ReFrame run on ARM with gcc, ARM and NVIDIA compilers.

```
==============================================================================
PERFORMANCE REPORT
------------------------------------------------------------------------------
CoMD_CoMD_weak_1_comd_1_1__gcc_10_3_0_N_1_MPI_1_OMP_1
- aws:c6gn
   - builtin
      * num_tasks: 1
      * Total Time: 44.911 s
------------------------------------------------------------------------------
CoMD_CoMD_weak_1_comd_1_1__arm_21_0_0_879_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Total Time: 39.5082 s
------------------------------------------------------------------------------
CoMD_CoMD_weak_1_comd_1_1__nvhpc_21_2_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Total Time: 28.5893 s
------------------------------------------------------------------------------
CoMD_CoMD_weak_2_comd_1_1__gcc_10_3_0_N_1_MPI_2_OMP_1
   - builtin
      * num_tasks: 2
      * Total Time: 45.5082 s
------------------------------------------------------------------------------
CoMD_CoMD_weak_2_comd_1_1__arm_21_0_0_879_N_1_MPI_2_OMP_1
   - builtin
      * num_tasks: 2
      * Total Time: 39.6867 s
------------------------------------------------------------------------------
CoMD_CoMD_weak_2_comd_1_1__nvhpc_21_2_N_1_MPI_2_OMP_1
   - builtin
      * num_tasks: 2
      * Total Time: 28.7488 s
------------------------------------------------------------------------------
CoMD_CoMD_weak_4_comd_1_1__gcc_10_3_0_N_1_MPI_4_OMP_1
   - builtin
      * num_tasks: 4
      * Total Time: 45.4903 s
------------------------------------------------------------------------------
CoMD_CoMD_weak_4_comd_1_1__arm_21_0_0_879_N_1_MPI_4_OMP_1
   - builtin
      * num_tasks: 4
      * Total Time: 39.7383 s
------------------------------------------------------------------------------
CoMD_CoMD_weak_4_comd_1_1__nvhpc_21_2_N_1_MPI_4_OMP_1
   - builtin
      * num_tasks: 4
      * Total Time: 28.8755 s
------------------------------------------------------------------------------
CoMD_CoMD_weak_8_comd_1_1__gcc_10_3_0_N_1_MPI_8_OMP_1
   - builtin
      * num_tasks: 8
      * Total Time: 45.8829 s
------------------------------------------------------------------------------
CoMD_CoMD_weak_8_comd_1_1__arm_21_0_0_879_N_1_MPI_8_OMP_1
   - builtin
      * num_tasks: 8
      * Total Time: 39.9327 s
------------------------------------------------------------------------------
CoMD_CoMD_weak_8_comd_1_1__nvhpc_21_2_N_1_MPI_8_OMP_1
   - builtin
      * num_tasks: 8
      * Total Time: 29.1963 s
------------------------------------------------------------------------------
CoMD_CoMD_weak_16_comd_1_1__gcc_10_3_0_N_1_MPI_16_OMP_1
   - builtin
      * num_tasks: 16
      * Total Time: 46.2156 s
------------------------------------------------------------------------------
CoMD_CoMD_weak_16_comd_1_1__arm_21_0_0_879_N_1_MPI_16_OMP_1
   - builtin
      * num_tasks: 16
      * Total Time: 41.1308 s
------------------------------------------------------------------------------
CoMD_CoMD_weak_16_comd_1_1__nvhpc_21_2_N_1_MPI_16_OMP_1
   - builtin
      * num_tasks: 16
      * Total Time: 30.4601 s
------------------------------------------------------------------------------
CoMD_CoMD_weak_32_comd_1_1__gcc_10_3_0_N_1_MPI_32_OMP_1
   - builtin
      * num_tasks: 32
      * Total Time: 49.983 s
------------------------------------------------------------------------------
CoMD_CoMD_weak_32_comd_1_1__arm_21_0_0_879_N_1_MPI_32_OMP_1
   - builtin
      * num_tasks: 32
      * Total Time: 44.027 s
------------------------------------------------------------------------------
CoMD_CoMD_weak_32_comd_1_1__nvhpc_21_2_N_1_MPI_32_OMP_1
   - builtin
      * num_tasks: 32
      * Total Time: 33.5083 s
------------------------------------------------------------------------------
CoMD_CoMD_weak_64_comd_1_1__gcc_10_3_0_N_1_MPI_64_OMP_1
   - builtin
      * num_tasks: 64
      * Total Time: 55.5555 s
------------------------------------------------------------------------------
CoMD_CoMD_weak_64_comd_1_1__arm_21_0_0_879_N_1_MPI_64_OMP_1
   - builtin
      * num_tasks: 64
      * Total Time: 44.1167 s
------------------------------------------------------------------------------
CoMD_CoMD_weak_64_comd_1_1__nvhpc_21_2_N_1_MPI_64_OMP_1
   - builtin
      * num_tasks: 64
      * Total Time: 38.6034 s
------------------------------------------------------------------------------
```

ReFrame run on x86 with gcc.

```
==============================================================================
PERFORMANCE REPORT
------------------------------------------------------------------------------
CoMD_CoMD_weak_1_comd_1_1__gcc_10_3_0_N_1_MPI_1_OMP_1
- aws:c5n
   - builtin
      * num_tasks: 1
      * Total Time: 52.1079 s
------------------------------------------------------------------------------
CoMD_CoMD_weak_2_comd_1_1__gcc_10_3_0_N_1_MPI_2_OMP_1
   - builtin
      * num_tasks: 2
      * Total Time: 52.0548 s
------------------------------------------------------------------------------
CoMD_CoMD_weak_4_comd_1_1__gcc_10_3_0_N_1_MPI_4_OMP_1
   - builtin
      * num_tasks: 4
      * Total Time: 52.5905 s
------------------------------------------------------------------------------
CoMD_CoMD_weak_8_comd_1_1__gcc_10_3_0_N_1_MPI_8_OMP_1
   - builtin
      * num_tasks: 8
      * Total Time: 52.5659 s
------------------------------------------------------------------------------
CoMD_CoMD_weak_16_comd_1_1__gcc_10_3_0_N_1_MPI_16_OMP_1
   - builtin
      * num_tasks: 16
      * Total Time: 52.5794 s
------------------------------------------------------------------------------
CoMD_CoMD_weak_32_comd_1_1__gcc_10_3_0_N_1_MPI_32_OMP_1
   - builtin
      * num_tasks: 32
      * Total Time: 53.8952 s
------------------------------------------------------------------------------
CoMD_CoMD_weak_64_comd_1_1__gcc_10_3_0_N_1_MPI_64_OMP_1
   - builtin
      * num_tasks: 64
      * Total Time: 56.7359 s
------------------------------------------------------------------------------
```

### On-node Compiler Comparison

Performance comparison of two compilers. Note: each step increases in complexity and work in order to utilize the extra MPI. Do not expect times to overall decrease. This demonstrates relative performance of different compiles as workload increases. 

| Cores | gcc@10.3.0 | arm@21.0.0.879 | nvhpc@21.2 |
|-------|------------|----------------|------------|
|   1   |   44.91    |  39.50         |  28.58     |
|   2   |   45.50    |  39.68         |  28.74     |
|   4   |   45.49    |  39.73         |  28.87     |
|   8   |   45.88    |  39.93         |  29.19     |
|   16  |   46.21    |  41.13         |  30.46     |
|   32  |   49.98    |  44.02         |  33.50     |
|   64  |   55.55    |  44.11         |  38.60     |


### Serial Hot-spot Profile

Serial hot-spot profiling was done with perf for the "weak scaling" test CoMD includes in the GitHub repo. `OMP_THREAD_LIMIT=1` was used to limit OMP and timing was confirmed to match expected single-thread timing.

For the C5n (Intel) here are the top ten application routines, with associated % of runtime for `gcc`

```
SPACK_DIR="/scratch/opt/spack/linux-amzn2-skylake_avx512/gcc-10.3.0/gperftools-2.8.1-nvbh4z2zua3abfjvhqq4hiovznkvqens"
env OMP_THREAD_LIMIT=1 LD_PRELOAD=$SPACK_DIR/lib/libprofiler.so CPUPROFILE=comd_gcc_weak_serial.profile CoMD-openmp -e -i 1 -j 1 -k 1 -x 20 -y 20 -z 20

COMD_DIR="/scratch/opt/spack/linux-amzn2-skylake_avx512/gcc-10.3.0/comd-1.1-6sifbzehxhqkgkerdq24qnzb4xegipyh"
pprof --text $COMD_DIR/bin/CoMD-openmp comd_gcc_weak_serial.profile

Total: 5041 samples
    1947  38.6%  38.6%     2370  47.0% eamForce._omp_fn.3
    1932  38.3%  76.9%     2596  51.5% eamForce._omp_fn.1
     859  17.0%  94.0%      957  19.0% interpolate
     125   2.5%  96.5%      125   2.5% __sqrt
      84   1.7%  98.1%       84   1.7% __floor_sse41
      26   0.5%  98.7%       26   0.5% _init
      18   0.4%  99.0%       18   0.4% advanceVelocity._omp_fn.0
       7   0.1%  99.1%       11   0.2% getBoxFromCoord
       7   0.1%  99.3%       11   0.2% sortAtomsInCell
       6   0.1%  99.4%       10   0.2% eamForce._omp_fn.0
```

For the C5n (Intel) here are the top ten application routines, with associated % of runtime for `nvhpc`

```
SPACK_DIR="/scratch/opt/spack/linux-amzn2-skylake_avx512/gcc-10.3.0/gperftools-2.8.1-nvbh4z2zua3abfjvhqq4hiovznkvqens"
env OMP_THREAD_LIMIT=1 LD_PRELOAD=$SPACK_DIR/lib/libprofiler.so CPUPROFILE=comd_nvhpc_weak_serial.profile CoMD-openmp -e -i 1 -j 1 -k 1 -x 20 -y 20 -z 20

COMD_DIR="/scratch/opt/spack/linux-amzn2-skylake_avx512/nvhpc-21.2/comd-1.1-chfwr76qbks5xpqlnuhuzjmc3zsxld5x"
pprof --text $COMD_DIR/bin/CoMD-openmp comd_nvhpc_weak_serial.profile

Total: 3569 samples
    1486  41.6%  41.6%     1731  48.5% __nv_eamForce_F1L328_4
    1421  39.8%  81.5%     1771  49.6% __nv_eamForce_F1L250_2
     597  16.7%  98.2%      597  16.7% interpolate
      10   0.3%  98.5%       12   0.3% __nv_eamForce_F1L239_1
       9   0.3%  98.7%        9   0.3% __nv_advanceVelocity_F1L72_1
       7   0.2%  98.9%        7   0.2% __memmove_avx_unaligned_erms
       7   0.2%  99.1%       15   0.4% sortAtomsInCell
       6   0.2%  99.3%        6   0.2% __nv_advancePosition_F1L86_2
       4   0.1%  99.4%        4   0.1% getBoxFromTuple
       3   0.1%  99.5%        5   0.1% __nv_eamForce_F1L305_3
```

For the C6gn (ARM) here are the top ten application routines, with associated % of runtime for `arm`

```
SPACK_DIR=/scratch/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/gperftools-2.8.1-nlcrjyzchw37gafuffie7h5vapyl5uhg
[jayson@ip-10-0-0-176 gatk]$ env OMP_THREAD_LIMIT=1 LD_PRELOAD=$SPACK_DIR/lib/libprofiler.so CPUPROFILE=comd_weak_arm_serial.profile CoMD-openmp -e -i 1 -j 1 -k 1 -x 20 -y 20 -z 20

COMD_DIR=/scratch/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/comd-1.1-phpsqbdm2lucpiarf7j5rd2m22owszc5
pprof --text $COMD_DIR/bin/CoMD-openmp comd_weak_arm_serial.profile  Using local file /scratch/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/comd-1.1-phpsqbdm2lucpiarf7j5rd2m22owszc5/bin/CoMD-openmp.
Using local file comd_weak_arm_serial.profile.
Total: 6495 samples
    2754  42.4%  42.4%     3306  50.9% .omp_outlined..5
    2750  42.3%  84.7%     3039  46.8% .omp_outlined..8
     834  12.8%  97.6%      834  12.8% interpolate
      28   0.4%  98.0%       53   0.8% .omp_outlined.@40beb4
      25   0.4%  98.4%       25   0.4% zeroReal3
      15   0.2%  98.6%       26   0.4% sortAtomsInCell
      13   0.2%  98.8%       13   0.2% __sqrt
      12   0.2%  99.0%       12   0.2% __brk
       9   0.1%  99.2%       13   0.2% getBoxFromCoord
       8   0.1%  99.3%        8   0.1% .omp_outlined..2
```


### Full Node Hot-spot Profile

Full node hot-spot profiling was done using gperf. CoMD reported OMP threads and timing was also used to confirm full node utilization.

For the C5n (Intel) here are the top ten application routines, with associated % of runtime for `gcc`

```
SPACK_DIR='/scratch/opt/spack/linux-amzn2-skylake_avx512/gcc-10.3.0/gperftools-2.8.1-nvbh4z2zua3abfjvhqq4hiovznkvqens/'
env LD_PRELOAD=$SPACK_DIR/lib/libprofiler.so CPUPROFILE=comd_weak_gcc_full.profile CoMD-openmp -e -i 1 -j 1 -k 1 -x 20 -y 20 -z 20

COMD_DIR='/scratch/opt/spack/linux-amzn2-skylake_avx512/gcc-10.3.0/comd-1.1-6sifbzehxhqkgkerdq24qnzb4xegipyh/bin/'
pprof --text $COMD_DIR/bin/CoMD-openmp comd_weak_gcc_full.profile

Total: 1108 samples
     574  51.8%  51.8%      581  52.4% do_spin (inline)
     491  44.3%  96.1%      491  44.3% ljForce._omp_fn.1
      13   1.2%  97.3%       13   1.2% advancePosition._omp_fn.0
       8   0.7%  98.0%        8   0.7% __brk
       7   0.6%  98.6%        7   0.6% cpu_relax (inline)
       4   0.4%  99.0%        7   0.6% sortAtomsInCell
       3   0.3%  99.3%        3   0.3% advanceVelocity._omp_fn.0
       2   0.2%  99.5%        2   0.2% loadAtomsBuffer
       2   0.2%  99.6%        2   0.2% sortAtomsById
       1   0.1%  99.7%        3   0.3% __GI___qsort_r
```

For the C5n (Intel) here are the top ten application routines, with associated % of runtime for `nvhpc`

```
SPACK_DIR='/scratch/opt/spack/linux-amzn2-skylake_avx512/gcc-10.3.0/gperftools-2.8.1-nvbh4z2zua3abfjvhqq4hiovznkvqens/'
env LD_PRELOAD={SPACK_DIR}/lib/libprofiler.so CPUPROFILE=comd_weak_nvhpc_full.profile CoMD-openmp -e -i 1 -j 1 -k 1 -x 20 -y 20 -z 20

COMD_DIR='/scratch/opt/spack/linux-amzn2-skylake_avx512/nvhpc-21.2/comd-1.1-chfwr76qbks5xpqlnuhuzjmc3zsxld5x'
pprof --text $COMD_DIR/bin/CoMD-openmp comd_weak_nvhpc_full.profile

Total: 1108 samples
     574  51.8%  51.8%      581  52.4% do_spin (inline)
     248  22.4%  74.2%      256  23.1% initAtomHaloExchange
     155  14.0%  88.2%      163  14.7% __nv_ljForce_F1L173_2
      41   3.7%  91.9%       41   3.7% zeroReal3
      20   1.8%  93.7%       20   1.8% comdMalloc
      15   1.4%  95.0%       15   1.4% comdFree
      13   1.2%  96.2%       13   1.2% timerStats
      12   1.1%  97.3%       12   1.1% pgCplus_compiled.
       8   0.7%  98.0%        8   0.7% __brk
       7   0.6%  98.6%        7   0.6% cpu_relax (inline)
       3   0.3%  98.9%       14   1.3% printPerformanceResultsYaml
       3   0.3%  99.2%        3   0.3% processArgs
       2   0.2%  99.4%        2   0.2% findOption
       2   0.2%  99.5%        2   0.2% mkForceSendCellList
       1   0.1%  99.6%        3   0.3% __GI___qsort_r
```

For the C6gn (ARM) here are the top ten application routines, with associated % of runtime for `arm`

```
SPACK_DIR="/scratch/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/gperftools-2.8.1-nlcrjyzchw37gafuffie7h5vapyl5uhg"
env LD_PRELOAD={SPACK_DIR}/lib/libprofiler.so CPUPROFILE=comd_arm.profile CoMD-openmp -e -i 1 -j 1 -k 1 -x 20 -y 20 -z 20

COMD_DIR="/scratch/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/comd-
1.1-phpsqbdm2lucpiarf7j5rd2m22owszc5"
pprof --text $COMD_DIR/bin/CoMD-openmp comd_arm.profile

Total: 170 samples
      85  50.0%  50.0%      114  67.1% .omp_outlined..2
      58  34.1%  84.1%       84  49.4% kmp_flag_64::wait
      23  13.5%  97.6%       23  13.5% __GI___sched_yield
       1   0.6%  98.2%        1   0.6% 0x0000ffff9bade348
       1   0.6%  98.8%        1   0.6% __kmp_yield
       1   0.6%  99.4%        1   0.6% _init
       1   0.6% 100.0%        1   0.6% zeroReal3
       0   0.0% 100.0%        1   0.6% __GI___gettimeofday
       0   0.0% 100.0%       29  17.1% __kmp_barrier
       0   0.0% 100.0%       55  32.4% __kmp_fork_barrier
```

### Strong Scaling Study

On-node scaling study for two compilers.

| Cores | gcc@10.3.0 | arm@21.0.0.879 |
|-------|------------|----------------|
|   1   |   44.91    |  39.50         |
|   2   |   45.50    |  39.68         |
|   4   |   45.49    |  39.73         |
|   8   |   45.88    |  39.93         |
|   16  |   46.21    |  41.13         |
|   32  |   49.98    |  44.02         |
|   64  |   55.55    |  44.11         |


### Off-Node Scaling Study

Off-node scaling study comparing C6g and C6gn instances was not done. No C6g resources were avavailable.


### On-Node Architecture Comparison

On-node scaling study for two architectures. `gcc@10.3.0` was used in both cases.


| Cores | C6gn (ARM) | C5n (Intel)    |
|-------|------------|----------------|
|   1   |   44.91    |  52.10         |
|   2   |   45.50    |  52.05         |
|   4   |   45.49    |  52.59         |
|   8   |   45.88    |  52.56         |
|   16  |   46.21    |  52.57         |
|   32  |   49.98    |  53.89         |
|   64  |   55.55    |  56.73         |


## Test Case 2

[ReFrame Benchmark 2](#)

```
reframe -c comd_strong.py -r --performance-report
```

### Validation

`Test Case 2` is a validation of the example "strong scaling" study data and based on the steps from the `mpi-strongScaling.sh` script in CoMD's repository. This test relies relies on the potentials from the `pots/Cu_u6.eam` file in the same GitHub repository.

See `comd_strong.py` for the steps, data download and copy of the test from CoMD's website.

### ReFrame Output

ReFrame output from the ARM HPC.

```
==============================================================================
PERFORMANCE REPORT
------------------------------------------------------------------------------
CoMD_CoMD_strong_1_comd_1_1__gcc_10_3_0_N_1_MPI_1_OMP_1
- aws:c6gn
   - builtin
      * num_tasks: 1
      * Total Time: 319.4221 s
------------------------------------------------------------------------------
CoMD_CoMD_strong_1_comd_1_1__arm_21_0_0_879_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Total Time: 282.6846 s
------------------------------------------------------------------------------
CoMD_CoMD_strong_1_comd_1_1__nvhpc_21_2_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Total Time: 203.7015 s
------------------------------------------------------------------------------
CoMD_CoMD_strong_2_comd_1_1__gcc_10_3_0_N_1_MPI_2_OMP_1
   - builtin
      * num_tasks: 2
      * Total Time: 322.864 s
------------------------------------------------------------------------------
CoMD_CoMD_strong_2_comd_1_1__arm_21_0_0_879_N_1_MPI_2_OMP_1
   - builtin
      * num_tasks: 2
      * Total Time: 282.3552 s
------------------------------------------------------------------------------
CoMD_CoMD_strong_2_comd_1_1__nvhpc_21_2_N_1_MPI_2_OMP_1
   - builtin
      * num_tasks: 2
      * Total Time: 203.505 s
------------------------------------------------------------------------------
CoMD_CoMD_strong_4_comd_1_1__gcc_10_3_0_N_1_MPI_4_OMP_1
   - builtin
      * num_tasks: 4
      * Total Time: 323.488 s
------------------------------------------------------------------------------
CoMD_CoMD_strong_4_comd_1_1__arm_21_0_0_879_N_1_MPI_4_OMP_1
   - builtin
      * num_tasks: 4
      * Total Time: 282.5151 s
------------------------------------------------------------------------------
CoMD_CoMD_strong_4_comd_1_1__nvhpc_21_2_N_1_MPI_4_OMP_1
   - builtin
      * num_tasks: 4
      * Total Time: 204.6477 s
------------------------------------------------------------------------------
CoMD_CoMD_strong_8_comd_1_1__gcc_10_3_0_N_1_MPI_8_OMP_1
   - builtin
      * num_tasks: 8
      * Total Time: 325.1472 s
------------------------------------------------------------------------------
CoMD_CoMD_strong_8_comd_1_1__arm_21_0_0_879_N_1_MPI_8_OMP_1
   - builtin
      * num_tasks: 8
      * Total Time: 283.0221 s
------------------------------------------------------------------------------
CoMD_CoMD_strong_8_comd_1_1__nvhpc_21_2_N_1_MPI_8_OMP_1
   - builtin
      * num_tasks: 8
      * Total Time: 205.5526 s
------------------------------------------------------------------------------
CoMD_CoMD_strong_16_comd_1_1__gcc_10_3_0_N_1_MPI_16_OMP_1
   - builtin
      * num_tasks: 16
      * Total Time: 332.2591 s
------------------------------------------------------------------------------
CoMD_CoMD_strong_16_comd_1_1__arm_21_0_0_879_N_1_MPI_16_OMP_1
   - builtin
      * num_tasks: 16
      * Total Time: 290.8025 s
------------------------------------------------------------------------------
CoMD_CoMD_strong_16_comd_1_1__nvhpc_21_2_N_1_MPI_16_OMP_1
   - builtin
      * num_tasks: 16
      * Total Time: 211.963 s
------------------------------------------------------------------------------
CoMD_CoMD_strong_32_comd_1_1__gcc_10_3_0_N_1_MPI_32_OMP_1
   - builtin
      * num_tasks: 32
      * Total Time: 335.1125 s
------------------------------------------------------------------------------
CoMD_CoMD_strong_32_comd_1_1__arm_21_0_0_879_N_1_MPI_32_OMP_1
   - builtin
      * num_tasks: 32
      * Total Time: 296.2035 s
------------------------------------------------------------------------------
CoMD_CoMD_strong_32_comd_1_1__nvhpc_21_2_N_1_MPI_32_OMP_1
   - builtin
      * num_tasks: 32
      * Total Time: 213.1795 s
------------------------------------------------------------------------------
CoMD_CoMD_strong_64_comd_1_1__gcc_10_3_0_N_1_MPI_64_OMP_1
   - builtin
      * num_tasks: 64
      * Total Time: 344.871 s
------------------------------------------------------------------------------
CoMD_CoMD_strong_64_comd_1_1__arm_21_0_0_879_N_1_MPI_64_OMP_1
   - builtin
      * num_tasks: 64
      * Total Time: 306.812 s
------------------------------------------------------------------------------
CoMD_CoMD_strong_64_comd_1_1__nvhpc_21_2_N_1_MPI_64_OMP_1
   - builtin
      * num_tasks: 64
      * Total Time: 224.3529 s
------------------------------------------------------------------------------
```

ReFrame output from the x86 HPC.

```
==============================================================================
PERFORMANCE REPORT
------------------------------------------------------------------------------
CoMD_CoMD_strong_1_comd_1_1__gcc_10_3_0_N_1_MPI_1_OMP_1
- aws:c5n
   - builtin
      * num_tasks: 1
      * Total Time: 369.6075 s
------------------------------------------------------------------------------
CoMD_CoMD_strong_2_comd_1_1__gcc_10_3_0_N_1_MPI_2_OMP_1
   - builtin
      * num_tasks: 2
      * Total Time: 372.4271 s
------------------------------------------------------------------------------
CoMD_CoMD_strong_4_comd_1_1__gcc_10_3_0_N_1_MPI_4_OMP_1
   - builtin
      * num_tasks: 4
      * Total Time: 372.2095 s
------------------------------------------------------------------------------
CoMD_CoMD_strong_8_comd_1_1__gcc_10_3_0_N_1_MPI_8_OMP_1
   - builtin
      * num_tasks: 8
      * Total Time: 375.1501 s
------------------------------------------------------------------------------
CoMD_CoMD_strong_16_comd_1_1__gcc_10_3_0_N_1_MPI_16_OMP_1
   - builtin
      * num_tasks: 16
      * Total Time: 379.333 s
------------------------------------------------------------------------------
CoMD_CoMD_strong_32_comd_1_1__gcc_10_3_0_N_1_MPI_32_OMP_1
   - builtin
      * num_tasks: 32
      * Total Time: 381.3141 s
------------------------------------------------------------------------------
CoMD_CoMD_strong_64_comd_1_1__gcc_10_3_0_N_1_MPI_64_OMP_1
   - builtin
      * num_tasks: 64
      * Total Time: 391.3633 s
------------------------------------------------------------------------------
```

### On-node Compiler Comparison

Performance comparison of three available compilers on the ARM HPC. Note: each step increases in complexity and work in order to utilize the extra MPI. Do not expect times to overall decrease. This demonstrates relative performance of different compiles as workload increases. 

| Cores | gcc@10.3.0 | arm@21.0.0.879 | nvhpc@21.2 |
|-------|------------|----------------|------------|
|   1   |  319.4     |  282.6         |  203.7     |
|   2   |  322.8     |  282.3         |  203.5     |
|   4   |  323.4     |  282.5         |  204.6     |
|   8   |  325.1     |  283.0         |  205.5     |
|   16  |  332.2     |  290.8         |  211.9     |
|   32  |  335.1     |  296.2         |  213.1     |
|   64  |  344.8     |  306.8         |  224.3     |

### Serial Hot-spot Profile

Serial hot-spot profiling was done with perf for the "strong scaling" test CoMD includes in the GitHub repo. `OMP_THREAD_LIMIT=1` was used to limit OMP and timing was confirmed to match expected single-thread timing.

For the C5n (Intel) here are the top ten application routines, with associated % of runtime for `gcc`

```
SPACK_DIR="/scratch/opt/spack/linux-amzn2-skylake_avx512/gcc-10.3.0/gperftools-2.8.1-nvbh4z2zua3abfjvhqq4hiovznkvqens"
env OMP_THREAD_LIMIT=1 LD_PRELOAD=$SPACK_DIR/lib/libprofiler.so CPUPROFILE=comd_gcc_strong_serial.profile CoMD-openmp -e -i 1 -j 1 -k 1 -x 40 -y 40 -z 40

COMD_DIR="/scratch/opt/spack/linux-amzn2-skylake_avx512/gcc-10.3.0/comd-1.1-6sifbzehxhqkgkerdq24qnzb4xegipyh"
pprof --text $COMD_DIR/bin/CoMD-openmp comd_gcc_strong_serial.profile

Total: 37996 samples
    6709  17.7%  17.7%     7472  19.7% _fini
    4292  11.3%  29.0%     4292  11.3% .S01798
    3274   8.6%  37.6%     3274   8.6% .S01764
    2850   7.5%  45.1%     2850   7.5% .S01376
    2688   7.1%  52.1%     2688   7.1% .S01382
    2607   6.9%  59.0%     2607   6.9% .S01814
    1796   4.7%  63.7%     1796   4.7% .S01768
    1504   4.0%  67.7%     1504   4.0% .S01278
    1295   3.4%  71.1%     1295   3.4% .S01770
    1286   3.4%  74.5%     1286   3.4% .S01379
    1192   3.1%  77.6%     1192   3.1% .S01373
     938   2.5%  80.1%      938   2.5% __sqrt
     868   2.3%  82.4%      868   2.3% .S01284
     669   1.8%  84.1%      669   1.8% .S01816
```

For the C5n (Intel) here are the top ten application routines, with associated % of runtime for `nvhpc`

```
SPACK_DIR="/scratch/opt/spack/linux-amzn2-skylake_avx512/gcc-10.3.0/gperftools-2.8.1-nvbh4z2zua3abfjvhqq4hiovznkvqens"
env OMP_THREAD_LIMIT=1 LD_PRELOAD=$SPACK_DIR/lib/libprofiler.so CPUPROFILE=comd_nvhpc_strong.profile CoMD-openmp -e -i 1 -j 1 -k 1 -x 40 -y 40 -z 40

COMD_DIR="/scratch/opt/spack/linux-amzn2-skylake_avx512/nvhpc-21.2/comd-1.1-chfwr76qbks5xpqlnuhuzjmc3zsxld5x"
pprof --text $COMD_DIR/bin/CoMD-openmp comd_nvhpc_strong_serial.profile

Total: 27307 samples
   11268  41.3%  41.3%    13193  48.3% __nv_eamForce_F1L328_4
   10714  39.2%  80.5%    13467  49.3% __nv_eamForce_F1L250_2
    4714  17.3%  97.8%     4714  17.3% interpolate
     101   0.4%  98.1%      134   0.5% __nv_eamForce_F1L239_1
      97   0.4%  98.5%       97   0.4% __nv_advanceVelocity_F1L72_1
      74   0.3%  98.8%      118   0.4% sortAtomsInCell
      58   0.2%  99.0%       58   0.2% __nv_advancePosition_F1L86_2
      48   0.2%  99.1%       61   0.2% getBoxFromCoord
      33   0.1%  99.3%       33   0.1% zeroReal3@40b210
      26   0.1%  99.4%       26   0.1% loadAtomsBuffer
```

### Full Node Hot-spot Profile

Full node hot-spot profiling was done using gperf. CoMD reported OMP threads and timing was also used to confirm full node utilization.

For the C5n (Intel) here are the top ten application routines, with associated % of runtime for `nvhpc`

```
SPACK_DIR="/scratch/opt/spack/linux-amzn2-skylake_avx512/gcc-10.3.0/gperftools-2.8.1-nvbh4z2zua3abfjvhqq4hiovznkvqens"
env LD_PRELOAD=$SPACK_DIR/lib/libprofiler.so CPUPROFILE=comd_nvhpc_strong_full.profile CoMD-openmp -e -i 1 -j 1 -k 1 -x 40 -y 40 -z 40

COMD_DIR="/scratch/opt/spack/linux-amzn2-skylake_avx512/nvhpc-21.2/comd-1.1-chfwr76qbks5xpqlnuhuzjmc3zsxld5x"
pprof --text $COMD_DIR/bin/CoMD-openmp comd_nvhpc_strong_full.profile

Total: 5552 samples
    1672  30.1%  30.1%     1958  35.3% __nv_eamForce_F1L250_2
    1656  29.8%  59.9%     1837  33.1% __nv_eamForce_F1L328_4
     820  14.8%  74.7%     1221  22.0% waitForNeighborThreads (inline)
     474   8.5%  83.2%      474   8.5% interpolate
     396   7.1%  90.4%      396   7.1% __GI___sched_yield
     106   1.9%  92.3%      123   2.2% __nv_eamForce_F1L239_1
      81   1.5%  93.8%       98   1.8% getBoxFromCoord
      51   0.9%  94.7%       79   1.4% unloadAtomsBuffer
      46   0.8%  95.5%       46   0.8% __nv_advancePosition_F1L86_2
      46   0.8%  96.3%       46   0.8% loadAtomsBuffer
```

For the C5n (Intel) here are the top ten application routines, with associated % of runtime for `gcc`

```
SPACK_DIR="/scratch/opt/spack/linux-amzn2-skylake_avx512/gcc-10.3.0/gperftools-2.8.1-nvbh4z2zua3abfjvhqq4hiovznkvqens"
env LD_PRELOAD=$SPACK_DIR/lib/libprofiler.so CPUPROFILE=comd_gcc_strong_full.profile CoMD-openmp -e -i 1 -j 1 -k 1 -x 40 -y 40 -z 40

COMD_DIR="/scratch/opt/spack/linux-amzn2-skylake_avx512/nvhpc-21.2/comd-1.1-chfwr76qbks5xpqlnuhuzjmc3zsxld5x"
pprof --text $COMD_DIR/bin/CoMD-openmp comd_gcc_strong_full.profile

Total: 8240 samples
    2175  26.4%  26.4%     2199  26.7% do_spin (inline)
     797   9.7%  36.1%      797   9.7% .S01764
     779   9.5%  45.5%      779   9.5% .S01376
     727   8.8%  54.3%      823  10.0% _fini
     594   7.2%  61.6%      594   7.2% .S01798
     327   4.0%  65.5%      327   4.0% .S01814
     315   3.8%  69.3%      315   3.8% .S01768
     297   3.6%  72.9%      297   3.6% .S01382
     233   2.8%  75.8%      233   2.8% .S01373
     159   1.9%  77.7%      159   1.9% .S01278
```

### Strong Scaling Study

On-node scaling study for two compilers.

| Cores | gcc@10.3.0 | arm@21.0.0.879 |
|-------|------------|----------------|
|   1   |  319.4     |  282.6         |
|   2   |  322.8     |  282.3         |
|   4   |  323.4     |  282.5         |
|   8   |  325.1     |  283.0         |
|   16  |  332.2     |  290.8         |
|   32  |  335.1     |  296.2         |
|   64  |  344.8     |  306.8         |

### Off-Node Scaling Study

Off-node scaling study comparing C6g and C6gn instances was not done. No C6g resources were avavailable.

### On-Node Architecture Comparison

On-node scaling study for two architectures. `gcc@10.3.0` was used in both cases.


| Cores | C6gn (ARM) | C5n (x86/Intel)    |
|-------|------------|----------------|
|   1   |  319.4     |  369.6         |
|   2   |  322.8     |  372.4         |
|   4   |  323.4     |  372.2         |
|   8   |  325.1     |  375.1         |
|   16  |  332.2     |  379.3         |
|   32  |  335.1     |  381.3         |
|   64  |  344.8     |  391.3         |


## Test Case 3

[ReFrame Benchmark 3](#)

```
reframe -c comd_weak_omp.py -r --performance-report
```

### Validation

`Test Case 3` is similar to `Test Case 1` using an example of the "weak scaling" study data and based on the steps from the `mpi-weakScaling.sh` script in CoMD's repository. This test relies relies on the potentials from the `pots/Cu_u6.eam` file in the same GitHub repository. The main difference here is that the code was re-compiled with OpenMP so that multiple cores could be used.

See `comd_weak_omp.py` for the steps, data download and copy of the test from CoMD's website.

These tests uses spack compiles with openmp and no mpi (they conflict).

```
spack install comd %arm@21.0.0.879 +openmp -mpi
spack install comd %nvhpc@21.2 +openmp -mpi
spack install comd %gcc@10.3.0 +openmp -mpi
```


### ReFrame Output

ReFrame output from the ARM HPC.

```
==============================================================================
PERFORMANCE REPORT
------------------------------------------------------------------------------
CoMD_CoMD_weak_omp_comd_1_1__gcc_10_3_0_N_1_MPI_1_OMP_1
- aws:c6gn
   - builtin
      * num_tasks: 1
      * Total Time: 74.4443 s
------------------------------------------------------------------------------
CoMD_CoMD_weak_omp_comd_1_1__gcc_10_3_0_N_1_MPI_1_OMP_2
   - builtin
      * num_tasks: 1
      * Total Time: 37.4329 s
------------------------------------------------------------------------------
CoMD_CoMD_weak_omp_comd_1_1__gcc_10_3_0_N_1_MPI_1_OMP_4
   - builtin
      * num_tasks: 1
      * Total Time: 18.9083 s
------------------------------------------------------------------------------
CoMD_CoMD_weak_omp_comd_1_1__gcc_10_3_0_N_1_MPI_1_OMP_8
   - builtin
      * num_tasks: 1
      * Total Time: 10.4632 s
------------------------------------------------------------------------------
CoMD_CoMD_weak_omp_comd_1_1__gcc_10_3_0_N_1_MPI_1_OMP_16
   - builtin
      * num_tasks: 1
      * Total Time: 5.5645 s
------------------------------------------------------------------------------
CoMD_CoMD_weak_omp_comd_1_1__gcc_10_3_0_N_1_MPI_1_OMP_32
   - builtin
      * num_tasks: 1
      * Total Time: 3.1011 s
------------------------------------------------------------------------------
CoMD_CoMD_weak_omp_comd_1_1__gcc_10_3_0_N_1_MPI_1_OMP_64
   - builtin
      * num_tasks: 1
      * Total Time: 1.9046 s
------------------------------------------------------------------------------
CoMD_CoMD_weak_omp_comd_1_1__arm_21_0_0_879_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Total Time: 64.6219 s
------------------------------------------------------------------------------
CoMD_CoMD_weak_omp_comd_1_1__arm_21_0_0_879_N_1_MPI_1_OMP_2
   - builtin
      * num_tasks: 1
      * Total Time: 32.4629 s
------------------------------------------------------------------------------
CoMD_CoMD_weak_omp_comd_1_1__arm_21_0_0_879_N_1_MPI_1_OMP_4
   - builtin
      * num_tasks: 1
      * Total Time: 16.4848 s
------------------------------------------------------------------------------
CoMD_CoMD_weak_omp_comd_1_1__arm_21_0_0_879_N_1_MPI_1_OMP_8
   - builtin
      * num_tasks: 1
      * Total Time: 9.1019 s
------------------------------------------------------------------------------
CoMD_CoMD_weak_omp_comd_1_1__arm_21_0_0_879_N_1_MPI_1_OMP_16
   - builtin
      * num_tasks: 1
      * Total Time: 4.8571 s
------------------------------------------------------------------------------
CoMD_CoMD_weak_omp_comd_1_1__arm_21_0_0_879_N_1_MPI_1_OMP_32
   - builtin
      * num_tasks: 1
      * Total Time: 2.6809 s
------------------------------------------------------------------------------
CoMD_CoMD_weak_omp_comd_1_1__arm_21_0_0_879_N_1_MPI_1_OMP_64
   - builtin
      * num_tasks: 1
      * Total Time: 1.784 s
------------------------------------------------------------------------------
CoMD_CoMD_weak_omp_comd_1_1__nvhpc_21_2_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Total Time: 56.4211 s
------------------------------------------------------------------------------
CoMD_CoMD_weak_omp_comd_1_1__nvhpc_21_2_N_1_MPI_1_OMP_2
   - builtin
      * num_tasks: 1
      * Total Time: 28.4626 s
------------------------------------------------------------------------------
CoMD_CoMD_weak_omp_comd_1_1__nvhpc_21_2_N_1_MPI_1_OMP_4
   - builtin
      * num_tasks: 1
      * Total Time: 14.4238 s
------------------------------------------------------------------------------
CoMD_CoMD_weak_omp_comd_1_1__nvhpc_21_2_N_1_MPI_1_OMP_8
   - builtin
      * num_tasks: 1
      * Total Time: 7.9631 s
------------------------------------------------------------------------------
CoMD_CoMD_weak_omp_comd_1_1__nvhpc_21_2_N_1_MPI_1_OMP_16
   - builtin
      * num_tasks: 1
      * Total Time: 4.2204 s
------------------------------------------------------------------------------
CoMD_CoMD_weak_omp_comd_1_1__nvhpc_21_2_N_1_MPI_1_OMP_32
   - builtin
      * num_tasks: 1
      * Total Time: 2.3234 s
------------------------------------------------------------------------------
CoMD_CoMD_weak_omp_comd_1_1__nvhpc_21_2_N_1_MPI_1_OMP_64
   - builtin
      * num_tasks: 1
      * Total Time: 1.5922 s
------------------------------------------------------------------------------
```

ReFrame report output from the x86 HPC.

```
==============================================================================
PERFORMANCE REPORT
------------------------------------------------------------------------------
CoMD_CoMD_weak_omp_comd_1_1__gcc_10_3_0_N_1_MPI_1_OMP_1
- aws:c5n
   - builtin
      * num_tasks: 1
      * Total Time: 67.7362 s
------------------------------------------------------------------------------
CoMD_CoMD_weak_omp_comd_1_1__gcc_10_3_0_N_1_MPI_1_OMP_2
   - builtin
      * num_tasks: 1
      * Total Time: 42.1041 s
------------------------------------------------------------------------------
CoMD_CoMD_weak_omp_comd_1_1__gcc_10_3_0_N_1_MPI_1_OMP_4
   - builtin
      * num_tasks: 1
      * Total Time: 20.9839 s
------------------------------------------------------------------------------
CoMD_CoMD_weak_omp_comd_1_1__gcc_10_3_0_N_1_MPI_1_OMP_8
   - builtin
      * num_tasks: 1
      * Total Time: 11.6725 s
------------------------------------------------------------------------------
CoMD_CoMD_weak_omp_comd_1_1__gcc_10_3_0_N_1_MPI_1_OMP_16
   - builtin
      * num_tasks: 1
      * Total Time: 6.205 s
------------------------------------------------------------------------------
CoMD_CoMD_weak_omp_comd_1_1__gcc_10_3_0_N_1_MPI_1_OMP_32
   - builtin
      * num_tasks: 1
      * Total Time: 3.6328 s
------------------------------------------------------------------------------
CoMD_CoMD_weak_omp_comd_1_1__gcc_10_3_0_N_1_MPI_1_OMP_64
   - builtin
      * num_tasks: 1
      * Total Time: 2.2041 s
------------------------------------------------------------------------------
CoMD_CoMD_weak_omp_comd_1_1__nvhpc_21_2_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Total Time: 37.1681 s
------------------------------------------------------------------------------
CoMD_CoMD_weak_omp_comd_1_1__nvhpc_21_2_N_1_MPI_1_OMP_2
   - builtin
      * num_tasks: 1
      * Total Time: 25.9963 s
------------------------------------------------------------------------------
CoMD_CoMD_weak_omp_comd_1_1__nvhpc_21_2_N_1_MPI_1_OMP_4
   - builtin
      * num_tasks: 1
      * Total Time: 25.3826 s
------------------------------------------------------------------------------
CoMD_CoMD_weak_omp_comd_1_1__nvhpc_21_2_N_1_MPI_1_OMP_8
   - builtin
      * num_tasks: 1
      * Total Time: 12.6117 s
------------------------------------------------------------------------------
CoMD_CoMD_weak_omp_comd_1_1__nvhpc_21_2_N_1_MPI_1_OMP_16
   - builtin
      * num_tasks: 1
      * Total Time: 8.5052 s
------------------------------------------------------------------------------
CoMD_CoMD_weak_omp_comd_1_1__nvhpc_21_2_N_1_MPI_1_OMP_32
   - builtin
      * num_tasks: 1
      * Total Time: 3.6825 s
------------------------------------------------------------------------------
CoMD_CoMD_weak_omp_comd_1_1__nvhpc_21_2_N_1_MPI_1_OMP_64
   - builtin
      * num_tasks: 1
      * Total Time: 1.6399 s
------------------------------------------------------------------------------
```

### On-node Compiler Comparison

Performance comparison of two available compilers on the ARM HPC. 

| Cores | gcc@10.3.0 | arm@21.0.0.879 | nvhpc@21.2 |
|-------|------------|----------------|------------|
|   1   |  74.44     |  64.62         |  56.42     |
|   2   |  37.43     |  32.46         |  28.46     |
|   4   |  18.90     |  16.48         |  14.42     |
|   8   |  10.46     |  9.10         |  7.96     |
|   16  |  5.56     |  4.85         |  4.22     |
|   32  |  3.10     |  2.68         |  2.32     |
|   64  |  1.90     |  1.78         |  1.59     |

### Serial Hot-spot Profile

This test was not hot-spot profiled.


### Full Node Hot-spot Profile

This test was not full node profiled.

### Strong Scaling Study

On-node scaling study for two compilers.

| Cores | gcc@10.3.0 | arm@21.0.0.879 |
|-------|------------|----------------|
|   1   |  74.44     |  64.62         |
|   2   |  37.43     |  32.46         |
|   4   |  18.90     |  16.48         |
|   8   |  10.46     |  9.10         |
|   16  |  5.56     |  4.85         |
|   32  |  3.10     |  2.68         |
|   64  |  1.90     |  1.78         |

### Off-Node Scaling Study

Off-node scaling was not done.

### On-Node Architecture Comparison

On-node scaling study comparing C5n and C6gn instances was done with `gcc` and `nvhpc`

Results from `gcc` on the different instance types.

| Cores | C6gn (ARM) | C5n (x86/Intel) |
|-------|------------|----------------|
|   1   |  74.44     |  67.73         |
|   2   |  37.43     |  42.10         |
|   4   |  18.90     |  20.98         |
|   8   |  10.46     |  11.67         |
|   16  |  5.56     |  6.20         |
|   32  |  3.10     |  3.63         |
|   64  |  1.90     |  2.20         |

Results from `nvhpc` on the different instance types.

| Cores | C6gn (ARM) | C5n (x86/Intel) |
|-------|------------|----------------|
|   1   |  56.42     |  37.16         |
|   2   |  28.46     |  25.99         |
|   4   |  14.42     |  25.38         |
|   8   |  7.96     |  12.61         |
|   16  |  4.22     |  8.50         |
|   32  |  2.32     |  3.68         |
|   64  |  1.59     |  1.63         |


Compiler optimization not tested.

## Test Case 4

[ReFrame Benchmark 4](#)

Optimized compiler flag testing on the ARM HPC with `gcc`, `nvhpc` and `arm` compilers.

```
reframe -c comd_weak_omp_optimized.py -r --performance-report
```

### Validation

See `Test Case 3`'s description. This test is split out because it focuses on trying compiler optimizations, mainly on the ARM HPC with all available compilers. See the "Optimisation" second for a summary of results and compilers and respective flags used.

See `comd_weak_omp_optimized.py` for the steps, data download and copy of the test from CoMD's website.


### ReFrame Output

ReFrame output from the ARM HPC.

```
==============================================================================
PERFORMANCE REPORT
------------------------------------------------------------------------------
CoMD_CoMD_weak_omp_optimize_compiler_flags_comd_1_1__gcc_10_3_0_N_1_MPI_1_OMP_1
- aws:c6gn
   - builtin
      * num_tasks: 1
      * Total Time: 74.1731 s
------------------------------------------------------------------------------
CoMD_CoMD_weak_omp_optimize_compiler_flags_comd_1_1__gcc_10_3_0_N_1_MPI_1_OMP_2
   - builtin
      * num_tasks: 1
      * Total Time: 37.4698 s
------------------------------------------------------------------------------
CoMD_CoMD_weak_omp_optimize_compiler_flags_comd_1_1__gcc_10_3_0_N_1_MPI_1_OMP_4
   - builtin
      * num_tasks: 1
      * Total Time: 18.9969 s
------------------------------------------------------------------------------
CoMD_CoMD_weak_omp_optimize_compiler_flags_comd_1_1__gcc_10_3_0_N_1_MPI_1_OMP_8
   - builtin
      * num_tasks: 1
      * Total Time: 10.4386 s
------------------------------------------------------------------------------
CoMD_CoMD_weak_omp_optimize_compiler_flags_comd_1_1__gcc_10_3_0_N_1_MPI_1_OMP_16
   - builtin
      * num_tasks: 1
      * Total Time: 5.5555 s
------------------------------------------------------------------------------
CoMD_CoMD_weak_omp_optimize_compiler_flags_comd_1_1__gcc_10_3_0_N_1_MPI_1_OMP_32
   - builtin
      * num_tasks: 1
      * Total Time: 3.0709 s
------------------------------------------------------------------------------
CoMD_CoMD_weak_omp_optimize_compiler_flags_comd_1_1__gcc_10_3_0_N_1_MPI_1_OMP_36
   - builtin
      * num_tasks: 1
      * Total Time: 2.8487 s
------------------------------------------------------------------------------
CoMD_CoMD_weak_omp_optimize_compiler_flags_comd_1_1__gcc_10_3_0_N_1_MPI_1_OMP_64
   - builtin
      * num_tasks: 1
      * Total Time: 1.935 s
------------------------------------------------------------------------------
CoMD_CoMD_weak_omp_optimize_compiler_flags_comd_1_1__arm_21_0_0_879_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Total Time: 64.3581 s
------------------------------------------------------------------------------
CoMD_CoMD_weak_omp_optimize_compiler_flags_comd_1_1__arm_21_0_0_879_N_1_MPI_1_OMP_2
   - builtin
      * num_tasks: 1
      * Total Time: 32.4968 s
------------------------------------------------------------------------------
CoMD_CoMD_weak_omp_optimize_compiler_flags_comd_1_1__arm_21_0_0_879_N_1_MPI_1_OMP_4
   - builtin
      * num_tasks: 1
      * Total Time: 16.4493 s
------------------------------------------------------------------------------
CoMD_CoMD_weak_omp_optimize_compiler_flags_comd_1_1__arm_21_0_0_879_N_1_MPI_1_OMP_8
   - builtin
      * num_tasks: 1
      * Total Time: 9.0953 s
------------------------------------------------------------------------------
CoMD_CoMD_weak_omp_optimize_compiler_flags_comd_1_1__arm_21_0_0_879_N_1_MPI_1_OMP_16
   - builtin
      * num_tasks: 1
      * Total Time: 4.8372 s
------------------------------------------------------------------------------
CoMD_CoMD_weak_omp_optimize_compiler_flags_comd_1_1__arm_21_0_0_879_N_1_MPI_1_OMP_32
   - builtin
      * num_tasks: 1
      * Total Time: 2.6707 s
------------------------------------------------------------------------------
CoMD_CoMD_weak_omp_optimize_compiler_flags_comd_1_1__arm_21_0_0_879_N_1_MPI_1_OMP_36
   - builtin
      * num_tasks: 1
      * Total Time: 2.4786 s
------------------------------------------------------------------------------
CoMD_CoMD_weak_omp_optimize_compiler_flags_comd_1_1__arm_21_0_0_879_N_1_MPI_1_OMP_64
   - builtin
      * num_tasks: 1
      * Total Time: 1.7449 s
------------------------------------------------------------------------------
CoMD_CoMD_weak_omp_optimize_compiler_flags_comd_1_1__nvhpc_21_2_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Total Time: 56.4017 s
------------------------------------------------------------------------------
CoMD_CoMD_weak_omp_optimize_compiler_flags_comd_1_1__nvhpc_21_2_N_1_MPI_1_OMP_2
   - builtin
      * num_tasks: 1
      * Total Time: 28.4105 s
------------------------------------------------------------------------------
CoMD_CoMD_weak_omp_optimize_compiler_flags_comd_1_1__nvhpc_21_2_N_1_MPI_1_OMP_4
   - builtin
      * num_tasks: 1
      * Total Time: 14.587 s
------------------------------------------------------------------------------
CoMD_CoMD_weak_omp_optimize_compiler_flags_comd_1_1__nvhpc_21_2_N_1_MPI_1_OMP_8
   - builtin
      * num_tasks: 1
      * Total Time: 7.999 s
------------------------------------------------------------------------------
CoMD_CoMD_weak_omp_optimize_compiler_flags_comd_1_1__nvhpc_21_2_N_1_MPI_1_OMP_16
   - builtin
      * num_tasks: 1
      * Total Time: 4.2243 s
------------------------------------------------------------------------------
CoMD_CoMD_weak_omp_optimize_compiler_flags_comd_1_1__nvhpc_21_2_N_1_MPI_1_OMP_32
   - builtin
      * num_tasks: 1
      * Total Time: 2.3321 s
------------------------------------------------------------------------------
CoMD_CoMD_weak_omp_optimize_compiler_flags_comd_1_1__nvhpc_21_2_N_1_MPI_1_OMP_36
   - builtin
      * num_tasks: 1
      * Total Time: 2.1806 s
------------------------------------------------------------------------------
CoMD_CoMD_weak_omp_optimize_compiler_flags_comd_1_1__nvhpc_21_2_N_1_MPI_1_OMP_64
   - builtin
      * num_tasks: 1
      * Total Time: 1.5382 s
------------------------------------------------------------------------------
```

Compiler optimization not run on the c5n (x86) HPC.

## Optimisation

Details of steps taken to optimise performance of the application.
Please document work with compiler flags, maths libraries, system libraries, code optimisations, etc.



### Compiler Flag Tuning

Same OpenMP compiling was done as in `Test Case 3`. Just different flags via `spack edit comd`. Here is a diff of the flags tried per-architecture.

```
     @property
     def build_targets(self):
         targets = []
```
Compiler flas before:
```
-        cflags = ' -std=c99 '
-        optflags = ' -g -O5 '
```

Compiler flags after:
```
+        # ARM HPC w/armclang
+        #cflags = ' -mcpu=native -std=c99 '
+        #optflags = ' -g -O5 -Ofast'
+
+        # ARM HPC w/gcc
+        cflags = ' -mcpu=native -std=c99 '
+        optflags = ' -g -Ofast -ffast-math'
+
+        # ARM HPC w/nvc
+        cflags = ' -std=c99 -mp=multicore'
+        optflags = ' -g -O4 -fast'
```

#### Compiler Flag Performance

`nvhpc` on C6gn (ARM), which was the best, previously observed performance before optimization.

No large difference observed. 

| Cores | Original Flags | New Flags |
|-------|------------|----------------|
|   1   |  56.42     |  56.40         |
|   2   |  28.46     |  28.41         |
|   4   |  14.42     |  14.587         |
|   8   |  7.96     |  7.99         |
|   16  |  4.22     |  4.22         |
|   32  |  2.32     |  2.33         |
|   64  |  1.59     |  2.18         |

Both `gcc` and `nvhpcc` also have very similar results. The spack config was double-checked to confirm it has the updated flags.

### Maths Library Report

Maths library report not generated.


### Performance Regression

OpenMP is the fastest the code has been observed. Compared to MPI, OpenMP allows for running `CoMD` with a linear(ish) increase per core. The changes done as part of this work were to enable OpenMP to correctly compile. MPI has limitations for `comd` based on CLI parameters of the analysis; however, OpenMP does not.

Testing showed sub-2 second timing for running the first "weak scaling" example step from `CoMD`. This is compared to the 30 seconds the test normally takes.


## Report

### Compilation Summary

Compilation of `CoMD` using MPI and appears to work equally well on the x86 HPC and ARM-based HPC. There were no surprises related to porting it to ARM and getting the code to correctly work with `spack`.

OpenMP builds of `CoMD` require `-mpi +openmp` and need the diff given in the intro. These builds were previously broken due to two different issues; however, when the PR merges the code will work as expected.

### Performance Summary

`CoMD` has notably better performance with the C6gn (ARM) HPC compared to the C5n HPC. The observed difference was that the x86 HPC was measurably slower, approximately 1.16x the time required (369.6s / 319.4s). This observation was consistent across scaled up workloads using MPI in both the "weak" and "strong scaling" tests that were added to this repo via ReFrame code. These tests and example potential data were taken directly from CoMD's repository.

Three different compilers were used on the C6gn (ARM) HPC to compare compiler differences: `gcc`, `arm` and `nvhpc`. The `nvhpc` compiler was observed to perform best, `arm` second and `gcc` last. This was across both the "weak scaling" and "strong scaling" tests. The approximate difference compared to `nvhpc` was that `arm` took 1.38x the time (39.50/28.58) and `gcc` took 1.57x the time (44.91/28.58). Under the heaviest load tested similar differences were also observed. `arm` was 1.37x the time (306.8 / 224.3) and `gcc` was 1.54x the time (344.8 / 224.3).

Overall, the `nvhpc` appear to perform best; however, all three compilers appear to work fine and `CoMD` produces identical results.


### Optimisation Summary

Compiler optimization did not appear to notably change the performance of the three compilers on the ARM HPC. The spack package for `comd` appears to compile efficiently with its existing flags.

`CoMD` appears to scale workload successfully via MPI; however, the program requires specific combinations of the `-i`, `-j` and `-k` flags to match the given MPI number.

OpenMP builds showed impressive results, almost halving the time to process for every doubling of processors. The more cores the better. This observation worked up to 64 cores. Using OpenMP instead of MPI seems to make the most sense when using this software package since the performance gains are not limited to CoMD's `-i * -j * -k` CLI equaling the exact number of MPI.
