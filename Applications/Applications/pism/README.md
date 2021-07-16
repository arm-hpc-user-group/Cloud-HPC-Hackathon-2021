# PISM 

**Description:** Parallel Ice Sheet Model

**URL:** http://pism-docs.org/wiki/doku.php

**Team:** Iman

## Compilation

### Spack Package Modification

Details of any changes to the Spack recipe used.

Git commit hash of checkout for pacakage: 

Pull request for Spack recipe changes: 

### Building PISM

#### Compiler 1 ARM

```
spack install pism%arm
```

```
$ spack spec -Il pism%arm
Input spec
--------------------------------
pism%arm

Concretized
--------------------------------
==> Warning: arm@21.0.0.879 cannot build optimized binaries for "graviton2". Using best target possible: "aarch64"
pism@1.1.4%arm@21.0.0.879~doc~everytrace~examples~extra~icebin~ipo~parallel-hdf5~parallel-netcdf3~parallel-netcdf4+proj~python+shared build_type=RelWithDebInfo arch=linux-amzn2-aarch64
    ^cmake@3.20.5%arm@21.0.0.879~doc+ncurses+openssl+ownlibs~qt build_type=Release arch=linux-amzn2-aarch64
        ^ncurses@6.2%arm@21.0.0.879~symlinks+termlib abi=none arch=linux-amzn2-aarch64
            ^pkgconf@1.7.4%arm@21.0.0.879 arch=linux-amzn2-aarch64
        ^openssl@1.1.1k%arm@21.0.0.879~docs+systemcerts arch=linux-amzn2-aarch64
            ^perl@5.32.1%arm@21.0.0.879+cpanm+shared+threads arch=linux-amzn2-aarch64
                ^berkeley-db@18.1.40%arm@21.0.0.879+cxx~docs+stl patches=b231fcc4d5cff05e5c3a4814f6a5af0e9a966428dc2176540d2c05aff41de522 arch=linux-amzn2-aarch64
                ^bzip2@1.0.8%arm@21.0.0.879~debug~pic+shared arch=linux-amzn2-aarch64
                    ^diffutils@3.7%arm@21.0.0.879 arch=linux-amzn2-aarch64
                        ^libiconv@1.16%arm@21.0.0.879 arch=linux-amzn2-aarch64
                ^gdbm@1.19%arm@21.0.0.879 arch=linux-amzn2-aarch64
                    ^readline@8.1%arm@21.0.0.879 arch=linux-amzn2-aarch64
                ^zlib@1.2.11%arm@21.0.0.879+optimize+pic+shared arch=linux-amzn2-aarch64
    ^fftw@3.3.9%arm@21.0.0.879+mpi~openmp~pfft_patches precision=double,float arch=linux-amzn2-aarch64
        ^openmpi@4.1.0%arm@21.0.0.879~atomics~cuda~cxx~cxx_exceptions+gpfs~internal-hwloc~java~legacylaunchers~lustre~memchecker+pmi~singularity~sqlite3+static~thread_multiple+vt+wrapper-rpath fabrics=ofi patches=60ce20bc14d98c572ef7883b9fcd254c3f232c2f3a13377480f96466169ac4c8 schedulers=slurm arch=linux-amzn2-aarch64
            ^hwloc@2.5.0%arm@21.0.0.879~cairo~cuda~gl~libudev+libxml2~netloc~nvml+pci+shared arch=linux-amzn2-aarch64
                ^libpciaccess@0.16%arm@21.0.0.879 arch=linux-amzn2-aarch64
                    ^libtool@2.4.6%arm@21.0.0.879 arch=linux-amzn2-aarch64
                        ^m4@1.4.18%arm@21.0.0.879+sigsegv patches=3877ab548f88597ab2327a2230ee048d2d07ace1062efe81fc92e91b7f39cd00,fc9b61654a3ba1a8d6cd78ce087e7c96366c290bc8d2c299f09828d793b853c8 arch=linux-amzn2-aarch64
                            ^libsigsegv@2.13%arm@21.0.0.879 arch=linux-amzn2-aarch64
                    ^util-macros@1.19.3%arm@21.0.0.879 arch=linux-amzn2-aarch64
                ^libxml2@2.9.10%arm@21.0.0.879~python arch=linux-amzn2-aarch64
                    ^xz@5.2.5%arm@21.0.0.879~pic libs=shared,static arch=linux-amzn2-aarch64
            ^libevent@2.1.12%arm@21.0.0.879+openssl arch=linux-amzn2-aarch64
            ^libfabric@1.11.1-aws%arm@21.0.0.879~debug~kdreg fabrics=sockets,tcp,udp arch=linux-amzn2-aarch64
            ^numactl@2.0.14%arm@21.0.0.879 patches=4e1d78cbbb85de625bad28705e748856033eaafab92a66dffd383a3d7e00cc94,62fc8a8bf7665a60e8f4c93ebbd535647cebf74198f7afafec4c085a8825c006 arch=linux-amzn2-aarch64
                ^autoconf@2.69%arm@21.0.0.879 arch=linux-amzn2-aarch64
                ^automake@1.16.3%arm@21.0.0.879 arch=linux-amzn2-aarch64
            ^openssh@8.5p1%arm@21.0.0.879 arch=linux-amzn2-aarch64
                ^libedit@3.1-20210216%arm@21.0.0.879 arch=linux-amzn2-aarch64
            ^slurm@20-02-4-1%arm@21.0.0.879~gtk~hdf5~hwloc~mariadb~pmix+readline~restd sysconfdir=PREFIX/etc arch=linux-amzn2-aarch64
    ^gsl@2.7%arm@21.0.0.879~external-cblas arch=linux-amzn2-aarch64
    ^netcdf-c@4.8.0%arm@21.0.0.879~dap~fsync~hdf4~jna+mpi~parallel-netcdf+pic+shared arch=linux-amzn2-aarch64
        ^hdf5@1.10.7%arm@21.0.0.879~cxx~fortran+hl~ipo~java+mpi+shared~szip~threadsafe+tools api=default build_type=RelWithDebInfo arch=linux-amzn2-aarch64
    ^petsc@3.15.1%arm@21.0.0.879~X~batch~cgns~complex~cuda~debug+double~exodusii~fftw~giflib+hdf5~hwloc+hypre~int64~jpeg~knl~libpng~libyaml~memkind+metis~mkl-pardiso~moab~mpfr+mpi~mumps~openmp~p4est~ptscotch~random123~rocm~saws+shared~suite-sparse+superlu-dist~trilinos~valgrind amdgpu_target=none clanguage=C cuda_arch=none arch=linux-amzn2-aarch64
        ^hypre@2.22.0%arm@21.0.0.879~complex~cuda~debug~int64~internal-superlu~mixedint+mpi~openmp+shared~superlu-dist~unified-memory cuda_arch=none arch=linux-amzn2-aarch64
            ^openblas@0.3.15%arm@21.0.0.879~bignuma~consistent_fpcsr~ilp64+locking+pic+shared threads=none arch=linux-amzn2-aarch64
        ^metis@5.1.0%arm@21.0.0.879~gdb~int64~real64+shared build_type=Release patches=4991da938c1d3a1d3dea78e49bbebecba00273f98df2a656e38b83d55b281da1 arch=linux-amzn2-aarch64
        ^parmetis@4.0.3%arm@21.0.0.879~gdb~int64~ipo+shared build_type=RelWithDebInfo patches=4f892531eb0a807eb1b82e683a416d3e35154a455274cf9b162fb02054d11a5b,50ed2081bc939269689789942067c58b3e522c269269a430d5d34c00edbc5870,704b84f7c7444d4372cb59cca6e1209df4ef3b033bc4ee3cf50f369bce972a9d arch=linux-amzn2-aarch64
        ^python@3.8.11%arm@21.0.0.879+bz2+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tix~tkinter~ucs4+uuid+zlib patches=0d98e93189bc278fbc37a50ed7f183bd8aaf249a8e1670a465f0db6bb4f8cf87 arch=linux-amzn2-aarch64
            ^expat@2.4.1%arm@21.0.0.879+libbsd arch=linux-amzn2-aarch64
                ^libbsd@0.11.3%arm@21.0.0.879 arch=linux-amzn2-aarch64
                    ^libmd@1.0.3%arm@21.0.0.879 arch=linux-amzn2-aarch64
            ^gettext@0.21%arm@21.0.0.879+bzip2+curses+git~libunistring+libxml2+tar+xz arch=linux-amzn2-aarch64
                ^tar@1.34%arm@21.0.0.879 arch=linux-amzn2-aarch64
            ^libffi@3.3%arm@21.0.0.879 patches=26f26c6f29a7ce9bf370ad3ab2610f99365b4bdd7b82e7c31df41a3370d685c0 arch=linux-amzn2-aarch64
            ^sqlite@3.35.5%arm@21.0.0.879+column_metadata+fts~functions~rtree arch=linux-amzn2-aarch64
            ^util-linux-uuid@2.36.2%arm@21.0.0.879 arch=linux-amzn2-aarch64
        ^superlu-dist@6.4.0%arm@21.0.0.879~cuda~int64~ipo~openmp+shared build_type=RelWithDebInfo cuda_arch=none arch=linux-amzn2-aarch64
    ^proj@4.9.2%arm@21.0.0.879+curl+tiff arch=linux-amzn2-aarch64
    ^udunits@2.2.28%arm@21.0.0.879 arch=linux-amzn2-aarch64

```

#### Compiler 2 GCC

```
spack install pism%gcc
```

```
$ spack spec -Il pism%gcc
Input spec
--------------------------------
 -   pism%gcc

Concretized
--------------------------------
[+]  cijv4kn  pism@1.1.4%gcc@10.3.0~doc~everytrace~examples~extra~icebin~ipo~parallel-hdf5~parallel-netcdf3~parallel-netcdf4+proj~python+shared build_type=RelWithDebInfo arch=linux-amzn2-graviton2
[+]  m7325ee      ^cmake@3.20.5%gcc@10.3.0~doc+ncurses+openssl+ownlibs~qt build_type=Release arch=linux-amzn2-graviton2
[+]  iwzirqc          ^ncurses@6.2%gcc@10.3.0~symlinks+termlib abi=none arch=linux-amzn2-graviton2
[+]  s4pw7zm              ^pkgconf@1.7.4%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  5i3lgfb          ^openssl@1.1.1k%gcc@10.3.0~docs+systemcerts arch=linux-amzn2-graviton2
[+]  4m7exgb              ^perl@5.32.1%gcc@10.3.0+cpanm+shared+threads arch=linux-amzn2-graviton2
[+]  y42m6yr                  ^berkeley-db@18.1.40%gcc@10.3.0+cxx~docs+stl patches=b231fcc4d5cff05e5c3a4814f6a5af0e9a966428dc2176540d2c05aff41de522 arch=linux-amzn2-graviton2
[+]  rqrpmap                  ^bzip2@1.0.8%gcc@10.3.0~debug~pic+shared arch=linux-amzn2-graviton2
[+]  2w7bert                      ^diffutils@3.7%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  y5ei3cm                          ^libiconv@1.16%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  wjwqncx                  ^gdbm@1.19%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  3zy7kxk                      ^readline@8.1%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  qepjcvj                  ^zlib@1.2.11%gcc@10.3.0+optimize+pic+shared arch=linux-amzn2-graviton2
[+]  cgb46v5      ^fftw@3.3.9%gcc@10.3.0+mpi~openmp~pfft_patches precision=double,float arch=linux-amzn2-graviton2
[+]  zvamksn          ^openmpi@4.1.0%gcc@10.3.0~atomics~cuda~cxx~cxx_exceptions+gpfs~internal-hwloc~java~legacylaunchers~lustre~memchecker+pmi~singularity~sqlite3+static~thread_multiple+vt+wrapper-rpath fabrics=ofi patches=60ce20bc14d98c572ef7883b9fcd254c3f232c2f3a13377480f96466169ac4c8 schedulers=slurm arch=linux-amzn2-graviton2
[+]  cukmqbg              ^hwloc@2.5.0%gcc@10.3.0~cairo~cuda~gl~libudev+libxml2~netloc~nvml+pci+shared arch=linux-amzn2-graviton2
[+]  asgtk6a                  ^libpciaccess@0.16%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  z2uysov                      ^libtool@2.4.6%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  ebhjpix                          ^m4@1.4.18%gcc@10.3.0+sigsegv patches=3877ab548f88597ab2327a2230ee048d2d07ace1062efe81fc92e91b7f39cd00,fc9b61654a3ba1a8d6cd78ce087e7c96366c290bc8d2c299f09828d793b853c8 arch=linux-amzn2-graviton2
[+]  ltbv6bk                              ^libsigsegv@2.13%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  4xr3hhh                      ^util-macros@1.19.3%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  iyhm3wi                  ^libxml2@2.9.10%gcc@10.3.0~python arch=linux-amzn2-graviton2
[+]  ye3kcvv                      ^xz@5.2.5%gcc@10.3.0~pic libs=shared,static arch=linux-amzn2-graviton2
[+]  tadxrfp              ^libevent@2.1.12%gcc@10.3.0+openssl arch=linux-amzn2-graviton2
[+]  72f5gvk              ^libfabric@1.11.1-aws%gcc@10.3.0~debug~kdreg fabrics=sockets,tcp,udp arch=linux-amzn2-graviton2
[+]  mhav5gn              ^numactl@2.0.14%gcc@10.3.0 patches=4e1d78cbbb85de625bad28705e748856033eaafab92a66dffd383a3d7e00cc94,62fc8a8bf7665a60e8f4c93ebbd535647cebf74198f7afafec4c085a8825c006 arch=linux-amzn2-graviton2
[+]  jkuhz64                  ^autoconf@2.69%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  xb2w5nc                  ^automake@1.16.3%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  wturp6c              ^openssh@8.5p1%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  ivotdt7                  ^libedit@3.1-20210216%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  wqpuvmh              ^slurm@20-02-4-1%gcc@10.3.0~gtk~hdf5~hwloc~mariadb~pmix+readline~restd sysconfdir=PREFIX/etc arch=linux-amzn2-graviton2
[+]  4m43k5h      ^gsl@2.7%gcc@10.3.0~external-cblas arch=linux-amzn2-graviton2
[+]  tfzbzgi      ^netcdf-c@4.8.0%gcc@10.3.0~dap~fsync~hdf4~jna+mpi~parallel-netcdf+pic+shared arch=linux-amzn2-graviton2
[+]  cg7z7ep          ^hdf5@1.10.7%gcc@10.3.0~cxx~fortran+hl~ipo~java+mpi+shared~szip~threadsafe+tools api=default build_type=RelWithDebInfo arch=linux-amzn2-graviton2
[+]  hgy2uze      ^petsc@3.15.1%gcc@10.3.0~X~batch~cgns~complex~cuda~debug+double~exodusii~fftw~giflib+hdf5~hwloc+hypre~int64~jpeg~knl~libpng~libyaml~memkind+metis~mkl-pardiso~moab~mpfr+mpi~mumps~openmp~p4est~ptscotch~random123~rocm~saws+shared~suite-sparse+superlu-dist~trilinos~valgrind amdgpu_target=none clanguage=C cuda_arch=none arch=linux-amzn2-graviton2
[+]  dxd63gx          ^hypre@2.22.0%gcc@10.3.0~complex~cuda~debug~int64~internal-superlu~mixedint+mpi~openmp+shared~superlu-dist~unified-memory cuda_arch=none arch=linux-amzn2-graviton2
[+]  rv7gj6u              ^openblas@0.3.15%gcc@10.3.0~bignuma~consistent_fpcsr~ilp64+locking+pic+shared threads=none arch=linux-amzn2-graviton2
[+]  a3tjh3r          ^metis@5.1.0%gcc@10.3.0~gdb~int64~real64+shared build_type=Release patches=4991da938c1d3a1d3dea78e49bbebecba00273f98df2a656e38b83d55b281da1,b1225da886605ea558db7ac08dd8054742ea5afe5ed61ad4d0fe7a495b1270d2 arch=linux-amzn2-graviton2
[+]  b2toc3n          ^parmetis@4.0.3%gcc@10.3.0~gdb~int64~ipo+shared build_type=RelWithDebInfo patches=4f892531eb0a807eb1b82e683a416d3e35154a455274cf9b162fb02054d11a5b,50ed2081bc939269689789942067c58b3e522c269269a430d5d34c00edbc5870,704b84f7c7444d4372cb59cca6e1209df4ef3b033bc4ee3cf50f369bce972a9d arch=linux-amzn2-graviton2
[+]  62czasr          ^python@3.8.11%gcc@10.3.0+bz2+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tix~tkinter~ucs4+uuid+zlib patches=0d98e93189bc278fbc37a50ed7f183bd8aaf249a8e1670a465f0db6bb4f8cf87 arch=linux-amzn2-graviton2
[+]  ychdz7l              ^expat@2.4.1%gcc@10.3.0+libbsd arch=linux-amzn2-graviton2
[+]  ourxkez                  ^libbsd@0.11.3%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  nssrqfc                      ^libmd@1.0.3%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  fqlpcsl              ^gettext@0.21%gcc@10.3.0+bzip2+curses+git~libunistring+libxml2+tar+xz arch=linux-amzn2-graviton2
[+]  v6cutkh                  ^tar@1.34%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  35cffos              ^libffi@3.3%gcc@10.3.0 patches=26f26c6f29a7ce9bf370ad3ab2610f99365b4bdd7b82e7c31df41a3370d685c0 arch=linux-amzn2-graviton2
[+]  2q753q6              ^sqlite@3.35.5%gcc@10.3.0+column_metadata+fts~functions~rtree arch=linux-amzn2-graviton2
[+]  2non7qx              ^util-linux-uuid@2.36.2%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  vge5zmp          ^superlu-dist@6.4.0%gcc@10.3.0~cuda~int64~ipo~openmp+shared build_type=RelWithDebInfo cuda_arch=none arch=linux-amzn2-graviton2
[+]  25zx47p      ^proj@4.9.2%gcc@10.3.0+curl+tiff arch=linux-amzn2-graviton2
[+]  pynfpe5      ^udunits@2.2.28%gcc@10.3.0 arch=linux-amzn2-graviton2
```

## Validation & Perf

** as they will be similar, let's go over this for all test cases here **

pism is a big project, and a well maintained one. They make verification super-easy and have an specific binary for it called _pismv_ which takes the problem pick (among a bunch of verification problems they have made) as a flag and runs it. They are documented here: https://pism-docs.org/sphinx/manual/verification/index.html#tab-tests

At the end, we convenienty get relative error in 'relmaxETA'.

## Test Case 1: A isothermal SIA, steady, flat bed, constant accumulation

[ReFrame Benchmark 1](#)

```
../bin/reframe -c t0.py -r --performance-report
```

### ReFrame Output

```
==============================================================================
PERFORMANCE REPORT
------------------------------------------------------------------------------
pism_test0_2_pism_1_1_4__arm_N_1_MPI_1_OMP_1
- aws:c6gn
   - builtin
      * num_tasks: 1
      * Total time: 54.78 s
------------------------------------------------------------------------------
pism_test0_2_pism_1_1_4__arm_N_1_MPI_4_OMP_1
   - builtin
      * num_tasks: 4
      * Total time: 22.47 s
------------------------------------------------------------------------------
pism_test0_2_pism_1_1_4__arm_N_1_MPI_16_OMP_1
   - builtin
      * num_tasks: 16
      * Total time: 18.89 s
------------------------------------------------------------------------------
pism_test0_2_pism_1_1_4__arm_N_1_MPI_64_OMP_1
   - builtin
      * num_tasks: 64
      * Total time: 26.76 s
------------------------------------------------------------------------------
pism_test0_2_pism_1_1_4__gcc__cijv4kn_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Total time: 63.62 s
------------------------------------------------------------------------------
pism_test0_2_pism_1_1_4__gcc__cijv4kn_N_1_MPI_4_OMP_1
   - builtin
      * num_tasks: 4
      * Total time: 22.2 s
------------------------------------------------------------------------------
pism_test0_2_pism_1_1_4__gcc__cijv4kn_N_1_MPI_16_OMP_1
   - builtin
      * num_tasks: 16
      * Total time: 18.68 s
------------------------------------------------------------------------------
pism_test0_2_pism_1_1_4__gcc__cijv4kn_N_1_MPI_64_OMP_1
   - builtin
      * num_tasks: 64
      * Total time: 26.35 s
------------------------------------------------------------------------------
```

### On-node Compiler Comparison

Performance comparison of two compilers. More details in later parts.

| Cores | ARM   | GCC   |
|-------|-------|-------|
| 64    | 26.76 | 26.35 |

### Strong Scaling Study

On-node scaling study for two compilers.

| Cores | arm   | gcc   |
|-------|-------|-------|
| 1     | 54.78 | 63.62 | 
| 4     | 22.47 | 22.2  | 
| 16    | 18.89 | 18.68 | 
| 64    | 26.76 | 26.35 | 

## Test Case 2: B isothermal SIA, steady, flat bed, zero accumulation

[ReFrame Benchmark 1](#)

```
../bin/reframe -c t1.py -r --performance-report
```

### ReFrame Output TC2

```
==============================================================================
PERFORMANCE REPORT
------------------------------------------------------------------------------
pism_test1_2_pism_1_1_4__arm_N_1_MPI_1_OMP_1
- aws:c6gn
   - builtin
      * num_tasks: 1
      * Total time: 8.13 s
------------------------------------------------------------------------------
pism_test1_2_pism_1_1_4__arm_N_1_MPI_4_OMP_1
   - builtin
      * num_tasks: 4
      * Total time: 4.05 s
------------------------------------------------------------------------------
pism_test1_2_pism_1_1_4__arm_N_1_MPI_16_OMP_1
   - builtin
      * num_tasks: 16
      * Total time: 3.98 s
------------------------------------------------------------------------------
pism_test1_2_pism_1_1_4__arm_N_1_MPI_64_OMP_1
   - builtin
      * num_tasks: 64
      * Total time: 6.42 s
------------------------------------------------------------------------------
pism_test1_2_pism_1_1_4__gcc__cijv4kn_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Total time: 8.45 s
------------------------------------------------------------------------------
pism_test1_2_pism_1_1_4__gcc__cijv4kn_N_1_MPI_4_OMP_1
   - builtin
      * num_tasks: 4
      * Total time: 4.35 s
------------------------------------------------------------------------------
pism_test1_2_pism_1_1_4__gcc__cijv4kn_N_1_MPI_16_OMP_1
   - builtin
      * num_tasks: 16
      * Total time: 3.97 s
------------------------------------------------------------------------------
pism_test1_2_pism_1_1_4__gcc__cijv4kn_N_1_MPI_64_OMP_1
   - builtin
      * num_tasks: 64
      * Total time: 6.36 s
------------------------------------------------------------------------------
```

### On-node Compiler Comparison TC2

Performance comparison of two compilers. More details in later parts.

| Cores | ARM   | GCC   |
|-------|-------|-------|
| 64    | 6.42  | 6.36  |

### Strong Scaling  TC2

On-node scaling study for two compilers. Time is measured in seconds.

| Cores | arm   | gcc   |
|-------|-------|-------|
| 1     |  8.13 | 8.45  | 
| 4     |  4.05 | 4.35  | 
| 16    |  3.98 | 3.97  | 
| 64    |  6.42 | 6.36  | 

## Test Case 3: B isothermal SIA, steady, flat bed, growing accumulation

[ReFrame Benchmark 3](#)

```
../bin/reframe -c t2.py -r --performance-report
```

### ReFrame Output TC3

```
==============================================================================
PERFORMANCE REPORT
------------------------------------------------------------------------------
pism_test2_2_pism_1_1_4__arm_N_1_MPI_1_OMP_1
- aws:c6gn
   - builtin
      * num_tasks: 1
      * Total time: 14.76 s
------------------------------------------------------------------------------
pism_test2_2_pism_1_1_4__arm_N_1_MPI_4_OMP_1
   - builtin
      * num_tasks: 4
      * Total time: 6.76 s
------------------------------------------------------------------------------
pism_test2_2_pism_1_1_4__arm_N_1_MPI_16_OMP_1
   - builtin
      * num_tasks: 16
      * Total time: 6.28 s
------------------------------------------------------------------------------
pism_test2_2_pism_1_1_4__arm_N_1_MPI_64_OMP_1
   - builtin
      * num_tasks: 64
      * Total time: 10.0 s
------------------------------------------------------------------------------
pism_test2_2_pism_1_1_4__gcc__cijv4kn_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Total time: 15.22 s
------------------------------------------------------------------------------
pism_test2_2_pism_1_1_4__gcc__cijv4kn_N_1_MPI_4_OMP_1
   - builtin
      * num_tasks: 4
      * Total time: 6.93 s
------------------------------------------------------------------------------
pism_test2_2_pism_1_1_4__gcc__cijv4kn_N_1_MPI_16_OMP_1
   - builtin
      * num_tasks: 16
      * Total time: 6.3 s
------------------------------------------------------------------------------
pism_test2_2_pism_1_1_4__gcc__cijv4kn_N_1_MPI_64_OMP_1
   - builtin
      * num_tasks: 64
      * Total time: 9.75 s
------------------------------------------------------------------------------
```

### On-node Compiler Comparison TC3

Performance comparison of two compilers. More details in later parts.

| Cores | ARM   | GCC   |
|-------|-------|-------|
| 64    | 11.73 | 9.75  |

### Strong Scaling  TC3

On-node scaling study for two compilers. Time is measured in seconds. There was a weird anomaly here at 16 core on gcc, so I ran again (appended the class name with REDO to get a new directory) and here are the redo resutls:

| Cores | arm   | gcc   |
|-------|-------|-------|
| 1     | 14.76 | 15.22 | 
| 4     |  6.76 | 6.93  | 
| 16    |  6.28 | 6.3   | 
| 64    | 10.0  | 9.75  | 

## Test Case 4: D isothermal SIA, steady, flat bed, oscillating accumulation

[ReFrame Benchmark 4](#)

```
../bin/reframe -c t3.py -r --performance-report
```

### ReFrame Output TC4

```
==============================================================================
PERFORMANCE REPORT
------------------------------------------------------------------------------
pism_test3_2_pism_1_1_4__arm_N_1_MPI_1_OMP_1
- aws:c6gn
   - builtin
      * num_tasks: 1
      * Total time: 158.09 s
------------------------------------------------------------------------------
pism_test3_2_pism_1_1_4__arm_N_1_MPI_4_OMP_1
   - builtin
      * num_tasks: 4
      * Total time: 57.77 s
------------------------------------------------------------------------------
pism_test3_2_pism_1_1_4__arm_N_1_MPI_16_OMP_1
   - builtin
      * num_tasks: 16
      * Total time: 46.54 s
------------------------------------------------------------------------------
pism_test3_2_pism_1_1_4__arm_N_1_MPI_64_OMP_1
   - builtin
      * num_tasks: 64
      * Total time: 62.55 s
------------------------------------------------------------------------------
pism_test3_2_pism_1_1_4__gcc__cijv4kn_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Total time: 170.12 s
------------------------------------------------------------------------------
pism_test3_2_pism_1_1_4__gcc__cijv4kn_N_1_MPI_4_OMP_1
   - builtin
      * num_tasks: 4
      * Total time: 69.12 s
------------------------------------------------------------------------------
pism_test3_2_pism_1_1_4__gcc__cijv4kn_N_1_MPI_16_OMP_1
   - builtin
      * num_tasks: 16
      * Total time: 48.71 s
------------------------------------------------------------------------------
pism_test3_2_pism_1_1_4__gcc__cijv4kn_N_1_MPI_64_OMP_1
   - builtin
      * num_tasks: 64
      * Total time: 60.4 s
------------------------------------------------------------------------------
```

### On-node Compiler Comparison 4

Performance comparison of two compilers. More details in later parts.

| Cores | ARM   | GCC   |
|-------|-------|-------|
| 64    | 62.55 | 60.4  |

### Strong Scaling  TC4

On-node scaling study for two compilers. Time is measured in seconds.

| Cores | arm   | gcc   |
|-------|-------|-------|
| 1     | 158.09| 170.12| 
| 4     |  57.77| 69.12 | 
| 16    |  46.54| 48.71 | 
| 64    |  62.55| 60.4  | 


## Maths Library Report on Test Case 1

Report on use of maths library calls generated by (Perf Lib Tools)[https://github.com/ARM-software/perf-libs-tools].

apl files are attached, but they are from stage directory as I had to disable verification to get the perf to work, so I had to leep stage files and check them out there, but I also checked the outputs and verified the relative errors to be in compliance, so the verifaction too would've passed.

Running our arm build we get: I was hoping that they automagically be arm perf libs, but turns out they are openblas. 

Process full dataset for BLAS, LAPACK and FFT function usage.
Opening file plt_out/58086.apl
BLAS level 1     : count       5551    total time       0.0251  user count       5551  user time       0.0251
BLAS level 2     : count          0    total time       0.0000  user count          0  user time       0.0000
BLAS level 3     : count          0    total time       0.0000  user count          0  user time       0.0000
LAPACK           : count          0    total time       0.0000  user count          0  user time       0.0000
FFT              : count          0    total time       0.0000  user count          0  user time       0.0000
 
Double precision : count       5551    total time       0.0251  user count       5551  user time       0.0251
Single precision : count          0    total time       0.0000  user count          0  user time       0.0000
Double complex   : count          0    total time       0.0000  user count          0  user time       0.0000
Single complex   : count          0    total time       0.0000  user count          0  user time       0.0000
 
BLAS cases:
----------
BLAS level 1:
  dscal_     cnt=       5551  totTime=       0.0251   called_tot=       5551  topTime=       0.0251    (%age of runtime:  0.046 )
