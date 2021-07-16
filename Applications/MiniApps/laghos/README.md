# Laghos 

**Description:** Laghos (LAGrangian High-Order Solver) is a CEED miniapp that solves the time-dependent Euler equations of compressible gas dynamics in a moving Lagrangian frame using unstructured high-order finite element spatial discretization and explicit high-order time-stepping.

**URL:** https://computing.llnl.gov/projects/co-design/laghos

**Team:**  Iman

##### notice: the output folders are dumped into /data for verification/further analysis (some directories might have been overwritten through runs that I set off wrong and cancelled, but hey, the graylogs are there and every test can also be run again)

## Compilation

### Spack Package Modification

Details of any changes to the Spack recipe used. (Not used until the last step, when I added ofast variant for the package to spack)

Git commit hash of checkout for pacakage: https://github.com/spack/spack/pull/24910/commits/886e372f0ff9a709579d38dc89b7a38b8b6d6b87

Pull request for Spack recipe changes: https://github.com/spack/spack/pull/24910

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
Laghos conveniently has specific run configurations and results for verification here: https://github.com/CEED/Laghos#verification-of-results Those verification tables are used to make the 4 test cases that follow, which checks the final iterations (step), time steps (dt) and the energy absolute values (|e|). I tried to pick 4 varied test cases from the table, including the longest and shortest runs.

## Test Case 1

[ReFrame Benchmark 1](#)

Test Case 1 (in t0.py, notice the filenames start from 0), is the verifaction example number 1 here: https://github.com/CEED/Laghos#verification-of-results

```
reframe --stage /scratch/home/${USER} -c t0.py -r --performance-report
```

### ReFrame Output

More verbose paper trail of various runs is available be in /data.

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

(this is a taste, more details of 3 compiler comparison later in scaling) **Also on next test case on this section I used the same data from scaling, one of those runs. The only reason is I got more savvy as time went on :) **
Performance comparison of 3 compilers. Measure is Major kernels total rate in megadorf x steps / seconds which is relevant and despite total time, an scalable measure.

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

On-node scaling study for 3 compilers. Here 'major kernels total time' in seconds, is reported. 

| Cores | arm  | gcc  | nvhpc |
|-------|------|------|-------|
| 1     | 2.66 | 2.31 | 2.86  |
| 4     | 1.47 | 1.40 | 1.56  |
| 16    | 2.13 | 2.17 | 2.20  |
| 64    | 3.58 | 3.83 | 3.71  |

## Test Case 2

[ReFrame Benchmark 2](#)

Test Case 2 (in t1.py, notice the filenames start from 0), is the verifaction example number 4 here: https://github.com/CEED/Laghos#verification-of-results

```
reframe --stage /scratch/home/${USER} -c t1.py -r --performance-report
```

### ReFrame Output

```
==============================================================================
PERFORMANCE REPORT
------------------------------------------------------------------------------
laghos_test1_laghos_3_1__arm_N_1_MPI_1_OMP_1
- aws:c6gn
   - builtin
      * num_tasks: 1
      * Major kernels total time: 136.110060353 s
      * Major kernels total rate: 6.6695623574 Mdofs x steps / s
------------------------------------------------------------------------------
laghos_test1_laghos_3_1__arm_N_1_MPI_4_OMP_1
   - builtin
      * num_tasks: 4
      * Major kernels total time: 38.311105694 s
      * Major kernels total rate: 23.691873872 Mdofs x steps / s
------------------------------------------------------------------------------
laghos_test1_laghos_3_1__arm_N_1_MPI_16_OMP_1
   - builtin
      * num_tasks: 16
      * Major kernels total time: 18.149532447 s
      * Major kernels total rate: 50.0093954294 Mdofs x steps / s
------------------------------------------------------------------------------
laghos_test1_laghos_3_1__arm_N_1_MPI_64_OMP_1
   - builtin
      * num_tasks: 64
      * Major kernels total time: 21.105944921 s
      * Major kernels total rate: 43.0043359062 Mdofs x steps / s
------------------------------------------------------------------------------
laghos_test1_laghos_3_1__gcc__3a63qmj_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Major kernels total time: 112.604552075 s
      * Major kernels total rate: 8.0617925144 Mdofs x steps / s
------------------------------------------------------------------------------
laghos_test1_laghos_3_1__gcc__3a63qmj_N_1_MPI_4_OMP_1
   - builtin
      * num_tasks: 4
      * Major kernels total time: 32.004987319 s
      * Major kernels total rate: 28.3600138614 Mdofs x steps / s
------------------------------------------------------------------------------
laghos_test1_laghos_3_1__gcc__3a63qmj_N_1_MPI_16_OMP_1
   - builtin
      * num_tasks: 16
      * Major kernels total time: 16.920477199 s
      * Major kernels total rate: 53.6419354091 Mdofs x steps / s
------------------------------------------------------------------------------
laghos_test1_laghos_3_1__gcc__3a63qmj_N_1_MPI_64_OMP_1
   - builtin
      * num_tasks: 64
      * Major kernels total time: 22.012998304 s
      * Major kernels total rate: 41.2323270308 Mdofs x steps / s
------------------------------------------------------------------------------
laghos_test1_laghos_3_1__nvhpc_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Major kernels total time: 122.91817339 s
      * Major kernels total rate: 7.3843972617 Mdofs x steps / s
------------------------------------------------------------------------------
laghos_test1_laghos_3_1__nvhpc_N_1_MPI_4_OMP_1
   - builtin
      * num_tasks: 4
      * Major kernels total time: 34.685442426 s
      * Major kernels total rate: 26.1679563966 Mdofs x steps / s
------------------------------------------------------------------------------
laghos_test1_laghos_3_1__nvhpc_N_1_MPI_16_OMP_1
   - builtin
      * num_tasks: 16
      * Major kernels total time: 17.74052262 s
      * Major kernels total rate: 51.1623678987 Mdofs x steps / s
------------------------------------------------------------------------------
laghos_test1_laghos_3_1__nvhpc_N_1_MPI_64_OMP_1
   - builtin
      * num_tasks: 64
      * Major kernels total time: 21.288998248 s
      * Major kernels total rate: 42.6345633753 Mdofs x steps / s
------------------------------------------------------------------------------
```

### On-node Compiler Comparison

(this is a taste, more details of 3 compiler comparison later in scaling)
Performance comparison of 3 compilers. Measure is Major kernels total rate in megadorf x steps / seconds which is relevant and despite total time, an scalable measure.

| Cores | arm        | gcc        | nvhpc      | 
|-------|------------|------------|------------|
|   64  | 21.10      |  22.01     | 21.29      |

### Serial Hot-spot Profile

List of top-10 functions / code locations from a serial profile.

Profiling command used: I actually used the normal reframe test case run, but the script includes flags for _PROFILE\_RUN_ and _DEBUG\_RUN_ which I use to set it up for profiling or a short run for debug. 
```
reframe --stage /scratch/home/${USER} -c t1.py -r --performance-report
```

The profiling is done on arm compiler, by using the ReFrame's _LaunchWrapper_ call map like this:
```
self.job.launcher = LauncherWrapper(self.job.launcher,'map',['--profile', '--export-functions='+self.proffile])
```

The resulting top 10:

|depth|Self |Total|Child|MPI|Overhead|Regions|Function                                                                                                                                                                                                                                                                                                            |
|-----|-----|-----|-----|---|--------|-------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|0    |29.0%|29.0%|     |   |        |       |mfem::PAMassApply(int, int, int, int, mfem::Array<double                                                                                                                                                                                                                                                            |
|0    |11.2%|46.4%|35.2%|   |        |       |void mfem::hydrodynamics::QUpdateBody<3>(int, int, int, int, bool, bool, double, double, double, double, double*, double*, double*, double*, double*, double*, double*, double*, double*, double const*, double const*, double const*, double const*, double const*, double const*, double const*, double*, double*)|
|0    |7.1% |7.1% |     |   |        |       |mfem::ElementRestriction::MultTranspose(mfem::Vector const&, mfem::Vector&) const                                                                                                                                                                                                                                   |
|0    |6.5% |6.5% |     |   |        |       |mfem::ElementRestriction::Mult(mfem::Vector const&, mfem::Vector&) const                                                                                                                                                                                                                                            |
|0    |6.2% |23.3%|17.1%|   |        |       |void mfem::kernels::CalcEigenvalues<3>(double const*, double*, double*)                                                                                                                                                                                                                                             |
|0    |6.1% |10.1%|4.0% |   |        |       |mfem::kernels::internal::KernelVector3S(int const&, double const&, double const&, double const&, double&, double&, double&)                                                                                                                                                                                         |
|0    |5.6% |12.0%|6.4% |   |        |       |double mfem::kernels::CalcSingularvalue<3>(double const*, int)                                                                                                                                                                                                                                                      |
|0    |4.3% |4.3% |     |   |        |       |cos                                                                                                                                                                                                                                                                                                                 |
|0    |4.1% |4.1% |     |   |        |       |mfem::D2QGrad(mfem::FiniteElementSpace const&, mfem::DofToQuad const*, mfem::Vector const&, mfem::Vector&)                                                                                                                                                                                                          |
|0    |3.8% |5.7% |1.9% |   |        |       |hypot                                                                                                                                                                                                                                                                                                               |

### Full Node Hot-spot Profile

List of top-10 functions / code locations from a full node profile.

Profiling command used: I actually used the normal reframe test case run, but the script includes flags for _PROFILE\_RUN_ and _DEBUG\_RUN_ which I use to set it up for profiling or a short run for debug. 
```
reframe --stage /scratch/home/${USER} -c t1.py -r --performance-report
```

The profiling is done on arm compiler, by using the ReFrame's _LaunchWrapper_ call map like this:
```
self.job.launcher = LauncherWrapper(self.job.launcher,'map',['--profile', '--export-functions='+self.proffile])
```

|depth|Self |Total|Child|MPI  |Overhead|Regions|Function                                                                                                                                                                                                                                                                                                            |
|-----|-----|-----|-----|-----|--------|-------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|0    |67.2%|67.2%|     |67.2%|        |       |MPI_Allreduce                                                                                                                                                                                                                                                                                                       |
|0    |10.0%|10.0%|     |10.0%|        |       |MPI_Waitall                                                                                                                                                                                                                                                                                                         |
|0    |8.1% |8.1% |     |8.1% |        |       |MPI_Waitany                                                                                                                                                                                                                                                                                                         |
|0    |5.4% |5.4% |     |5.4% |        |       |MPI_Isend                                                                                                                                                                                                                                                                                                           |
|0    |3.4% |3.4% |     |3.4% |        |       |MPI_Irecv                                                                                                                                                                                                                                                                                                           |
|0    |1.3% |1.3% |     |     |        |       |mfem::PAMassApply(int, int, int, int, mfem::Array<double                                                                                                                                                                                                                                                            |
|0    |0.5% |2.0% |1.5% |     |        |       |void mfem::hydrodynamics::QUpdateBody<3>(int, int, int, int, bool, bool, double, double, double, double, double*, double*, double*, double*, double*, double*, double*, double*, double*, double const*, double const*, double const*, double const*, double const*, double const*, double const*, double*, double*)|
|0    |0.4% |0.4% |     |     |        |       |mfem::ElementRestriction::Mult(mfem::Vector const&, mfem::Vector&) const                                                                                                                                                                                                                                            |
|0    |0.3% |0.5% |0.2% |     |        |       |mfem::kernels::internal::KernelVector3S(int const&, double const&, double const&, double const&, double&, double&, double&)                                                                                                                                                                                         |
|0    |0.3% |0.3% |     |     |        |       |mfem::ElementRestriction::MultTranspose(mfem::Vector const&, mfem::Vector&) const                                                                                                                                                                                                                                   |

### Strong Scaling Study

On-node scaling study for 3 compilers. Here 'major kernels total time' in seconds, is reported. 

| Cores | arm    | gcc    | nvhpc  |
|-------|--------|--------|--------|
| 1     | 136.11 | 112.60 | 122.92 |
| 4     | 38.31  | 32.00  | 34.68  |
| 16    | 18.15  | 16.92  | 17.74  |
| 64    | 21.11  | 22.01  | 21.29  |

## Test Case 3

[ReFrame Benchmark 3](#)

Test Case 3 (in t2.py, notice the filenames start from 0), is the verifaction example number 3 here: https://github.com/CEED/Laghos#verification-of-results

```
reframe --stage /scratch/home/${USER} -c t2.py -r --performance-report
```

### ReFrame Output

```
==============================================================================
PERFORMANCE REPORT
------------------------------------------------------------------------------
laghos_test2_laghos_3_1__arm_N_1_MPI_1_OMP_1
- aws:c6gn
   - builtin
      * num_tasks: 1
      * Major kernels total time: 11.582825254 s
      * Major kernels total rate: 18.3152461811 Mdofs x steps / s
------------------------------------------------------------------------------
laghos_test2_laghos_3_1__arm_N_1_MPI_4_OMP_1
   - builtin
      * num_tasks: 4
      * Major kernels total time: 6.001865907 s
      * Major kernels total rate: 35.3460572574 Mdofs x steps / s
------------------------------------------------------------------------------
laghos_test2_laghos_3_1__arm_N_1_MPI_16_OMP_1
   - builtin
      * num_tasks: 16
      * Major kernels total time: 8.70790653 s
      * Major kernels total rate: 24.3620318235 Mdofs x steps / s
------------------------------------------------------------------------------
laghos_test2_laghos_3_1__arm_N_1_MPI_64_OMP_1
   - builtin
      * num_tasks: 64
      * Major kernels total time: 14.013425059 s
      * Major kernels total rate: 15.1385043347 Mdofs x steps / s
------------------------------------------------------------------------------
laghos_test2_laghos_3_1__gcc__3a63qmj_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Major kernels total time: 10.088893639 s
      * Major kernels total rate: 21.0273101879 Mdofs x steps / s
------------------------------------------------------------------------------
laghos_test2_laghos_3_1__gcc__3a63qmj_N_1_MPI_4_OMP_1
   - builtin
      * num_tasks: 4
      * Major kernels total time: 5.863037985 s
      * Major kernels total rate: 36.1829987359 Mdofs x steps / s
------------------------------------------------------------------------------
laghos_test2_laghos_3_1__gcc__3a63qmj_N_1_MPI_16_OMP_1
   - builtin
      * num_tasks: 16
      * Major kernels total time: 8.818843213 s
      * Major kernels total rate: 24.0555695204 Mdofs x steps / s
------------------------------------------------------------------------------
laghos_test2_laghos_3_1__gcc__3a63qmj_N_1_MPI_64_OMP_1
   - builtin
      * num_tasks: 64
      * Major kernels total time: 14.922970587 s
      * Major kernels total rate: 14.2158221624 Mdofs x steps / s
------------------------------------------------------------------------------
laghos_test2_laghos_3_1__nvhpc_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Major kernels total time: 12.110388458 s
      * Major kernels total rate: 17.5173816047 Mdofs x steps / s
------------------------------------------------------------------------------
laghos_test2_laghos_3_1__nvhpc_N_1_MPI_4_OMP_1
   - builtin
      * num_tasks: 4
      * Major kernels total time: 6.382783241 s
      * Major kernels total rate: 33.2366442647 Mdofs x steps / s
------------------------------------------------------------------------------
laghos_test2_laghos_3_1__nvhpc_N_1_MPI_16_OMP_1
   - builtin
      * num_tasks: 16
      * Major kernels total time: 9.009894686 s
      * Major kernels total rate: 23.5454800964 Mdofs x steps / s
------------------------------------------------------------------------------
laghos_test2_laghos_3_1__nvhpc_N_1_MPI_64_OMP_1
   - builtin
      * num_tasks: 64
      * Major kernels total time: 14.868176572 s
      * Major kernels total rate: 14.2682120415 Mdofs x steps / s
------------------------------------------------------------------------------
```

### On-node Compiler Comparison

(this is a taste, more details of 3 compiler comparison later in scaling)
Performance comparison of 3 compilers. Measure is Major kernels total rate in megadorf x steps / seconds which is relevant and despite total time, an scalable measure.

| Cores | arm        | gcc        | nvhpc      | 
|-------|------------|------------|------------|
| 64    | 14.01      | 14.92      | 14.86      |

### Serial Hot-spot Profile

List of top-10 functions / code locations from a serial profile.

Profiling command used: I actually used the normal reframe test case run, but the script includes flags for _PROFILE\_RUN_ and _DEBUG\_RUN_ which I use to set it up for profiling or a short run for debug. 
```
reframe --stage /scratch/home/${USER} -c t2.py -r --performance-report
```

The profiling is done on arm compiler, by using the ReFrame's _LaunchWrapper_ call map like this:
```
self.job.launcher = LauncherWrapper(self.job.launcher,'map',['--profile', '--export-functions='+self.proffile])
```

The resulting top 10:

|depth|Self |Total|Child|MPI|Overhead|Regions|Function                                                                                                                                                                                                                                                                                                            |
|-----|-----|-----|-----|---|--------|-------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|0    |25.9%|25.9%|     |   |        |       |mfem::PAMassApply(int, int, int, int, mfem::Array<double                                                                                                                                                                                                                                                            |
|0    |23.1%|23.9%|0.8% |   |        |       |void mfem::hydrodynamics::QUpdateBody<2>(int, int, int, int, bool, bool, double, double, double, double, double*, double*, double*, double*, double*, double*, double*, double*, double*, double const*, double const*, double const*, double const*, double const*, double const*, double const*, double*, double*)|
|0    |13.6%|13.6%|     |   |        |       |mfem::ElementRestriction::MultTranspose(mfem::Vector const&, mfem::Vector&) const                                                                                                                                                                                                                                   |
|0    |12.8%|12.8%|     |   |        |       |mfem::ElementRestriction::Mult(mfem::Vector const&, mfem::Vector&) const                                                                                                                                                                                                                                            |
|0    |5.8% |5.8% |     |   |        |       |mfem::add(mfem::Vector const&, double, mfem::Vector const&, mfem::Vector&)                                                                                                                                                                                                                                          |
|0    |3.6% |3.6% |     |   |        |       |mfem::Vector::operator*(mfem::Vector const&) const                                                                                                                                                                                                                                                                  |
|0    |3.0% |3.0% |     |   |        |       |mfem::D2QGrad(mfem::FiniteElementSpace const&, mfem::DofToQuad const*, mfem::Vector const&, mfem::Vector&)                                                                                                                                                                                                          |
|0    |1.7% |1.7% |     |   |        |       |void mfem::hydrodynamics::ForceMult2D<2, 3, 4, 2, 1>(int, mfem::Array<double                                                                                                                                                                                                                                        |
|0    |1.4% |1.4% |     |   |        |       |void mfem::hydrodynamics::ForceMultTranspose2D<2, 3, 4, 2, 1>(int, mfem::Array<double                                                                                                                                                                                                                               |
|0    |1.3% |1.3% |     |   |        |       |memcpy                                                                                                                                                                                                                                                                                                              |

### Full Node Hot-spot Profile

List of top-10 functions / code locations from a full node profile.

Profiling command used: I actually used the normal reframe test case run, but the script includes flags for _PROFILE\_RUN_ and _DEBUG\_RUN_ which I use to set it up for profiling or a short run for debug. 
```
reframe --stage /scratch/home/${USER} -c t2.py -r --performance-report
```

The profiling is done on arm compiler, by using the ReFrame's _LaunchWrapper_ call map like this:
```
self.job.launcher = LauncherWrapper(self.job.launcher,'map',['--profile', '--export-functions='+self.proffile])
```

|depth|Self |Total|Child|MPI  |Overhead|Regions|Function                                                                                                                                                                                                                                                                                                            |
|-----|-----|-----|-----|-----|--------|-------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|0    |79.2%|79.2%|     |79.2%|        |       |MPI_Allreduce                                                                                                                                                                                                                                                                                                       |
|0    |6.4% |6.4% |     |6.4% |        |       |MPI_Waitany                                                                                                                                                                                                                                                                                                         |
|0    |6.3% |6.3% |     |6.3% |        |       |MPI_Waitall                                                                                                                                                                                                                                                                                                         |
|0    |3.5% |3.5% |     |3.5% |        |       |MPI_Isend                                                                                                                                                                                                                                                                                                           |
|0    |2.4% |2.4% |     |2.4% |        |       |MPI_Irecv                                                                                                                                                                                                                                                                                                           |
|0    |0.4% |0.4% |     |0.4% |        |       |MPI_Barrier                                                                                                                                                                                                                                                                                                         |
|0    |0.2% |0.2% |     |     |        |       |mfem::PAMassApply(int, int, int, int, mfem::Array<double                                                                                                                                                                                                                                                            |
|0    |0.1% |0.1% |<0.1%|     |        |       |void mfem::hydrodynamics::QUpdateBody<2>(int, int, int, int, bool, bool, double, double, double, double, double*, double*, double*, double*, double*, double*, double*, double*, double*, double const*, double const*, double const*, double const*, double const*, double const*, double const*, double*, double*)|
|0    |0.1% |0.1% |     |0.1% |        |       |MPI_Finalize                                                                                                                                                                                                                                                                                                        |
|0    |0.1% |0.1% |     |0.1% |        |       |MPI_Scan                                                                                                                                                                                                                                                                                                            |

### Strong Scaling Study

On-node scaling study for 3 compilers. Here 'major kernels total time' in seconds, is reported. 

| Cores | arm    | gcc    | nvhpc  |
|-------|--------|--------|--------|
| 1     | 11.58  | 10.09  | 12.11  |
| 4     | 6.00   | 5.86   | 6.38   |
| 16    | 8.70   | 8.81   | 9.00   |
| 64    | 14.01  | 14.92  | 14.86  |

## Test Case 4

[ReFrame Benchmark 4](#)

Test Case 4 (in t3.py, notice the filenames start from 0), is the verifaction example number 2 here: https://github.com/CEED/Laghos#verification-of-results

```
reframe --stage /scratch/home/${USER} -c t3.py -r --performance-report
```

### ReFrame Output

```
==============================================================================
PERFORMANCE REPORT
------------------------------------------------------------------------------
laghos_test3_laghos_3_1__arm_N_1_MPI_1_OMP_1
- aws:c6gn
   - builtin
      * num_tasks: 1
      * Major kernels total time: 19.162289123 s
      * Major kernels total rate: 10.202975842 Mdofs x steps / s
------------------------------------------------------------------------------
laghos_test3_laghos_3_1__arm_N_1_MPI_4_OMP_1
   - builtin
      * num_tasks: 4
      * Major kernels total time: 9.533126451 s
      * Major kernels total rate: 20.5087359331 Mdofs x steps / s
------------------------------------------------------------------------------
laghos_test3_laghos_3_1__arm_N_1_MPI_16_OMP_1
   - builtin
      * num_tasks: 16
      * Major kernels total time: 14.211477484 s
      * Major kernels total rate: 13.7573572642 Mdofs x steps / s
------------------------------------------------------------------------------
laghos_test3_laghos_3_1__arm_N_1_MPI_64_OMP_1
   - builtin
      * num_tasks: 64
      * Major kernels total time: 25.775125467 s
      * Major kernels total rate: 7.5853121743 Mdofs x steps / s
------------------------------------------------------------------------------
laghos_test3_laghos_3_1__gcc__3a63qmj_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Major kernels total time: 14.99363824 s
      * Major kernels total rate: 13.0396885579 Mdofs x steps / s
------------------------------------------------------------------------------
laghos_test3_laghos_3_1__gcc__3a63qmj_N_1_MPI_4_OMP_1
   - builtin
      * num_tasks: 4
      * Major kernels total time: 8.606444554 s
      * Major kernels total rate: 22.716973516 Mdofs x steps / s
------------------------------------------------------------------------------
laghos_test3_laghos_3_1__gcc__3a63qmj_N_1_MPI_16_OMP_1
   - builtin
      * num_tasks: 16
      * Major kernels total time: 14.683130275 s
      * Major kernels total rate: 13.3154422346 Mdofs x steps / s
------------------------------------------------------------------------------
laghos_test3_laghos_3_1__gcc__3a63qmj_N_1_MPI_64_OMP_1
   - builtin
      * num_tasks: 64
      * Major kernels total time: 25.600715535 s
      * Major kernels total rate: 7.636988612 Mdofs x steps / s
------------------------------------------------------------------------------
laghos_test3_laghos_3_1__nvhpc_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Major kernels total time: 17.060229793 s
      * Major kernels total rate: 11.4601254129 Mdofs x steps / s
------------------------------------------------------------------------------
laghos_test3_laghos_3_1__nvhpc_N_1_MPI_4_OMP_1
   - builtin
      * num_tasks: 4
      * Major kernels total time: 9.159993388 s
      * Major kernels total rate: 21.344160931 Mdofs x steps / s
------------------------------------------------------------------------------
laghos_test3_laghos_3_1__nvhpc_N_1_MPI_16_OMP_1
   - builtin
      * num_tasks: 16
      * Major kernels total time: 14.841085262 s
      * Major kernels total rate: 13.1737248017 Mdofs x steps / s
------------------------------------------------------------------------------
laghos_test3_laghos_3_1__nvhpc_N_1_MPI_64_OMP_1
   - builtin
      * num_tasks: 64
      * Major kernels total time: 26.239687812 s
      * Major kernels total rate: 7.4510174969 Mdofs x steps / s
------------------------------------------------------------------------------
```

### On-node Compiler Comparison

(this is a taste, more details of 3 compiler comparison later in scaling)
Performance comparison of 3 compilers. Measure is Major kernels total rate in megadorf x steps / seconds which is relevant and despite total time, an scalable measure.

| Cores | arm        | gcc        | nvhpc      | 
|-------|------------|------------|------------|
| 64    | 25.77      | 25.60      | 26.23      |

### Serial Hot-spot Profile

List of top-10 functions / code locations from a serial profile.

Profiling command used: I actually used the normal reframe test case run, but the script includes flags for _PROFILE\_RUN_ and _DEBUG\_RUN_ which I use to set it up for profiling or a short run for debug. 
```
reframe --stage /scratch/home/${USER} -c t3.py -r --performance-report
```

The profiling is done on arm compiler, by using the ReFrame's _LaunchWrapper_ call map like this:
```
self.job.launcher = LauncherWrapper(self.job.launcher,'map',['--profile', '--export-functions='+self.proffile])
```

The resulting top 10:

|depth|Self |Total|Child|MPI|Overhead|Regions|Function                                                                                                                                                                                                                                                                                                            |
|-----|-----|-----|-----|---|--------|-------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|0    |35.1%|35.1%|     |   |        |       |mfem::PAMassApply(int, int, int, int, mfem::Array<double                                                                                                                                                                                                                                                            |
|0    |8.7% |19.1%|10.4%|   |        |       |double mfem::kernels::CalcSingularvalue<3>(double const*, int)                                                                                                                                                                                                                                                      |
|0    |8.5% |8.5% |     |   |        |       |mfem::ElementRestriction::MultTranspose(mfem::Vector const&, mfem::Vector&) const                                                                                                                                                                                                                                   |
|0    |7.0% |26.1%|19.1%|   |        |       |void mfem::hydrodynamics::QUpdateBody<3>(int, int, int, int, bool, bool, double, double, double, double, double*, double*, double*, double*, double*, double*, double*, double*, double*, double const*, double const*, double const*, double const*, double const*, double const*, double const*, double*, double*)|
|0    |6.5% |6.5% |     |   |        |       |mfem::D2QGrad(mfem::FiniteElementSpace const&, mfem::DofToQuad const*, mfem::Vector const&, mfem::Vector&)                                                                                                                                                                                                          |
|0    |6.5% |6.5% |     |   |        |       |mfem::ElementRestriction::Mult(mfem::Vector const&, mfem::Vector&) const                                                                                                                                                                                                                                            |
|0    |4.1% |4.1% |     |   |        |       |void mfem::hydrodynamics::ForceMult3D<3, 3, 4, 2>(int, mfem::Array<double                                                                                                                                                                                                                                           |
|0    |3.6% |4.8% |1.2% |   |        |       |mfem::kernels::internal::KernelVector3S(int const&, double const&, double const&, double const&, double&, double&, double&)                                                                                                                                                                                         |
|0    |3.0% |3.0% |     |   |        |       |void mfem::hydrodynamics::ForceMultTranspose3D<3, 3, 4, 2>(int, mfem::Array<double                                                                                                                                                                                                                                  |
|0    |2.5% |2.5% |     |   |        |       |mfem::add(mfem::Vector const&, double, mfem::Vector const&, mfem::Vector&)                                                                                                                                                                                                                                          |


### Full Node Hot-spot Profile

List of top-10 functions / code locations from a full node profile.

Profiling command used: I actually used the normal reframe test case run, but the script includes flags for _PROFILE\_RUN_ and _DEBUG\_RUN_ which I use to set it up for profiling or a short run for debug. 
```
reframe --stage /scratch/home/${USER} -c t2.py -r --performance-report
```

The profiling is done on arm compiler, by using the ReFrame's _LaunchWrapper_ call map like this:
```
self.job.launcher = LauncherWrapper(self.job.launcher,'map',['--profile', '--export-functions='+self.proffile])
```

|depth|Self |Total|Child|MPI  |Overhead|Regions|Function                                                                                                                                                                                                                                                                                                            |
|-----|-----|-----|-----|-----|--------|-------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|0    |71.1%|71.1%|     |71.1%|        |       |MPI_Allreduce                                                                                                                                                                                                                                                                                                       |
|0    |10.1%|10.1%|     |10.1%|        |       |MPI_Waitall                                                                                                                                                                                                                                                                                                         |
|0    |8.1% |8.1% |     |8.1% |        |       |MPI_Waitany                                                                                                                                                                                                                                                                                                         |
|0    |5.3% |5.3% |     |5.3% |        |       |MPI_Isend                                                                                                                                                                                                                                                                                                           |
|0    |3.5% |3.5% |     |3.5% |        |       |MPI_Irecv                                                                                                                                                                                                                                                                                                           |
|0    |0.3% |0.3% |     |     |        |       |mfem::PAMassApply(int, int, int, int, mfem::Array<double                                                                                                                                                                                                                                                            |
|0    |0.2% |0.2% |     |0.2% |        |       |MPI_Barrier                                                                                                                                                                                                                                                                                                         |
|0    |0.1% |4.5% |4.4% |4.4% |        |       |void mfem::GroupCommunicator::BcastBegin<double>(double*, int) const                                                                                                                                                                                                                                                |
|0    |0.1% |0.1% |     |0.1% |        |       |MPI_Finalize                                                                                                                                                                                                                                                                                                        |
|0    |0.1% |4.5% |4.4% |4.4% |        |       |void mfem::GroupCommunicator::ReduceBegin<double>(double const*) const                                                                                                                                                                                                                                              |

### Strong Scaling Study

On-node scaling study for 3 compilers. Here 'major kernels total time' in seconds, is reported. 

| Cores | arm    | gcc    | nvhpc  |
|-------|--------|--------|--------|
| 1     | 19.16  | 14.99  | 17.06  |
| 4     | 9.53   | 8.60   | 9.15   |
| 16    | 14.21  | 14.68  | 14.84  |
| 64    | 25.77  | 25.60  | 26.23  |

### Maths Library Report (OR how we analyzed the absence of math libraries)

Ok I don't have Maths Library report, but as I put time into this, I just want to document this: initially we didn't know if an app was using blas or not, as the perf lib tool thing, did not even make an empty file in case there was no call (not nice!) so first I made sure that openblas was there, like, in real to do that I tried ldd to see what libraries are linked:

```
 ldd /scratch/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/laghos-3.1-qsrtkaefmj3xu4lx676h2syhsspwwzpo/bin/laghos | grep blas
```

Showing openblas, but it turned out it was only there due to HYPRE bringing it in (HYPRE itself there due to MFEM) so long story short being in ldd we thought it must be using it but it didn't but how would we be sure? ltrace to the rescue:
```
 ltrace -l libopenblas.so.0 laghos
```
and no calls! Case closed.

## Optimisation

Initially the package did not set _any_ compiler flag. I fiddled with them a little bit, and the clear thing to do was to go with inlining and -Ofast. I picked gnu compiler as it was the fastest among the compilers and added those flags (and well, Ofast is only available on gnu). Gains were mostly evident in serial (single core) and they where still very modest changes as it can be seen, but well, C'est la vie! (A modest 3% enhancement is observed)

### Compiler Flag Tuning

No compiler flag was set before.

Compiler flags after:
```
CXXFLAGS= -Ofast -finline-functions
```

#### Compiler Flag Performance

Major kernel time for different test cases. Among the enhancements are 2 or 3%, greatest enhancement is in test case 3 of a modest 3.3% .

| test case | Original Flags | New Flags |
|-----------|----------------|-----------|
| 1         | 2.31           | 2.27      |
| 2         | 112.60         | 108.81    |
| 3         | 10.09          | 9.75      |
| 4         | 14.99          | 14.58     |

### Performance Regression

How fast can you make the code? 3% faster with compiler tuning.

## Report

### Compilation Summary

The program compiled smoothly for all but 1 compiler, and that 1 was _nvhpc_ due to it being unable to compile cmake, the solution was to build whatever nvhpc can't build with other (in my case I went with gcc) compilers which can.

### Performance Summary

![alt text](https://raw.githubusercontent.com/ImanHosseini/Cloud-HPC-Hackathon-2021/app/laghos/Applications/MiniApps/laghos/ser_sum.PNG)
 
The application uses _MFEM_ which in itself brings in _HYPRE_ which then draws along _openblas_ but it seems that no call to blas is made, even though using _ldd_ showed that openblas **IS** linked. Using the _ARM MAP_ profiler for a serial run, we can see that the app is compute bound and we have low CPI (Cycles Per Instruction) which is nice and hints at good vectorization. 

### Optimisation Summary

The app didn't set any compiler flag, so the obvious thing to do was to add a variant with optimization flags, this got us a modest increase of 3% through 'Ofast' and function inline being added.  
