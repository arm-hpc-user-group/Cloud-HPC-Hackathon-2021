# Kripke 

**Description:** Kripke is a simple, scalable, 3D Sn deterministic particle transport proxy/mini app.

**URL:** https://computing.llnl.gov/projects/co-design/kripke

**Team:** dogecointothemoon

**What we have done:**

- We have built Kripke with three different compilers, and wrote four test cases. 
- Each test case, and compilers, we have verified the program runs correctly with different cores.
- Each test case we got the strong scaling result.
- Each test case we compared the architecture difference.

For each test case and each compilers, we run with 1,2,4,8,16,32,64,128, and 256 cores, and there are three compilers,
so when running the reframe for any of these test, you are expected to see that the program passed 27 unit tests.

Because the output of the reframe is too long, so I just show only some lines of them.

Comparing different archs shares the same reframe file for each test case. But, as request, we only compared the arch effect with one compiler which is GCC in our project. We have recorded that as well, and store them in txt file in this directory.

TODO hotspot, flag optimazation

## Compilation

### Spack Package Modification

Details of any changes to the Spack recipe used.

Git commit hash of checkout for pacakage:

Pull request for Spack recipe changes:

### Building Kripke

#### GCC 10.3.0

```
spack install kripke@1.2.4%gcc@10.3.0
```

```
[+]  ivphnkj  kripke@1.2.4%gcc@10.3.0~caliper~ipo+mpi+openmp build_type=RelWithDebInfo arch=linux-amzn2-graviton2
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
[+]  zvamksn      ^openmpi@4.1.0%gcc@10.3.0~atomics~cuda~cxx~cxx_exceptions+gpfs~internal-hwloc~java~legacylaunchers~lustre~memchecker+pmi~singularity~sqlite3+static~thread_multiple+vt+wrapper-rpath fabrics=ofi patches=60ce20bc14d98c572ef7883b9fcd254c3f232c2f3a13377480f96466169ac4c8 schedulers=slurm arch=linux-amzn2-graviton2
[+]  cukmqbg          ^hwloc@2.5.0%gcc@10.3.0~cairo~cuda~gl~libudev+libxml2~netloc~nvml+pci+shared arch=linux-amzn2-graviton2
[+]  asgtk6a              ^libpciaccess@0.16%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  z2uysov                  ^libtool@2.4.6%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  ebhjpix                      ^m4@1.4.18%gcc@10.3.0+sigsegv patches=3877ab548f88597ab2327a2230ee048d2d07ace1062efe81fc92e91b7f39cd00,fc9b61654a3ba1a8d6cd78ce087e7c96366c290bc8d2c299f09828d793b853c8 arch=linux-amzn2-graviton2
[+]  ltbv6bk                          ^libsigsegv@2.13%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  4xr3hhh                  ^util-macros@1.19.3%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  iyhm3wi              ^libxml2@2.9.10%gcc@10.3.0~python arch=linux-amzn2-graviton2
[+]  ye3kcvv                  ^xz@5.2.5%gcc@10.3.0~pic libs=shared,static arch=linux-amzn2-graviton2
[+]  tadxrfp          ^libevent@2.1.12%gcc@10.3.0+openssl arch=linux-amzn2-graviton2
[+]  72f5gvk          ^libfabric@1.11.1-aws%gcc@10.3.0~debug~kdreg fabrics=sockets,tcp,udp arch=linux-amzn2-graviton2
[+]  mhav5gn          ^numactl@2.0.14%gcc@10.3.0 patches=4e1d78cbbb85de625bad28705e748856033eaafab92a66dffd383a3d7e00cc94,62fc8a8bf7665a60e8f4c93ebbd535647cebf74198f7afafec4c085a8825c006 arch=linux-amzn2-graviton2
[+]  jkuhz64              ^autoconf@2.69%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  xb2w5nc              ^automake@1.16.3%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  wturp6c          ^openssh@8.5p1%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  ivotdt7              ^libedit@3.1-20210216%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  wqpuvmh          ^slurm@20-02-4-1%gcc@10.3.0~gtk~hdf5~hwloc~mariadb~pmix+readline~restd sysconfdir=PREFIX/etc arch=linux-amzn2-graviton2
```

#### ARM 21.0.0.879

```
spack install kripke@1.2.4%arm@21.0.0.879
```

```
$ spack spec -Il kripke@1.2.4%arm@21.0.0.879

[+]  ogpzdqf  kripke@1.2.4%arm@21.0.0.879~caliper~ipo+mpi+openmp build_type=RelWithDebInfo arch=linux-amzn2-aarch64
[+]  fqvybaf      ^cmake@3.20.5%arm@21.0.0.879~doc+ncurses+openssl+ownlibs~qt build_type=Release arch=linux-amzn2-aarch64
[+]  uhtqtlb          ^ncurses@6.2%arm@21.0.0.879~symlinks+termlib abi=none arch=linux-amzn2-aarch64
[+]  zpuzm23              ^pkgconf@1.7.4%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  vc3waha          ^openssl@1.1.1k%arm@21.0.0.879~docs+systemcerts arch=linux-amzn2-aarch64
[+]  vv6txro              ^perl@5.32.1%arm@21.0.0.879+cpanm+shared+threads arch=linux-amzn2-aarch64
[+]  33wiajj                  ^berkeley-db@18.1.40%arm@21.0.0.879+cxx~docs+stl patches=b231fcc4d5cff05e5c3a4814f6a5af0e9a966428dc2176540d2c05aff41de522 arch=linux-amzn2-aarch64
[+]  z4ybgri                  ^bzip2@1.0.8%arm@21.0.0.879~debug~pic+shared arch=linux-amzn2-aarch64
[+]  adtc6yc                      ^diffutils@3.7%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  7vnthzn                          ^libiconv@1.16%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  645q4qj                  ^gdbm@1.19%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  3haw5gt                      ^readline@8.1%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  puuxvg2                  ^zlib@1.2.11%arm@21.0.0.879+optimize+pic+shared arch=linux-amzn2-aarch64
[+]  lmaoy5t      ^openmpi@4.1.0%arm@21.0.0.879~atomics~cuda~cxx~cxx_exceptions+gpfs~internal-hwloc~java~legacylaunchers~lustre~memchecker+pmi~singularity~sqlite3+static~thread_multiple+vt+wrapper-rpath fabrics=ofi patches=60ce20bc14d98c572ef7883b9fcd254c3f232c2f3a13377480f96466169ac4c8 schedulers=slurm arch=linux-amzn2-aarch64
[+]  xl6anaa          ^hwloc@2.5.0%arm@21.0.0.879~cairo~cuda~gl~libudev+libxml2~netloc~nvml+pci+shared arch=linux-amzn2-aarch64
[+]  jueqz7p              ^libpciaccess@0.16%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  e4ssqx6                  ^libtool@2.4.6%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  i2jmeo4                      ^m4@1.4.18%arm@21.0.0.879+sigsegv patches=3877ab548f88597ab2327a2230ee048d2d07ace1062efe81fc92e91b7f39cd00,fc9b61654a3ba1a8d6cd78ce087e7c96366c290bc8d2c299f09828d793b853c8 arch=linux-amzn2-aarch64
[+]  6jhzlul                          ^libsigsegv@2.13%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  uwcxkin                  ^util-macros@1.19.3%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  dypqz2i              ^libxml2@2.9.10%arm@21.0.0.879~python arch=linux-amzn2-aarch64
[+]  zqsab4f                  ^xz@5.2.5%arm@21.0.0.879~pic libs=shared,static arch=linux-amzn2-aarch64
[+]  gonqskn          ^libevent@2.1.12%arm@21.0.0.879+openssl arch=linux-amzn2-aarch64
[+]  qdn27nh          ^libfabric@1.11.1-aws%arm@21.0.0.879~debug~kdreg fabrics=sockets,tcp,udp arch=linux-amzn2-aarch64
[+]  mv2g7r5          ^numactl@2.0.14%arm@21.0.0.879 patches=4e1d78cbbb85de625bad28705e748856033eaafab92a66dffd383a3d7e00cc94,62fc8a8bf7665a60e8f4c93ebbd535647cebf74198f7afafec4c085a8825c006 arch=linux-amzn2-aarch64
[+]  dcs645r              ^autoconf@2.69%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  edezkz3              ^automake@1.16.3%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  6vvthuo          ^openssh@8.5p1%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  xe4evc4              ^libedit@3.1-20210216%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  x5xehti          ^slurm@20-02-4-1%arm@21.0.0.879~gtk~hdf5~hwloc~mariadb~pmix+readline~restd sysconfdir=PREFIX/etc arch=linux-amzn2-aarch64

```

#### NVHPC 21.2

```
spack install kripke@1.2.4%nvhpc@21.2 ^cmake%gcc@10.3.0
```

```
[+]  td2xax7  kripke@1.2.4%nvhpc@21.2~caliper~ipo+mpi+openmp build_type=RelWithDebInfo arch=linux-amzn2-graviton2
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
[+]  okl5z2h      ^openmpi@4.1.0%nvhpc@21.2~atomics~cuda~cxx~cxx_exceptions+gpfs~internal-hwloc~java~legacylaunchers~lustre~memchecker+pmi~singularity~sqlite3+static~thread_multiple+vt+wrapper-rpath fabrics=ofi patches=60ce20bc14d98c572ef7883b9fcd254c3f232c2f3a13377480f96466169ac4c8,fba0d3a784a9723338722b48024a22bb32f6a951db841a4e9f08930a93f41d7a schedulers=slurm arch=linux-amzn2-graviton2
[+]  dultkd7          ^hwloc@2.5.0%nvhpc@21.2~cairo~cuda~gl~libudev+libxml2~netloc~nvml+pci+shared arch=linux-amzn2-graviton2
[+]  e4m4ued              ^libpciaccess@0.16%nvhpc@21.2 patches=6e08dc445ece06e9e8b1344397f2d3f169005703ddc0f2ae24f366cde78c7377 arch=linux-amzn2-graviton2
[+]  kk4ax3i                  ^libtool@2.4.6%nvhpc@21.2 arch=linux-amzn2-graviton2
[+]  6c4kz5g                      ^m4@1.4.18%nvhpc@21.2+sigsegv patches=3877ab548f88597ab2327a2230ee048d2d07ace1062efe81fc92e91b7f39cd00,5746cf51f45b405661c3edae7a78c33d41e54d83f635d16e2bf1f956dbfbf635,fc9b61654a3ba1a8d6cd78ce087e7c96366c290bc8d2c299f09828d793b853c8 arch=linux-amzn2-graviton2
[+]  pa6wm5j                          ^libsigsegv@2.13%nvhpc@21.2 arch=linux-amzn2-graviton2
[+]  4imdwuy                  ^util-macros@1.19.3%nvhpc@21.2 arch=linux-amzn2-graviton2
[+]  flzyc7v              ^libxml2@2.9.10%nvhpc@21.2~python patches=05ff238cf435825ef835c7ae39376b52dc83d8caf19e962f0766c841386a305a,10a88ad47f9797cf7cf2d7d07241f665a3b6d1f31fa026728c8c2ae93e1664e9 arch=linux-amzn2-graviton2
[+]  br733tn                  ^xz@5.2.5%nvhpc@21.2~pic libs=shared,static arch=linux-amzn2-graviton2
[+]  qmlezth          ^libevent@2.1.12%nvhpc@21.2+openssl arch=linux-amzn2-graviton2
[+]  xl6zavq          ^libfabric@1.11.1-aws%nvhpc@21.2~debug~kdreg fabrics=sockets,tcp,udp arch=linux-amzn2-graviton2
[+]  5yq4tpw          ^numactl@2.0.14%nvhpc@21.2 patches=4e1d78cbbb85de625bad28705e748856033eaafab92a66dffd383a3d7e00cc94,62fc8a8bf7665a60e8f4c93ebbd535647cebf74198f7afafec4c085a8825c006 arch=linux-amzn2-graviton2
[+]  vslxuhy              ^autoconf@2.69%nvhpc@21.2 arch=linux-amzn2-graviton2
[+]  pqaylup              ^automake@1.16.3%nvhpc@21.2 arch=linux-amzn2-graviton2
[+]  wturp6c          ^openssh@8.5p1%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  ivotdt7              ^libedit@3.1-20210216%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  zehhooy          ^slurm@20-02-4-1%nvhpc@21.2~gtk~hdf5~hwloc~mariadb~pmix+readline~restd sysconfdir=PREFIX/etc arch=linux-amzn2-graviton2
```

## Test Case 1: Default configuraion

In all the test case, we compare the result of the value of the `particle` and which should not changed with diffrent cores. 
In the first case, we use the default configuration withg zones=32,32,32. Because the execution time with the orignial zone(16,16,16)
is very short when the core=256, so we decide to make the problem size bigger to get the accurate result.

```
reframe --stage /scratch/home/${USER} -v -c kripke_single_node_test_default.py -r --performance-report
```

### ReFrame partial output

Performance: Only showing the result of the GCC, we have got the result of ARM and NVHPC but we think it is not necessary to show all of them.
```
==============================================================================
PERFORMANCE REPORT
------------------------------------------------------------------------------
Kripke_default_kripke_1_2_4_gcc_10_3_0_N_1_MPI_1_OMP_1
- aws:c6gn
   - builtin
      * num_tasks: 1
      * Total Time: 105.84846 s
------------------------------------------------------------------------------
Kripke_default_kripke_1_2_4_gcc_10_3_0_N_1_MPI_2_OMP_1
   - builtin
      * num_tasks: 2
      * Total Time: 53.05502 s
------------------------------------------------------------------------------
Kripke_default_kripke_1_2_4_gcc_10_3_0_N_1_MPI_4_OMP_1
   - builtin
      * num_tasks: 4
      * Total Time: 28.32205 s
------------------------------------------------------------------------------
Kripke_default_kripke_1_2_4_gcc_10_3_0_N_1_MPI_8_OMP_1
   - builtin
      * num_tasks: 8
      * Total Time: 16.52515 s
------------------------------------------------------------------------------
Kripke_default_kripke_1_2_4_gcc_10_3_0_N_1_MPI_16_OMP_1
   - builtin
      * num_tasks: 16
      * Total Time: 9.92737 s
------------------------------------------------------------------------------
Kripke_default_kripke_1_2_4_gcc_10_3_0_N_1_MPI_32_OMP_1
   - builtin
      * num_tasks: 32
      * Total Time: 4.70694 s
------------------------------------------------------------------------------
Kripke_default_kripke_1_2_4_gcc_10_3_0_N_1_MPI_64_OMP_1
   - builtin
      * num_tasks: 64
      * Total Time: 1.9935 s
------------------------------------------------------------------------------
Kripke_default_kripke_1_2_4_gcc_10_3_0_N_2_MPI_128_OMP_1
   - builtin
      * num_tasks: 128
      * Total Time: 0.96298 s
------------------------------------------------------------------------------
Kripke_default_kripke_1_2_4_gcc_10_3_0_N_4_MPI_256_OMP_1
   - builtin
      * num_tasks: 256
      * Total Time: 0.76485 s
------------------------------------------------------------------------------
```

### Strong Scaling(1-4 nodes) and Compiler Comparison

We only used MPI library to parallize the code. The thread per process always keep 1.

| Cores(MPI rank) | GCC | ARM | NVHPC|
|-------|------------|------------|------------|
|  1     |  105.85   | 81.40| 126.14  |  
|  2     |  53.06    | 41.17| 64.26	|
|  4     |  28.32    | 21.54| 33.99	|
|  8     |  16.53    | 10.19| 16.28	|
|  16    |  9.93     | 7.41 | 8.69	|
|  32    |  4.71     | 3.73 | 4.86	|
|  64    |  1.99     | 1.94 | 2.56	|
|  128   |  0.96     | 0.91	| 1.20	|
|  256   |  0.76	 | 0.69	| 1.00  |

### Strong Scaling(1-4 nodes) and Compiler Comparison

We only used MPI library to parallize the code. The thread per process always keep 1.

| Cores(MPI rank) | GCC | ARM | NVHPC|
|-------|------------|------------|------------|
|  1     |  105.85   | 81.40| 126.14  |
|  2     |  53.06    | 41.17| 64.26	|
|  4     |  28.32    | 21.54| 33.99	|
|  8     |  16.53    | 10.19| 16.28	|
|  16    |  9.93     | 7.41 | 8.69	|
|  32    |  4.71     | 3.73 | 4.86	|
|  64    |  1.99     | 1.94 | 2.56	|
|  128   |  0.96     | 0.91	| 1.20	|
|  256   |  0.76	 | 0.69	| 1.00  |

### Serial Hot-spot Profile

List of top-10 functions / code locations from a serial profile.

Use GCC compiler.

Profiling command used:
```
map --profile srun -N 1 -n 1 kripke.exe --zones 32,32,32
```

| Position | Routine                                                      | Time (%) |
| -------- | ------------------------------------------------------------ | -------- |
| 1        | gomp_team_barrier_wait_end                                   | 24.8%    |
| 2        | [OpenMP overhead (no region active)]                         | 6.0%     |
| 3        | RAJA::operators::plus<long, long, long>::operator()(long const&, long const&) const | 3.8%     |
| 4        | RAJA::detail::LayoutBase_impl<camp::int_seq<long, 0l, 1l, 2l>, long, 2l>::operator()<long, long, long>(long, long, long) const [inlined] | 3.4%     |
| 5        | camp::forward<long&>(camp::type::ref::rem_s<long&>::type&)   | 2.0%     |
| 6        | camp::forward<RAJA::operators::plus<long, long, long         | 1.7%     |
| 7        | RAJA::View<double, RAJA::TypedLayout<long, camp::tuple<Kripke::Moment, Kripke::Group, Kripke::Zone>, 2l>, double*>::operator()<Kripke::Moment, Kripke::Group, Kripke::Zone>(Kripke::Moment, Kripke::Group, Kripke::Zone) const [inlined] | 1.5%     |
| 8        | RAJA::stripIndexType\<long\>(long) [inlined] (OpenMP)        | 1.5%     |
| 9        | camp::internal::tuple_storage<3l, long>::get_inner()         | 1.4%     |
| 10       | LPlusTimesSdom::operator()<Kripke::ArchLayoutT<Kripke::ArchT_OpenMP, Kripke::LayoutT_DGZ (OpenMP) | 1.2%     |

### Full Node Hot-spot Profile

List of top-10 functions / code locations from a full node profile.

Use GCC compiler.

Profiling command used:
```
map --profile srun -N 1 -n 64 kripke.exe --zones 32,32,32 --procs 4,4,4
```

| Position | Routine                                                      | Time (%) | MPI (%) |
| -------- | ------------------------------------------------------------ | -------- | ------- |
| 1        | RAJA::operators::plus<long, long, long>::operator()(long const&, long const&) const | 5.7%     |         |
| 2        | RAJA::detail::LayoutBase_impl<camp::int_seq<long, 0l, 1l, 2l>, long, 2l>::operator()<long, long, long>(long, long, long) const [inlined] | 5.1%     |         |
| 3        | camp::forward<long&>(camp::type::ref::rem_s<long&>::type&)   | 3.0%     |         |
| 4        | camp::forward<RAJA::operators::plus<long, long, long         | 2.8%     |         |
| 5        | RAJA::stripIndexType\<long\>(long) [inlined] (OpenMP)        | 2.4%     |         |
| 6        | RAJA::View<double, RAJA::TypedLayout<long, camp::tuple<Kripke::Moment, Kripke::Group, Kripke::Zone>, 2l>, double*>::operator()<Kripke::Moment, Kripke::Group, Kripke::Zone>(Kripke::Moment, Kripke::Group, Kripke::Zone) const [inlined] | 2.4%     |         |
| 7        | camp::internal::tuple_storage<3l, long>::get_inner()         | 2.0%     |         |
| 8        | std::forward<RAJA::internal::LoopData<camp::list<RAJA::statement::Collapse<RAJA::omp_parallel_collapse_exec, camp::int_seq<long, 0l, 2l>, RAJA::statement::For<1l, RAJA::policy::loop::loop_exec, RAJA::statement::For<3l, RAJA::policy::loop::loop_exec, RAJA::statement::Lambda<0l | 2.0%     |         |
| 9        | MPI_Testany                                                  | 1.9%     | 1.9%    |
| 10       | RAJA::IndexValue<Kripke::Group, long>::IndexValue(long) [inlined] | 1.8%     |         |

### Architecture Comparison

We used the gcc@10.3.0 compiler in the architecture Comparison.

| Cores | C6gn (Aarch64) | C5n (X86) |
|-------|----------------|-----------|
| 1     |    98.18		 | 114.07	 |
| 2     |    49.21       | 69.71	 |
| 4     |    27.10       | 36.85     |
| 8     |    15.12       | 19.71	 |
| 16    |    9.82        | 11.32     |
| 32    |    4.69        | 5.15      |
| 64    |    1.99        | 2.50      |
| 128	|	 0.99		 | 1.13		 |
| 256	|    0.74		 | 0.60		 |

## Test Case 2: More iteration

In the second case, we use run the program with zones=32,32,32 --niter=20. the default iterations is 10.

```
reframe --stage /scratch/home/${USER} -v -c test_more_iter.py
```

### ReFrame partial output

Performance:
```
==============================================================================
PERFORMANCE REPORT
------------------------------------------------------------------------------
Kripke_more_iterations_kripke_1_2_4_gcc_10_3_0_N_1_MPI_1_OMP_1
- aws:c6gn
   - builtin
      * num_tasks: 1
      * Total Time: 208.84063 s
------------------------------------------------------------------------------
Kripke_more_iterations_kripke_1_2_4_gcc_10_3_0_N_1_MPI_2_OMP_1
   - builtin
      * num_tasks: 2
      * Total Time: 106.46899 s
------------------------------------------------------------------------------
Kripke_more_iterations_kripke_1_2_4_gcc_10_3_0_N_1_MPI_4_OMP_1
   - builtin
      * num_tasks: 4
      * Total Time: 58.33841 s
------------------------------------------------------------------------------
Kripke_more_iterations_kripke_1_2_4_gcc_10_3_0_N_1_MPI_8_OMP_1
   - builtin
      * num_tasks: 8
      * Total Time: 33.03246 s
------------------------------------------------------------------------------
Kripke_more_iterations_kripke_1_2_4_gcc_10_3_0_N_1_MPI_16_OMP_1
   - builtin
      * num_tasks: 16
      * Total Time: 18.97311 s
------------------------------------------------------------------------------
Kripke_more_iterations_kripke_1_2_4_gcc_10_3_0_N_1_MPI_32_OMP_1
   - builtin
      * num_tasks: 32
      * Total Time: 9.09939 s
------------------------------------------------------------------------------
Kripke_more_iterations_kripke_1_2_4_gcc_10_3_0_N_1_MPI_64_OMP_1
   - builtin
      * num_tasks: 64
      * Total Time: 3.68728 s
------------------------------------------------------------------------------
Kripke_more_iterations_kripke_1_2_4_gcc_10_3_0_N_2_MPI_128_OMP_1
   - builtin
      * num_tasks: 128
      * Total Time: 1.80796 s
------------------------------------------------------------------------------
Kripke_more_iterations_kripke_1_2_4_gcc_10_3_0_N_4_MPI_256_OMP_1
   - builtin
      * num_tasks: 256
      * Total Time: 1.31311 s
------------------------------------------------------------------------------
```

### Strong Scaling(1-4 nodes) and Compiler Comparison

We only used MPI library to parallize the code. The thread per process always keep 1.

| Cores(MPI rank) | GCC | ARM | NVHPC|
|-------|------------|------------|------------|
|  1     | 208.84| 161.70 |248.36	|  
|  2     | 106.47| 80.05  |127.39 	|
|  4     | 58.34 | 42.67  |67.19	|
|  8     | 33.03 | 22.86  |30.90	|
|  16    | 18.97 | 13.58  |22.15 	|
|  32    | 9.10  | 7.03   |10.60 	|
|  64    | 3.69  | 3.84   |5.05 	|
|  128   | 1.81	 | 1.75	  |2.38		|
|  256   | 1.31	 | 1.79	  |1.58		|

### Serial Hot-spot Profile

List of top-10 functions / code locations from a serial profile.

Use GCC compiler

Profiling command used:

```
map --profile srun -N 1 -n 1 kripke.exe --zones 32,32,32 --niter 20
```

| Position | Routine                                                      | Time (%) |
| -------- | ------------------------------------------------------------ | -------- |
| 1        | gomp_team_barrier_wait_end                                   | 24.6%    |
| 2        | [OpenMP overhead (no region active)]                         | 7.0%     |
| 3        | RAJA::operators::plus<long, long, long>::operator()(long const&, long const&) const | 3.8%     |
| 4        | RAJA::detail::LayoutBase_impl<camp::int_seq<long, 0l, 1l, 2l>, long, 2l>::operator()<long, long, long>(long, long, long) const [inlined] | 3.4%     |
| 5        | camp::forward<long&>(camp::type::ref::rem_s<long&>::type&) (OpenMP) | 2.0%     |
| 6        | camp::forward<RAJA::operators::plus<long, long, long         | 1.9%     |
| 7        | RAJA::stripIndexType\<long\>(long) [inlined] (OpenMP)        | 1.6%     |
| 8        | RAJA::View<double, RAJA::TypedLayout<long, camp::tuple<Kripke::Moment, Kripke::Group, Kripke::Zone>, 2l>, double*>::operator()<Kripke::Moment, Kripke::Group, Kripke::Zone>(Kripke::Moment, Kripke::Group, Kripke::Zone) const [inlined] | 1.5%     |
| 9        | camp::internal::tuple_storage<3l, long>::get_inner()         | 1.4%     |
| 10       | LPlusTimesSdom::operator()<Kripke::ArchLayoutT<Kripke::ArchT_OpenMP, Kripke::LayoutT_DGZ (OpenMP) | 1.2%     |

### Full Node Hot-spot Profile

List of top-10 functions / code locations from a full node profile.

Use GCC compiler

Profiling command used:

```
map --profile srun -N 1 -n 64 kripke.exe --zones 32,32,32 --niter 20 --procs 4,4,4
```

| Position | Routine                                                      | Time (%) | MPI (%) |
| -------- | ------------------------------------------------------------ | -------- | ------- |
| 1        | RAJA::operators::plus<long, long, long>::operator()(long const&, long const&) const | 5.7%     |         |
| 2        | RAJA::detail::LayoutBase_impl<camp::int_seq<long, 0l, 1l, 2l>, long, 2l>::operator()<long, long, long>(long, long, long) const [inlined] | 5.3%     |         |
| 3        | camp::forward<long&>(camp::type::ref::rem_s<long&>::type&)   | 3.0%     |         |
| 4        | camp::forward<RAJA::operators::plus<long, long, long         | 2.8%     |         |
| 5        | RAJA::View<double, RAJA::TypedLayout<long, camp::tuple<Kripke::Moment, Kripke::Group, Kripke::Zone>, 2l>, double*>::operator()<Kripke::Moment, Kripke::Group, Kripke::Zone>(Kripke::Moment, Kripke::Group, Kripke::Zone) const [inlined] | 2.3%     |         |
| 6        | RAJA::stripIndexType\<long\>(long) [inlined] (OpenMP)        | 2.2%     |         |
| 7        | camp::internal::tuple_storage<3l, long>::get_inner()         | 2.0%     |         |
| 8        | std::forward<RAJA::internal::LoopData<camp::list<RAJA::statement::Collapse<RAJA::omp_parallel_collapse_exec, camp::int_seq<long, 0l, 2l>, RAJA::statement::For<1l, RAJA::policy::loop::loop_exec, RAJA::statement::For<3l, RAJA::policy::loop::loop_exec, RAJA::statement::Lambda<0l | 1.9%     |         |
| 9        | RAJA::IndexValue<Kripke::Group, long>::IndexValue(long) [inlined] | 1.7%     |         |
| 10       | RAJA::detail::ConditionalMultiply<1l, 2l>::multiply<long, long>(long, long) [inlined] | 1.7%     |         |

### Architecture Comparison

We used the gcc@10.3.0 compiler in the architecture Comparison.

| Cores | C6gn (Aarch64) | C5n (X86) |
|-------|----------------|-----------|
| 1     | 187.28		 | 229.46	 |
| 2     | 91.91          | 140.92    |
| 4     | 47.06          | 73.95     |
| 8     | 27.27          | 39.63     |
| 16    | 16.63          | 22.79     |
| 32    | 8.31           | 10.31     |
| 64    | 3.72           | 5.00      |
| 128	| 1.83			 | 2.24		 |
| 256	| 1.29			 | 1.18		 |

## Test Case 3: More groups

In the third case, we use the default configuration withg zones=32,32,32 groups=64. The default group is 32.

```
reframe --stage /scratch/home/${USER} -v -c kripke_single_node_test_more_groups.py -r --performance-report
```

### ReFrame partial output

Performance:
```
```

### Strong Scaling(1-4 nodes) and Compiler Comparison

We only used MPI library to parallize the code. The thread per process always keep 1.

| Cores(MPI rank) | GCC | ARM | NVHPC|
|-------|------------|------------|------------|
|  1     | 256.41 | 225.11|314.67	|  
|  2     | 124.01 | 108.87|157.30	|
|  4     | 65.81  | 55.84 |81.26	|
|  8     | 37.49  | 31.67 |41.28 	|
|  16    | 23.87  | 19.12 |23.77 	|
|  32    | 13.26  | 10.85 |12.47	|
|  64    | 6.53   | 6.77  |7.80	    |
|  128   | 2.43	  |	2.48  |3.20	    |
|  256   | 1.23	  | 1.30  |1.73	    |

### Serial Hot-spot Profile

List of top-10 functions / code locations from a serial profile.

Use GCC compiler

Profiling command used:

```
map --profile srun -N 1 -n 1 kripke.exe --zones 32,32,32 --groups 64
```

| Position | Routine                                                      | Time (%) |
| -------- | ------------------------------------------------------------ | -------- |
| 1        | gomp_team_barrier_wait_end                                   | 23.1%    |
| 2        | [OpenMP overhead (no region active)]                         | 4.3%     |
| 3        | RAJA::operators::plus<long, long, long>::operator()(long const&, long const&) const | 4.1%     |
| 4        | RAJA::detail::LayoutBase_impl<camp::int_seq<long, 0l, 1l, 2l>, long, 2l>::operator()<long, long, long>(long, long, long) const [inlined] | 3.5%     |
| 5        | camp::forward<long&>(camp::type::ref::rem_s<long&>::type&) (OpenMP) | 2.3%     |
| 6        | camp::forward<RAJA::operators::plus<long, long, long         | 1.9%     |
| 7        | ScatteringSdom::operator()<Kripke::ArchLayoutT<Kripke::ArchT_OpenMP, Kripke::LayoutT_DGZ | 1.8%     |
| 8        | RAJA::stripIndexType\<long\>(long) [inlined] (OpenMP)        | 1.7%     |
| 9        | RAJA::View<double, RAJA::TypedLayout<long, camp::tuple<Kripke::Moment, Kripke::Group, Kripke::Zone>, 2l>, double*>::operator()<Kripke::Moment, Kripke::Group, Kripke::Zone>(Kripke::Moment, Kripke::Group, Kripke::Zone) const [inlined] | 1.7%     |
| 10       | camp::internal::tuple_storage<3l, long>::get_inner()         | 1.4%     |

### Full Node Hot-spot Profile

List of top-10 functions / code locations from a full node profile.

Use GCC compiler

Profiling command used:

```
map --profile srun -N 1 -n 64 kripke.exe --zones 32,32,32 --groups 64 --procs 4,4,4
```

| Position | Routine                                                      | Time (%) | MPI (%) |
| -------- | ------------------------------------------------------------ | -------- | ------- |
| 1        | RAJA::operators::plus<long, long, long>::operator()(long const&, long const&) const | 5.6%     |         |
| 2        | RAJA::detail::LayoutBase_impl<camp::int_seq<long, 0l, 1l, 2l>, long, 2l>::operator()<long, long, long>(long, long, long) const [inlined] | 5.2%     |         |
| 3        | camp::forward<long&>(camp::type::ref::rem_s<long&>::type&)   | 3.1%     |         |
| 4        | ScatteringSdom::operator()<Kripke::ArchLayoutT<Kripke::ArchT_OpenMP, Kripke::LayoutT_DGZ | 2.9%     |         |
| 5        | RAJA::stripIndexType<long>(long) [inlined] (OpenMP)          | 2.5%     |         |
| 6        | RAJA::View<double, RAJA::TypedLayout<long, camp::tuple<Kripke::Moment, Kripke::Group, Kripke::Zone>, 2l>, double*>::operator()<Kripke::Moment, Kripke::Group, Kripke::Zone>(Kripke::Moment, Kripke::Group, Kripke::Zone) const [inlined] | 2.5%     |         |
| 7        | camp::forward<RAJA::operators::plus<long, long, long         | 2.5%     |         |
| 8        | camp::internal::tuple_storage<3l, long>::get_inner()         | 2.0%     |         |
| 9        | RAJA::IndexValue<Kripke::Group, long>::IndexValue(long) [inlined] | 1.8%     |         |
| 10       | RAJA::IndexValue<Kripke::Zone, long>::IndexValue(long) [inlined] | 1.6%     |         |

### Architecture Comparison

We used the gcc@10.3.0 compiler in the architecture Comparison.

| Cores | C6gn (Aarch64) | C5n (X86) |
|-------|----------------|-----------|
| 1     | 215.53         | 255.64          |
| 2     | 105.29         | 157.45          |
| 4     | 56.70          | 78.07          |
| 8     | 33.60          | 41.56          |
| 16    | 22.15          | 24.04          |
| 32    | 14.43          | 12.03          |
| 64    | 5.62           | 6.12          |
| 128	| 2.01			 | 2.59			 |
| 256	| 1.20			 | 1.29			 |

## Test Case 4: Large zone size

In the fourth case, we use the default configuration withg zones=32,32,64. 

```
reframe --stage /scratch/home/${USER} -v -c kripke_single_node_large_zone.py -r --performance-report
```

### ReFrame partial output

Performance:
```
==============================================================================
PERFORMANCE REPORT
------------------------------------------------------------------------------
Kripke_Large zone_kripke_1_2_4_gcc_10_3_0_N_1_MPI_1_OMP_1
- aws:c6gn
   - builtin
      * num_tasks: 1
      * Total Time: 221.14925 s
------------------------------------------------------------------------------
Kripke_Large zone_kripke_1_2_4_gcc_10_3_0_N_1_MPI_2_OMP_1
   - builtin
      * num_tasks: 2
      * Total Time: 109.16955 s
------------------------------------------------------------------------------
Kripke_Large zone_kripke_1_2_4_gcc_10_3_0_N_1_MPI_4_OMP_1
   - builtin
      * num_tasks: 4
      * Total Time: 56.77418 s
------------------------------------------------------------------------------
Kripke_Large zone_kripke_1_2_4_gcc_10_3_0_N_1_MPI_8_OMP_1
   - builtin
      * num_tasks: 8
      * Total Time: 33.72403 s
------------------------------------------------------------------------------
Kripke_Large zone_kripke_1_2_4_gcc_10_3_0_N_1_MPI_16_OMP_1
   - builtin
      * num_tasks: 16
      * Total Time: 22.18686 s
------------------------------------------------------------------------------
Kripke_Large zone_kripke_1_2_4_gcc_10_3_0_N_1_MPI_32_OMP_1
   - builtin
      * num_tasks: 32
      * Total Time: 14.56125 s
------------------------------------------------------------------------------
Kripke_Large zone_kripke_1_2_4_gcc_10_3_0_N_1_MPI_64_OMP_1
   - builtin
      * num_tasks: 64
      * Total Time: 5.60811 s
------------------------------------------------------------------------------
Kripke_Large zone_kripke_1_2_4_gcc_10_3_0_N_2_MPI_128_OMP_1
   - builtin
      * num_tasks: 128
      * Total Time: 2.08542 s
------------------------------------------------------------------------------
Kripke_Large zone_kripke_1_2_4_gcc_10_3_0_N_4_MPI_256_OMP_1
   - builtin
      * num_tasks: 256
      * Total Time: 1.17601 s
------------------------------------------------------------------------------
```

### Strong Scaling(1-4 nodes) and Compiler Comparison

We only used MPI library to parallize the code. The thread per process always keep 1.

| Cores(MPI rank) | GCC | ARM | NVHPC|
|-------|------------|------------|------------|
|  1     | 221.15  | 176.01 |  305.77 |  
|  2     | 109.17  | 82.60  |  138.06 |
|  4     | 56.77   | 49.50  |  61.22  |
|  8     | 33.72   | 31.77  |  33.06  |
|  16    | 22.19   | 20.99  |  18.65  |
|  32    | 14.56   | 14.22  |  11.54  |
|  64    | 5.61    | 5.64   |  6.87	  |
|  128   | 2.09	   | 2.03  	|  2.89	  |
|  256   | 1.18	   | 1.08  	|  1.46	  |

### Serial Hot-spot Profile

List of top-10 functions / code locations from a serial profile.

Use GCC compiler

Profiling command used:

```
map --profile srun -N 1 -n 1 kripke.exe --zones 32,32,64
```

| Position | Routine                                                      | Time (%) |
| -------- | ------------------------------------------------------------ | -------- |
| 1        | gomp_team_barrier_wait_end                                   | 22.9%    |
| 2        | [OpenMP overhead (no region active)]                         | 4.9%     |
| 3        | RAJA::operators::plus<long, long, long>::operator()(long const&, long const&) const | 3.9%     |
| 4        | RAJA::detail::LayoutBase_impl<camp::int_seq<long, 0l, 1l, 2l>, long, 2l>::operator()<long, long, long>(long, long, long) const [inlined] | 3.7%     |
| 5        | camp::forward<long&>(camp::type::ref::rem_s<long&>::type&)   | 2.0%     |
| 6        | camp::forward<RAJA::operators::plus<long, long, long         | 1.9%     |
| 7        | RAJA::View<double, RAJA::TypedLayout<long, camp::tuple<Kripke::Moment, Kripke::Group, Kripke::Zone>, 2l>, double*>::operator()<Kripke::Moment, Kripke::Group, Kripke::Zone>(Kripke::Moment, Kripke::Group, Kripke::Zone) const [inlined] | 1.7%     |
| 8        | RAJA::stripIndexType\<long\>(long) [inlined] (OpenMP)        | 1.6%     |
| 9        | std::forward<RAJA::internal::LoopData<camp::list<RAJA::statement::Collapse<RAJA::omp_parallel_collapse_exec, camp::int_seq<long, 0l, 2l>, RAJA::statement::For<1l, RAJA::policy::loop::loop_exec, RAJA::statement::For<3l, RAJA::policy::loop::loop_exec, RAJA::statement::Lambda<0l | 1.4%     |
| 10       | camp::internal::tuple_storage<3l, long>::get_inner()         | 1.4%     |

### Full Node Hot-spot Profile

List of top-10 functions / code locations from a full node profile.

Use GCC compiler

Profiling command used:

```
map --profile srun -N 1 -n 64 kripke.exe --zones 32,32,64 --procs 4,4,4
```

| Position | Routine                                                      | Time (%) | MPI (%) |
| -------- | ------------------------------------------------------------ | -------- | ------- |
| 1        | RAJA::operators::plus<long, long, long>::operator()(long const&, long const&) const | 5.7%     |         |
| 2        | RAJA::detail::LayoutBase_impl<camp::int_seq<long, 0l, 1l, 2l>, long, 2l>::operator()<long, long, long>(long, long, long) const [inlined] | 4.9%     |         |
| 3        | camp::forward<long&>(camp::type::ref::rem_s<long&>::type&)   | 3.0%     |         |
| 4        | camp::forward<RAJA::operators::plus<long, long, long         | 2.7%     |         |
| 5        | RAJA::View<double, RAJA::TypedLayout<long, camp::tuple<Kripke::Moment, Kripke::Group, Kripke::Zone>, 2l>, double*>::operator()<Kripke::Moment, Kripke::Group, Kripke::Zone>(Kripke::Moment, Kripke::Group, Kripke::Zone) const [inlined] | 2.4%     |         |
| 6        | RAJA::stripIndexType\<long\>(long) [inlined] (OpenMP)        | 2.4%     |         |
| 7        | camp::internal::tuple_storage<3l, long>::get_inner()         | 2.1%     |         |
| 8        | std::forward<RAJA::internal::LoopData<camp::list<RAJA::statement::Collapse<RAJA::omp_parallel_collapse_exec, camp::int_seq<long, 0l, 2l>, RAJA::statement::For<1l, RAJA::policy::loop::loop_exec, RAJA::statement::For<3l, RAJA::policy::loop::loop_exec, RAJA::statement::Lambda<0l | 1.9%     |         |
| 9        | RAJA::IndexValue<Kripke::Group, long>::IndexValue(long) [inlined] | 1.8%     |         |
| 10       | LTimesSdom::operator()<Kripke::ArchLayoutT<Kripke::ArchT_OpenMP, Kripke::LayoutT_DGZ | 1.8%     |         |


### Architecture Comparison

We used the gcc@10.3.0 compiler in the architecture Comparison.

| Cores | C6gn (Aarch64) | C5n (X86) |
|-------|----------------|-----------|
| 1     | 243.57         | 281.04    |
| 2     | 121.73         | 173.20    |
| 4     | 66.28          | 91.03     |
| 8     | 37.50          | 48.76     |
| 16    | 23.87          | 27.67     |
| 32    | 13.26          | 13.27     |
| 64    | 6.31           | 7.07      |
| 128	| 2.33			 | 3.26		 |
| 256	| 1.35			 | 1.47		 |


## Optimisation

Details of steps taken to optimise performance of the application.
Please document work with compiler flags, maths libraries, system libraries, code optimisations, etc.

### Compiler Flag Tuning

Compiler flags before:
```
N/A
```

Compiler flags after:
```
CPPFLAGS="-Ofast -mcpu=native -ffast-math"
```

#### Compiler Flag Performance

| Cores | Original Flags | New Flags |
|-------|----------------|-----------|
| 1     |   105.85       | 96.48327  |
| 2     |   53.06        | 48.31512  |
| 4     |   28.32        | 26.40836  |
| 8     |   16.53        | 14.8952   |
| 16    |   9.93         | 9.56009   |
| 32    |   4.71         | 4.64924   |
| 64    |    1.99        | 1.99078   |
| 128   |    0.96        | 1.06009   |
| 256   |    0.76        | 1.12626   |

As the performance table shows, we can see some improvements during the use of fewer cores; however, as cores number goes up, we can see the performance boost decreases to none. For further later improvement, we can focus on multi-core collaborations. 

### Performance Regression

How fast can you make the code?

Use all of the above aproaches and any others to make the code as fast as possible.
Demonstrate your gains by providing a scaling study for your test case, demonstrating the performance before and after.

## Report

### Compilation Summary

Kripke can work perfectly out of the box, except we have to manually disable the -sse2 before compiling. The provides us a good start to dig deeper into the usage of tools like spack/reframe, etc. 

### Performance Summary

Kripke can perform good, which is in inline with our expectations. The running time can be drastically decreased, benefited from multi-cores.


### Optimisation Summary

Optimisations in tuning the compiler flags can be tricky sometimes, but some flags can do perform better compared to the others. We should also decide the flags with profiling result / code analysis to have the optimal result.