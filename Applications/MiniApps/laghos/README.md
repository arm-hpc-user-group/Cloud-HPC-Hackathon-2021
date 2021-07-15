# Laghos 

**Description:** Laghos (LAGrangian High-Order Solver) is a CEED miniapp that solves the time-dependent Euler equations of compressible gas dynamics in a moving Lagrangian frame using unstructured high-order finite element spatial discretization and explicit high-order time-stepping.

**URL:** https://computing.llnl.gov/projects/co-design/laghos

**Team:**  Iman

##### notice: the output folders are dumped into /data for verification/further analysis

## Compilation

### Spack Package Modification

Details of any changes to the Spack recipe used.

Git commit hash of checkout for pacakage:

Pull request for Spack recipe changes:

### Building Laghos

#### Compiler 1

```
spack install laghos%arm
```

```
$ spack spec -Il laghos%arm
Input spec
--------------------------------
 -   laghos%arm

Concretized
--------------------------------
==> Warning: arm@21.0.0.879 cannot build optimized binaries for "graviton2". Using best target possible: "aarch64"
[+]  qsrtkae  laghos@3.1%arm@21.0.0.879+metis arch=linux-amzn2-aarch64
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

#### Compiler 2

```
spack install laghos%gcc
```

```
$ spack spec -Il laghos%arm
Input spec
--------------------------------
 -   laghos%gcc

Concretized
--------------------------------
[+]  3a63qmj  laghos@3.1%gcc@10.3.0+metis arch=linux-amzn2-graviton2
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

#### Compiler 3

```
spack install laghos%nvhpc
```

This did not work due to conflict with cmake and later openblas, more info: https://github.com/spack/spack/issues/20781 The solution:

```
spack install laghos%nvhpc ^cmake%gcc ^openblas%gcc
```

```
$ spack spec -Il laghos%nvhpc ^cmake%gcc
Input spec
--------------------------------
 -   laghos%nvhpc
 -       ^cmake%gcc
 -       ^openblas%gcc

Concretized
--------------------------------
[+]  3f3xcws  laghos@3.1%nvhpc@21.2+metis arch=linux-amzn2-graviton2
[+]  y6cu7p3      ^mfem@4.2.0%nvhpc@21.2~amgx~conduit~cuda~debug~examples~gnutls~gslib~lapack~libceed~libunwind+metis~miniapps~mpfr+mpi~netcdf~occa~openmp~petsc~pumi~raja~rocm~shared~slepc+static~strumpack~suite-sparse~sundials~superlu-dist~threadsafe~umpire+zlib amdgpu_target=none cuda_arch=none timer=auto arch=linux-amzn2-graviton2
[+]  3ebaawd          ^hypre@2.20.0%nvhpc@21.2~complex~cuda~debug~int64~internal-superlu~mixedint+mpi~openmp+shared~superlu-dist~unified-memory cuda_arch=none patches=6e3336b1d62155f6350dfe42b0f9ea25d4fa0af60c7e540959139deb93a26059 arch=linux-amzn2-graviton2
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
[+]  okl5z2h              ^openmpi@4.1.0%nvhpc@21.2~atomics~cuda~cxx~cxx_exceptions+gpfs~internal-hwloc~java~legacylaunchers~lustre~memchecker+pmi~singularity~sqlite3+static~thread_multiple+vt+wrapper-rpath fabrics=ofi patches=60ce20bc14d98c572ef7883b9fcd254c3f232c2f3a13377480f96466169ac4c8,fba0d3a784a9723338722b48024a22bb32f6a951db841a4e9f08930a93f41d7a schedulers=slurm arch=linux-amzn2-graviton2
[+]  dultkd7                  ^hwloc@2.5.0%nvhpc@21.2~cairo~cuda~gl~libudev+libxml2~netloc~nvml+pci+shared arch=linux-amzn2-graviton2
[+]  e4m4ued                      ^libpciaccess@0.16%nvhpc@21.2 patches=6e08dc445ece06e9e8b1344397f2d3f169005703ddc0f2ae24f366cde78c7377 arch=linux-amzn2-graviton2
[+]  kk4ax3i                          ^libtool@2.4.6%nvhpc@21.2 arch=linux-amzn2-graviton2
[+]  6c4kz5g                              ^m4@1.4.18%nvhpc@21.2+sigsegv patches=3877ab548f88597ab2327a2230ee048d2d07ace1062efe81fc92e91b7f39cd00,5746cf51f45b405661c3edae7a78c33d41e54d83f635d16e2bf1f956dbfbf635,fc9b61654a3ba1a8d6cd78ce087e7c96366c290bc8d2c299f09828d793b853c8 arch=linux-amzn2-graviton2
[+]  pa6wm5j                                  ^libsigsegv@2.13%nvhpc@21.2 arch=linux-amzn2-graviton2
[+]  4imdwuy                          ^util-macros@1.19.3%nvhpc@21.2 arch=linux-amzn2-graviton2
[+]  flzyc7v                      ^libxml2@2.9.10%nvhpc@21.2~python patches=05ff238cf435825ef835c7ae39376b52dc83d8caf19e962f0766c841386a305a,10a88ad47f9797cf7cf2d7d07241f665a3b6d1f31fa026728c8c2ae93e1664e9 arch=linux-amzn2-graviton2
[+]  br733tn                          ^xz@5.2.5%nvhpc@21.2~pic libs=shared,static arch=linux-amzn2-graviton2
[+]  qmlezth                  ^libevent@2.1.12%nvhpc@21.2+openssl arch=linux-amzn2-graviton2
[+]  5i3lgfb                      ^openssl@1.1.1k%gcc@10.3.0~docs+systemcerts arch=linux-amzn2-graviton2
[+]  xl6zavq                  ^libfabric@1.11.1-aws%nvhpc@21.2~debug~kdreg fabrics=sockets,tcp,udp arch=linux-amzn2-graviton2
[+]  5yq4tpw                  ^numactl@2.0.14%nvhpc@21.2 patches=4e1d78cbbb85de625bad28705e748856033eaafab92a66dffd383a3d7e00cc94,62fc8a8bf7665a60e8f4c93ebbd535647cebf74198f7afafec4c085a8825c006 arch=linux-amzn2-graviton2
[+]  vslxuhy                      ^autoconf@2.69%nvhpc@21.2 arch=linux-amzn2-graviton2
[+]  pqaylup                      ^automake@1.16.3%nvhpc@21.2 arch=linux-amzn2-graviton2
[+]  wturp6c                  ^openssh@8.5p1%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  ivotdt7                      ^libedit@3.1-20210216%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  zehhooy                  ^slurm@20-02-4-1%nvhpc@21.2~gtk~hdf5~hwloc~mariadb~pmix+readline~restd sysconfdir=PREFIX/etc arch=linux-amzn2-graviton2
[+]  h2ymlmt          ^metis@5.1.0%nvhpc@21.2~gdb~int64~real64+shared build_type=Release patches=4991da938c1d3a1d3dea78e49bbebecba00273f98df2a656e38b83d55b281da1 arch=linux-amzn2-graviton2
[+]  m7325ee              ^cmake@3.20.5%gcc@10.3.0~doc+ncurses+openssl+ownlibs~qt build_type=Release arch=linux-amzn2-graviton2
```

## Validation
Laghos conveniently has specific run configurations and results for verification here: https://github.com/CEED/Laghos#verification-of-results Those verification tables are used to make the 4 test cases that follow, which checks the final iterations (step), time steps (dt) and the energy absolute values (|e|). 

## Test Case 1

[ReFrame Benchmark 1](#)

```
reframe --stage /scratch/home/${USER} -c t0.py -r --performance-report
```

### ReFrame Output

```
==============================================================================
PERFORMANCE REPORT
------------------------------------------------------------------------------
laghos_test0_laghos_3_1__arm_N_1_MPI_32_OMP_1
- aws:c6gn
   - builtin
      * num_tasks: 32
      * Major kernels total time: 2.585816651 s
      * Major kernels total rate: 20.8506446036 Mdofs x steps / s
------------------------------------------------------------------------------
laghos_test0_laghos_3_1__arm_N_2_MPI_64_OMP_1
   - builtin
      * num_tasks: 64
      * Major kernels total time: 6.400724779 s
      * Major kernels total rate: 8.4234123262 Mdofs x steps / s
------------------------------------------------------------------------------
laghos_test0_laghos_3_1__arm_N_2_MPI_128_OMP_1
   - builtin
      * num_tasks: 128
      * Major kernels total time: 10.900726409 s
      * Major kernels total rate: 4.9460872585 Mdofs x steps / s
------------------------------------------------------------------------------
laghos_test0_laghos_3_1__arm_N_4_MPI_256_OMP_1
   - builtin
      * num_tasks: 256
      * Major kernels total time: 14.234962723 s
      * Major kernels total rate: 3.7875718433 Mdofs x steps / s
------------------------------------------------------------------------------
laghos_test0_laghos_3_1__gcc_N_1_MPI_32_OMP_1
   - builtin
      * num_tasks: 32
      * Major kernels total time: 2.676560093 s
      * Major kernels total rate: 20.1437450035 Mdofs x steps / s
------------------------------------------------------------------------------
laghos_test0_laghos_3_1__gcc_N_2_MPI_64_OMP_1
   - builtin
      * num_tasks: 64
      * Major kernels total time: 6.41461884 s
      * Major kernels total rate: 8.4051672196 Mdofs x steps / s
------------------------------------------------------------------------------
laghos_test0_laghos_3_1__gcc_N_2_MPI_128_OMP_1
   - builtin
      * num_tasks: 128
      * Major kernels total time: 10.80813928 s
      * Major kernels total rate: 4.9884575507 Mdofs x steps / s
------------------------------------------------------------------------------
laghos_test0_laghos_3_1__gcc_N_4_MPI_256_OMP_1
   - builtin
      * num_tasks: 256
      * Major kernels total time: 13.939522901 s
      * Major kernels total rate: 3.8678471554 Mdofs x steps / s
------------------------------------------------------------------------------
laghos_test0_laghos_3_1__nvhpc_N_1_MPI_32_OMP_1
   - builtin
      * num_tasks: 32
      * Major kernels total time: 2.707359012 s
      * Major kernels total rate: 19.9145897389 Mdofs x steps / s
------------------------------------------------------------------------------
laghos_test0_laghos_3_1__nvhpc_N_2_MPI_64_OMP_1
   - builtin
      * num_tasks: 64
      * Major kernels total time: 6.440125839 s
      * Major kernels total rate: 8.3718774055 Mdofs x steps / s
------------------------------------------------------------------------------
laghos_test0_laghos_3_1__nvhpc_N_2_MPI_128_OMP_1
   - builtin
      * num_tasks: 128
      * Major kernels total time: 10.287958023 s
      * Major kernels total rate: 5.24068468 Mdofs x steps / s
------------------------------------------------------------------------------
laghos_test0_laghos_3_1__nvhpc_N_4_MPI_256_OMP_1
   - builtin
      * num_tasks: 256
      * Major kernels total time: 13.354695338 s
      * Major kernels total rate: 4.0372275545 Mdofs x steps / s
------------------------------------------------------------------------------
```

### On-node Compiler Comparison

Performance comparison of two compilers. Measure is Major kernels total rate in megadorf x steps / seconds.

| Cores | arm        | gcc        | nvhpc      | 
|-------|------------|------------|------------|
|   32  | 20.85      |  20.14     | 19.91      |

### Serial Hot-spot Profile

List of top-10 functions / code locations from a serial profile.

Profiling command used: I actually used the normal reframe test case run, but the script includes flags for _PROFILE\_RUN_ and _DEBUG\_RUN_ which I use to set it up for profiling or a short run for debug. 
```
reframe --stage /scratch/home/${USER} -c t0.py -r --performance-report
```

The profiling is done on arm compiler, by using the ReFrame's _LaunchWrapper_ call map like this:
```
self.job.launcher = LauncherWrapper(self.job.launcher,'map',['--profile', '--export-functions='+self.proffile])
```

The resulting top 10:

|depth|Self |Total|Child|MPI|Overhead|Regions|Function                                                                                                                                                                                                                                                                                                            |
|-----|-----|-----|-----|---|--------|-------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|0    |17.0%|17.0%|     |   |        |       |mfem::PAMassApply(int, int, int, int, mfem::Array<double                                                                                                                                                                                                                                                            |
|0    |11.6%|11.6%|     |   |        |       |cos                                                                                                                                                                                                                                                                                                                 |
|0    |9.0% |9.7% |0.7% |   |        |       |void mfem::hydrodynamics::QUpdateBody<2>(int, int, int, int, bool, bool, double, double, double, double, double*, double*, double*, double*, double*, double*, double*, double*, double*, double const*, double const*, double const*, double const*, double const*, double const*, double const*, double*, double*)|
|0    |7.2% |7.2% |     |   |        |       |mfem::add(mfem::Vector const&, double, mfem::Vector const&, mfem::Vector&)                                                                                                                                                                                                                                          |
|0    |6.5% |6.5% |     |   |        |       |mfem::ElementRestriction::Mult(mfem::Vector const&, mfem::Vector&) const                                                                                                                                                                                                                                            |
|0    |6.5% |6.5% |     |   |        |       |mfem::ElementRestriction::MultTranspose(mfem::Vector const&, mfem::Vector&) const                                                                                                                                                                                                                                   |
|0    |6.1% |6.1% |     |   |        |       |mfem::Mult(mfem::DenseMatrix const&, mfem::DenseMatrix const&, mfem::DenseMatrix&)                                                                                                                                                                                                                                  |
|0    |4.0% |4.0% |     |   |        |       |mfem::Poly_1D::Basis::Eval(double, mfem::Vector&) const                                                                                                                                                                                                                                                             |
|0    |3.2% |3.2% |     |   |        |       |mfem::Poly_1D::Basis::Eval(double, mfem::Vector&, mfem::Vector&) const                                                                                                                                                                                                                                              |
|0    |3.2% |8.3% |5.1% |   |        |       |mfem::IsoparametricTransformation::Transform(mfem::IntegrationPoint const&, mfem::Vector&)                                                                                                                                                                                                                          |

### Full Node Hot-spot Profile

List of top-10 functions / code locations from a full node profile.

Profiling command used: I actually used the normal reframe test case run, but the script includes flags for _PROFILE\_RUN_ and _DEBUG\_RUN_ which I use to set it up for profiling or a short run for debug. 
```
reframe --stage /scratch/home/${USER} -c t0.py -r --performance-report
```

The profiling is done on arm compiler, by using the ReFrame's _LaunchWrapper_ call map like this:
```
self.job.launcher = LauncherWrapper(self.job.launcher,'map',['--profile', '--export-functions='+self.proffile])
```

|depth|Self |Total|Child|MPI  |Overhead|Regions|Function                                                |
|-----|-----|-----|-----|-----|--------|-------|--------------------------------------------------------|
|0    |80.1%|80.1%|     |80.1%|        |       |MPI_Allreduce                                           |
|0    |6.1% |6.1% |     |6.1% |        |       |MPI_Waitall                                             |
|0    |5.9% |5.9% |     |5.9% |        |       |MPI_Waitany                                             |
|0    |3.0% |3.0% |     |3.0% |        |       |MPI_Isend                                               |
|0    |1.9% |1.9% |     |1.9% |        |       |MPI_Irecv                                               |
|0    |0.5% |0.5% |     |0.5% |        |       |MPI_Barrier                                             |
|0    |0.4% |0.4% |     |0.4% |        |       |MPI_Finalize                                            |
|0    |0.3% |0.3% |     |0.3% |        |       |MPI_Scan                                                |
|0    |0.2% |0.2% |     |     |        |       |mfem::PAMassApply(int, int, int, int, mfem::Array<double|
|0    |0.1% |0.1% |     |     |        |       |cos                                                     |


### Strong Scaling Study

On-node scaling study for two compilers. Here 'major kernels total time' in seconds, is reported. 

| Cores | arm  | gcc  | nvhpc |
|-------|------|------|-------|
| 1     | 2.66 | 2.31 | 2.86  |
| 4     | 1.47 | 1.40 | 1.56  |
| 16    | 2.13 | 2.17 | 2.20  |
| 64    | 3.58 | 3.83 | 3.71  |


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

