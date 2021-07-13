# Remhos 

**Description:** (REMap High-Order Solver) is a CEED miniapp that performs monotonic and conservative high-order discontinuous field interpolation (remap) using DG advection-based spatial discretization and explicit high-order time-stepping.

**URL:** https://github.com/CEED/Remhos/tree/v1.0

**Team:** C3SR

## Compilation

### Spack Package Modification

Details of any changes to the Spack recipe used.

Git commit hash of checkout for package: 667ab50 (current HEAD of Spack)

Pull request for Spack recipe changes: No changes are required

### Building Remhos



#### Compiler 1: GCC 10.3.0

```
spack install remhos%gcc@10.3.0
```

```
$ spack spec -Il remhos%gcc@10.3.0

[+]  cbm2ozl  remhos@1.0%gcc@10.3.0+metis arch=linux-amzn2-graviton2
[+]  5qtpyhi      ^mfem@4.2.0%gcc@10.3.0~amgx~conduit~cuda~debug~examples~gnutls~gslib~lapack~libceed~libunwind+metis~miniapps~mpfr+mpi~netcdf~occa~openmp~petsc~pumi~raja~rocm~shared~slepc+static~strumpack~suite-sparse~sundials~superlu-dist~threadsafe~umpire+zlib amdgpu_target=none cuda_arch=none timer=auto arch=linux-amzn2-graviton2
[+]  iqm2dsc          ^hypre@2.20.0%gcc@10.3.0~complex~cuda~debug~int64~internal-superlu~mixedint+mpi~openmp+shared~superlu-dist~unified-memory cuda_arch=none patches=6e3336b1d62155f6350dfe42b0f9ea25d4fa0af60c7e540959139deb93a26059 arch=linux-amzn2-graviton2
[+]  rv7gj6u              ^openblas@0.3.15%gcc@10.3.0~bignuma~consistent_fpcsr~ilp64+locking+pic+shared threads=none arch=linux-amzn2-graviton2
[+]  4m7exgb                  ^perl@5.32.1%gcc@10.3.0+cpanm+shared+threads arch=linux-amzn2-graviton2
[+]  y42m6yr                      ^berkeley-db@18.1.40%gcc@10.3.0+cxx~docs+stl patches=b231fcc4d5cff05e5c3a4814f6a5af0e9a966428dc2176540d2c05aff41de522 arch=linux-amzn2-graviton2
[+]  rqrpmap                      ^bzip2@1.0.8%gcc@10.3.0~debug~pic+shared arch=linux-amzn2-graviton2
[+]  2w7bert                          ^diffutils@3.7%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  y5ei3cm                              ^libiconv@1.16%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  wjwqncx                      ^gdbm@1.19%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  3zy7kxk                          ^readline@8.1%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  iwzirqc                              ^ncurses@6.2%gcc@10.3.0~symlinks+termlib abi=none arch=linux-amzn2-graviton2
[+]  s4pw7zm                                  ^pkgconf@1.7.4%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  qepjcvj                      ^zlib@1.2.11%gcc@10.3.0+optimize+pic+shared arch=linux-amzn2-graviton2
[+]  zvamksn              ^openmpi@4.1.0%gcc@10.3.0~atomics~cuda~cxx~cxx_exceptions+gpfs~internal-hwloc~java~legacylaunchers~lustre~memchecker+pmi~singularity~sqlite3+static~thread_multiple+vt+wrapper-rpath fabrics=ofi patches=60ce20bc14d98c572ef7883b9fcd254c3f232c2f3a13377480f96466169ac4c8 schedulers=slurm arch=linux-amzn2-graviton2
[+]  cukmqbg                  ^hwloc@2.5.0%gcc@10.3.0~cairo~cuda~gl~libudev+libxml2~netloc~nvml+pci+shared arch=linux-amzn2-graviton2
[+]  asgtk6a                      ^libpciaccess@0.16%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  z2uysov                          ^libtool@2.4.6%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  ebhjpix                              ^m4@1.4.18%gcc@10.3.0+sigsegv patches=3877ab548f88597ab2327a2230ee048d2d07ace1062efe81fc92e91b7f39cd00,fc9b61654a3ba1a8d6cd78ce087e7c96366c290bc8d2c299f09828d793b853c8 arch=linux-amzn2-graviton2
[+]  ltbv6bk                                  ^libsigsegv@2.13%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  4xr3hhh                          ^util-macros@1.19.3%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  iyhm3wi                      ^libxml2@2.9.10%gcc@10.3.0~python arch=linux-amzn2-graviton2
[+]  ye3kcvv                          ^xz@5.2.5%gcc@10.3.0~pic libs=shared,static arch=linux-amzn2-graviton2
[+]  tadxrfp                  ^libevent@2.1.12%gcc@10.3.0+openssl arch=linux-amzn2-graviton2
[+]  5i3lgfb                      ^openssl@1.1.1k%gcc@10.3.0~docs+systemcerts arch=linux-amzn2-graviton2
[+]  72f5gvk                  ^libfabric@1.11.1-aws%gcc@10.3.0~debug~kdreg fabrics=sockets,tcp,udp arch=linux-amzn2-graviton2
[+]  mhav5gn                  ^numactl@2.0.14%gcc@10.3.0 patches=4e1d78cbbb85de625bad28705e748856033eaafab92a66dffd383a3d7e00cc94,62fc8a8bf7665a60e8f4c93ebbd535647cebf74198f7afafec4c085a8825c006 arch=linux-amzn2-graviton2
[+]  jkuhz64                      ^autoconf@2.69%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  xb2w5nc                      ^automake@1.16.3%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  wturp6c                  ^openssh@8.5p1%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  ivotdt7                      ^libedit@3.1-20210216%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  wqpuvmh                  ^slurm@20-02-4-1%gcc@10.3.0~gtk~hdf5~hwloc~mariadb~pmix+readline~restd sysconfdir=PREFIX/etc arch=linux-amzn2-graviton2
[+]  a3tjh3r          ^metis@5.1.0%gcc@10.3.0~gdb~int64~real64+shared build_type=Release patches=4991da938c1d3a1d3dea78e49bbebecba00273f98df2a656e38b83d55b281da1,b1225da886605ea558db7ac08dd8054742ea5afe5ed61ad4d0fe7a495b1270d2 arch=linux-amzn2-graviton2
[+]  m7325ee              ^cmake@3.20.5%gcc@10.3.0~doc+ncurses+openssl+ownlibs~qt build_type=Release arch=linux-amzn2-graviton2
```

#### Compiler 2: Arm 21.0.0.879

```
spack install remhos%arm@21.0.0.879
```

```
$ spack spec -Il remhos%arm@21.0.0.879

[+]  q2vad4t  remhos@1.0%arm@21.0.0.879+metis arch=linux-amzn2-aarch64
[+]  gpr7usm      ^mfem@4.2.0%arm@21.0.0.879~amgx~conduit~cuda~debug~examples~gnutls~gslib~lapack~libceed~libunwind+metis~miniapps~mpfr+mpi~netcdf~occa~openmp~petsc~pumi~raja~rocm~shared~slepc+static~strumpack~suite-sparse~sundials~superlu-dist~threadsafe~umpire+zlib amdgpu_target=none cuda_arch=none timer=auto arch=linux-amzn2-aarch64
[+]  fihv4qx          ^hypre@2.20.0%arm@21.0.0.879~complex~cuda~debug~int64~internal-superlu~mixedint+mpi~openmp+shared~superlu-dist~unified-memory cuda_arch=none patches=6e3336b1d62155f6350dfe42b0f9ea25d4fa0af60c7e540959139deb93a26059 arch=linux-amzn2-aarch64
[+]  cwuo4ek              ^openblas@0.3.15%arm@21.0.0.879~bignuma~consistent_fpcsr~ilp64+locking+pic+shared threads=none arch=linux-amzn2-aarch64
[+]  vv6txro                  ^perl@5.32.1%arm@21.0.0.879+cpanm+shared+threads arch=linux-amzn2-aarch64
[+]  33wiajj                      ^berkeley-db@18.1.40%arm@21.0.0.879+cxx~docs+stl patches=b231fcc4d5cff05e5c3a4814f6a5af0e9a966428dc2176540d2c05aff41de522 arch=linux-amzn2-aarch64
[+]  z4ybgri                      ^bzip2@1.0.8%arm@21.0.0.879~debug~pic+shared arch=linux-amzn2-aarch64
[+]  adtc6yc                          ^diffutils@3.7%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  7vnthzn                              ^libiconv@1.16%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  645q4qj                      ^gdbm@1.19%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  3haw5gt                          ^readline@8.1%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  uhtqtlb                              ^ncurses@6.2%arm@21.0.0.879~symlinks+termlib abi=none arch=linux-amzn2-aarch64
[+]  zpuzm23                                  ^pkgconf@1.7.4%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  puuxvg2                      ^zlib@1.2.11%arm@21.0.0.879+optimize+pic+shared arch=linux-amzn2-aarch64
[+]  lmaoy5t              ^openmpi@4.1.0%arm@21.0.0.879~atomics~cuda~cxx~cxx_exceptions+gpfs~internal-hwloc~java~legacylaunchers~lustre~memchecker+pmi~singularity~sqlite3+static~thread_multiple+vt+wrapper-rpath fabrics=ofi patches=60ce20bc14d98c572ef7883b9fcd254c3f232c2f3a13377480f96466169ac4c8 schedulers=slurm arch=linux-amzn2-aarch64
[+]  xl6anaa                  ^hwloc@2.5.0%arm@21.0.0.879~cairo~cuda~gl~libudev+libxml2~netloc~nvml+pci+shared arch=linux-amzn2-aarch64
[+]  jueqz7p                      ^libpciaccess@0.16%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  e4ssqx6                          ^libtool@2.4.6%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  i2jmeo4                              ^m4@1.4.18%arm@21.0.0.879+sigsegv patches=3877ab548f88597ab2327a2230ee048d2d07ace1062efe81fc92e91b7f39cd00,fc9b61654a3ba1a8d6cd78ce087e7c96366c290bc8d2c299f09828d793b853c8 arch=linux-amzn2-aarch64
[+]  6jhzlul                                  ^libsigsegv@2.13%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  uwcxkin                          ^util-macros@1.19.3%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  dypqz2i                      ^libxml2@2.9.10%arm@21.0.0.879~python arch=linux-amzn2-aarch64
[+]  zqsab4f                          ^xz@5.2.5%arm@21.0.0.879~pic libs=shared,static arch=linux-amzn2-aarch64
[+]  gonqskn                  ^libevent@2.1.12%arm@21.0.0.879+openssl arch=linux-amzn2-aarch64
[+]  vc3waha                      ^openssl@1.1.1k%arm@21.0.0.879~docs+systemcerts arch=linux-amzn2-aarch64
[+]  qdn27nh                  ^libfabric@1.11.1-aws%arm@21.0.0.879~debug~kdreg fabrics=sockets,tcp,udp arch=linux-amzn2-aarch64
[+]  mv2g7r5                  ^numactl@2.0.14%arm@21.0.0.879 patches=4e1d78cbbb85de625bad28705e748856033eaafab92a66dffd383a3d7e00cc94,62fc8a8bf7665a60e8f4c93ebbd535647cebf74198f7afafec4c085a8825c006 arch=linux-amzn2-aarch64
[+]  dcs645r                      ^autoconf@2.69%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  edezkz3                      ^automake@1.16.3%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  6vvthuo                  ^openssh@8.5p1%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  xe4evc4                      ^libedit@3.1-20210216%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  x5xehti                  ^slurm@20-02-4-1%arm@21.0.0.879~gtk~hdf5~hwloc~mariadb~pmix+readline~restd sysconfdir=PREFIX/etc arch=linux-amzn2-aarch64
[+]  myrsq4g          ^metis@5.1.0%arm@21.0.0.879~gdb~int64~real64+shared build_type=Release patches=4991da938c1d3a1d3dea78e49bbebecba00273f98df2a656e38b83d55b281da1 arch=linux-amzn2-aarch64
[+]  fqvybaf              ^cmake@3.20.5%arm@21.0.0.879~doc+ncurses+openssl+ownlibs~qt build_type=Release arch=linux-amzn2-aarch64
```

#### Compiler 3: NVHPC 21.2
Note that nvhpc conflicts with cmake and its upstream/downstream dependencies. Therefore, we compile these dependencies with gcc instead of nvhpc.

```
spack install remhos%nvhpc@21.2 ^cmake%gcc@10.3.0 ^zlib%gcc@10.3.0 ^openblas%gcc@10.3.0
```

```
$ spack spec -Il remhos%nvhpc@21.2 ^cmake%gcc@10.3.0 ^zlib%gcc@10.3.0 ^openblas%gcc@10.3.0

[+]  ykj5gel  remhos@1.0%nvhpc@21.2+metis arch=linux-amzn2-graviton2
[+]  vw7uuvz      ^mfem@4.2.0%nvhpc@21.2~amgx~conduit~cuda~debug~examples~gnutls~gslib~lapack~libceed~libunwind+metis~miniapps~mpfr+mpi~netcdf~occa~openmp~petsc~pumi~raja~rocm~shared~slepc+static~strumpack~suite-sparse~sundials~superlu-dist~threadsafe~umpire+zlib amdgpu_target=none cuda_arch=none timer=auto arch=linux-amzn2-graviton2
[+]  ujlyezy          ^hypre@2.20.0%nvhpc@21.2~complex~cuda~debug~int64~internal-superlu~mixedint+mpi~openmp+shared~superlu-dist~unified-memory cuda_arch=none patches=6e3336b1d62155f6350dfe42b0f9ea25d4fa0af60c7e540959139deb93a26059 arch=linux-amzn2-graviton2
[+]  rv7gj6u              ^openblas@0.3.15%gcc@10.3.0~bignuma~consistent_fpcsr~ilp64+locking+pic+shared threads=none arch=linux-amzn2-graviton2
[+]  3exmk65                  ^perl@5.32.1%nvhpc@21.2+cpanm+shared+threads patches=21cf6a73cec16760f8de2e8895ace1299aff2d8e92dc581cd18f1d95a4503048 arch=linux-amzn2-graviton2
[+]  5uyf3k4                      ^berkeley-db@18.1.40%nvhpc@21.2+cxx~docs+stl patches=b231fcc4d5cff05e5c3a4814f6a5af0e9a966428dc2176540d2c05aff41de522 arch=linux-amzn2-graviton2
[+]  wsi7g3j                      ^bzip2@1.0.8%nvhpc@21.2~debug~pic+shared arch=linux-amzn2-graviton2
[+]  s4mb5no                          ^diffutils@3.7%nvhpc@21.2 patches=6e42dc243f17aab29fd167f060f5bc1f08813e03368eb301b43c95d4b1386681 arch=linux-amzn2-graviton2
[+]  r7mmkdp                              ^libiconv@1.16%nvhpc@21.2 arch=linux-amzn2-graviton2
[+]  m2wdbeo                      ^gdbm@1.19%nvhpc@21.2 arch=linux-amzn2-graviton2
[+]  zori3wf                          ^readline@8.1%nvhpc@21.2 arch=linux-amzn2-graviton2
[+]  asgm7mt                              ^ncurses@6.2%nvhpc@21.2~symlinks+termlib abi=none arch=linux-amzn2-graviton2
[+]  vtiml6g                                  ^pkgconf@1.7.4%nvhpc@21.2 arch=linux-amzn2-graviton2
[+]  qepjcvj                      ^zlib@1.2.11%gcc@10.3.0+optimize+pic+shared arch=linux-amzn2-graviton2
[+]  kxm5yi7              ^openmpi@4.1.0%nvhpc@21.2~atomics~cuda~cxx~cxx_exceptions+gpfs~internal-hwloc~java~legacylaunchers~lustre~memchecker+pmi~singularity~sqlite3+static~thread_multiple+vt+wrapper-rpath fabrics=ofi patches=60ce20bc14d98c572ef7883b9fcd254c3f232c2f3a13377480f96466169ac4c8,fba0d3a784a9723338722b48024a22bb32f6a951db841a4e9f08930a93f41d7a schedulers=slurm arch=linux-amzn2-graviton2
[+]  cma7gv7                  ^hwloc@2.5.0%nvhpc@21.2~cairo~cuda~gl~libudev+libxml2~netloc~nvml+pci+shared arch=linux-amzn2-graviton2
[+]  e4m4ued                      ^libpciaccess@0.16%nvhpc@21.2 patches=6e08dc445ece06e9e8b1344397f2d3f169005703ddc0f2ae24f366cde78c7377 arch=linux-amzn2-graviton2
[+]  kk4ax3i                          ^libtool@2.4.6%nvhpc@21.2 arch=linux-amzn2-graviton2
[+]  6c4kz5g                              ^m4@1.4.18%nvhpc@21.2+sigsegv patches=3877ab548f88597ab2327a2230ee048d2d07ace1062efe81fc92e91b7f39cd00,5746cf51f45b405661c3edae7a78c33d41e54d83f635d16e2bf1f956dbfbf635,fc9b61654a3ba1a8d6cd78ce087e7c96366c290bc8d2c299f09828d793b853c8 arch=linux-amzn2-graviton2
[+]  pa6wm5j                                  ^libsigsegv@2.13%nvhpc@21.2 arch=linux-amzn2-graviton2
[+]  4imdwuy                          ^util-macros@1.19.3%nvhpc@21.2 arch=linux-amzn2-graviton2
[+]  6t3d2gf                      ^libxml2@2.9.10%nvhpc@21.2~python patches=05ff238cf435825ef835c7ae39376b52dc83d8caf19e962f0766c841386a305a,10a88ad47f9797cf7cf2d7d07241f665a3b6d1f31fa026728c8c2ae93e1664e9 arch=linux-amzn2-graviton2
[+]  br733tn                          ^xz@5.2.5%nvhpc@21.2~pic libs=shared,static arch=linux-amzn2-graviton2
[+]  7r56fbr                  ^libevent@2.1.12%nvhpc@21.2+openssl arch=linux-amzn2-graviton2
[+]  dnkus2k                      ^openssl@1.1.1k%nvhpc@21.2~docs+systemcerts arch=linux-amzn2-graviton2
[+]  xl6zavq                  ^libfabric@1.11.1-aws%nvhpc@21.2~debug~kdreg fabrics=sockets,tcp,udp arch=linux-amzn2-graviton2
[+]  5yq4tpw                  ^numactl@2.0.14%nvhpc@21.2 patches=4e1d78cbbb85de625bad28705e748856033eaafab92a66dffd383a3d7e00cc94,62fc8a8bf7665a60e8f4c93ebbd535647cebf74198f7afafec4c085a8825c006 arch=linux-amzn2-graviton2
[+]  n53ocxh                      ^autoconf@2.69%nvhpc@21.2 arch=linux-amzn2-graviton2
[+]  jbjqmqr                      ^automake@1.16.3%nvhpc@21.2 arch=linux-amzn2-graviton2
[+]  gfp4dte                  ^openssh@8.5p1%nvhpc@21.2 arch=linux-amzn2-graviton2
[+]  yvqpq74                      ^libedit@3.1-20210216%nvhpc@21.2 arch=linux-amzn2-graviton2
[+]  zehhooy                  ^slurm@20-02-4-1%nvhpc@21.2~gtk~hdf5~hwloc~mariadb~pmix+readline~restd sysconfdir=PREFIX/etc arch=linux-amzn2-graviton2
[+]  h2ymlmt          ^metis@5.1.0%nvhpc@21.2~gdb~int64~real64+shared build_type=Release patches=4991da938c1d3a1d3dea78e49bbebecba00273f98df2a656e38b83d55b281da1 arch=linux-amzn2-graviton2
[+]  hz44w7s              ^cmake@3.20.5%gcc@10.3.0~doc+ncurses+openssl+ownlibs~qt build_type=Release arch=linux-amzn2-graviton2
```

### Validating Remhos
[ReFrame Validation Script](remhos_validation.py)

```
reframe -c remhos_validation.py -r --performance-report -v
```

#### Validation Test Cases Details
For validation, we have a combination of 3 compilers, 7 mpi parameters and 4 test cases, which results into 84 test runs in total. The 3 compilers are` gcc@10.3.0`, `arm@21.0.0.879`, and `nvhpc@21.2`. The 7 mpi parameters are numbers of CPUs used, which are powers of 2 from 1(2^0) to 64(2^6). The 4 test cases are verification of 6, 7, 9, and 10 of https://github.com/CEED/Remhos/tree/v1.0#verification-of-results, which are chosen to cover the {Remap Mode, Transport Mode} x {2D Mode, 3D Mode} combination. As suggested by Remhos, we compare the resulting `mass` and `max` to the values, with a tolerance of relative error of `1e-9`. 

| Test Case     | `mass`        | `max`        |
|---------------|---------------|--------------|
| 2DRemap       | 0.08479546727 | 0.8378749205 |
| 3DRemap       | 0.1197297047  | 0.9985405673 |
| 2DTransport   | 0.1623263888  | 0.7469836332 |
| 3DTransport   | 0.9607429525  | 0.767823337  |

#### [ReFrame Validation Output](validation.txt)

```
[ [32m      OK[0m ] ( 1/84) Remhos_Remhos3DTransportValidationTest_remhos_1_0_arm_21_0_0_879_N_1_MPI_16_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 6.260s total: 6.422s]
==> timings: setup: 0.006s compile: 0.005s run: 6.260s sanity: 0.001s performance: 0.074s total: 6.422s
[ [32m      OK[0m ] ( 2/84) Remhos_Remhos3DTransportValidationTest_remhos_1_0_gcc_10_3_0_N_1_MPI_16_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 10.148s total: 10.325s]
==> timings: setup: 0.012s compile: 0.005s run: 10.148s sanity: 0.000s performance: 0.073s total: 10.325s
[ [32m      OK[0m ] ( 3/84) Remhos_Remhos3DTransportValidationTest_remhos_1_0_gcc_10_3_0_N_1_MPI_2_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 12.300s total: 12.476s]
==> timings: setup: 0.006s compile: 0.005s run: 12.300s sanity: 0.000s performance: 0.073s total: 12.476s
[ [32m      OK[0m ] ( 4/84) Remhos_Remhos3DTransportValidationTest_remhos_1_0_gcc_10_3_0_N_1_MPI_4_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 11.700s total: 11.869s]
==> timings: setup: 0.006s compile: 0.005s run: 11.700s sanity: 0.000s performance: 0.073s total: 11.869s
[ [32m      OK[0m ] ( 5/84) Remhos_Remhos2DTransportValidationTest_remhos_1_0_nvhpc_21_2_N_1_MPI_64_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 13.853s total: 14.041s]
==> timings: setup: 0.006s compile: 0.005s run: 13.853s sanity: 0.000s performance: 0.073s total: 14.041s
[ [32m      OK[0m ] ( 6/84) Remhos_Remhos2DTransportValidationTest_remhos_1_0_nvhpc_21_2_N_1_MPI_16_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 15.271s total: 15.444s]
==> timings: setup: 0.006s compile: 0.005s run: 15.271s sanity: 0.000s performance: 0.072s total: 15.444s
[ [32m      OK[0m ] ( 7/84) Remhos_Remhos2DTransportValidationTest_remhos_1_0_arm_21_0_0_879_N_1_MPI_32_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 18.653s total: 18.829s]
==> timings: setup: 0.006s compile: 0.005s run: 18.653s sanity: 0.000s performance: 0.073s total: 18.829s
[ [32m      OK[0m ] ( 8/84) Remhos_Remhos2DTransportValidationTest_remhos_1_0_arm_21_0_0_879_N_1_MPI_16_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 19.564s total: 19.745s]
==> timings: setup: 0.006s compile: 0.005s run: 19.564s sanity: 0.000s performance: 0.073s total: 19.745s
[ [32m      OK[0m ] ( 9/84) Remhos_Remhos2DTransportValidationTest_remhos_1_0_gcc_10_3_0_N_1_MPI_64_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 22.471s total: 22.637s]
==> timings: setup: 0.006s compile: 0.005s run: 22.471s sanity: 0.000s performance: 0.073s total: 22.637s
[ [32m      OK[0m ] (10/84) Remhos_Remhos2DTransportValidationTest_remhos_1_0_gcc_10_3_0_N_1_MPI_32_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 23.374s total: 23.541s]
==> timings: setup: 0.006s compile: 0.005s run: 23.374s sanity: 0.000s performance: 0.073s total: 23.541s
[ [32m      OK[0m ] (11/84) Remhos_Remhos2DTransportValidationTest_remhos_1_0_gcc_10_3_0_N_1_MPI_8_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 24.771s total: 24.934s]
==> timings: setup: 0.006s compile: 0.005s run: 24.771s sanity: 0.000s performance: 0.073s total: 24.934s
[ [32m      OK[0m ] (12/84) Remhos_Remhos3DRemapValidationTest_remhos_1_0_arm_21_0_0_879_N_1_MPI_1_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 34.224s total: 34.397s]
==> timings: setup: 0.006s compile: 0.005s run: 34.224s sanity: 0.000s performance: 0.073s total: 34.397s
[ [32m      OK[0m ] (13/84) Remhos_Remhos3DRemapValidationTest_remhos_1_0_nvhpc_21_2_N_1_MPI_8_OMP_1 on aws:c6gn using builtin [compile: 0.019s run: 28.895s total: 29.074s]
==> timings: setup: 0.006s compile: 0.019s run: 28.895s sanity: 0.000s performance: 0.073s total: 29.074s
[ [32m      OK[0m ] (14/84) Remhos_Remhos3DRemapValidationTest_remhos_1_0_nvhpc_21_2_N_1_MPI_16_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 28.444s total: 28.465s]
==> timings: setup: 0.006s compile: 0.005s run: 28.444s sanity: 0.000s performance: 0.073s total: 28.465s
[ [32m      OK[0m ] (15/84) Remhos_Remhos3DRemapValidationTest_remhos_1_0_arm_21_0_0_879_N_1_MPI_4_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 33.444s total: 33.602s]
==> timings: setup: 0.006s compile: 0.005s run: 33.444s sanity: 0.000s performance: 0.074s total: 33.602s
[ [32m      OK[0m ] (16/84) Remhos_Remhos2DRemapValidationTest_remhos_1_0_nvhpc_21_2_N_1_MPI_64_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 39.087s total: 39.261s]
==> timings: setup: 0.006s compile: 0.005s run: 39.087s sanity: 0.000s performance: 0.074s total: 39.261s
[ [32m      OK[0m ] (17/84) Remhos_Remhos2DRemapValidationTest_remhos_1_0_gcc_10_3_0_N_1_MPI_1_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 50.497s total: 50.518s]
==> timings: setup: 0.006s compile: 0.005s run: 50.497s sanity: 0.000s performance: 0.073s total: 50.518s
[ [32m      OK[0m ] (18/84) Remhos_Remhos2DRemapValidationTest_remhos_1_0_nvhpc_21_2_N_1_MPI_8_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 41.133s total: 41.304s]
==> timings: setup: 0.006s compile: 0.005s run: 41.133s sanity: 0.000s performance: 0.073s total: 41.304s
[ [32m      OK[0m ] (19/84) Remhos_Remhos2DRemapValidationTest_remhos_1_0_gcc_10_3_0_N_1_MPI_2_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 50.195s total: 50.216s]
==> timings: setup: 0.006s compile: 0.005s run: 50.195s sanity: 0.000s performance: 0.074s total: 50.216s
[ [32m      OK[0m ] (20/84) Remhos_Remhos2DRemapValidationTest_remhos_1_0_gcc_10_3_0_N_1_MPI_4_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 49.742s total: 49.763s]
==> timings: setup: 0.006s compile: 0.005s run: 49.742s sanity: 0.000s performance: 0.073s total: 49.763s
[ [32m      OK[0m ] (21/84) Remhos_Remhos2DRemapValidationTest_remhos_1_0_gcc_10_3_0_N_1_MPI_8_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 49.290s total: 49.311s]
==> timings: setup: 0.006s compile: 0.005s run: 49.290s sanity: 0.000s performance: 0.074s total: 49.311s
[ [32m      OK[0m ] (22/84) Remhos_Remhos3DTransportValidationTest_remhos_1_0_arm_21_0_0_879_N_1_MPI_64_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 9.479s total: 9.656s]
==> timings: setup: 0.006s compile: 0.005s run: 9.479s sanity: 0.000s performance: 0.074s total: 9.656s
[ [32m      OK[0m ] (23/84) Remhos_Remhos3DTransportValidationTest_remhos_1_0_nvhpc_21_2_N_1_MPI_2_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 9.221s total: 9.380s]
==> timings: setup: 0.006s compile: 0.005s run: 9.221s sanity: 0.000s performance: 0.073s total: 9.380s
[ [32m      OK[0m ] (24/84) Remhos_Remhos3DTransportValidationTest_remhos_1_0_nvhpc_21_2_N_1_MPI_64_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 7.964s total: 8.127s]
==> timings: setup: 0.006s compile: 0.005s run: 7.964s sanity: 0.000s performance: 0.074s total: 8.127s
[ [32m      OK[0m ] (25/84) Remhos_Remhos3DTransportValidationTest_remhos_1_0_nvhpc_21_2_N_1_MPI_32_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 5.369s total: 11.335s]
==> timings: setup: 0.006s compile: 0.005s run: 5.369s sanity: 0.000s performance: 0.073s total: 11.335s
[ [32m      OK[0m ] (26/84) Remhos_Remhos3DTransportValidationTest_remhos_1_0_nvhpc_21_2_N_1_MPI_1_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 14.901s total: 15.077s]
==> timings: setup: 0.006s compile: 0.005s run: 14.901s sanity: 0.000s performance: 0.074s total: 15.077s
[ [32m      OK[0m ] (27/84) Remhos_Remhos3DTransportValidationTest_remhos_1_0_nvhpc_21_2_N_1_MPI_16_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 5.603s total: 13.328s]
==> timings: setup: 0.006s compile: 0.005s run: 5.603s sanity: 0.000s performance: 0.075s total: 13.328s
[ [32m      OK[0m ] (28/84) Remhos_Remhos3DTransportValidationTest_remhos_1_0_nvhpc_21_2_N_1_MPI_8_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 5.366s total: 15.098s]
==> timings: setup: 0.006s compile: 0.005s run: 5.366s sanity: 0.000s performance: 0.073s total: 15.098s
[ [32m      OK[0m ] (29/84) Remhos_Remhos3DTransportValidationTest_remhos_1_0_nvhpc_21_2_N_1_MPI_4_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 6.446s total: 19.383s]
==> timings: setup: 0.006s compile: 0.005s run: 6.446s sanity: 0.000s performance: 0.074s total: 19.383s
[ [32m      OK[0m ] (30/84) Remhos_Remhos3DTransportValidationTest_remhos_1_0_arm_21_0_0_879_N_1_MPI_32_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 6.450s total: 22.863s]
==> timings: setup: 0.006s compile: 0.005s run: 6.450s sanity: 0.000s performance: 0.073s total: 22.863s
[ [32m      OK[0m ] (31/84) Remhos_Remhos3DTransportValidationTest_remhos_1_0_arm_21_0_0_879_N_1_MPI_8_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 6.462s total: 24.865s]
==> timings: setup: 0.006s compile: 0.005s run: 6.462s sanity: 0.000s performance: 0.074s total: 24.865s
[ [32m      OK[0m ] (32/84) Remhos_Remhos3DTransportValidationTest_remhos_1_0_arm_21_0_0_879_N_1_MPI_4_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 6.441s total: 26.613s]
==> timings: setup: 0.006s compile: 0.005s run: 6.441s sanity: 0.000s performance: 0.074s total: 26.613s
[ [32m      OK[0m ] (33/84) Remhos_Remhos3DTransportValidationTest_remhos_1_0_arm_21_0_0_879_N_1_MPI_2_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 7.751s total: 32.208s]
==> timings: setup: 0.006s compile: 0.005s run: 7.751s sanity: 0.000s performance: 0.074s total: 32.208s
[ [32m      OK[0m ] (34/84) Remhos_Remhos3DTransportValidationTest_remhos_1_0_gcc_10_3_0_N_1_MPI_32_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 5.736s total: 34.423s]
==> timings: setup: 0.006s compile: 0.005s run: 5.736s sanity: 0.000s performance: 0.074s total: 34.423s
[ [32m      OK[0m ] (35/84) Remhos_Remhos3DTransportValidationTest_remhos_1_0_gcc_10_3_0_N_1_MPI_64_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 7.730s total: 34.666s]
==> timings: setup: 0.006s compile: 0.005s run: 7.730s sanity: 0.000s performance: 0.074s total: 34.666s
[ [32m      OK[0m ] (36/84) Remhos_Remhos3DTransportValidationTest_remhos_1_0_gcc_10_3_0_N_1_MPI_8_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 4.832s total: 39.861s]
==> timings: setup: 0.006s compile: 0.005s run: 4.832s sanity: 0.000s performance: 0.074s total: 39.861s
[ [32m      OK[0m ] (37/84) Remhos_Remhos3DTransportValidationTest_remhos_1_0_arm_21_0_0_879_N_1_MPI_1_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 13.166s total: 38.853s]
==> timings: setup: 0.006s compile: 0.005s run: 13.166s sanity: 0.000s performance: 0.073s total: 38.853s
[ [32m      OK[0m ] (38/84) Remhos_Remhos2DTransportValidationTest_remhos_1_0_nvhpc_21_2_N_1_MPI_32_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 6.659s total: 46.426s]
==> timings: setup: 0.006s compile: 0.005s run: 6.659s sanity: 0.000s performance: 0.073s total: 46.426s
[ [32m      OK[0m ] (39/84) Remhos_Remhos2DTransportValidationTest_remhos_1_0_nvhpc_21_2_N_1_MPI_8_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 4.718s total: 49.184s]
==> timings: setup: 0.006s compile: 0.005s run: 4.718s sanity: 0.000s performance: 0.073s total: 49.184s
[ [32m      OK[0m ] (40/84) Remhos_Remhos2DTransportValidationTest_remhos_1_0_nvhpc_21_2_N_1_MPI_4_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 4.966s total: 51.177s]
==> timings: setup: 0.006s compile: 0.005s run: 4.966s sanity: 0.000s performance: 0.074s total: 51.177s
[ [32m      OK[0m ] (41/84) Remhos_Remhos3DTransportValidationTest_remhos_1_0_gcc_10_3_0_N_1_MPI_1_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 13.773s total: 51.535s]
==> timings: setup: 0.006s compile: 0.005s run: 13.773s sanity: 0.000s performance: 0.073s total: 51.535s
[ [32m      OK[0m ] (42/84) Remhos_Remhos2DTransportValidationTest_remhos_1_0_nvhpc_21_2_N_1_MPI_2_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 7.019s total: 55.788s]
==> timings: setup: 0.006s compile: 0.005s run: 7.019s sanity: 0.000s performance: 0.073s total: 55.788s
[ [32m      OK[0m ] (43/84) Remhos_Remhos2DTransportValidationTest_remhos_1_0_arm_21_0_0_879_N_1_MPI_64_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 7.092s total: 59.825s]
==> timings: setup: 0.006s compile: 0.005s run: 7.092s sanity: 0.000s performance: 0.074s total: 59.825s
[ [32m      OK[0m ] (44/84) Remhos_Remhos2DTransportValidationTest_remhos_1_0_arm_21_0_0_879_N_1_MPI_8_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 4.953s total: 63.078s]
==> timings: setup: 0.006s compile: 0.005s run: 4.953s sanity: 0.000s performance: 0.074s total: 63.078s
[ [32m      OK[0m ] (45/84) Remhos_Remhos2DTransportValidationTest_remhos_1_0_nvhpc_21_2_N_1_MPI_1_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 10.541s total: 61.301s]
==> timings: setup: 0.006s compile: 0.005s run: 10.541s sanity: 0.001s performance: 0.073s total: 61.301s
[ [32m      OK[0m ] (46/84) Remhos_Remhos2DTransportValidationTest_remhos_1_0_arm_21_0_0_879_N_1_MPI_4_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 5.679s total: 65.042s]
==> timings: setup: 0.006s compile: 0.005s run: 5.679s sanity: 0.000s performance: 0.073s total: 65.042s
[ [32m      OK[0m ] (47/84) Remhos_Remhos2DTransportValidationTest_remhos_1_0_arm_21_0_0_879_N_1_MPI_2_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 6.854s total: 69.763s]
==> timings: setup: 0.006s compile: 0.005s run: 6.854s sanity: 0.000s performance: 0.074s total: 69.763s
[ [32m      OK[0m ] (48/84) Remhos_Remhos2DTransportValidationTest_remhos_1_0_gcc_10_3_0_N_1_MPI_16_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 6.391s total: 73.772s]
==> timings: setup: 0.006s compile: 0.005s run: 6.391s sanity: 0.000s performance: 0.074s total: 73.772s
[ [32m      OK[0m ] (49/84) Remhos_Remhos2DTransportValidationTest_remhos_1_0_gcc_10_3_0_N_1_MPI_4_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 6.384s total: 75.741s]
==> timings: setup: 0.006s compile: 0.005s run: 6.384s sanity: 0.000s performance: 0.073s total: 75.741s
[ [32m      OK[0m ] (50/84) Remhos_Remhos2DTransportValidationTest_remhos_1_0_arm_21_0_0_879_N_1_MPI_1_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 12.059s total: 76.715s]
==> timings: setup: 0.006s compile: 0.005s run: 12.059s sanity: 0.000s performance: 0.074s total: 76.715s
[ [32m      OK[0m ] (51/84) Remhos_Remhos2DTransportValidationTest_remhos_1_0_gcc_10_3_0_N_1_MPI_2_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 7.096s total: 81.171s]
==> timings: setup: 0.006s compile: 0.005s run: 7.096s sanity: 0.000s performance: 0.073s total: 81.171s
[ [32m      OK[0m ] (52/84) Remhos_Remhos3DRemapValidationTest_remhos_1_0_nvhpc_21_2_N_1_MPI_64_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 5.614s total: 82.907s]
==> timings: setup: 0.006s compile: 0.005s run: 5.614s sanity: 0.000s performance: 0.074s total: 82.907s
[ [32m      OK[0m ] (53/84) Remhos_Remhos3DRemapValidationTest_remhos_1_0_nvhpc_21_2_N_1_MPI_32_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 4.856s total: 86.867s]
==> timings: setup: 0.006s compile: 0.005s run: 4.856s sanity: 0.000s performance: 0.074s total: 86.867s
[ [32m      OK[0m ] (54/84) Remhos_Remhos2DTransportValidationTest_remhos_1_0_gcc_10_3_0_N_1_MPI_1_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 10.531s total: 86.604s]
==> timings: setup: 0.006s compile: 0.005s run: 10.531s sanity: 0.000s performance: 0.073s total: 86.604s
[ [32m      OK[0m ] (55/84) Remhos_Remhos3DRemapValidationTest_remhos_1_0_nvhpc_21_2_N_1_MPI_4_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 9.045s total: 93.662s]
==> timings: setup: 0.006s compile: 0.005s run: 9.045s sanity: 0.000s performance: 0.074s total: 93.662s
[ [32m      OK[0m ] (56/84) Remhos_Remhos3DRemapValidationTest_remhos_1_0_arm_21_0_0_879_N_1_MPI_64_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 6.166s total: 97.235s]
==> timings: setup: 0.006s compile: 0.005s run: 6.166s sanity: 0.000s performance: 0.074s total: 97.235s
[ [32m      OK[0m ] (57/84) Remhos_Remhos3DRemapValidationTest_remhos_1_0_nvhpc_21_2_N_1_MPI_2_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 11.080s total: 96.948s]
==> timings: setup: 0.006s compile: 0.005s run: 11.080s sanity: 0.000s performance: 0.075s total: 96.948s
[ [32m      OK[0m ] (58/84) Remhos_Remhos3DRemapValidationTest_remhos_1_0_arm_21_0_0_879_N_1_MPI_32_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 5.084s total: 100.833s]
==> timings: setup: 0.006s compile: 0.005s run: 5.084s sanity: 0.000s performance: 0.074s total: 100.833s
[ [32m      OK[0m ] (59/84) Remhos_Remhos3DRemapValidationTest_remhos_1_0_arm_21_0_0_879_N_1_MPI_16_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 5.742s total: 104.039s]
==> timings: setup: 0.006s compile: 0.005s run: 5.742s sanity: 0.000s performance: 0.074s total: 104.039s
[ [32m      OK[0m ] (60/84) Remhos_Remhos3DRemapValidationTest_remhos_1_0_arm_21_0_0_879_N_1_MPI_8_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 5.734s total: 105.250s]
==> timings: setup: 0.006s compile: 0.005s run: 5.734s sanity: 0.000s performance: 0.073s total: 105.250s
[ [32m      OK[0m ] (61/84) Remhos_Remhos3DRemapValidationTest_remhos_1_0_nvhpc_21_2_N_1_MPI_1_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 16.496s total: 106.335s]
==> timings: setup: 0.006s compile: 0.005s run: 16.496s sanity: 0.000s performance: 0.074s total: 106.335s
[ [32m      OK[0m ] (62/84) Remhos_Remhos3DRemapValidationTest_remhos_1_0_gcc_10_3_0_N_1_MPI_32_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 5.336s total: 113.654s]
==> timings: setup: 0.006s compile: 0.005s run: 5.336s sanity: 0.001s performance: 0.073s total: 113.654s
[ [32m      OK[0m ] (63/84) Remhos_Remhos3DRemapValidationTest_remhos_1_0_arm_21_0_0_879_N_1_MPI_2_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 9.751s total: 112.879s]
==> timings: setup: 0.006s compile: 0.005s run: 9.751s sanity: 0.000s performance: 0.074s total: 112.879s
[ [32m      OK[0m ] (64/84) Remhos_Remhos3DRemapValidationTest_remhos_1_0_gcc_10_3_0_N_1_MPI_64_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 7.764s total: 114.857s]
==> timings: setup: 0.006s compile: 0.005s run: 7.764s sanity: 0.000s performance: 0.073s total: 114.857s
[ [32m      OK[0m ] (65/84) Remhos_Remhos3DRemapValidationTest_remhos_1_0_gcc_10_3_0_N_1_MPI_16_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 5.234s total: 117.106s]
==> timings: setup: 0.006s compile: 0.005s run: 5.234s sanity: 0.000s performance: 0.073s total: 117.106s
[ [32m      OK[0m ] (66/84) Remhos_Remhos3DRemapValidationTest_remhos_1_0_gcc_10_3_0_N_1_MPI_8_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 4.639s total: 119.389s]
==> timings: setup: 0.006s compile: 0.005s run: 4.639s sanity: 0.000s performance: 0.074s total: 119.389s
[ [32m      OK[0m ] (67/84) Remhos_Remhos3DRemapValidationTest_remhos_1_0_gcc_10_3_0_N_1_MPI_4_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 6.031s total: 122.245s]
==> timings: setup: 0.006s compile: 0.005s run: 6.031s sanity: 0.000s performance: 0.073s total: 122.245s
[ [32m      OK[0m ] (68/84) Remhos_Remhos3DRemapValidationTest_remhos_1_0_gcc_10_3_0_N_1_MPI_2_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 7.680s total: 125.133s]
==> timings: setup: 0.006s compile: 0.005s run: 7.680s sanity: 0.000s performance: 0.073s total: 125.133s
[ [32m      OK[0m ] (69/84) Remhos_Remhos2DRemapValidationTest_remhos_1_0_nvhpc_21_2_N_1_MPI_32_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 6.158s total: 128.374s]
==> timings: setup: 0.006s compile: 0.005s run: 6.158s sanity: 0.000s performance: 0.075s total: 128.374s
[ [32m      OK[0m ] (70/84) Remhos_Remhos2DRemapValidationTest_remhos_1_0_nvhpc_21_2_N_1_MPI_16_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 6.480s total: 131.559s]
==> timings: setup: 0.006s compile: 0.005s run: 6.480s sanity: 0.000s performance: 0.073s total: 131.559s
[ [32m      OK[0m ] (71/84) Remhos_Remhos3DRemapValidationTest_remhos_1_0_gcc_10_3_0_N_1_MPI_1_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 13.005s total: 132.201s]
==> timings: setup: 0.006s compile: 0.005s run: 13.005s sanity: 0.000s performance: 0.074s total: 132.201s
[ [32m      OK[0m ] (72/84) Remhos_Remhos2DRemapValidationTest_remhos_1_0_nvhpc_21_2_N_1_MPI_4_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 9.561s total: 138.262s]
==> timings: setup: 0.006s compile: 0.005s run: 9.561s sanity: 0.000s performance: 0.074s total: 138.262s
[ [32m      OK[0m ] (73/84) Remhos_Remhos2DRemapValidationTest_remhos_1_0_arm_21_0_0_879_N_1_MPI_64_OMP_1 on aws:c6gn using builtin [compile: 0.006s run: 8.096s total: 144.876s]
==> timings: setup: 0.006s compile: 0.006s run: 8.096s sanity: 0.001s performance: 0.073s total: 144.876s
[ [32m      OK[0m ] (74/84) Remhos_Remhos2DRemapValidationTest_remhos_1_0_arm_21_0_0_879_N_1_MPI_32_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 6.536s total: 146.893s]
==> timings: setup: 0.006s compile: 0.005s run: 6.536s sanity: 0.000s performance: 0.074s total: 146.893s
[ [32m      OK[0m ] (75/84) Remhos_Remhos2DRemapValidationTest_remhos_1_0_nvhpc_21_2_N_1_MPI_2_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 15.906s total: 146.589s]
==> timings: setup: 0.006s compile: 0.005s run: 15.906s sanity: 0.000s performance: 0.074s total: 146.589s
[ [32m      OK[0m ] (76/84) Remhos_Remhos2DRemapValidationTest_remhos_1_0_arm_21_0_0_879_N_1_MPI_16_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 6.496s total: 152.457s]
==> timings: setup: 0.006s compile: 0.005s run: 6.496s sanity: 0.000s performance: 0.074s total: 152.457s
[ [32m      OK[0m ] (77/84) Remhos_Remhos2DRemapValidationTest_remhos_1_0_arm_21_0_0_879_N_1_MPI_8_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 6.770s total: 154.744s]
==> timings: setup: 0.006s compile: 0.005s run: 6.770s sanity: 0.000s performance: 0.074s total: 154.744s
[ [32m      OK[0m ] (78/84) Remhos_Remhos2DRemapValidationTest_remhos_1_0_arm_21_0_0_879_N_1_MPI_4_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 9.153s total: 158.837s]
==> timings: setup: 0.006s compile: 0.005s run: 9.153s sanity: 0.000s performance: 0.073s total: 158.837s
[ [32m      OK[0m ] (79/84) Remhos_Remhos2DRemapValidationTest_remhos_1_0_nvhpc_21_2_N_1_MPI_1_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 24.538s total: 158.421s]
==> timings: setup: 0.006s compile: 0.005s run: 24.538s sanity: 0.000s performance: 0.073s total: 158.421s
[ [32m      OK[0m ] (80/84) Remhos_Remhos2DRemapValidationTest_remhos_1_0_arm_21_0_0_879_N_1_MPI_2_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 13.283s total: 167.338s]
==> timings: setup: 0.006s compile: 0.005s run: 13.283s sanity: 0.000s performance: 0.073s total: 167.338s
[ [32m      OK[0m ] (81/84) Remhos_Remhos2DRemapValidationTest_remhos_1_0_gcc_10_3_0_N_1_MPI_64_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 233.397s total: 233.419s]
==> timings: setup: 0.006s compile: 0.005s run: 233.397s sanity: 0.000s performance: 0.074s total: 233.419s
[ [32m      OK[0m ] (82/84) Remhos_Remhos2DRemapValidationTest_remhos_1_0_gcc_10_3_0_N_1_MPI_16_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 234.766s total: 234.787s]
==> timings: setup: 0.006s compile: 0.005s run: 234.766s sanity: 0.000s performance: 0.074s total: 234.787s
[ [32m      OK[0m ] (83/84) Remhos_Remhos2DRemapValidationTest_remhos_1_0_gcc_10_3_0_N_1_MPI_32_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 234.542s total: 234.563s]
==> timings: setup: 0.006s compile: 0.005s run: 234.542s sanity: 0.000s performance: 0.074s total: 234.563s
[ [32m      OK[0m ] (84/84) Remhos_Remhos2DRemapValidationTest_remhos_1_0_arm_21_0_0_879_N_1_MPI_1_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 277.949s total: 277.970s]
==> timings: setup: 0.006s compile: 0.005s run: 277.949s sanity: 0.000s performance: 0.073s total: 277.970s
[----------] all spawned checks have finished

[ [32m PASSED [0m ] Ran 84/84 test case(s) from 84 check(s) (0 failure(s), 0 skipped)
[==========] Finished on Tue Jul 13 16:03:20 2021
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
