# branson 

**Description:** Branson's purpose is to study different algorithms for parallel Monte Carlo transport. Currently it contains particle passing and mesh passing methods for domain decomposition.

**notice for /data , they are there as they _might_ be helpful but they are far from perfect: for example, I initally forgot to update the name of test class from previous app, so the first few tests were for branson but were named "LaghosTest0", or sometimes directories got overwritten, but we have the Graylog server for a reason! Everything is reprodicible _AND_ already logged to Graylog.**

**URL:** https://github.com/lanl/branson

**Team:** Iman

## Compilation

### Spack Package Modification

Details of any changes to the Spack recipe used.

Git commit hash of checkout for pacakage:

Pull request for Spack recipe changes:

Pull request to branson: https://github.com/lanl/branson/pull/23 (tiny fix for an input file which did not run due to transport type / cell count)

### Building branson

#### Compiler 1: ARM

```
spack install branson%arm
```

```
$ spack spec -Il branson%arm
Input spec
--------------------------------
 -   branson%arm

Concretized
--------------------------------
==> Warning: arm@21.0.0.879 cannot build optimized binaries for "graviton2". Using best target possible: "aarch64"
[+]  jnkdmcc  branson@0.82%arm@21.0.0.879~ipo build_type=RelWithDebInfo arch=linux-amzn2-aarch64
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
[+]  myrsq4g      ^metis@5.1.0%arm@21.0.0.879~gdb~int64~real64+shared build_type=Release patches=4991da938c1d3a1d3dea78e49bbebecba00273f98df2a656e38b83d55b281da1 arch=linux-amzn2-aarch64
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

#### Compiler 2: GCC

```
spack install branson%gcc
```

```
$ spack spec -Il branson%gcc
Input spec
--------------------------------
 -   branson%gcc

Concretized
--------------------------------
[+]  gsc3hlo  branson@0.82%gcc@10.3.0~ipo build_type=RelWithDebInfo arch=linux-amzn2-graviton2
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
[+]  a3tjh3r      ^metis@5.1.0%gcc@10.3.0~gdb~int64~real64+shared build_type=Release patches=4991da938c1d3a1d3dea78e49bbebecba00273f98df2a656e38b83d55b281da1,b1225da886605ea558db7ac08dd8054742ea5afe5ed61ad4d0fe7a495b1270d2 arch=linux-amzn2-graviton2
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

#### Compiler 3: NVHPC

```
spack install branson%nvhpc
```

This did not work due to conflict with cmake and later openblas, more info: https://github.com/spack/spack/issues/20781 The solution:

```
spack install branson%nvhpc ^cmake%gcc
```

```
$ spack spec -Il branson%nvhpc ^cmake%gcc
Input spec
--------------------------------
 -   branson%nvhpc
 -       ^cmake%gcc

Concretized
--------------------------------
[+]  hpkflre  branson@0.82%nvhpc@21.2~ipo build_type=RelWithDebInfo arch=linux-amzn2-graviton2
[+]  it4etcv      ^cmake@3.20.5%gcc@10.3.0~doc+ncurses+openssl+ownlibs~qt build_type=Release arch=linux-amzn2-graviton2
[+]  iwzirqc          ^ncurses@6.2%gcc@10.3.0~symlinks+termlib abi=none arch=linux-amzn2-graviton2
[+]  vtiml6g              ^pkgconf@1.7.4%nvhpc@21.2 arch=linux-amzn2-graviton2
[+]  kssecxk          ^openssl@1.1.1k%gcc@10.3.0~docs+systemcerts arch=linux-amzn2-graviton2
[+]  elargtq              ^perl@5.32.1%nvhpc@21.2+cpanm+shared+threads patches=21cf6a73cec16760f8de2e8895ace1299aff2d8e92dc581cd18f1d95a4503048 arch=linux-amzn2-graviton2
[+]  5uyf3k4                  ^berkeley-db@18.1.40%nvhpc@21.2+cxx~docs+stl patches=b231fcc4d5cff05e5c3a4814f6a5af0e9a966428dc2176540d2c05aff41de522 arch=linux-amzn2-graviton2
[+]  wsi7g3j                  ^bzip2@1.0.8%nvhpc@21.2~debug~pic+shared arch=linux-amzn2-graviton2
[+]  s4mb5no                      ^diffutils@3.7%nvhpc@21.2 patches=6e42dc243f17aab29fd167f060f5bc1f08813e03368eb301b43c95d4b1386681 arch=linux-amzn2-graviton2
[+]  r7mmkdp                          ^libiconv@1.16%nvhpc@21.2 arch=linux-amzn2-graviton2
[+]  dnih4ar                  ^gdbm@1.19%nvhpc@21.2 arch=linux-amzn2-graviton2
[+]  67vez67                      ^readline@8.1%nvhpc@21.2 arch=linux-amzn2-graviton2
[+]  4js6ect                  ^zlib@1.2.11%nvhpc@21.2+optimize+pic+shared arch=linux-amzn2-graviton2
[+]  h2ymlmt      ^metis@5.1.0%nvhpc@21.2~gdb~int64~real64+shared build_type=Release patches=4991da938c1d3a1d3dea78e49bbebecba00273f98df2a656e38b83d55b281da1 arch=linux-amzn2-graviton2
[+]  tr5nj6k      ^openmpi@4.1.0%nvhpc@21.2~atomics~cuda~cxx~cxx_exceptions+gpfs~internal-hwloc~java~legacylaunchers~lustre~memchecker+pmi~singularity~sqlite3+static~thread_multiple+vt+wrapper-rpath fabrics=ofi patches=60ce20bc14d98c572ef7883b9fcd254c3f232c2f3a13377480f96466169ac4c8,fba0d3a784a9723338722b48024a22bb32f6a951db841a4e9f08930a93f41d7a schedulers=slurm arch=linux-amzn2-graviton2
[+]  uogiais          ^hwloc@2.5.0%nvhpc@21.2~cairo~cuda~gl~libudev+libxml2~netloc~nvml+pci+shared arch=linux-amzn2-graviton2
[+]  e4m4ued              ^libpciaccess@0.16%nvhpc@21.2 patches=6e08dc445ece06e9e8b1344397f2d3f169005703ddc0f2ae24f366cde78c7377 arch=linux-amzn2-graviton2
[+]  kk4ax3i                  ^libtool@2.4.6%nvhpc@21.2 arch=linux-amzn2-graviton2
[+]  6c4kz5g                      ^m4@1.4.18%nvhpc@21.2+sigsegv patches=3877ab548f88597ab2327a2230ee048d2d07ace1062efe81fc92e91b7f39cd00,5746cf51f45b405661c3edae7a78c33d41e54d83f635d16e2bf1f956dbfbf635,fc9b61654a3ba1a8d6cd78ce087e7c96366c290bc8d2c299f09828d793b853c8 arch=linux-amzn2-graviton2
[+]  pa6wm5j                          ^libsigsegv@2.13%nvhpc@21.2 arch=linux-amzn2-graviton2
[+]  4imdwuy                  ^util-macros@1.19.3%nvhpc@21.2 arch=linux-amzn2-graviton2
[+]  wo4l72s              ^libxml2@2.9.10%nvhpc@21.2~python patches=05ff238cf435825ef835c7ae39376b52dc83d8caf19e962f0766c841386a305a,10a88ad47f9797cf7cf2d7d07241f665a3b6d1f31fa026728c8c2ae93e1664e9 arch=linux-amzn2-graviton2
[+]  br733tn                  ^xz@5.2.5%nvhpc@21.2~pic libs=shared,static arch=linux-amzn2-graviton2
[+]  qs5m2pb          ^libevent@2.1.12%nvhpc@21.2+openssl arch=linux-amzn2-graviton2
[+]  xl6zavq          ^libfabric@1.11.1-aws%nvhpc@21.2~debug~kdreg fabrics=sockets,tcp,udp arch=linux-amzn2-graviton2
[+]  5yq4tpw          ^numactl@2.0.14%nvhpc@21.2 patches=4e1d78cbbb85de625bad28705e748856033eaafab92a66dffd383a3d7e00cc94,62fc8a8bf7665a60e8f4c93ebbd535647cebf74198f7afafec4c085a8825c006 arch=linux-amzn2-graviton2
[+]  az3tryp              ^autoconf@2.69%nvhpc@21.2 arch=linux-amzn2-graviton2
[+]  yz4jfjs              ^automake@1.16.3%nvhpc@21.2 arch=linux-amzn2-graviton2
[+]  tydb3k5          ^openssh@8.5p1%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  ivotdt7              ^libedit@3.1-20210216%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  zehhooy          ^slurm@20-02-4-1%nvhpc@21.2~gtk~hdf5~hwloc~mariadb~pmix+readline~restd sysconfdir=PREFIX/etc arch=linux-amzn2-graviton2
```

## Validation
This app's repo has a convenient document included with **figure of merit** and test cases and sanity conditions specified. I implemented the test cases right from that document: https://www.lanl.gov/projects/crossroads/_assets/docs/ssi/summary-branson.pdf For verification (correctness) I quote the docment: 

" _The output of Branson can be assumed to be correct if the values for radiation conservation and material conservation are on the order of 1.0e-13 relative to the emission energy and census energy._ " ** EVERY test case and every run we have IS validated **

## Test Case 1: Proxy Small

[ReFrame Benchmark 1](#)

As descibed, the repo has verification examples, which the reframe tests pull and later verify results, and chart the figure of merit: 

```
prerun_cmds = ['wget -O branson.in https://raw.githubusercontent.com/lanl/branson/develop/inputs/proxy_small.xml']
```
But for _proxy small_ (this test case) the configuration throws an error as no paritioning occures: there are two ways to make it work, more cells, or change the transport type from cell pass to replicated, I apllied this change and instead of wgeting I load my patched input. I also made a pull request to branson repo: https://github.com/lanl/branson/pull/23

```
reframe --stage /scratch/home/${USER} -c t0.py -r --performance-report
```

### ReFrame Output

```
==============================================================================
PERFORMANCE REPORT
------------------------------------------------------------------------------
branson_test0_2_branson_0_82__arm_N_1_MPI_1_OMP_1
- aws:c6gn
   - builtin
      * num_tasks: 1
      * Total transport: 5875.65 s
------------------------------------------------------------------------------
branson_test0_2_branson_0_82__arm_N_1_MPI_4_OMP_1
   - builtin
      * num_tasks: 4
      * Total transport: 1562.39 s
------------------------------------------------------------------------------
branson_test0_2_branson_0_82__arm_N_1_MPI_16_OMP_1
   - builtin
      * num_tasks: 16
      * Total transport: 500.085 s
------------------------------------------------------------------------------
branson_test0_2_branson_0_82__arm_N_1_MPI_64_OMP_1
   - builtin
      * num_tasks: 64
      * Total transport: 297.64 s
------------------------------------------------------------------------------
branson_test0_2_branson_0_82__gcc__gsc3hlo_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Total transport: 8131.49 s
------------------------------------------------------------------------------
branson_test0_2_branson_0_82__gcc__gsc3hlo_N_1_MPI_4_OMP_1
   - builtin
      * num_tasks: 4
      * Total transport: 2195.08 s
------------------------------------------------------------------------------
branson_test0_2_branson_0_82__gcc__gsc3hlo_N_1_MPI_16_OMP_1
   - builtin
      * num_tasks: 16
      * Total transport: 663.968 s
------------------------------------------------------------------------------
branson_test0_2_branson_0_82__gcc__gsc3hlo_N_1_MPI_64_OMP_1
   - builtin
      * num_tasks: 64
      * Total transport: 348.833 s
------------------------------------------------------------------------------
branson_test0_2_branson_0_82__nvhpc_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Total transport: 6362.01 s
------------------------------------------------------------------------------
branson_test0_2_branson_0_82__nvhpc_N_1_MPI_4_OMP_1
   - builtin
      * num_tasks: 4
      * Total transport: 1692.63 s
------------------------------------------------------------------------------
branson_test0_2_branson_0_82__nvhpc_N_1_MPI_16_OMP_1
   - builtin
      * num_tasks: 16
      * Total transport: 531.085 s
------------------------------------------------------------------------------
branson_test0_2_branson_0_82__nvhpc_N_1_MPI_64_OMP_1
   - builtin
      * num_tasks: 64
      * Total transport: 308.267 s
------------------------------------------------------------------------------
```

### On-node Compiler Comparison

Performance comparison of two compilers. Measure is Total transport time in seconds.

| Cores | ARM    | GCC     | NVHPC   |
|-------|--------|---------|---------|
| 64    | 297.64 | 348.833 | 308.267 |

This is one of those apps where ARM compiler really shines, Kudos!

### Serial Hot-spot Profile

List of top-10 functions / code locations from a serial profile.

Profiling command used: I actually used the normal reframe test case run, but the script includes flags for _HSPOT\_RUN_ and _DEBUG\_RUN_ which I use to set it up for profiling or a short run for debug. 
```
reframe --stage /scratch/home/${USER} -c t0.py -r --performance-report
```

The profiling is done on arm compiler, by using the ReFrame's _LaunchWrapper_ call map like this:
```
self.job.launcher = LauncherWrapper(self.job.launcher,'map',['--profile', '--export-functions='+self.proffile])
```

|depth|Self |Total|Child|MPI|Overhead|Regions|Function                                                                                                                       |
|-----|-----|-----|-----|---|--------|-------|-------------------------------------------------------------------------------------------------------------------------------|
|0    |24.0%|24.0%|     |   |        |       |optr_gcc_exp_f64                                                                                                               |
|0    |21.7%|89.1%|67.4%|   |        |       |transport_photon_particle_pass(Photon&, Mesh const&, RNG*, double&, double&, double&, std::vector<double, std::allocator<double|
|0    |18.6%|18.6%|     |   |        |       |optr_ac_log_f64                                                                                                                |
|0    |5.0% |5.0% |     |   |        |       |threefry2x64_R(unsigned int, r123array2x64, r123array2x64) [inlined]                                                           |
|0    |4.2% |4.2% |     |   |        |       |cos                                                                                                                            |
|0    |2.8% |2.8% |     |   |        |       |(anonymous namespace)::_ran(unsigned long*) [inlined]                                                                          |
|0    |2.8% |2.8% |     |   |        |       |std::__introsort_loop<__gnu_cxx::__normal_iterator<Photon*, std::vector<Photon, std::allocator<Photon                          |
|0    |2.6% |2.6% |     |   |        |       |sin                                                                                                                            |
|0    |1.9% |1.9% |     |   |        |       |log@plt                                                                                                                        |
|0    |1.9% |1.9% |     |   |        |       |Cell::get_f() const [inlined]                                                                                                  |



### Full Node Hot-spot Profile

List of top-10 functions / code locations from a full node profile.

Profiling command used: I actually used the normal reframe test case run, but the script includes flags for _HSPOT\_RUN_ and _DEBUG\_RUN_ which I use to set it up for profiling or a short run for debug. 
```
reframe --stage /scratch/home/${USER} -c t0.py -r --performance-report
```

The profiling is done on arm compiler, by using the ReFrame's _LaunchWrapper_ call map like this:
```
self.job.launcher = LauncherWrapper(self.job.launcher,'map',['--profile', '--export-functions='+self.proffile])
```

|depth|Self |Total|Child|MPI |Overhead|Regions|Function                                                                                                                       |
|-----|-----|-----|-----|----|--------|-------|-------------------------------------------------------------------------------------------------------------------------------|
|0    |21.9%|72.6%|50.7%|    |        |       |transport_photon_particle_pass(Photon&, Mesh const&, RNG*, double&, double&, double&, std::vector<double, std::allocator<double|
|0    |17.0%|17.0%|     |    |        |       |Mesh::get_on_rank_cell(unsigned int) const [inlined]                                                                           |
|0    |10.9%|10.9%|     |    |        |       |optr_gcc_exp_f64                                                                                                               |
|0    |8.0% |8.0% |     |    |        |       |optr_ac_log_f64                                                                                                                |
|0    |5.8% |5.8% |<0.1%|    |        |       |std::__introsort_loop<__gnu_cxx::__normal_iterator<Photon*, std::vector<Photon, std::allocator<Photon                          |
|0    |4.5% |4.5% |     |    |        |       |Mesh::get_on_rank_cell(unsigned int) const [inlined]                                                                           |
|0    |3.0% |3.0% |     |    |        |       |syscall                                                                                                                        |
|0    |2.4% |2.4% |     |    |        |       |threefry2x64_R(unsigned int, r123array2x64, r123array2x64) [inlined]                                                           |
|0    |1.6% |1.6% |<0.1%|    |        |       |cos                                                                                                                            |
|0    |1.2% |1.2% |     |1.2%|        |       |MPI_Barrier                                                                                                                    |

Waaaait what? Take the above result (full node top 10 function) with a grain of salt, no time to investigate but they might be trash because where are all the rest of mpi calls?

### Strong Scaling Study

On-node scaling study for two compilers. Transport time in seconds. Branson test cases are long, so no seconds!

| Cores | arm  | gcc  | nvhpc |
|-------|------|------|-------|
| 1     | 5875 | 8131 | 6362  |
| 4     | 1562 | 2195 | 1692  |
| 16    | 500  | 663  |  531  |
| 64    | 297  | 348  |  308  |


## Report

### Compilation Summary

No hitches here.

### Performance Summary

Branson test case was long running, and so good for a performance review. I ran the map profiler (not the one for functions) for 32 cores. First stop: the app is compute bound, at 98.8 in compute. Well let's get back to what BRANSON does: first, no I/O obviously, but why so little MPI? Well for 1, it is shamefully a parallel thing to do: there is only two barriers after all is done, and with good load balancing everything would just do in parallel.

CPU metrics is reasonable, CPI could be less (more SIMD, probably would be less CPI on an x86 machine I guess?). What we described about two barriers first and last, shows in MPI breakdown: collective calls trump p2p. Thread breakdown also shows system load at 50% (remember we picked 32) so great.
