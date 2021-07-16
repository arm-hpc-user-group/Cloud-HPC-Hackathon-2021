# PICSARlite 

**Description:** PICSARlite is a self-contained proxy that adequately portrays the computational loads and dataflow of more complex PIC codes.

**URL:** https://picsar.net

**Team:** TeamEPCC 

## Compilation

### Spack Package Modification

Details of any changes to the Spack recipe used.

Git commit hash of checkout for pacakage:

Pull request for Spack recipe changes:

### Building PICSARlite

#### gcc 10.3.0

```
spack install picsarlite@0.1%gcc@10.3.0
```

```
$ spack spec -Il picsarlite@0.1%gcc
Input spec
--------------------------------
 -   picsarlite@0.1%gcc@10.3.0

Concretized
--------------------------------
[+]  x4t2nz4  picsarlite@0.1%gcc@10.3.0~debug~library~map+prod~prod_spectral~sde~vtune arch=linux-amzn2-graviton2
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

#### nvhpc 21.2

```
spack install picsarlite@0.1%nvhpc@21.2
```

```
$ spack spec -Il picsarlite@0.1%nvhpc@21.2
Input spec
--------------------------------
 -   picsarlite@0.1%nvhpc@21.2

Concretized
--------------------------------
[+]  vycm7mr  picsarlite@0.1%nvhpc@21.2~debug~library~map+prod~prod_spectral~sde~vtune arch=linux-amzn2-graviton2
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

#### arm 21.0.0.879

```
spack install picsarlite@0.1%arm@21.0.0.879
```

```
$ spack spec -Il picsarlite@0.1%arm@21.0.0.879
Input spec
--------------------------------
 -   picsarlite@0.1%arm@21.0.0.879

Concretized
--------------------------------
==> Warning: arm@21.0.0.879 cannot build optimized binaries for "graviton2". Using best target possible: "aarch64"
[+]  vl3qm2y  picsarlite@0.1%arm@21.0.0.879~debug~library~map+prod~prod_spectral~sde~vtune arch=linux-amzn2-aarch64
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

We provide two test cases, both with input files from the original PICSARlite Github repository:
- Test Case 1: `homogeneous_plasma_lite.pixr` with fixed and pre-defined number of MPI processes = 8
- Test Case 2: `test.pixr` for scaling

## Test Case 1: `homogeneous_plasma_lite.pixr`

[picsarlite_homogeneous_plasma_lite.py](picsarlite_homogeneous_plasma_lite.py)

Runs PICSARlite with input file `homogeneous_plasma_lite.pixr`. This input file defines `nprocx`, `nprocy` and `nprocz` each equal to `2`, thus overall `8` MPI processes. Note the number of MPI processes must match 
`nprocx * nprocy * nprocz` (see input file). If `nprocx`, `nprocy`, `nprocz` are not set, the code performs 
automatic CPU split in each direction. For our scaling experiments we use Test Case 2. 

```
reframe -c picsarlite_homogeneous_plasma_lite.py -r --performance-report
```

### Validation

We validate the number of iterations and capture the overall runtime in seconds

### ReFrame Output

```
==============================================================================
PERFORMANCE REPORT
------------------------------------------------------------------------------
PICSARlite_homogeneous_plasma_lite_picsarlite_0_1_gcc_10_3_0_N_1_MPI_8_OMP_1
- aws:c6gn
   - builtin
      * num_tasks: 8
      * Total runtime: 387.926863036 s
------------------------------------------------------------------------------
PICSARlite_homogeneous_plasma_lite_picsarlite_0_1_gcc_10_3_0_N_1_MPI_8_OMP_2
   - builtin
      * num_tasks: 8
      * Total runtime: 406.39875088 s
------------------------------------------------------------------------------
PICSARlite_homogeneous_plasma_lite_picsarlite_0_1_gcc_10_3_0_N_1_MPI_8_OMP_4
   - builtin
      * num_tasks: 8
      * Total runtime: 405.552957961 s
------------------------------------------------------------------------------
PICSARlite_homogeneous_plasma_lite_picsarlite_0_1_gcc_10_3_0_N_1_MPI_8_OMP_8
   - builtin
      * num_tasks: 8
      * Total runtime: 4.5810799200000005 s
------------------------------------------------------------------------------
PICSARlite_homogeneous_plasma_lite_picsarlite_0_1_arm_21_0_0_879_N_1_MPI_8_OMP_1
   - builtin
      * num_tasks: 8
      * Total runtime: 405.019452226 s
------------------------------------------------------------------------------
PICSARlite_homogeneous_plasma_lite_picsarlite_0_1_arm_21_0_0_879_N_1_MPI_8_OMP_2
   - builtin
      * num_tasks: 8
      * Total runtime: 409.369153733 s
------------------------------------------------------------------------------
PICSARlite_homogeneous_plasma_lite_picsarlite_0_1_arm_21_0_0_879_N_1_MPI_8_OMP_4
   - builtin
      * num_tasks: 8
      * Total runtime: 407.698176702 s
------------------------------------------------------------------------------
PICSARlite_homogeneous_plasma_lite_picsarlite_0_1_arm_21_0_0_879_N_1_MPI_8_OMP_8
   - builtin
      * num_tasks: 8
      * Total runtime: 4.538984616 s
------------------------------------------------------------------------------
PICSARlite_homogeneous_plasma_lite_picsarlite_0_1_nvhpc_21_2_N_1_MPI_8_OMP_1
   - builtin
      * num_tasks: 8
      * Total runtime: 400.859910264 s
------------------------------------------------------------------------------
PICSARlite_homogeneous_plasma_lite_picsarlite_0_1_nvhpc_21_2_N_1_MPI_8_OMP_2
   - builtin
      * num_tasks: 8
      * Total runtime: 397.239915761 s
------------------------------------------------------------------------------
PICSARlite_homogeneous_plasma_lite_picsarlite_0_1_nvhpc_21_2_N_1_MPI_8_OMP_4
   - builtin
      * num_tasks: 8
      * Total runtime: 395.821321116 s
------------------------------------------------------------------------------
PICSARlite_homogeneous_plasma_lite_picsarlite_0_1_nvhpc_21_2_N_1_MPI_8_OMP_8
   - builtin
      * num_tasks: 8
      * Total runtime: 6.426646157 s
------------------------------------------------------------------------------
```

### Hot-spot Profile

List of top-10 functions / code locations from a profile on 8 MPI processes and 8 OMP threads.

Profiling command used:
```
reframe -c picsarlite_homogeneous_plasma_lite.py -r --performance-report
```

| Position | depth | Self  | Total | Child | MPI  | Overhead | Regions | Function                    |
|----------|-------|-------|-------|-------|–-----|–---------|–--------|–----------------------------|
|  1       | 0     | 21.0% | 21.0% |       |      |          |         | depose_jxjyjz_scalar_1_1_1\_ |
|  2       | 0     | 12.8% | 12.8% |       |      | 12.8%    |         | GOMP_parallel               |
|  3       | 0     | 12.6% | 12.6% |       | 12.6%|          |         | mpi_waitall\_                |
|  4  | 0 | 9.6% | 9.6% |  |  |  |  | pxr_boris_push_u_3d\_ |
|  5  | 0 | 4.4% | 4.4% |  |  |  |  | mpi_file_close˜_ |
|  6  | 0 | 3.2% | 9.2% | 6.0% | 4.8% |  |  | __particle_boundary_MOD_particle_bcs_mpi_non_blocking |
|  7  | 0 | 3.1% | 3.1% |  |  |  |  | mpi_file_open\_ |
|  8  | 0 | 2.5% | 2.5% |  |  |  |  | pxr_set_gamma\_ |
|  9  | 0 | 2.3% | 2.3% |  |  |  |  | sincos |
| 10  | 0 | 1.5% | 1.5% |  | 1.5% |  |  | mpi_isend\_ |

### On-node Compiler Comparison

Performance comparison of two compilers.

### On-Node Architecture Comparison

On-node study for two architectures, for 8 cores.

| OMP threads | C6gn (Aarch64) | C5n (X86) |
|-------|----------------|-----------|
| 1     |                | 115.77          |
| 2     |                | 114.33          |
| 4     |                | 120.98          |
| 6     |                | 145.33          |
| 8     |                | 149.64          |
| 9     |                | 4.28            |



## Test Case 2: `test.pixr`

[picsarlite_test.py](picsarlite_test.py)

We run PICSARlite with the available input file `test.pixr`. This input file does not set the number of processes
(`nprocx`, `nprocy`, `nprocz`). Therefore the code performs automatic CPU split in each direction. We use this input
file for our scaling experiments

### Validation

We validate the number of iterations and capture the overall runtime in seconds


### ReFrame Output

```
==============================================================================
PERFORMANCE REPORT
------------------------------------------------------------------------------
PICSARlite_test_picsarlite_x4t2nz4_N_1_MPI_1_OMP_64
- aws:c6gn
   - builtin
      * num_tasks: 1
      * Total runtime: 51.966538171 s
------------------------------------------------------------------------------
PICSARlite_test_picsarlite_x4t2nz4_N_1_MPI_1_OMP_32
   - builtin
      * num_tasks: 1
      * Total runtime: 50.721606025999996 s
------------------------------------------------------------------------------
PICSARlite_test_picsarlite_x4t2nz4_N_1_MPI_1_OMP_16
   - builtin
      * num_tasks: 1
      * Total runtime: 49.395405507999996 s
------------------------------------------------------------------------------
PICSARlite_test_picsarlite_x4t2nz4_N_1_MPI_1_OMP_8
   - builtin
      * num_tasks: 1
      * Total runtime: 50.701942140999996 s
------------------------------------------------------------------------------
PICSARlite_test_picsarlite_x4t2nz4_N_1_MPI_1_OMP_4
   - builtin
      * num_tasks: 1
      * Total runtime: 49.789617261 s
------------------------------------------------------------------------------
PICSARlite_test_picsarlite_x4t2nz4_N_1_MPI_1_OMP_2
   - builtin
      * num_tasks: 1
      * Total runtime: 48.377375558000004 s
------------------------------------------------------------------------------
PICSARlite_test_picsarlite_x4t2nz4_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Total runtime: 52.530946395 s
------------------------------------------------------------------------------
PICSARlite_test_picsarlite_x4t2nz4_N_1_MPI_2_OMP_32
   - builtin
      * num_tasks: 2
      * Total runtime: 30.163100086000004 s
------------------------------------------------------------------------------
PICSARlite_test_picsarlite_x4t2nz4_N_1_MPI_4_OMP_16
   - builtin
      * num_tasks: 4
      * Total runtime: 15.692876724 s
------------------------------------------------------------------------------
PICSARlite_test_picsarlite_x4t2nz4_N_1_MPI_8_OMP_8
   - builtin
      * num_tasks: 8
      * Total runtime: 11.057022929999999 s
------------------------------------------------------------------------------
PICSARlite_test_picsarlite_x4t2nz4_N_1_MPI_16_OMP_4
   - builtin
      * num_tasks: 16
      * Total runtime: 10.756425262 s
------------------------------------------------------------------------------
PICSARlite_test_picsarlite_x4t2nz4_N_1_MPI_32_OMP_2
   - builtin
      * num_tasks: 32
      * Total runtime: 12.524753389 s
------------------------------------------------------------------------------
PICSARlite_test_picsarlite_x4t2nz4_N_2_MPI_32_OMP_4
   - builtin
      * num_tasks: 32
      * Total runtime: 12.822177423000001 s
------------------------------------------------------------------------------
PICSARlite_test_picsarlite_x4t2nz4_N_4_MPI_64_OMP_4
   - builtin
      * num_tasks: 64
      * Total runtime: 17.659731462000003 s
------------------------------------------------------------------------------
PICSARlite_test_picsarlite_x4t2nz4_N_8_MPI_128_OMP_4
   - builtin
      * num_tasks: 128
      * Total runtime: 32.42011801 s
------------------------------------------------------------------------------
PICSARlite_test_picsarlite_0_1_arm_21_0_0_879_N_1_MPI_1_OMP_64
   - builtin
      * num_tasks: 1
      * Total runtime: 51.286288268 s
------------------------------------------------------------------------------
PICSARlite_test_picsarlite_0_1_arm_21_0_0_879_N_1_MPI_1_OMP_32
   - builtin
      * num_tasks: 1
      * Total runtime: 51.13050524000001 s
------------------------------------------------------------------------------
PICSARlite_test_picsarlite_0_1_arm_21_0_0_879_N_1_MPI_1_OMP_16
   - builtin
      * num_tasks: 1
      * Total runtime: 52.672364026 s
------------------------------------------------------------------------------
PICSARlite_test_picsarlite_0_1_arm_21_0_0_879_N_1_MPI_1_OMP_8
   - builtin
      * num_tasks: 1
      * Total runtime: 52.521627971 s
------------------------------------------------------------------------------
PICSARlite_test_picsarlite_0_1_arm_21_0_0_879_N_1_MPI_1_OMP_4
   - builtin
      * num_tasks: 1
      * Total runtime: 52.55687753799999 s
------------------------------------------------------------------------------
PICSARlite_test_picsarlite_0_1_arm_21_0_0_879_N_1_MPI_1_OMP_2
   - builtin
      * num_tasks: 1
      * Total runtime: 52.155587018 s
------------------------------------------------------------------------------
PICSARlite_test_picsarlite_0_1_arm_21_0_0_879_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Total runtime: 57.15923297000001 s
------------------------------------------------------------------------------
PICSARlite_test_picsarlite_0_1_arm_21_0_0_879_N_1_MPI_2_OMP_32
   - builtin
      * num_tasks: 2
      * Total runtime: 28.944272849 s
------------------------------------------------------------------------------
PICSARlite_test_picsarlite_0_1_arm_21_0_0_879_N_1_MPI_4_OMP_16
   - builtin
      * num_tasks: 4
      * Total runtime: 15.905347231 s
------------------------------------------------------------------------------
PICSARlite_test_picsarlite_0_1_arm_21_0_0_879_N_1_MPI_8_OMP_8
   - builtin
      * num_tasks: 8
      * Total runtime: 11.228849816 s
------------------------------------------------------------------------------
PICSARlite_test_picsarlite_0_1_arm_21_0_0_879_N_1_MPI_16_OMP_4
   - builtin
      * num_tasks: 16
      * Total runtime: 11.145546451 s
------------------------------------------------------------------------------
PICSARlite_test_picsarlite_0_1_arm_21_0_0_879_N_1_MPI_32_OMP_2
   - builtin
      * num_tasks: 32
      * Total runtime: 12.702112956 s
------------------------------------------------------------------------------
PICSARlite_test_picsarlite_0_1_arm_21_0_0_879_N_2_MPI_32_OMP_4
   - builtin
      * num_tasks: 32
      * Total runtime: 12.723491531 s
------------------------------------------------------------------------------
PICSARlite_test_picsarlite_0_1_arm_21_0_0_879_N_4_MPI_64_OMP_4
   - builtin
      * num_tasks: 64
      * Total runtime: 17.350770082 s
------------------------------------------------------------------------------
PICSARlite_test_picsarlite_0_1_arm_21_0_0_879_N_8_MPI_128_OMP_4
   - builtin
      * num_tasks: 128
      * Total runtime: 23.196907566 s
------------------------------------------------------------------------------
PICSARlite_test_picsarlite_0_1_nvhpc_21_2_N_1_MPI_1_OMP_64
   - builtin
      * num_tasks: 1
      * Total runtime: 59.411256294 s
------------------------------------------------------------------------------
PICSARlite_test_picsarlite_0_1_nvhpc_21_2_N_1_MPI_1_OMP_32
   - builtin
      * num_tasks: 1
      * Total runtime: 57.084200103 s
------------------------------------------------------------------------------
PICSARlite_test_picsarlite_0_1_nvhpc_21_2_N_1_MPI_1_OMP_16
   - builtin
      * num_tasks: 1
      * Total runtime: 58.650855046 s
------------------------------------------------------------------------------
PICSARlite_test_picsarlite_0_1_nvhpc_21_2_N_1_MPI_1_OMP_8
   - builtin
      * num_tasks: 1
      * Total runtime: 56.283797448 s
------------------------------------------------------------------------------
PICSARlite_test_picsarlite_0_1_nvhpc_21_2_N_1_MPI_1_OMP_4
   - builtin
      * num_tasks: 1
      * Total runtime: 55.671080273 s
------------------------------------------------------------------------------
PICSARlite_test_picsarlite_0_1_nvhpc_21_2_N_1_MPI_1_OMP_2
   - builtin
      * num_tasks: 1
      * Total runtime: 54.934499843 s
------------------------------------------------------------------------------
PICSARlite_test_picsarlite_0_1_nvhpc_21_2_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Total runtime: 60.41649414399999 s
------------------------------------------------------------------------------
PICSARlite_test_picsarlite_0_1_nvhpc_21_2_N_1_MPI_2_OMP_32
   - builtin
      * num_tasks: 2
      * Total runtime: 32.704636574 s
------------------------------------------------------------------------------
PICSARlite_test_picsarlite_0_1_nvhpc_21_2_N_1_MPI_4_OMP_16
   - builtin
      * num_tasks: 4
      * Total runtime: 19.879228132 s
------------------------------------------------------------------------------
PICSARlite_test_picsarlite_0_1_nvhpc_21_2_N_1_MPI_8_OMP_8
   - builtin
      * num_tasks: 8
      * Total runtime: 13.665182876 s
------------------------------------------------------------------------------
PICSARlite_test_picsarlite_0_1_nvhpc_21_2_N_1_MPI_16_OMP_4
   - builtin
      * num_tasks: 16
      * Total runtime: 12.429395744 s
------------------------------------------------------------------------------
PICSARlite_test_picsarlite_0_1_nvhpc_21_2_N_1_MPI_32_OMP_2
   - builtin
      * num_tasks: 32
      * Total runtime: 14.213967743 s
------------------------------------------------------------------------------
PICSARlite_test_picsarlite_0_1_nvhpc_21_2_N_2_MPI_32_OMP_4
   - builtin
      * num_tasks: 32
      * Total runtime: 16.44956686 s
------------------------------------------------------------------------------
PICSARlite_test_picsarlite_0_1_nvhpc_21_2_N_4_MPI_64_OMP_4
   - builtin
      * num_tasks: 64
      * Total runtime: 21.632913658 s
------------------------------------------------------------------------------
PICSARlite_test_picsarlite_0_1_nvhpc_21_2_N_8_MPI_128_OMP_4
   - builtin
      * num_tasks: 128
      * Total runtime: 27.083935557 s
------------------------------------------------------------------------------
```

### On-node Compiler Comparison

Performance comparison of two compilers.

| Cores | MPI proc | OMP threads | GCC 10.3  | arm 21.0   | nvhpc 21.2 |
|-------|----|----|-----------|------------|------------|
| 1     |  1 |  1 | 51.56     | 56.92      | 60.12   |
| 2     |  2 |  1 | 166.60    | 164.00     | 166.34  |
| 4     |  4 |  1 | 355.80    | 344.03     | 366.55  |
| 8     |  8 |  1 | 1088.42   | 1111.04    | 1071.93 |
| 16    | 16 |  1 | 3003.27   | 2994.75    | 2887.36 |
| 32    | 32 |  1 | 7346.60   | 7496.28    | 7161.18 |
| 64    | 64 |  1 | 16.64     | 14.40      |  16.15  |

### tbc
| Cores | MPI proc | OMP threads | GCC 10.3  | arm 21.0   | nvhpc 21.2 |
|-------|----|----|-----------|------------|------------|
| 1     |  1 |  1 | 51.56     | 56.92      | 60.12   |
| 2     |  1 |  2 | 166.60    | 164.00     | 166.34  |
| 4     |  1 |  4 | 355.80    | 344.03     | 366.55  |
| 8     |  1 |  8 | 1088.42   | 1111.04    | 1071.93 |
| 16    |  1 | 16 | 3003.27   | 2994.75    | 2887.36 |
| 32    |  1 | 32 | 7346.60   | 7496.28    | 7161.18 |
| 64    |  1 | 64 | 16.64     | 14.40      |  16.15  |

### tbc
| Cores | MPI proc | OMP threads | GCC 10.3  | arm 21.0   | nvhpc 21.2 |
|-------|----|----|-----------|------------|------------|
| 1     |  1 | 64 |    |  51.89     |   |
| 2     |  2 | 32 |    |  29.22     |   |
| 4     |  4 | 16 |    |  15.90     |   |
| 8     |  8 |  8 |    |  11.21     |  |
| 16    | 16 |  4 |    |  10.38     |  |
| 32    | 32 |  2 |    |  11.88     |  |
| 64    | 64 |  1 |    |  17.97     |  |

### Serial Hot-spot Profile

List of top-10 functions / code locations from a serial profile.

Profiling command used:
```
reframe -c picsarlite_test_hotspot_serial.py -r --performance-report
```

The `map` profile does not show runtime in seconds:

| Position | depth | Self | Total | Child | MPI | Overhead | Regions | Function |
|----------|-------|------|-------|-------|–----|–---------|–--------|–---------|
|  1 | 0 | 26.9% | 26.9% |  |  |  |  | depose_jxjyjz_scalar_1_1_1 |
|  2 | 0 | 16.7% | 16.7% |  |  |  |  | field_gathering_plus_particle_pusher_1_1_1_.1.L.LB11_729.preheader (OpenMP) |
|  3 | 0 | 12.6% | 12.6% |  |  |  |  | __kmp_invoke_microtask |
|  4 | 0 | 11.7% | 11.7% |  |  |  |  | pxr_boris_push_u_3d |
|  5 | 0 | 8.1% | 8.1% |  |  |  |  | mpi_file_write_all_ |
|  6 | 0 | 3.0% | 3.0% |  |  |  |  | pxr_set_gamma |
|  7 | 0 | 3.0% | 19.7% | 16.7% |  |  |  | field_gathering_plus_particle_pusher_cacheblock_sub_ [OpenMP region 2] |
|  8 | 0 | 2.2% | 2.2% |  |  | 2.2% |  | __kmpc_critical_with_hint |
|  9 | 0 | 2.0% | 2.0% |  |  |  |  | cos |
| 10 | 0 | 1.9% | 1.9% |  |  |  |  | tiling::add_particle_at_tile |

### Full Node Hot-spot Profile

List of top-10 functions / code locations from a full node profile.

Profiling command used:
```
reframe -c picsarlite_test_hotspot_fullnode.py -r --performance-report
```
OMP threads = 1
MPI processes  = 64

| Position | depth | Self | Total | Child | MPI | Overhead | Regions | Function |
|----------|-------|------|-------|-------|–----|–---------|–--------|–---------|
|  1 | 0 | 67.9% | 67.9% |  |  |  |  | mpi_file_open_ |
|  2 | 0 | 17.3% | 17.3% |  |  |  |  | mpi_file_close_ |
|  3 | 0 | 2.9% | 2.9% |  | 2.9% |  |  | mpi_waitall_ |
|  4 | 0 | 2.9% | 2.9% |  |  |  |  | mpi_file_write_all_ |
|  5 | 0 | 1.7% | 1.7% |  |  |  |  | field_gathering_plus_particle_pusher_1_1_1_.1.L.LB11_729.preheader (OpenMP) |
|  6 | 0 | 1.5% | 1.5% |  |  |  |  | depose_jxjyjz_scalar_1_1_1 |
|  7 | 0 | 1.2% | 1.2% |  |  |  |  | __kmp_invoke_microtask |
|  8 | 0 | 0.8% | 0.8% |  |  |  |  | pxr_boris_push_u_3d |
|  9 | 0 | 0.8% | 0.8% |  | 0.8% |  |  | mpi_barrier_ |
|  10| 0 | 0.4% | 0.4% |  | 0.4% |  |  | mpi_routines::mpi_minimal_init |

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
