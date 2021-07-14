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
For validation, we have a combination of 3 compilers, 7 mpi parameters and 4 test cases, which results into 84 test runs in total. The 3 compilers are `gcc@10.3.0`, `arm@21.0.0.879`, and `nvhpc@21.2`. The 7 mpi parameters are numbers of cores used, which are powers of 2 from 1(2^0) to 64(2^6). The 4 test cases are verification of 6, 7, 9, and 10 of https://github.com/CEED/Remhos/tree/v1.0#verification-of-results, which are chosen to cover the {Remap Mode, Transport Mode} x {2D Mode, 3D Mode} combination. As suggested by Remhos, we compare the resulting `mass` and `max` to the values, with a tolerance of relative error of `1e-9`. 

| Test Case     | `mass`        | `max`        |
|---------------|---------------|--------------|
| 2DRemap       | 0.08479546727 | 0.8378749205 |
| 3DRemap       | 0.1197297047  | 0.9985405673 |
| 2DTransport   | 0.1623263888  | 0.7469836332 |
| 3DTransport   | 0.9607429525  | 0.767823337  |

#### ReFrame Validation Output

Refer to [validation.txt](validation.txt) to check the Reframe Validation Output.

### Performance Analysis

#### On-node Profiling Across Compilers and Test Cases

We choose the execution time of the program as our metric. These data come with the validation script since we enable the performance report and set the corresponding reference and pattern. Refer to [perflogs/aws/c6gn/](perflogs/aws/c6gn/) and [validation.txt](validation.txt) to check the raw performance report. The following tables collect the result across different test cases, different compilers and different resourses, where the experiments are done on AWS C6gn.

##### Test Case 1: 2DRemap
| Cores | `gcc@10.3.0` | `arm@21.0.0.879` | `nvhpc@21.2` |
|-------|--------------|------------------|--------------|
| 1     |  18.55 s     |   21.20 s        |   22.83 s    |
| 2     |  10.07 s     |   11.09 s        |   12.22 s    |
| 4     |   5.99 s     |    6.47 s        |    7.03 s    |
| 8     |   4.22 s     |    4.45 s        |    5.16 s    |
| 16    |   4.57 s     |    3.85 s        |    4.03 s    |
| 32    |   5.03 s     |    4.07 s        |    4.20 s    |
| 64    |   7.39 s     |    5.44 s        |    6.17 s    |

##### Test Case 2: 3DRemap
| Cores | `gcc@10.3.0` | `arm@21.0.0.879` | `nvhpc@21.2` |
|-------|--------------|------------------|--------------|
| 1     |  10.46 s     |   12.08 s        |   13.35 s    |
| 2     |   5.82 s     |    6.49 s        |    7.29 s    |
| 4     |   3.60 s     |    4.21 s        |    4.31 s    |
| 8     |   2.51 s     |    2.67 s        |    3.24 s    |
| 16    |   2.21 s     |    2.28 s        |    2.39 s    |
| 32    |   2.37 s     |    2.42 s        |    2.50 s    |
| 64    |   3.27 s     |    3.34 s        |    3.35 s    |

##### Test Case 3: 2DTransport
| Cores | `gcc@10.3.0` | `arm@21.0.0.879` | `nvhpc@21.2` |
|-------|--------------|------------------|--------------|
| 1     |   7.42 s     |    7.52 s        |    7.85 s    |
| 2     |   4.45 s     |    4.50 s        |    4.67 s    |
| 4     |   3.03 s     |    3.06 s        |    3.15 s    |
| 8     |   2.47 s     |    2.48 s        |    2.53 s    |
| 16    |   2.53 s     |    2.45 s        |    2.48 s    |
| 32    |   2.87 s     |    3.35 s        |    2.89 s    |
| 64    |   4.09 s     |    4.07 s        |    4.71 s    |

##### Test Case 4: 3DTransport
| Cores | `gcc@10.3.0` | `arm@21.0.0.879` | `nvhpc@21.2` |
|-------|--------------|------------------|--------------|
| 1     |   9.70 s     |   10.19 s        |   11.46 s    |
| 2     |   5.67 s     |    5.93 s        |    6.48 s    |
| 4     |   3.71 s     |    3.87 s        |    4.13 s    |
| 8     |   2.95 s     |    3.04 s        |    3.17 s    |
| 16    |   3.04 s     |    3.48 s        |    3.10 s    |
| 32    |   3.46 s     |    3.48 s        |    3.55 s    |
| 64    |   4.72 s     |    4.87 s        |    4.76 s    |

#### Serial Hot-spot Profile
Refer to [profile/serial/README.md](profile/serial/README.md).

#### Full Node Hot-spot Profile
Refer to [profile/full/README.md](profile/full/README.md).

#### Strong Scaling Study
[ReFrame Strong Scaling Script](remhos_strong_scaling.py)

```
reframe -c remhos_strong_scaling.py -r --performance-report -v
```

#### Strong Scaling Study Details
For strong scaling study, we have a combination of 3 compilers, 9 parallelism schemes and 4 test cases, which results into 108 test runs in total. The 3 compilers are `gcc@10.3.0`, `arm@21.0.0.879`, and `nvhpc@21.2`. The 9 parallelism schemes are {1 node, 2 nodes, 4 nodes} x {16 cores in total, 32 cores in total, 64 cores in total}. The 4 test cases are verification of 6, 7, 9, and 10 of https://github.com/CEED/Remhos/tree/v1.0#verification-of-results, which are chosen to cover the {Remap Mode, Transport Mode} x {2D Mode, 3D Mode} combination. The following tables collect the result across different test cases, different compilers and different resourses, where the experiments are done on AWS C6gn.

##### Test Case 1: 2DRemap
| Nodes | Cores Per Node | Total Cores | `gcc@10.3.0` | `arm@21.0.0.879` | `nvhpc@21.2` |
|-------|----------------|-------------|--------------|------------------|--------------|
| 1     |         16     |        16   |              |                  |              |
| 1     |         32     |        32   |              |                  |              |
| 1     |         64     |        64   |              |                  |              |
| 2     |          8     |        16   |              |                  |              |
| 2     |         16     |        32   |              |                  |              |
| 2     |         32     |        64   |              |                  |              |
| 4     |          4     |        16   |              |                  |              |
| 4     |          8     |        32   |              |                  |              |
| 4     |         16     |        64   |              |                  |              |

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
