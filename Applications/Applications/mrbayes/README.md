# MrBayes 

**Description:** MrBayes is a program for Bayesian inference and model choice across a wide range of phylogenetic and evolutionary models. MrBayes uses Markov chain Monte Carlo (MCMC) methods to estimate the posterior distribution of model parameters.

**URL:** http://mrbayes.sourceforge.net

**Team:**  

## Compilation

### Spack Package Modification

Details of any changes to the Spack recipe used.

Git commit hash of checkout for pacakage:

Pull request for Spack recipe changes:

### Building MrBayes



#### Compiler 1: gcc@10.3.0
```
spack install mrbayes%gcc
```
```
$ spack spec -Il mrbayes%gcc
----------------------------------
 -   74u7ov5  mrbayes@3.2.7a%gcc@10.3.0+beagle+mpi~readline arch=linux-amzn2-graviton2
[+]  miuo6nu      ^libbeagle@3.1.2%gcc@10.3.0~cuda cuda_arch=none arch=linux-amzn2-graviton2
[+]  jkuhz64          ^autoconf@2.69%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  ebhjpix              ^m4@1.4.18%gcc@10.3.0+sigsegv patches=3877ab548f88597ab2327a2230ee048d2d07ace1062efe81fc92e91b7f39cd00,fc9b61654a3ba1a8d6cd78ce087e7c96366c290bc8d2c299f09828d793b853c8 arch=linux-amzn2-graviton2
[+]  ltbv6bk                  ^libsigsegv@2.13%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  4m7exgb              ^perl@5.32.1%gcc@10.3.0+cpanm+shared+threads arch=linux-amzn2-graviton2
[+]  y42m6yr                  ^berkeley-db@18.1.40%gcc@10.3.0+cxx~docs+stl patches=b231fcc4d5cff05e5c3a4814f6a5af0e9a966428dc2176540d2c05aff41de522 arch=linux-amzn2-graviton2
[+]  rqrpmap                  ^bzip2@1.0.8%gcc@10.3.0~debug~pic+shared arch=linux-amzn2-graviton2
[+]  2w7bert                      ^diffutils@3.7%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  y5ei3cm                          ^libiconv@1.16%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  wjwqncx                  ^gdbm@1.19%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  3zy7kxk                      ^readline@8.1%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  iwzirqc                          ^ncurses@6.2%gcc@10.3.0~symlinks+termlib abi=none arch=linux-amzn2-graviton2
[+]  s4pw7zm                              ^pkgconf@1.7.4%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  qepjcvj                  ^zlib@1.2.11%gcc@10.3.0+optimize+pic+shared arch=linux-amzn2-graviton2
[+]  xb2w5nc          ^automake@1.16.3%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  z2uysov          ^libtool@2.4.6%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  5g5g4bf          ^openjdk@11.0.0-2020-01-01%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  dh67fng          ^subversion@1.14.0%gcc@10.3.0~perl+serf arch=linux-amzn2-graviton2
[+]  mjfwjv5              ^apr@1.7.0%gcc@10.3.0 patches=a4128488c546646b4a585c3d49706675b1c016139dd61bdd153fb3151bbcb12c arch=linux-amzn2-graviton2
[+]  2non7qx                  ^util-linux-uuid@2.36.2%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  qbx5g7c              ^apr-util@1.6.1%gcc@10.3.0+crypto~gdbm~odbc~pgsql~sqlite arch=linux-amzn2-graviton2
[+]  ychdz7l                  ^expat@2.4.1%gcc@10.3.0+libbsd arch=linux-amzn2-graviton2
[+]  ourxkez                      ^libbsd@0.11.3%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  nssrqfc                          ^libmd@1.0.3%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  5i3lgfb                  ^openssl@1.1.1k%gcc@10.3.0~docs+systemcerts arch=linux-amzn2-graviton2
[+]  pytpp72              ^lz4@1.9.3%gcc@10.3.0 libs=shared,static arch=linux-amzn2-graviton2
[+]  onskchf              ^serf@1.3.9%gcc@10.3.0~debug patches=b6593a4dafea97d1bef13b5d57fecb1410f02452d7def51b31f76bf76a85c4ad arch=linux-amzn2-graviton2
[+]  23v43px                  ^scons@3.1.2%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  s6xqcwm                      ^py-setuptools@50.3.2%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  62czasr                          ^python@3.8.11%gcc@10.3.0+bz2+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tix~tkinter~ucs4+uuid+zlib patches=0d98e93189bc278fbc37a50ed7f183bd8aaf249a8e1670a465f0db6bb4f8cf87 arch=linux-amzn2-graviton2
[+]  fqlpcsl                              ^gettext@0.21%gcc@10.3.0+bzip2+curses+git~libunistring+libxml2+tar+xz arch=linux-amzn2-graviton2
[+]  iyhm3wi                                  ^libxml2@2.9.10%gcc@10.3.0~python arch=linux-amzn2-graviton2
[+]  ye3kcvv                                      ^xz@5.2.5%gcc@10.3.0~pic libs=shared,static arch=linux-amzn2-graviton2
[+]  v6cutkh                                  ^tar@1.34%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  35cffos                              ^libffi@3.3%gcc@10.3.0 patches=26f26c6f29a7ce9bf370ad3ab2610f99365b4bdd7b82e7c31df41a3370d685c0 arch=linux-amzn2-graviton2
[+]  2q753q6                              ^sqlite@3.35.5%gcc@10.3.0+column_metadata+fts~functions~rtree arch=linux-amzn2-graviton2
[+]  azgubgn              ^utf8proc@2.4.0%gcc@10.3.0~ipo build_type=RelWithDebInfo arch=linux-amzn2-graviton2
[+]  m7325ee                  ^cmake@3.20.5%gcc@10.3.0~doc+ncurses+openssl+ownlibs~qt build_type=Release arch=linux-amzn2-graviton2
 -   zvamksn      ^openmpi@4.1.0%gcc@10.3.0~atomics~cuda~cxx~cxx_exceptions+gpfs~internal-hwloc~java~legacylaunchers~lustre~memchecker+pmi~singularity~sqlite3+static~thread_multiple+vt+wrapper-rpath fabrics=ofi patches=60ce20bc14d98c572ef7883b9fcd254c3f232c2f3a13377480f96466169ac4c8 schedulers=slurm arch=linux-amzn2-graviton2
 -   cukmqbg          ^hwloc@2.5.0%gcc@10.3.0~cairo~cuda~gl~libudev+libxml2~netloc~nvml+pci+shared arch=linux-amzn2-graviton2
[+]  asgtk6a              ^libpciaccess@0.16%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  4xr3hhh                  ^util-macros@1.19.3%gcc@10.3.0 arch=linux-amzn2-graviton2
 -   tadxrfp          ^libevent@2.1.12%gcc@10.3.0+openssl arch=linux-amzn2-graviton2
 -   72f5gvk          ^libfabric@1.11.1-aws%gcc@10.3.0~debug~kdreg fabrics=sockets,tcp,udp arch=linux-amzn2-graviton2
 -   mhav5gn          ^numactl@2.0.14%gcc@10.3.0 patches=4e1d78cbbb85de625bad28705e748856033eaafab92a66dffd383a3d7e00cc94,62fc8a8bf7665a60e8f4c93ebbd535647cebf74198f7afafec4c085a8825c006 arch=linux-amzn2-graviton2
[+]  wturp6c          ^openssh@8.5p1%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  ivotdt7              ^libedit@3.1-20210216%gcc@10.3.0 arch=linux-amzn2-graviton2
 -   wqpuvmh          ^slurm@20-02-4-1%gcc@10.3.0~gtk~hdf5~hwloc~mariadb~pmix+readline~restd sysconfdir=PREFIX/etc arch=linux-amzn2-graviton2

```
#### Compiler 2: arm@21.0.0.879
```
spack install mrbayes%arm
```

```
[+]  nlksl7w  mrbayes@3.2.7a%arm@21.0.0.879+beagle+mpi~readline arch=linux-amzn2-graviton2
[+]  mai56bx      ^libbeagle@3.1.2%arm@21.0.0.879~cuda cuda_arch=none arch=linux-amzn2-graviton2
[+]  mbkv7qv          ^autoconf@2.69%arm@21.0.0.879 arch=linux-amzn2-graviton2
[+]  guhrr3n              ^m4@1.4.18%arm@21.0.0.879+sigsegv patches=3877ab548f88597ab2327a2230ee048d2d07ace1062efe81fc92e91b7f39cd00,fc9b61654a3ba1a8d6cd78ce087e7c96366c290bc8d2c299f09828d793b853c8 arch=linux-amzn2-graviton2
[+]  q27ybb5                  ^libsigsegv@2.13%arm@21.0.0.879 arch=linux-amzn2-graviton2
[+]  aoyzxyq              ^perl@5.32.1%arm@21.0.0.879+cpanm+shared+threads arch=linux-amzn2-graviton2
[+]  rd3hv7n                  ^berkeley-db@18.1.40%arm@21.0.0.879+cxx~docs+stl patches=b231fcc4d5cff05e5c3a4814f6a5af0e9a966428dc2176540d2c05aff41de522 arch=linux-amzn2-graviton2
[+]  qaavobd                  ^bzip2@1.0.8%arm@21.0.0.879~debug~pic+shared arch=linux-amzn2-graviton2
[+]  qchmimy                      ^diffutils@3.7%arm@21.0.0.879 arch=linux-amzn2-graviton2
[+]  4fpawwk                          ^libiconv@1.16%arm@21.0.0.879 arch=linux-amzn2-graviton2
[+]  jbenr5m                  ^gdbm@1.19%arm@21.0.0.879 arch=linux-amzn2-graviton2
[+]  7fjq32x                      ^readline@8.1%arm@21.0.0.879 arch=linux-amzn2-graviton2
[+]  5fshnbc                          ^ncurses@6.2%arm@21.0.0.879~symlinks+termlib abi=none arch=linux-amzn2-graviton2
[+]  s6jl232                              ^pkgconf@1.7.4%arm@21.0.0.879 arch=linux-amzn2-graviton2
[+]  kfhtmo3                  ^zlib@1.2.11%arm@21.0.0.879+optimize+pic+shared arch=linux-amzn2-graviton2
[+]  toijtok          ^automake@1.16.3%arm@21.0.0.879 arch=linux-amzn2-graviton2
[+]  xcqslvj          ^libtool@2.4.6%arm@21.0.0.879 arch=linux-amzn2-graviton2
[+]  dreriht          ^openjdk@11.0.0-2020-01-01%arm@21.0.0.879 arch=linux-amzn2-graviton2
[+]  ca5dqxj          ^subversion@1.14.0%arm@21.0.0.879~perl+serf arch=linux-amzn2-graviton2
[+]  kslaauw              ^apr@1.7.0%arm@21.0.0.879 patches=a4128488c546646b4a585c3d49706675b1c016139dd61bdd153fb3151bbcb12c arch=linux-amzn2-graviton2
[+]  svjr2ln                  ^util-linux-uuid@2.36.2%arm@21.0.0.879 arch=linux-amzn2-graviton2
[+]  t32mlc7              ^apr-util@1.6.1%arm@21.0.0.879+crypto~gdbm~odbc~pgsql~sqlite arch=linux-amzn2-graviton2
[+]  yasvmv6                  ^expat@2.4.1%arm@21.0.0.879+libbsd arch=linux-amzn2-graviton2
[+]  dexaowa                      ^libbsd@0.11.3%arm@21.0.0.879 arch=linux-amzn2-graviton2
[+]  xfbz5kc                          ^libmd@1.0.3%arm@21.0.0.879 arch=linux-amzn2-graviton2
[+]  b6rhpqo                  ^openssl@1.1.1k%arm@21.0.0.879~docs+systemcerts arch=linux-amzn2-graviton2
[+]  jcmu45t              ^lz4@1.9.3%arm@21.0.0.879 libs=shared,static arch=linux-amzn2-graviton2
[+]  hmyu3t7              ^serf@1.3.9%arm@21.0.0.879~debug patches=b6593a4dafea97d1bef13b5d57fecb1410f02452d7def51b31f76bf76a85c4ad arch=linux-amzn2-graviton2
[+]  cjoainj                  ^scons@3.1.2%arm@21.0.0.879 arch=linux-amzn2-graviton2
[+]  n2zxeey                      ^py-setuptools@50.3.2%arm@21.0.0.879 arch=linux-amzn2-graviton2
[+]  lazul7b                          ^python@3.8.11%arm@21.0.0.879+bz2+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tix~tkinter~ucs4+uuid+zlib patches=0d98e93189bc278fbc37a50ed7f183bd8aaf249a8e1670a465f0db6bb4f8cf87 arch=linux-amzn2-graviton2
[+]  cs6d7td                              ^gettext@0.21%arm@21.0.0.879+bzip2+curses+git~libunistring+libxml2+tar+xz arch=linux-amzn2-graviton2
[+]  7og6524                                  ^libxml2@2.9.10%arm@21.0.0.879~python arch=linux-amzn2-graviton2
[+]  3uhexv5                                      ^xz@5.2.5%arm@21.0.0.879~pic libs=shared,static arch=linux-amzn2-graviton2
[+]  3wep6qj                                  ^tar@1.34%arm@21.0.0.879 arch=linux-amzn2-graviton2
[+]  mqvnz77                              ^libffi@3.3%arm@21.0.0.879 patches=26f26c6f29a7ce9bf370ad3ab2610f99365b4bdd7b82e7c31df41a3370d685c0 arch=linux-amzn2-graviton2
[+]  to7xt4x                              ^sqlite@3.35.5%arm@21.0.0.879+column_metadata+fts~functions~rtree arch=linux-amzn2-graviton2
[+]  6xgl2uh              ^utf8proc@2.4.0%arm@21.0.0.879~ipo build_type=RelWithDebInfo arch=linux-amzn2-graviton2
[+]  kbrbmhy                  ^cmake@3.20.5%arm@21.0.0.879~doc+ncurses+openssl+ownlibs~qt build_type=Release arch=linux-amzn2-graviton2
[+]  huifkle      ^openmpi@4.1.0%arm@21.0.0.879~atomics~cuda~cxx~cxx_exceptions+gpfs~internal-hwloc~java~legacylaunchers~lustre~memchecker+pmi~singularity~sqlite3+static~thread_multiple+vt+wrapper-rpath fabrics=ofi patches=60ce20bc14d98c572ef7883b9fcd254c3f232c2f3a13377480f96466169ac4c8 schedulers=slurm arch=linux-amzn2-graviton2
[+]  xsh5tug          ^hwloc@2.5.0%arm@21.0.0.879~cairo~cuda~gl~libudev+libxml2~netloc~nvml+pci+shared arch=linux-amzn2-graviton2
[+]  heo5xlh              ^libpciaccess@0.16%arm@21.0.0.879 arch=linux-amzn2-graviton2
[+]  6eey55q                  ^util-macros@1.19.3%arm@21.0.0.879 arch=linux-amzn2-graviton2
[+]  hj5l7x5          ^libevent@2.1.12%arm@21.0.0.879+openssl arch=linux-amzn2-graviton2
[+]  v75lszn          ^libfabric@1.11.1-aws%arm@21.0.0.879~debug~kdreg fabrics=sockets,tcp,udp arch=linux-amzn2-graviton2
[+]  325gh7i          ^numactl@2.0.14%arm@21.0.0.879 patches=4e1d78cbbb85de625bad28705e748856033eaafab92a66dffd383a3d7e00cc94,62fc8a8bf7665a60e8f4c93ebbd535647cebf74198f7afafec4c085a8825c006 arch=linux-amzn2-graviton2
[+]  7cmi2lb          ^openssh@8.5p1%arm@21.0.0.879 arch=linux-amzn2-graviton2
[+]  qytqrqe              ^libedit@3.1-20210216%arm@21.0.0.879 arch=linux-amzn2-graviton2
[+]  uxllonc          ^slurm@20-02-4-1%arm@21.0.0.879~gtk~hdf5~hwloc~mariadb~pmix+readline~restd sysconfdir=PREFIX/etc arch=linux-amzn2-graviton2
```

#### Compiler 3: nvhpc@21.2
```
spack install mrbayes%nvhpc ^cmake%gcc ^python%gcc ^util-linux-uuid%gcc ^libbsd%gcc ^apr-util%gcc ^sqlite%gcc ^serf%gcc ^libbeagle%gcc
```
> Yeah, I know compiling by *nvhpc* looks like the ship of Theseus.
```
[+]  cwgvvib  mrbayes@3.2.7a%nvhpc@21.2+beagle+mpi~readline arch=linux-amzn2-graviton2
[+]  miuo6nu      ^libbeagle@3.1.2%gcc@10.3.0~cuda cuda_arch=none arch=linux-amzn2-graviton2
[+]  jkuhz64          ^autoconf@2.69%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  ebhjpix              ^m4@1.4.18%gcc@10.3.0+sigsegv patches=3877ab548f88597ab2327a2230ee048d2d07ace1062efe81fc92e91b7f39cd00,fc9b61654a3ba1a8d6cd78ce087e7c96366c290bc8d2c299f09828d793b853c8 arch=linux-amzn2-graviton2
[+]  ltbv6bk                  ^libsigsegv@2.13%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  4m7exgb              ^perl@5.32.1%gcc@10.3.0+cpanm+shared+threads arch=linux-amzn2-graviton2
[+]  y42m6yr                  ^berkeley-db@18.1.40%gcc@10.3.0+cxx~docs+stl patches=b231fcc4d5cff05e5c3a4814f6a5af0e9a966428dc2176540d2c05aff41de522 arch=linux-amzn2-graviton2
[+]  rqrpmap                  ^bzip2@1.0.8%gcc@10.3.0~debug~pic+shared arch=linux-amzn2-graviton2
[+]  2w7bert                      ^diffutils@3.7%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  y5ei3cm                          ^libiconv@1.16%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  wjwqncx                  ^gdbm@1.19%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  3zy7kxk                      ^readline@8.1%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  iwzirqc                          ^ncurses@6.2%gcc@10.3.0~symlinks+termlib abi=none arch=linux-amzn2-graviton2
[+]  s4pw7zm                              ^pkgconf@1.7.4%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  qepjcvj                  ^zlib@1.2.11%gcc@10.3.0+optimize+pic+shared arch=linux-amzn2-graviton2
[+]  xb2w5nc          ^automake@1.16.3%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  z2uysov          ^libtool@2.4.6%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  5g5g4bf          ^openjdk@11.0.0-2020-01-01%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  dh67fng          ^subversion@1.14.0%gcc@10.3.0~perl+serf arch=linux-amzn2-graviton2
[+]  mjfwjv5              ^apr@1.7.0%gcc@10.3.0 patches=a4128488c546646b4a585c3d49706675b1c016139dd61bdd153fb3151bbcb12c arch=linux-amzn2-graviton2
[+]  2non7qx                  ^util-linux-uuid@2.36.2%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  qbx5g7c              ^apr-util@1.6.1%gcc@10.3.0+crypto~gdbm~odbc~pgsql~sqlite arch=linux-amzn2-graviton2
[+]  ychdz7l                  ^expat@2.4.1%gcc@10.3.0+libbsd arch=linux-amzn2-graviton2
[+]  ourxkez                      ^libbsd@0.11.3%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  nssrqfc                          ^libmd@1.0.3%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  5i3lgfb                  ^openssl@1.1.1k%gcc@10.3.0~docs+systemcerts arch=linux-amzn2-graviton2
[+]  pytpp72              ^lz4@1.9.3%gcc@10.3.0 libs=shared,static arch=linux-amzn2-graviton2
[+]  onskchf              ^serf@1.3.9%gcc@10.3.0~debug patches=b6593a4dafea97d1bef13b5d57fecb1410f02452d7def51b31f76bf76a85c4ad arch=linux-amzn2-graviton2
[+]  23v43px                  ^scons@3.1.2%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  s6xqcwm                      ^py-setuptools@50.3.2%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  62czasr                          ^python@3.8.11%gcc@10.3.0+bz2+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tix~tkinter~ucs4+uuid+zlib patches=0d98e93189bc278fbc37a50ed7f183bd8aaf249a8e1670a465f0db6bb4f8cf87 arch=linux-amzn2-graviton2
[+]  fqlpcsl                              ^gettext@0.21%gcc@10.3.0+bzip2+curses+git~libunistring+libxml2+tar+xz arch=linux-amzn2-graviton2
[+]  iyhm3wi                                  ^libxml2@2.9.10%gcc@10.3.0~python arch=linux-amzn2-graviton2
[+]  ye3kcvv                                      ^xz@5.2.5%gcc@10.3.0~pic libs=shared,static arch=linux-amzn2-graviton2
[+]  v6cutkh                                  ^tar@1.34%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  35cffos                              ^libffi@3.3%gcc@10.3.0 patches=26f26c6f29a7ce9bf370ad3ab2610f99365b4bdd7b82e7c31df41a3370d685c0 arch=linux-amzn2-graviton2
[+]  2q753q6                              ^sqlite@3.35.5%gcc@10.3.0+column_metadata+fts~functions~rtree arch=linux-amzn2-graviton2
[+]  azgubgn              ^utf8proc@2.4.0%gcc@10.3.0~ipo build_type=RelWithDebInfo arch=linux-amzn2-graviton2
[+]  m7325ee                  ^cmake@3.20.5%gcc@10.3.0~doc+ncurses+openssl+ownlibs~qt build_type=Release arch=linux-amzn2-graviton2
[+]  ziwrq5e      ^openmpi@4.1.0%nvhpc@21.2~atomics~cuda~cxx~cxx_exceptions+gpfs~internal-hwloc~java~legacylaunchers~lustre~memchecker+pmi~singularity~sqlite3+static~thread_multiple+vt+wrapper-rpath fabrics=ofi patches=60ce20bc14d98c572ef7883b9fcd254c3f232c2f3a13377480f96466169ac4c8,fba0d3a784a9723338722b48024a22bb32f6a951db841a4e9f08930a93f41d7a schedulers=slurm arch=linux-amzn2-graviton2
[+]  f5xzi2q          ^hwloc@2.5.0%nvhpc@21.2~cairo~cuda~gl~libudev+libxml2~netloc~nvml+pci+shared arch=linux-amzn2-graviton2
[+]  e4m4ued              ^libpciaccess@0.16%nvhpc@21.2 patches=6e08dc445ece06e9e8b1344397f2d3f169005703ddc0f2ae24f366cde78c7377 arch=linux-amzn2-graviton2
[+]  4imdwuy                  ^util-macros@1.19.3%nvhpc@21.2 arch=linux-amzn2-graviton2
[+]  qmlezth          ^libevent@2.1.12%nvhpc@21.2+openssl arch=linux-amzn2-graviton2
[+]  xl6zavq          ^libfabric@1.11.1-aws%nvhpc@21.2~debug~kdreg fabrics=sockets,tcp,udp arch=linux-amzn2-graviton2
[+]  5yq4tpw          ^numactl@2.0.14%nvhpc@21.2 patches=4e1d78cbbb85de625bad28705e748856033eaafab92a66dffd383a3d7e00cc94,62fc8a8bf7665a60e8f4c93ebbd535647cebf74198f7afafec4c085a8825c006 arch=linux-amzn2-graviton2
[+]  wturp6c          ^openssh@8.5p1%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  ivotdt7              ^libedit@3.1-20210216%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  zehhooy          ^slurm@20-02-4-1%nvhpc@21.2~gtk~hdf5~hwloc~mariadb~pmix+readline~restd sysconfdir=PREFIX/etc arch=linux-amzn2-graviton2
```
## Test Case 1

> mb cynmix.nex

[ReFrame Benchmark 1](#)

```
../bin/reframe -c benchmark.py -r --performance-report
```

### Validation

Details of the validation for `Test Case 1`.


### ReFrame Output

```
==============================================================================
PERFORMANCE REPORT
------------------------------------------------------------------------------
     **** 
------------------------------------------------------------------------------
```

### On-node Compiler Comparison

Performance comparison of two compilers.

| Cores | Compiler 1 | Compiler 2 |
|-------|------------|------------|
|       |            |            |


### Serial Hot-spot Profile

List of top-10 functions / code locations from a serial profile.

Use the GCC compiler.

Profiling command used:
```
map --profile srun -N 1 -n 1 mb cynmix.nex
```

| Position | Routine               | Time (%) |
| -------- | --------------------- | -------- |
| 1        | pthread_cond_signal   | 70.8%    |
| 2        | \_\_log_finite          | 5.8%     |
| 3        | Move_ParsSPR          | 4.3%     |
| 4        | CondLikeDown_Std      | 3.5%     |
| 5        | CondLikeScaler_Std    | 3.2%     |
| 6        | TreeLikelihood_Beagle | 1.4%     |
| 7        | GetFitchPartials      | 1.4%     |
| 8        | \_\_GI\_\_IO_file_sync    | 1.4% |
| 9        | __exp_finite | 1.2% |
| 10       | CondLikeRoot_Std | 0.9% |

### Full Node Hot-spot Profile

List of top-10 functions / code locations from a full node profile.

Use GCC compiler.

Profiling command used:
```
map --profile srun -N 1 -n 64 mb cynmix.nex
```

| Position | Routine             | Time (%) | MPI (%) |
| -------- | ------------------- | -------- | ------- |
| 1        | MPI_Allreduce       | 89.6%    | 89.6%   |
| 2        | pthread_cond_signal | 5.9%     |         |
| 3        | MPI_Waitall         | 0.9%     | 0.9%    |
| 4        | __log_finite        | 0.4%     |         |
| 5        | CondLikeDown_Std    | 0.3%     |         |
| 6        | Move_ParsSPR        | 0.3%     |         |
| 7        | open64              | 0.2%     |         |
| 8        | GetFitchPartials    | 0.2%     |         |
| 9        | MPI_Isend           | 0.2%     | 0.2%    |
| 10       | CondLikeScaler_Std  | 0.2%     |         |

## Test Case 2

> mb hym.nex

[ReFrame Benchmark 1](#)

```
../bin/reframe -c benchmark.py -r --performance-report
```

### Validation

Details of the validation for `Test Case 1`.


### ReFrame Output

```
==============================================================================
PERFORMANCE REPORT
------------------------------------------------------------------------------
     **** 
------------------------------------------------------------------------------
```

### On-node Compiler Comparison

Performance comparison of two compilers.

| Cores | Compiler 1 | Compiler 2 |
| ----- | ---------- | ---------- |
|       |            |            |


### Serial Hot-spot Profile

List of top-10 functions / code locations from a serial profile.

Use the GCC compiler.

Profiling command used:

```
map --profile srun -N 1 -n 1 mb hym.nex
```

| Position | Routine                                                      | Time (%) |
| -------- | ------------------------------------------------------------ | -------- |
| 1        | CondLikeDown_Std                                             | 22.8%    |
| 2        | CondLikeScaler_Std                                           | 17.8%    |
| 3        | __log_finite                                                 | 15.1%    |
| 4        | CondLikeRoot_Std                                             | 9.6%     |
| 5        | beagle::cpu::BeagleCPU4StateImpl<float, 1, 0>::calcStatesPartials(float*, int const*, float const*, float const*, float const*, int, int) | 6.9%     |
| 6        | beagle::cpu::EigenDecompositionCube<float, 1>::updateTransitionMatrices(int, int const*, int const*, int const*, double const*, double const*, float**, int) | 3.8%     |
| 7        | Likelihood_Std                                               | 3.3%     |
| 8        | beagle::cpu::BeagleCPU4StateImpl<float, 1, 0>::calcPartialsPartials(float*, float const*, float const*, float const*, float const*, int, int) | 3.1%     |
| 9        | __exp_finite                                                 | 2.9%     |
| 10       | beagle::cpu::BeagleCPU4StateImpl<float, 1, 0>::calcEdgeLogLikelihoods(int, int, int, int, int, int, double*) | 2.7%     |

### Full Node Hot-spot Profile

List of top-10 functions / code locations from a full node profile.

Use GCC compiler.

Profiling command used:

```
map --profile srun -N 1 -n 64 mb hym.nex
```

| Position | Routine                                                      | Time (%) | MPI (%) |
| -------- | ------------------------------------------------------------ | -------- | ------- |
| 1        | MPI_Allreduce                                                | 42.1%    | 42.1%   |
| 2        | CondLikeDown_Std                                             | 12.0%    |         |
| 3        | CondLikeScaler_Std                                           | 8.6%     |         |
| 4        | __log_finite                                                 | 7.9%     |         |
| 5        | MPI_Waitall                                                  | 6.0%     | 6.0%    |
| 6        | CondLikeRoot_Std                                             | 5.0%     |         |
| 7        | beagle::cpu::BeagleCPU4StateImpl<float, 1, 0>::calcStatesPartials(float*, int const*, float const*, float const*, float const*, int, int) | 3.2%     |         |
| 8        | __exp_finite                                                 | 1.6%     |         |
| 9        | beagle::cpu::EigenDecompositionCube<float, 1>::updateTransitionMatrices(int, int const*, int const*, int const*, double const*, double const*, float**, int) | 1.4%     |         |
| 10       | beagle::cpu::BeagleCPU4StateImpl<float, 1, 0>::calcPartialsPartials(float*, float const*, float const*, float const*, float const*, int, int) | 1.4%     |         |

## Test Case 3

> mb kim.nex

[ReFrame Benchmark 1](#)

```
../bin/reframe -c benchmark.py -r --performance-report
```

### Validation

Details of the validation for `Test Case 1`.


### ReFrame Output

```
==============================================================================
PERFORMANCE REPORT
------------------------------------------------------------------------------
     **** 
------------------------------------------------------------------------------
```

### On-node Compiler Comparison

Performance comparison of two compilers.

| Cores | Compiler 1 | Compiler 2 |
| ----- | ---------- | ---------- |
|       |            |            |


### Serial Hot-spot Profile

List of top-10 functions / code locations from a serial profile.

Use the GCC compiler.

Profiling command used:

```
map --profile srun -N 1 -n 1 mb kim.nex
```

| Position | Routine                | Time (%) |
| -------- | ---------------------- | -------- |
| 1        | CheckExpandedModels    | 50.0%    |
| 2        | ProtID [inlined]       | 16.7%    |
| 3        | \_\_GI\_\_IO_file_sync | 16.7%    |
| 4        | MPI_Finalize           | 16.7%    |
| 5        | main                   | <0.1%    |
| 6        | CommandLine            | <0.1%    |
| 7        | ParseCommand           | <0.1%    |
| 8        | DoExecute              | <0.1%    |
| 9        | DoMatrixParm           | <0.1%    |
| 10       | CharacterCode          | <0.1%    |

### Full Node Hot-spot Profile

List of top-10 functions / code locations from a full node profile.

Use GCC compiler.

Profiling command used:

```
map --profile srun -N 1 -n 64 mb kim.nex
```

| Position | Routine                     | Time (%) | MPI (%) |
| -------- | --------------------------- | -------- | ------- |
| 1        | MPI_Allreduce               | 54.2%    | 54.2%   |
| 2        | MPI_Finalize                | 25.9%    | 25.9%   |
| 3        | MPI_Bcast                   | 4.4%     | 4.4%    |
| 4        | \_\_GI\_\_IO_file_fopen     | 3.1%     |         |
| 5        | CompressData                | 2.4%     |         |
| 6        | CheckExpandedModels         | 1.7%     |         |
| 7        | IsIn [inlined]              | 1.4%     |         |
| 8        | ParseCommand                | 0.7%     | 54.2%   |
| 9        | strlen                      | 0.7%     |         |
| 10       | \_\_GI\_\_IO_file_underflow | 0.6%     |         |

## Test Case 4

> mb primates.nex

[ReFrame Benchmark 1](#)

```
../bin/reframe -c benchmark.py -r --performance-report
```

### Validation

Details of the validation for `Test Case 1`.


### ReFrame Output

```
==============================================================================
PERFORMANCE REPORT
------------------------------------------------------------------------------
     **** 
------------------------------------------------------------------------------
```

### On-node Compiler Comparison

Performance comparison of two compilers.

| Cores | Compiler 1 | Compiler 2 |
| ----- | ---------- | ---------- |
|       |            |            |


### Serial Hot-spot Profile

List of top-10 functions / code locations from a serial profile.

Use the GCC compiler.

Profiling command used:

```
map --profile srun -N 1 -n 1 mb primates.nex
```

| Position | Routine                                                      | Time (%) |
| -------- | ------------------------------------------------------------ | -------- |
| 1        | pthread_cond_signal                                          | 62.8%    |
| 2        | __log_finite                                                 | 11.2%    |
| 3        | beagle::cpu::BeagleCPU4StateImpl<float, 1, 0>::calcEdgeLogLikelihoods(int, int, int, int, int, int, double*) | 7.6%     |
| 4        | Move_ParsSPR                                                 | 2.6%     |
| 5        | TreeLikelihood_Beagle                                        | 2.1%     |
| 6        | beagle::cpu::EigenDecompositionCube<float, 1>::updateTransitionMatrices(int, int const*, int const*, int const*, double const*, double const*, float**, int) | 1.9%     |
| 7        | log                                                          | 1.2%     |
| 8        | GetFitchPartials                                             | 1.2%     |
| 9        | __exp_finite                                                 | 1.1%     |
| 10       | GetParsFP                                                    | 0.9%     |

### Full Node Hot-spot Profile

List of top-10 functions / code locations from a full node profile.

Use GCC compiler.

Profiling command used:

```
map --profile srun -N 1 -n 64 mb primates.nex
```

| Position | Routine                                                      | Time (%) | MPI (%) |
| -------- | ------------------------------------------------------------ | -------- | ------- |
| 1        | MPI_Allreduce                                                | 86.8%    | 86.8%   |
| 2        | pthread_cond_signal                                          | 6.6%     |         |
| 3        | __log_finite                                                 | 1.4%     |         |
| 4        | MPI_Waitall                                                  | 1.0%     | 1.0%    |
| 5        | beagle::cpu::BeagleCPU4StateImpl<float, 1, 0>::calcEdgeLogLikelihoods(int, int, int, int, int, int, double*) | 0.9%     |         |
| 6        | MPI_Barrier                                                  | 0.7%     | 0.7%    |
| 7        | Move_ParsSPR                                                 | 0.3%     |         |
| 8        | TreeLikelihood_Beagle                                        | 0.3%     |         |
| 9        | MPI_Send                                                     | 0.2%     | 0.2%    |
| 10       | beagle::cpu::EigenDecompositionCube<float, 1>::updateTransitionMatrices(int, int const*, int const*, int const*, double const*, double const*, float**, int) | 0.2%     |         |

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