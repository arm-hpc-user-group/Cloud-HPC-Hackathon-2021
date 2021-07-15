# miniVite 

**Description:** proxy application that implements a single phase of Louvain method in distributed memory for graph community detection

**URL:** https://github.com/Exa-Graph/miniVite 

**Team:** Garotes de Premia 

## Compilation

### Spack Package Modification

Details of any changes to the Spack recipe used.

Git commit hash of checkout for pacakage:

Pull request for Spack recipe changes:

### Building miniVite

#### Compiler 1

##### x86

```
spack install minivite%gcc@10.3.0
```
```
$ spack spec -Il minivite%gcc@10.3.0
Input spec
--------------------------------
 -   minivite%gcc@10.3.0

Concretized
--------------------------------
[+]  yqaajvk  minivite@1.1%gcc@10.3.0+openmp+opt arch=linux-amzn2-skylake_avx512
[+]  pmn26hx      ^openmpi@4.1.0%gcc@10.3.0~atomics~cuda~cxx~cxx_exceptions+gpfs~internal-hwloc~java~legacylaunchers~lustre~memchecker+pmi~singularity~sqlite3+static~thread_multiple+vt+wrapper-rpath fabrics=ofi patches=60ce20bc14d98c572ef7883b9fcd254c3f232c2f3a13377480f96466169ac4c8 schedulers=slurm arch=linux-amzn2-skylake_avx512
[+]  xkz726a          ^hwloc@2.5.0%gcc@10.3.0~cairo~cuda~gl~libudev+libxml2~netloc~nvml+pci+shared arch=linux-amzn2-skylake_avx512
[+]  a4nq5nh              ^libpciaccess@0.16%gcc@10.3.0 arch=linux-amzn2-skylake_avx512
[+]  ya47eic                  ^libtool@2.4.6%gcc@10.3.0 arch=linux-amzn2-skylake_avx512
[+]  6y53od3                      ^m4@1.4.18%gcc@10.3.0+sigsegv patches=3877ab548f88597ab2327a2230ee048d2d07ace1062efe81fc92e91b7f39cd00,fc9b61654a3ba1a8d6cd78ce087e7c96366c290bc8d2c299f09828d793b853c8 arch=linux-amzn2-skylake_avx512
[+]  5qpmdxk                          ^libsigsegv@2.13%gcc@10.3.0 arch=linux-amzn2-skylake_avx512
[+]  i665ooz                  ^pkgconf@1.7.4%gcc@10.3.0 arch=linux-amzn2-skylake_avx512
[+]  4fouma3                  ^util-macros@1.19.3%gcc@10.3.0 arch=linux-amzn2-skylake_avx512
[+]  mztzlil              ^libxml2@2.9.10%gcc@10.3.0~python arch=linux-amzn2-skylake_avx512
[+]  qmzfn6j                  ^libiconv@1.16%gcc@10.3.0 arch=linux-amzn2-skylake_avx512
[+]  p7yqdpr                  ^xz@5.2.5%gcc@10.3.0~pic libs=shared,static arch=linux-amzn2-skylake_avx512
[+]  q2x25kt                  ^zlib@1.2.11%gcc@10.3.0+optimize+pic+shared arch=linux-amzn2-skylake_avx512
[+]  xbybdoz              ^ncurses@6.2%gcc@10.3.0~symlinks+termlib abi=none arch=linux-amzn2-skylake_avx512
[+]  rt2yj4o          ^libevent@2.1.12%gcc@10.3.0+openssl arch=linux-amzn2-skylake_avx512
[+]  larjnul              ^openssl@1.1.1k%gcc@10.3.0~docs+systemcerts arch=linux-amzn2-skylake_avx512
[+]  fb3kjch                  ^perl@5.32.1%gcc@10.3.0+cpanm+shared+threads arch=linux-amzn2-skylake_avx512
[+]  i5lbkjo                      ^berkeley-db@18.1.40%gcc@10.3.0+cxx~docs+stl patches=b231fcc4d5cff05e5c3a4814f6a5af0e9a966428dc2176540d2c05aff41de522 arch=linux-amzn2-skylake_avx512
[+]  s36txvt                      ^bzip2@1.0.8%gcc@10.3.0~debug~pic+shared arch=linux-amzn2-skylake_avx512
[+]  kjoplsl                          ^diffutils@3.7%gcc@10.3.0 arch=linux-amzn2-skylake_avx512
[+]  fgwgsih                      ^gdbm@1.19%gcc@10.3.0 arch=linux-amzn2-skylake_avx512
[+]  i35suwy                          ^readline@8.1%gcc@10.3.0 arch=linux-amzn2-skylake_avx512
[+]  aodqozx          ^libfabric@1.11.1-aws%gcc@10.3.0~debug~kdreg fabrics=sockets,tcp,udp arch=linux-amzn2-skylake_avx512
[+]  uqxtsju          ^numactl@2.0.14%gcc@10.3.0 patches=4e1d78cbbb85de625bad28705e748856033eaafab92a66dffd383a3d7e00cc94,62fc8a8bf7665a60e8f4c93ebbd535647cebf74198f7afafec4c085a8825c006 arch=linux-amzn2-skylake_avx512
[+]  qx56ujy              ^autoconf@2.69%gcc@10.3.0 arch=linux-amzn2-skylake_avx512
[+]  xveamuz              ^automake@1.16.3%gcc@10.3.0 arch=linux-amzn2-skylake_avx512
[+]  7t25qrr          ^openssh@8.5p1%gcc@10.3.0 arch=linux-amzn2-skylake_avx512
[+]  7523zhe              ^libedit@3.1-20210216%gcc@10.3.0 arch=linux-amzn2-skylake_avx512
[+]  724okpi          ^slurm@20-02-4-1%gcc@10.3.0~gtk~hdf5~hwloc~mariadb~pmix+readline~restd sysconfdir=PREFIX/etc arch=linux-amzn2-skylake_avx512
```
##### ARM

```
spack install minivite%gcc@10.3.0
```
```
spack spec -Il minivite%gcc@10.3.0
Input spec
--------------------------------
 -   minivite%gcc@10.3.0

Concretized
--------------------------------
[+]  uvqmav3  minivite@1.1%gcc@10.3.0+openmp+opt arch=linux-amzn2-graviton2
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
#### Compiler 2
```
spack install minivite%arm@21.0.0.879
```
```
spack spec -Il minivite%arm@21.0.0.879
Input spec
--------------------------------
  -   minivite%arm@21.0.0.879

Concretized
--------------------------------
==> Warning: arm@21.0.0.879 cannot build optimized binaries for "graviton2". Using best target possible: "aarch64"
[+]  tvb2q7v  minivite@1.1%arm@21.0.0.879+openmp+opt arch=linux-amzn2-aarch64
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
#### Compiler 3
##### x86

```
spack install minivite%nvhpc@21.2^openssh%gcc@10.3.0
```
```
spack spec -Il minivite%nvhpc@21.2^openssh%gcc@10.3.0
Input spec
--------------------------------
 -   minivite%nvhpc
 -       ^openssh%gcc

Concretized
--------------------------------
[+]  effle4z  minivite@1.1%nvhpc@21.2+openmp+opt arch=linux-amzn2-skylake_avx512
[+]  drkjuxc      ^openmpi@4.1.0%nvhpc@21.2~atomics~cuda~cxx~cxx_exceptions+gpfs~internal-hwloc~java~legacylaunchers~lustre~memchecker+pmi~singularity~sqlite3+static~thread_multiple+vt+wrapper-rpath fabrics=ofi patches=60ce20bc14d98c572ef7883b9fcd254c3f232c2f3a13377480f96466169ac4c8,fba0d3a784a9723338722b48024a22bb32f6a951db841a4e9f08930a93f41d7a schedulers=slurm arch=linux-amzn2-skylake_avx512
[+]  dkc2lhx          ^hwloc@2.5.0%nvhpc@21.2~cairo~cuda~gl~libudev+libxml2~netloc~nvml+pci+shared arch=linux-amzn2-skylake_avx512
[+]  ing2shq              ^libpciaccess@0.16%nvhpc@21.2 patches=6e08dc445ece06e9e8b1344397f2d3f169005703ddc0f2ae24f366cde78c7377 arch=linux-amzn2-skylake_avx512
[+]  4wbhxku                  ^libtool@2.4.6%nvhpc@21.2 arch=linux-amzn2-skylake_avx512
[+]  kyu37po                      ^m4@1.4.18%nvhpc@21.2+sigsegv patches=3877ab548f88597ab2327a2230ee048d2d07ace1062efe81fc92e91b7f39cd00,5746cf51f45b405661c3edae7a78c33d41e54d83f635d16e2bf1f956dbfbf635,fc9b61654a3ba1a8d6cd78ce087e7c96366c290bc8d2c299f09828d793b853c8 arch=linux-amzn2-skylake_avx512
[+]  y2tupel                          ^libsigsegv@2.13%nvhpc@21.2 arch=linux-amzn2-skylake_avx512
[+]  2njg2ak                  ^pkgconf@1.7.4%nvhpc@21.2 arch=linux-amzn2-skylake_avx512
[+]  c7dllp5                  ^util-macros@1.19.3%nvhpc@21.2 arch=linux-amzn2-skylake_avx512
[+]  v6qedll              ^libxml2@2.9.10%nvhpc@21.2~python patches=05ff238cf435825ef835c7ae39376b52dc83d8caf19e962f0766c841386a305a,10a88ad47f9797cf7cf2d7d07241f665a3b6d1f31fa026728c8c2ae93e1664e9 arch=linux-amzn2-skylake_avx512
[+]  amrpz4o                  ^libiconv@1.16%nvhpc@21.2 arch=linux-amzn2-skylake_avx512
[+]  2cm4yqx                  ^xz@5.2.5%nvhpc@21.2~pic libs=shared,static arch=linux-amzn2-skylake_avx512
[+]  mxvwz75                  ^zlib@1.2.11%nvhpc@21.2+optimize+pic+shared arch=linux-amzn2-skylake_avx512
[+]  i7nsry6              ^ncurses@6.2%nvhpc@21.2~symlinks+termlib abi=none arch=linux-amzn2-skylake_avx512
[+]  hu6jlcd          ^libevent@2.1.12%nvhpc@21.2+openssl arch=linux-amzn2-skylake_avx512
[+]  mfx6dcx              ^openssl@1.1.1k%gcc@10.3.0~docs+systemcerts arch=linux-amzn2-skylake_avx512
[+]  t2gqkke                  ^perl@5.32.1%nvhpc@21.2+cpanm+shared+threads patches=21cf6a73cec16760f8de2e8895ace1299aff2d8e92dc581cd18f1d95a4503048 arch=linux-amzn2-skylake_avx512
[+]  o5ucyic                      ^berkeley-db@18.1.40%nvhpc@21.2+cxx~docs+stl patches=b231fcc4d5cff05e5c3a4814f6a5af0e9a966428dc2176540d2c05aff41de522 arch=linux-amzn2-skylake_avx512
[+]  6ons5uc                      ^bzip2@1.0.8%nvhpc@21.2~debug~pic+shared arch=linux-amzn2-skylake_avx512
[+]  tdkxrxq                          ^diffutils@3.7%nvhpc@21.2 patches=6e42dc243f17aab29fd167f060f5bc1f08813e03368eb301b43c95d4b1386681 arch=linux-amzn2-skylake_avx512
[+]  n672euc                      ^gdbm@1.19%nvhpc@21.2 arch=linux-amzn2-skylake_avx512
[+]  ujhndzw                          ^readline@8.1%nvhpc@21.2 arch=linux-amzn2-skylake_avx512
[+]  bwx3qe4          ^libfabric@1.11.1-aws%nvhpc@21.2~debug~kdreg fabrics=sockets,tcp,udp arch=linux-amzn2-skylake_avx512
[+]  vxh5iyi          ^numactl@2.0.14%nvhpc@21.2 patches=4e1d78cbbb85de625bad28705e748856033eaafab92a66dffd383a3d7e00cc94,62fc8a8bf7665a60e8f4c93ebbd535647cebf74198f7afafec4c085a8825c006 arch=linux-amzn2-skylake_avx512
[+]  7anp7bk              ^autoconf@2.69%nvhpc@21.2 arch=linux-amzn2-skylake_avx512
[+]  yrlpchd              ^automake@1.16.3%nvhpc@21.2 arch=linux-amzn2-skylake_avx512
[+]  uzot5q7          ^openssh@8.5p1%gcc@10.3.0 arch=linux-amzn2-skylake_avx512
[+]  m6zajlb              ^libedit@3.1-20210216%gcc@10.3.0 arch=linux-amzn2-skylake_avx512
[+]  3dfoict          ^slurm@20-02-4-1%nvhpc@21.2~gtk~hdf5~hwloc~mariadb~pmix+readline~restd sysconfdir=PREFIX/etc arch=linux-amzn2-skylake_avx512
```
##### ARM
```
spack install minivte%nvhpc@21.2
```
```
spack spec -Il minivite%nvhpc@21.2
Input spec
--------------------------------
 -   minivite%nvhpc@21.2

Concretized
--------------------------------
[+]  emly6c6  minivite@1.1%nvhpc@21.2+openmp+opt arch=linux-amzn2-graviton2
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

[ReFrame Benchmark 1](minivite_short.py)

```
reframe -c minivite_short.py -r --performance-report
```

### Validation

Details of the validation for `Test Case 1`.


### ReFrame Output

```
======================================
PERFORMANCE REPORT
------------------------------------------------------------------------------
miniVite_N 1000000_minivite_1_1__gcc_10_3_0_N_1_MPI_1_OMP_1
- aws:c6gn
   - builtin
      * num_tasks: 1
      * Run Time: 17.3677 None
------------------------------------------------------------------------------
miniVite_N 1000000_minivite_1_1__gcc_10_3_0_N_1_MPI_2_OMP_1
   - builtin
      * num_tasks: 2
      * Run Time: 11.0794 None
------------------------------------------------------------------------------
miniVite_N 1000000_minivite_1_1__gcc_10_3_0_N_1_MPI_4_OMP_1
   - builtin
      * num_tasks: 4
      * Run Time: 4.83797 None
------------------------------------------------------------------------------
miniVite_N 1000000_minivite_1_1__gcc_10_3_0_N_1_MPI_8_OMP_1
   - builtin
      * num_tasks: 8
      * Run Time: 2.47868 None
------------------------------------------------------------------------------
miniVite_N 1000000_minivite_1_1__gcc_10_3_0_N_1_MPI_16_OMP_1
   - builtin
      * num_tasks: 16
      * Run Time: 1.0096 None
------------------------------------------------------------------------------
miniVite_N 1000000_minivite_1_1__gcc_10_3_0_N_1_MPI_32_OMP_1
   - builtin
      * num_tasks: 32
      * Run Time: 0.476241 None
------------------------------------------------------------------------------
miniVite_N 1000000_minivite_1_1__gcc_10_3_0_N_1_MPI_64_OMP_1
   - builtin
      * num_tasks: 64
      * Run Time: 0.231478 None
------------------------------------------------------------------------------
miniVite_N 1000000_minivite_1_1__arm_21_0_0_879_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Run Time: 19.261 None
------------------------------------------------------------------------------
miniVite_N 1000000_minivite_1_1__arm_21_0_0_879_N_1_MPI_2_OMP_1
   - builtin
      * num_tasks: 2
      * Run Time: 11.2518 None
------------------------------------------------------------------------------
miniVite_N 1000000_minivite_1_1__arm_21_0_0_879_N_1_MPI_4_OMP_1
   - builtin
      * num_tasks: 4
      * Run Time: 5.68812 None
------------------------------------------------------------------------------
miniVite_N 1000000_minivite_1_1__arm_21_0_0_879_N_1_MPI_8_OMP_1
   - builtin
      * num_tasks: 8
      * Run Time: 2.85111 None
------------------------------------------------------------------------------
miniVite_N 1000000_minivite_1_1__arm_21_0_0_879_N_1_MPI_16_OMP_1
   - builtin
      * num_tasks: 16
      * Run Time: 1.25349 None
------------------------------------------------------------------------------
miniVite_N 1000000_minivite_1_1__arm_21_0_0_879_N_1_MPI_32_OMP_1
   - builtin
      * num_tasks: 32
      * Run Time: 0.553428 None
------------------------------------------------------------------------------
miniVite_N 1000000_minivite_1_1__arm_21_0_0_879_N_1_MPI_64_OMP_1
   - builtin
      * num_tasks: 64
      * Run Time: 0.362229 None
------------------------------------------------------------------------------
miniVite_N 1000000_minivite_1_1__nvhpc_21_2_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Run Time: 19.9492 None
------------------------------------------------------------------------------
miniVite_N 1000000_minivite_1_1__nvhpc_21_2_N_1_MPI_2_OMP_1
   - builtin
      * num_tasks: 2
      * Run Time: 12.5433 None
------------------------------------------------------------------------------
miniVite_N 1000000_minivite_1_1__nvhpc_21_2_N_1_MPI_4_OMP_1
   - builtin
      * num_tasks: 4
      * Run Time: 5.50243 None
------------------------------------------------------------------------------
miniVite_N 1000000_minivite_1_1__nvhpc_21_2_N_1_MPI_8_OMP_1
   - builtin
      * num_tasks: 8
      * Run Time: 2.93296 None
------------------------------------------------------------------------------
miniVite_N 1000000_minivite_1_1__nvhpc_21_2_N_1_MPI_16_OMP_1
   - builtin
      * num_tasks: 16
      * Run Time: 1.28025 None
------------------------------------------------------------------------------
miniVite_N 1000000_minivite_1_1__nvhpc_21_2_N_1_MPI_32_OMP_1
   - builtin
      * num_tasks: 32
      * Run Time: 1.0272 None
------------------------------------------------------------------------------
miniVite_N 1000000_minivite_1_1__nvhpc_21_2_N_1_MPI_64_OMP_1
   - builtin
      * num_tasks: 64
      * Run Time: 1.25819 None
------------------------------------------------------------------------------
```

### On-node Compiler Comparison

Performance comparison of three compilers.

| Cores | Compiler 1 | Compiler 2 | Compiler 3|
|-------|------------|------------|-----------|
|   1   |  17.3677 s |  19.261  s | 19.9492 s |
|   2   |  11.0794 s |  11.2518 s | 12.5433 s |
|   4   |  4.83797 s |  5.68812 s | 5.50243 s |
|   8   |  2.47868 s |  2.85111 s | 2.93296 s |
|   16  |   1.0096 s |  1.25349 s | 1.28025 s |
|   32  |  0.47624 s | 0.553428 s |  1.0272 s |
|   64  | 0.231478 s | 0.362229 s | 1.25819 s |

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

| Cores | Compiler 1 | Compiler 2 | Compiler 3 |
|-------|------------|------------|------------|
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
