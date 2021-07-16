# SIESTA 

**Description:** SIESTA performs electronic structure calculations and ab initio molecular dynamics simulations of molecules and solids.

**URL:** https://departments.icmab.es/leem/siesta/

**Team:** Garotes de Premià

## Compilation

### Spack Package Modification

Details of any changes to the Spack recipe used.

Git commit hash of checkout for pacakage:

Pull request for Spack recipe changes:

### Building SIESTA



#### GNU Fortran Compiler (GNU)

```
spack install siesta@4.0.1%gcc@10.3.0+metis
```

```
$ spack spec -Il siesta@4.0.1%gcc@10.3.0+metis
Input spec
 -   siesta@4.0.1%gcc@10.3.0+metis

Concretized
--------------------------------
[+]  e374e4q  siesta@4.0.1%gcc@10.3.0+metis patches=b8f722add750b1524767062c7a86de63a1da7990c27fda5321e43e34179e50fc arch=linux-amzn2-graviton2
[+]  a3tjh3r      ^metis@5.1.0%gcc@10.3.0~gdb~int64~real64+shared build_type=Release patches=4991da938c1d3a1d3dea78e49bbebecba00273f98df2a656e38b83d55b281da1,b1225da886605ea558db7ac08dd8054742ea5afe5ed61ad4d0fe7a495b1270d2 arch=linux-amzn2-graviton2
[+]  m7325ee          ^cmake@3.20.5%gcc@10.3.0~doc+ncurses+openssl+ownlibs~qt build_type=Release arch=linux-amzn2-graviton2
[+]  iwzirqc              ^ncurses@6.2%gcc@10.3.0~symlinks+termlib abi=none arch=linux-amzn2-graviton2
[+]  s4pw7zm                  ^pkgconf@1.7.4%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  5i3lgfb              ^openssl@1.1.1k%gcc@10.3.0~docs+systemcerts arch=linux-amzn2-graviton2
[+]  4m7exgb                  ^perl@5.32.1%gcc@10.3.0+cpanm+shared+threads arch=linux-amzn2-graviton2
[+]  y42m6yr                      ^berkeley-db@18.1.40%gcc@10.3.0+cxx~docs+stl patches=b231fcc4d5cff05e5c3a4814f6a5af0e9a966428dc2176540d2c05aff41de522 arch=linux-amzn2-graviton2
[+]  rqrpmap                      ^bzip2@1.0.8%gcc@10.3.0~debug~pic+shared arch=linux-amzn2-graviton2
[+]  2w7bert                          ^diffutils@3.7%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  y5ei3cm                              ^libiconv@1.16%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  wjwqncx                      ^gdbm@1.19%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  3zy7kxk                          ^readline@8.1%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  qepjcvj                      ^zlib@1.2.11%gcc@10.3.0+optimize+pic+shared arch=linux-amzn2-graviton2
[+]  tfzbzgi      ^netcdf-c@4.8.0%gcc@10.3.0~dap~fsync~hdf4~jna+mpi~parallel-netcdf+pic+shared arch=linux-amzn2-graviton2
[+]  cg7z7ep          ^hdf5@1.10.7%gcc@10.3.0~cxx~fortran+hl~ipo~java+mpi+shared~szip~threadsafe+tools api=default build_type=RelWithDebInfo arch=linux-amzn2-graviton2
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
[+]  72f5gvk                  ^libfabric@1.11.1-aws%gcc@10.3.0~debug~kdreg fabrics=sockets,tcp,udp arch=linux-amzn2-graviton2
[+]  mhav5gn                  ^numactl@2.0.14%gcc@10.3.0 patches=4e1d78cbbb85de625bad28705e748856033eaafab92a66dffd383a3d7e00cc94,62fc8a8bf7665a60e8f4c93ebbd535647cebf74198f7afafec4c085a8825c006 arch=linux-amzn2-graviton2
[+]  jkuhz64                      ^autoconf@2.69%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  xb2w5nc                      ^automake@1.16.3%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  wturp6c                  ^openssh@8.5p1%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  ivotdt7                      ^libedit@3.1-20210216%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  wqpuvmh                  ^slurm@20-02-4-1%gcc@10.3.0~gtk~hdf5~hwloc~mariadb~pmix+readline~restd sysconfdir=PREFIX/etc arch=linux-amzn2-graviton2
[+]  6ku6khi      ^netcdf-fortran@4.5.3%gcc@10.3.0~doc+pic+shared arch=linux-amzn2-graviton2
[+]  2jffbna      ^netlib-scalapack@2.1.0%gcc@10.3.0~ipo~pic+shared build_type=Release patches=1c9ce5fee1451a08c2de3cc87f446aeda0b818ebbce4ad0d980ddf2f2a0b2dc4,f2baedde688ffe4c20943c334f580eb298e04d6f35c86b90a1f4e8cb7ae344a2 arch=linux-amzn2-graviton2
[+]  rv7gj6u          ^openblas@0.3.15%gcc@10.3.0~bignuma~consistent_fpcsr~ilp64+locking+pic+shared threads=none arch=linux-amzn2-graviton2
```

#### ARM and Nvidia HPC Compilers

Unfortunetly we could not compile siesta with neither the ARM compiler nor the Nvidia one. 

On both compilers the compilation ends with the same error, after solving all the other errors
we encountered. The error is due to multiple definitions of `mpi_comm_world`, and we were not
able to find a solution. The error:

```
==> siesta: Executing phase: 'build'
==> Error: ProcessError: Command exited with status 2:
    'make'

2 errors found in build log:
     355    NVFORTRAN-S-0155-mpi_comm_world is use-associated from modules mpi_siesta and mpi__include, and cannot be accessed (/tmp/jvinyals/spack-stage/spack-stage-siesta-4.0.1-emukb7kkp46sefjkkzjt5nafsfai54l7/spack-src/Src/fdf/fdf
            .F90: 2829)
     356    NVFORTRAN-S-0155-mpi_comm_world is use-associated from modules mpi_siesta and mpi__include, and cannot be accessed (/tmp/jvinyals/spack-stage/spack-stage-siesta-4.0.1-emukb7kkp46sefjkkzjt5nafsfai54l7/spack-src/Src/fdf/fdf
            .F90: 2837)
     357      0 inform,   0 warnings,   2 severes, 0 fatal for fdf_sendinput
     358    NVFORTRAN-S-0155-mpi_comm_world is use-associated from modules mpi_siesta and mpi__include, and cannot be accessed (/tmp/jvinyals/spack-stage/spack-stage-siesta-4.0.1-emukb7kkp46sefjkkzjt5nafsfai54l7/spack-src/Src/fdf/fdf
            .F90: 2868)
     359    NVFORTRAN-S-0155-mpi_comm_world is use-associated from modules mpi_siesta and mpi__include, and cannot be accessed (/tmp/jvinyals/spack-stage/spack-stage-siesta-4.0.1-emukb7kkp46sefjkkzjt5nafsfai54l7/spack-src/Src/fdf/fdf
            .F90: 2881)
     360      0 inform,   0 warnings,   2 severes, 0 fatal for fdf_recvinput
  >> 361    make[1]: *** [fdf.o] Error 2
     362    make[1]: Leaving directory `/tmp/jvinyals/spack-stage/spack-stage-siesta-4.0.1-emukb7kkp46sefjkkzjt5nafsfai54l7/spack-src/Obj/fdf'
  >> 363    make: *** [libfdf.a] Error 2
```

##### ARM

Our first try was using the `spack install` command as below, only specifying the compiler. This did not work.

```
spack install siesta%arm
```

The first error we found in whilst compiling with the ARM compiler was a module overload by the siesta code.
The code overloaded the `iso_fortran_env`. To solve these we added in the configure phase two commands to rename
the module to `siesta_fortran_env`.

```
def configure(self, spec, prefix):
        
        ...        

        sh("-c", "find -type  f -exec sed -i 's/iso_fortran_env/siesta_fortran_env/g' {} \\;")
        sh("-c", "find -iname iso_fortran_env.F90 -exec rename iso siesta {} \\;
        
        ...        

```

This solved the problem leading us to the final problem with this compiler (mentioned avove). Leaving
the final spec of our attempt to install it as shown below.

```
$ spack spec -Il siesta%arm

Input spec
--------------------------------
 -   siesta%arm

Concretized
--------------------------------
==> Warning: arm@21.0.0.879 cannot build optimized binaries for "graviton2". Using best target possible: "aarch64"
 -   564l6xo  siesta@4.0.1%arm@21.0.0.879~metis patches=b8f722add750b1524767062c7a86de63a1da7990c27fda5321e43e34179e50fc arch=linux-amzn2-aarch64
[+]  32qnomy      ^netcdf-c@4.8.0%arm@21.0.0.879~dap~fsync~hdf4~jna+mpi~parallel-netcdf+pic+shared arch=linux-amzn2-aarch64
[+]  e4dajf6          ^hdf5@1.10.7%arm@21.0.0.879~cxx~fortran+hl~ipo~java+mpi+shared~szip~threadsafe+tools api=default build_type=RelWithDebInfo arch=linux-amzn2-aarch64
[+]  fqvybaf              ^cmake@3.20.5%arm@21.0.0.879~doc+ncurses+openssl+ownlibs~qt build_type=Release arch=linux-amzn2-aarch64
[+]  uhtqtlb                  ^ncurses@6.2%arm@21.0.0.879~symlinks+termlib abi=none arch=linux-amzn2-aarch64
[+]  zpuzm23                      ^pkgconf@1.7.4%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  vc3waha                  ^openssl@1.1.1k%arm@21.0.0.879~docs+systemcerts arch=linux-amzn2-aarch64
[+]  vv6txro                      ^perl@5.32.1%arm@21.0.0.879+cpanm+shared+threads arch=linux-amzn2-aarch64
[+]  33wiajj                          ^berkeley-db@18.1.40%arm@21.0.0.879+cxx~docs+stl patches=b231fcc4d5cff05e5c3a4814f6a5af0e9a966428dc2176540d2c05aff41de522 arch=linux-amzn2-aarch64
[+]  z4ybgri                          ^bzip2@1.0.8%arm@21.0.0.879~debug~pic+shared arch=linux-amzn2-aarch64
[+]  adtc6yc                              ^diffutils@3.7%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  7vnthzn                                  ^libiconv@1.16%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  645q4qj                          ^gdbm@1.19%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  3haw5gt                              ^readline@8.1%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  puuxvg2                          ^zlib@1.2.11%arm@21.0.0.879+optimize+pic+shared arch=linux-amzn2-aarch64
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
[+]  qdn27nh                  ^libfabric@1.11.1-aws%arm@21.0.0.879~debug~kdreg fabrics=sockets,tcp,udp arch=linux-amzn2-aarch64
[+]  mv2g7r5                  ^numactl@2.0.14%arm@21.0.0.879 patches=4e1d78cbbb85de625bad28705e748856033eaafab92a66dffd383a3d7e00cc94,62fc8a8bf7665a60e8f4c93ebbd535647cebf74198f7afafec4c085a8825c006 arch=linux-amzn2-aarch64
[+]  dcs645r                      ^autoconf@2.69%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  edezkz3                      ^automake@1.16.3%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  6vvthuo                  ^openssh@8.5p1%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  xe4evc4                      ^libedit@3.1-20210216%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  x5xehti                  ^slurm@20-02-4-1%arm@21.0.0.879~gtk~hdf5~hwloc~mariadb~pmix+readline~restd sysconfdir=PREFIX/etc arch=linux-amzn2-aarch64
[+]  im5sbgn      ^netcdf-fortran@4.5.3%arm@21.0.0.879~doc+pic+shared arch=linux-amzn2-aarch64
[+]  xc2r6zp      ^netlib-scalapack@2.1.0%arm@21.0.0.879~ipo~pic+shared build_type=Release patches=1c9ce5fee1451a08c2de3cc87f446aeda0b818ebbce4ad0d980ddf2f2a0b2dc4,f2baedde688ffe4c20943c334f580eb298e04d6f35c86b90a1f4e8cb7ae344a2 arch=linux-amzn2-aarch64
[+]  cwuo4ek          ^openblas@0.3.15%arm@21.0.0.879~bignuma~consistent_fpcsr~ilp64+locking+pic+shared threads=none arch=linux-amzn2-aarch64
```

##### Nvidia HPC (NVHPC)

Our first aproach was again to simpli specify the Nvidia HPC Compiler. The problem with this module was 
a conflict with both `cmake` and `openblas` which weren compatibles with the compiler.

```
spack install siesta%nvhpc
```

Then we tried to compile these modules with the GNU Compiler, trying to get a binary, using the `spack` command
below. This solved the conflicts, and lead us to the final error. 
Because we were not able to solve the `mpi_comm_world` problem, we did not try to patch the packages of the dependencies
to compile with this compiler.

```
spack install siesta%nvhpc ^cmake%gcc ^openblas%gcc
```

The final spec of our attempt to compile it was as below.

```
$ spack spec -Il siesta%nvhpc ^cmake%gcc ^openblas%gcc

Input spec
--------------------------------
 -   siesta%nvhpc
 -       ^cmake%gcc
 -       ^openblas%gcc

Concretized
--------------------------------
 -   emukb7k  siesta@4.0.1%nvhpc@21.2~metis patches=b8f722add750b1524767062c7a86de63a1da7990c27fda5321e43e34179e50fc arch=linux-amzn2-graviton2
[+]  baltkx5      ^netcdf-c@4.8.0%nvhpc@21.2~dap~fsync~hdf4~jna+mpi~parallel-netcdf+pic+shared arch=linux-amzn2-graviton2
[+]  wwncepq          ^hdf5@1.10.7%nvhpc@21.2~cxx~fortran+hl~ipo~java+mpi+shared~szip~threadsafe+tools api=default build_type=RelWithDebInfo arch=linux-amzn2-graviton2
[+]  it4etcv              ^cmake@3.20.5%gcc@10.3.0~doc+ncurses+openssl+ownlibs~qt build_type=Release arch=linux-amzn2-graviton2
[+]  iwzirqc                  ^ncurses@6.2%gcc@10.3.0~symlinks+termlib abi=none arch=linux-amzn2-graviton2
[+]  s4pw7zm                      ^pkgconf@1.7.4%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  kssecxk                  ^openssl@1.1.1k%gcc@10.3.0~docs+systemcerts arch=linux-amzn2-graviton2
[+]  zyh3ju5                      ^perl@5.32.1%gcc@10.3.0+cpanm+shared+threads arch=linux-amzn2-graviton2
[+]  y42m6yr                          ^berkeley-db@18.1.40%gcc@10.3.0+cxx~docs+stl patches=b231fcc4d5cff05e5c3a4814f6a5af0e9a966428dc2176540d2c05aff41de522 arch=linux-amzn2-graviton2
[+]  rqrpmap                          ^bzip2@1.0.8%gcc@10.3.0~debug~pic+shared arch=linux-amzn2-graviton2
[+]  2w7bert                              ^diffutils@3.7%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  y5ei3cm                                  ^libiconv@1.16%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  wjwqncx                          ^gdbm@1.19%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  3zy7kxk                              ^readline@8.1%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  4js6ect                          ^zlib@1.2.11%nvhpc@21.2+optimize+pic+shared arch=linux-amzn2-graviton2
[+]  dc5i2vh              ^openmpi@4.1.0%nvhpc@21.2~atomics~cuda~cxx~cxx_exceptions+gpfs~internal-hwloc~java~legacylaunchers~lustre~memchecker+pmi~singularity~sqlite3+static~thread_multiple+vt+wrapper-rpath fabrics=ofi patches=60ce20bc14d98c572ef7883b9fcd254c3f232c2f3a13377480f96466169ac4c8,fba0d3a784a9723338722b48024a22bb32f6a951db841a4e9f08930a93f41d7a schedulers=slurm arch=linux-amzn2-graviton2
[+]  euby7td                  ^hwloc@2.5.0%nvhpc@21.2~cairo~cuda~gl~libudev+libxml2~netloc~nvml+pci+shared arch=linux-amzn2-graviton2
[+]  e4m4ued                      ^libpciaccess@0.16%nvhpc@21.2 patches=6e08dc445ece06e9e8b1344397f2d3f169005703ddc0f2ae24f366cde78c7377 arch=linux-amzn2-graviton2
[+]  kk4ax3i                          ^libtool@2.4.6%nvhpc@21.2 arch=linux-amzn2-graviton2
[+]  6c4kz5g                              ^m4@1.4.18%nvhpc@21.2+sigsegv patches=3877ab548f88597ab2327a2230ee048d2d07ace1062efe81fc92e91b7f39cd00,5746cf51f45b405661c3edae7a78c33d41e54d83f635d16e2bf1f956dbfbf635,fc9b61654a3ba1a8d6cd78ce087e7c96366c290bc8d2c299f09828d793b853c8 arch=linux-amzn2-graviton2
[+]  pa6wm5j                                  ^libsigsegv@2.13%nvhpc@21.2 arch=linux-amzn2-graviton2
[+]  4imdwuy                          ^util-macros@1.19.3%nvhpc@21.2 arch=linux-amzn2-graviton2
[+]  jzxyspx                      ^libxml2@2.9.10%nvhpc@21.2~python patches=05ff238cf435825ef835c7ae39376b52dc83d8caf19e962f0766c841386a305a,10a88ad47f9797cf7cf2d7d07241f665a3b6d1f31fa026728c8c2ae93e1664e9 arch=linux-amzn2-graviton2
[+]  br733tn                          ^xz@5.2.5%nvhpc@21.2~pic libs=shared,static arch=linux-amzn2-graviton2
[+]  qs5m2pb                  ^libevent@2.1.12%nvhpc@21.2+openssl arch=linux-amzn2-graviton2
[+]  xl6zavq                  ^libfabric@1.11.1-aws%nvhpc@21.2~debug~kdreg fabrics=sockets,tcp,udp arch=linux-amzn2-graviton2
[+]  5yq4tpw                  ^numactl@2.0.14%nvhpc@21.2 patches=4e1d78cbbb85de625bad28705e748856033eaafab92a66dffd383a3d7e00cc94,62fc8a8bf7665a60e8f4c93ebbd535647cebf74198f7afafec4c085a8825c006 arch=linux-amzn2-graviton2
[+]  dghtild                      ^autoconf@2.69%nvhpc@21.2 arch=linux-amzn2-graviton2
[+]  umo35bq                      ^automake@1.16.3%nvhpc@21.2 arch=linux-amzn2-graviton2
[+]  tydb3k5                  ^openssh@8.5p1%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  ivotdt7                      ^libedit@3.1-20210216%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  zehhooy                  ^slurm@20-02-4-1%nvhpc@21.2~gtk~hdf5~hwloc~mariadb~pmix+readline~restd sysconfdir=PREFIX/etc arch=linux-amzn2-graviton2
[+]  vekbvrj      ^netcdf-fortran@4.5.3%nvhpc@21.2~doc+pic+shared arch=linux-amzn2-graviton2
[+]  5vrjohv      ^netlib-scalapack@2.1.0%nvhpc@21.2~ipo~pic+shared build_type=Release patches=1c9ce5fee1451a08c2de3cc87f446aeda0b818ebbce4ad0d980ddf2f2a0b2dc4,f2baedde688ffe4c20943c334f580eb298e04d6f35c86b90a1f4e8cb7ae344a2 arch=linux-amzn2-graviton2
[+]  rv7gj6u          ^openblas@0.3.15%gcc@10.3.0~bignuma~consistent_fpcsr~ilp64+locking+pic+shared threads=none arch=linux-amzn2-graviton2


```

## Test Case 1

[ReFrame Benchmark 1](#)

```
$ reframe -c job.onnode.py -r --performance-report
```

### Validation

The only validation that we do is check that the execution finishes without error. We used this
method because we did not know about the science behind, and were not able to find validation data.


### ReFrame Output

#### On-node

```
==============================================================================
PERFORMANCE REPORT
------------------------------------------------------------------------------
SIESTA_Scalability h2o_64 input_siesta_4_0_1__gcc_10_3_0__metis_N_1_MPI_2_OMP_1
- aws:c6gn
   - builtin
      * num_tasks: 2
      * Run Time: 1356.59 None
------------------------------------------------------------------------------
SIESTA_Scalability h2o_64 input_siesta_4_0_1__gcc_10_3_0__metis_N_1_MPI_4_OMP_1
   - builtin
      * num_tasks: 4
      * Run Time: 753.26 None
------------------------------------------------------------------------------
SIESTA_Scalability h2o_64 input_siesta_4_0_1__gcc_10_3_0__metis_N_1_MPI_8_OMP_1
   - builtin
      * num_tasks: 8
      * Run Time: 435.4 None
------------------------------------------------------------------------------
SIESTA_Scalability h2o_64 input_siesta_4_0_1__gcc_10_3_0__metis_N_1_MPI_16_OMP_1
   - builtin
      * num_tasks: 16
      * Run Time: 280.76 None
------------------------------------------------------------------------------
SIESTA_Scalability h2o_64 input_siesta_4_0_1__gcc_10_3_0__metis_N_1_MPI_32_OMP_1
   - builtin
      * num_tasks: 32
      * Run Time: 187.52 None
------------------------------------------------------------------------------
SIESTA_Scalability h2o_64 input_siesta_4_0_1__gcc_10_3_0__metis_N_1_MPI_64_OMP_1
   - builtin
      * num_tasks: 64
      * Run Time: 151.42 None
------------------------------------------------------------------------------
```

#### Off-node

```
==============================================================================
PERFORMANCE REPORT
------------------------------------------------------------------------------
SIESTA_Scalability h2o_64 input_siesta_4_0_1__gcc_10_3_0__metis_N_1_MPI_8_OMP_1
- aws:c6gn
   - builtin
      * num_tasks: 8
      * Run Time: 430.85 None
------------------------------------------------------------------------------
SIESTA_Scalability h2o_64 input_siesta_4_0_1__gcc_10_3_0__metis_N_1_MPI_16_OMP_1
   - builtin
      * num_tasks: 16
      * Run Time: 278.13 None
------------------------------------------------------------------------------
SIESTA_Scalability h2o_64 input_siesta_4_0_1__gcc_10_3_0__metis_N_1_MPI_32_OMP_1
   - builtin
      * num_tasks: 32
      * Run Time: 185.62 None
------------------------------------------------------------------------------
SIESTA_Scalability h2o_64 input_siesta_4_0_1__gcc_10_3_0__metis_N_1_MPI_64_OMP_1
   - builtin
      * num_tasks: 64
      * Run Time: 152.54 None
------------------------------------------------------------------------------
SIESTA_Scalability h2o_64 input_siesta_4_0_1__gcc_10_3_0__metis_N_2_MPI_128_OMP_1
   - builtin
      * num_tasks: 128
      * Run Time: 230.6 None
------------------------------------------------------------------------------
SIESTA_Scalability h2o_64 input_siesta_4_0_1__gcc_10_3_0__metis_N_4_MPI_256_OMP_1
   - builtin
      * num_tasks: 256
      * Run Time: 306.58 None
```

### On-node Compiler Comparison

Performance comparison of two compilers.

| Cores |    GNU   |
|-------|----------|
|     2 |  1356.59 |
|     4 |   753.26 |
|     8 |   435.40 |
|    16 |   280.76 |
|    32 |   187.52 |
|    64 |   151.52 |


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

On-node scaling study for the GNU Compiler.

| Cores |    GNU   |
|-------|----------|
|     2 |  1356.59 |
|     4 |   753.26 |
|     8 |   435.40 |
|    16 |   280.76 |
|    32 |   187.52 |
|    64 |   151.52 |

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
