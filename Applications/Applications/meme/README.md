# meme

**Description:** The MEME Suite allows the biologist to discover novel motifs in collections of unaligned nucleotide or protein sequences, and to perform a wide variety of other motif-based analyses.

**URL:** http://meme-suite.org

**Team:** TeamEPCC

## Compilation

### Modifications

  - `meme` has to be patched for `arm`
    - https://github.com/spack/spack/pull/24883/files#diff-765aeff1784028c4b0d57514f10e8ddf9357fb3153f93b6823e4f9c9027c1620
    - We'll try to get this included upstream.
  - `spack meme` has to be patched for `arm` and `nvhpc`
    - https://github.com/spack/spack/pull/24883
  - `spack libxslt` has to be patched for `nvhpc`
    - https://github.com/spack/spack/pull/24873

These patches are included below.

### Building meme

  - Our `packages.yaml`

```
$ cat ~/.spack/packages.yaml
packages:
  libfabric:
    buildable: false
    externals:
    - spec: libfabric@1.11.1-aws
      prefix: /opt/amazon/efa/
  slurm:
    buildable: false
    externals:
    - spec: slurm@20-02-4-1
      prefix: /opt/slurm/
  openmpi:
    variants: +pmi fabrics=ofi schedulers=slurm
    version:
       - 4.1.0
  perl:
    version:
       - 5.32.1
  python:
    externals:
    - spec: python@2.7.18+bz2+ctypes+dbm+lzma+nis+pyexpat+readline+sqlite3+ssl~tix~tkinter+uuid+zlib
      prefix: /usr
    - spec: python@3.7.10+bz2+ctypes+dbm+lzma+nis+pyexpat+readline+sqlite3+ssl~tix~tkinter+uuid+zlib
      prefix: /usr
```

### Arm

  - By default `meme` does not build due to the way some inline functions are declared, so we patched it as below (probably will try to get this included upstream).

```
--- a/src/mtwist.h	2021-07-14 12:18:25.848290454 +0000
+++ b/src/mtwist.h	2021-07-14 12:37:35.581368981 +0000
@@ -285,6 +285,7 @@
   prototypes using the ifdef.
 */
 #ifndef __APPLE__
+#ifndef __ARM_LINUX_COMPILER__
 extern uint32_t		mts_lrand(mt_state* state);
 					/* Generate 32-bit value, any gen. */
 #ifdef UINT64_MAX
@@ -310,6 +311,7 @@
 					/* Generate floating value */
 					/* Slower, with 64-bit precision */
 #endif
+#endif

 /*
  * Tempering parameters.  These are perhaps the most magic of all the magic
@@ -381,10 +383,14 @@
 #ifdef __cplusplus
 #define MT_EXTERN			/* C++ doesn't need static */
 #else /* __cplusplus */
-#ifndef __APPLE__
-#define MT_EXTERN	extern		/* C (at least gcc) needs extern */
-#else
+#ifdef __APPLE__
 #define MT_EXTERN	static 		/* The apple compiler freaks out if the definitions are not static */
+#else /* __APPLE__ */
+#ifdef __ARM_LINUX_COMPILER__
+#define MT_EXTERN	static 		/* The Arm compiler complains if the definitions are not static */
+#else /* __ARM_LINUX_COMPILER__ */
+#define MT_EXTERN	extern		/* C (at least gcc) needs extern */
+#endif /* __ARM_LINUX_COMPILER__ */
 #endif /* __APPLE__ */
 #endif /* __cplusplus */
 #endif /* MT_EXTERN */
```

  - Here's the patch for `spack`'s `meme` package, including the changes required to compile with `nvhpc` as well (see below).

```
diff --git a/var/spack/repos/builtin/packages/meme/package.py b/var/spack/repos/builtin/packages/meme/package.py
index 78e21ca595..f61b014d07 100644
--- a/var/spack/repos/builtin/packages/meme/package.py
+++ b/var/spack/repos/builtin/packages/meme/package.py
@@ -31,6 +31,10 @@ class Meme(AutotoolsPackage):
     depends_on('mpi', when='+mpi')
     depends_on('imagemagick', type=('build', 'run'), when='+image-magick')
     depends_on('perl-xml-parser', type=('build', 'run'))
+    depends_on('libxml2', type=('build', 'run'))
+    depends_on('libxslt', type=('build', 'run'))
+
+    patch('arm.patch', when='%arm')

     def url_for_version(self, version):
         url = 'http://meme-suite.org/meme-software/{0}/meme{1}{2}.tar.gz'
@@ -40,7 +44,14 @@ def url_for_version(self, version):
     def configure_args(self):
         spec = self.spec
         # have meme build its own versions of libxml2/libxslt, see #6736
-        args = ['--enable-build-libxml2', '--enable-build-libxslt']
+        #args = ['--enable-build-libxml2', '--enable-build-libxslt']
+        args = []
         if '~mpi' in spec:
             args += ['--enable-serial']
         return args
+
+    def patch(self):
+        # Remove flags not recognized by the NVIDIA compiler
+        if self.spec.satisfies('%nvhpc'):
+            filter_file('-fno-common', '', 'configure')
+            filter_file('-Wno-unused', '', 'configure')
```

```
$ spack install meme%arm
```

```
$ spack spec -Il meme%arm
Input spec
--------------------------------
 -   meme%arm

Concretized
--------------------------------
==> Warning: arm@21.0.0.879 cannot build optimized binaries for "graviton2". Using best target possible: "aarch64"
[+]  csigtg7  meme@5.3.0%arm@21.0.0.879~image-magick+mpi patches=5007c0d69900e6bfcb06fce5385670ab153f01de1aea9f62220c20e0497a2ba2 arch=linux-amzn2-aarch64
[+]  xc6udaz      ^libgcrypt@1.9.3%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  45e7cf6          ^libgpg-error@1.42%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  r5sadrn              ^gawk@5.1.0%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  rl3qj47                  ^gettext@0.21%arm@21.0.0.879+bzip2+curses+git~libunistring+libxml2+tar+xz arch=linux-amzn2-aarch64
[+]  z4ybgri                      ^bzip2@1.0.8%arm@21.0.0.879~debug~pic+shared arch=linux-amzn2-aarch64
[+]  adtc6yc                          ^diffutils@3.7%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  7vnthzn                              ^libiconv@1.16%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  dypqz2i                      ^libxml2@2.9.10%arm@21.0.0.879~python arch=linux-amzn2-aarch64
[+]  zpuzm23                          ^pkgconf@1.7.4%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  zqsab4f                          ^xz@5.2.5%arm@21.0.0.879~pic libs=shared,static arch=linux-amzn2-aarch64
[+]  puuxvg2                          ^zlib@1.2.11%arm@21.0.0.879+optimize+pic+shared arch=linux-amzn2-aarch64
[+]  uhtqtlb                      ^ncurses@6.2%arm@21.0.0.879~symlinks+termlib abi=none arch=linux-amzn2-aarch64
[+]  fohku26                      ^tar@1.34%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  y7o4xce                  ^gmp@6.2.1%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  par2wrm                      ^autoconf@2.69%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  lnai6aq                          ^m4@1.4.19%arm@21.0.0.879+sigsegv arch=linux-amzn2-aarch64
[+]  6jhzlul                              ^libsigsegv@2.13%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  vv6txro                          ^perl@5.32.1%arm@21.0.0.879+cpanm+shared+threads arch=linux-amzn2-aarch64
[+]  33wiajj                              ^berkeley-db@18.1.40%arm@21.0.0.879+cxx~docs+stl patches=b231fcc4d5cff05e5c3a4814f6a5af0e9a966428dc2176540d2c05aff41de522 arch=linux-amzn2-aarch64
[+]  645q4qj                              ^gdbm@1.19%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  3haw5gt                                  ^readline@8.1%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  edezkz3                      ^automake@1.16.3%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  e4ssqx6                      ^libtool@2.4.6%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  s55efue                  ^mpfr@4.1.0%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  36hcfzw                      ^autoconf-archive@2019.01.06%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  wqpjcrw                      ^texinfo@6.5%arm@21.0.0.879 patches=12f6edb0c6b270b8c8dba2ce17998c580db01182d871ee32b7b6e4129bd1d23a,1732115f651cff98989cb0215d8f64da5e0f7911ebf0c13b064920f088f2ffe1 arch=linux-amzn2-aarch64
[+]  jaizlxa      ^libxslt@1.1.33%arm@21.0.0.879+crypto~python arch=linux-amzn2-aarch64
[+]  lmaoy5t      ^openmpi@4.1.0%arm@21.0.0.879~atomics~cuda~cxx~cxx_exceptions+gpfs~internal-hwloc~java~legacylaunchers~lustre~memchecker+pmi~singularity~sqlite3+static~thread_multiple+vt+wrapper-rpath fabrics=ofi patches=60ce20bc14d98c572ef7883b9fcd254c3f232c2f3a13377480f96466169ac4c8 schedulers=slurm arch=linux-amzn2-aarch64
[+]  xl6anaa          ^hwloc@2.5.0%arm@21.0.0.879~cairo~cuda~gl~libudev+libxml2~netloc~nvml+pci+shared arch=linux-amzn2-aarch64
[+]  jueqz7p              ^libpciaccess@0.16%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  uwcxkin                  ^util-macros@1.19.3%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  gonqskn          ^libevent@2.1.12%arm@21.0.0.879+openssl arch=linux-amzn2-aarch64
[+]  vc3waha              ^openssl@1.1.1k%arm@21.0.0.879~docs+systemcerts arch=linux-amzn2-aarch64
[+]  qdn27nh          ^libfabric@1.11.1-aws%arm@21.0.0.879~debug~kdreg fabrics=sockets,tcp,udp arch=linux-amzn2-aarch64
[+]  mv2g7r5          ^numactl@2.0.14%arm@21.0.0.879 patches=4e1d78cbbb85de625bad28705e748856033eaafab92a66dffd383a3d7e00cc94,62fc8a8bf7665a60e8f4c93ebbd535647cebf74198f7afafec4c085a8825c006 arch=linux-amzn2-aarch64
[+]  6vvthuo          ^openssh@8.5p1%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  xe4evc4              ^libedit@3.1-20210216%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  x5xehti          ^slurm@20-02-4-1%arm@21.0.0.879~gtk~hdf5~hwloc~mariadb~pmix+readline~restd sysconfdir=PREFIX/etc arch=linux-amzn2-aarch64
[+]  abuse3a      ^perl-xml-parser@2.44%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  oyfuwk3          ^expat@2.4.1%arm@21.0.0.879+libbsd arch=linux-amzn2-aarch64
[+]  5q4lmyg              ^libbsd@0.11.3%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  srfepw2                  ^libmd@1.0.3%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  yigrrto          ^perl-libwww-perl@6.33%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  miszmcn              ^perl-encode-locale@1.05%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  qppjxlc              ^perl-file-listing@6.04%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  gnnb256                  ^perl-http-date@6.02%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  pkjgw5v              ^perl-html-parser@3.72%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  plc6lno                  ^perl-html-tagset@3.20%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  dwuwymu              ^perl-http-cookies@6.04%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  tjhb3pi                  ^perl-http-message@6.13%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  fbhtyzq                      ^perl-io-html@1.001%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  2p4t5hi                      ^perl-lwp-mediatypes@6.02%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  63xetxb                      ^perl-try-tiny@0.28%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  ardflxy                      ^perl-uri@1.72%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  hlpexym                          ^perl-test-needs@0.002005%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  zrmw65n              ^perl-http-daemon@6.01%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  d6j4vei                  ^perl-module-build-tiny@0.039%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  h5t34a4                      ^perl-extutils-config@0.008%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  nmupwpi                      ^perl-extutils-helpers@0.026%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  e7eerio                      ^perl-extutils-installpaths@0.012%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  ec7ahmp                      ^perl-module-build@0.4224%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  f7wxi23              ^perl-http-negotiate@6.01%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  gzm6crb              ^perl-net-http@6.17%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  kwobb4g              ^perl-www-robotrules@6.02%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  lijfbsl      ^perl-xml-simple@2.24%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  ck4dsab      ^python@3.7.10%arm@21.0.0.879+bz2+ctypes+dbm~debug+libxml2+lzma+nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tix~tkinter~ucs4+uuid+zlib patches=0d98e93189bc278fbc37a50ed7f183bd8aaf249a8e1670a465f0db6bb4f8cf87 arch=linux-amzn2-aarch64
```

### GCC

  - No major errors were detected when building with `gcc`.


```
$ spack install meme%gcc
```

```
$ spack spec -Il meme%gcc
Input spec
--------------------------------
 -   meme%gcc

Concretized
--------------------------------
[+]  xzjirlu  meme@5.3.0%gcc@10.3.0~image-magick+mpi arch=linux-amzn2-graviton2
[+]  equosbj      ^libgcrypt@1.9.3%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  hjnbovy          ^libgpg-error@1.42%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  wbcp5ow              ^gawk@5.1.0%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  fqlpcsl                  ^gettext@0.21%gcc@10.3.0+bzip2+curses+git~libunistring+libxml2+tar+xz arch=linux-amzn2-graviton2
[+]  rqrpmap                      ^bzip2@1.0.8%gcc@10.3.0~debug~pic+shared arch=linux-amzn2-graviton2
[+]  2w7bert                          ^diffutils@3.7%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  y5ei3cm                              ^libiconv@1.16%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  iyhm3wi                      ^libxml2@2.9.10%gcc@10.3.0~python arch=linux-amzn2-graviton2
[+]  s4pw7zm                          ^pkgconf@1.7.4%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  ye3kcvv                          ^xz@5.2.5%gcc@10.3.0~pic libs=shared,static arch=linux-amzn2-graviton2
[+]  qepjcvj                          ^zlib@1.2.11%gcc@10.3.0+optimize+pic+shared arch=linux-amzn2-graviton2
[+]  iwzirqc                      ^ncurses@6.2%gcc@10.3.0~symlinks+termlib abi=none arch=linux-amzn2-graviton2
[+]  v6cutkh                      ^tar@1.34%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  rego5fd                  ^gmp@6.2.1%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  djnylog                      ^autoconf@2.69%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  3mz7xyt                          ^m4@1.4.19%gcc@10.3.0+sigsegv arch=linux-amzn2-graviton2
[+]  ltbv6bk                              ^libsigsegv@2.13%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  4m7exgb                          ^perl@5.32.1%gcc@10.3.0+cpanm+shared+threads arch=linux-amzn2-graviton2
[+]  y42m6yr                              ^berkeley-db@18.1.40%gcc@10.3.0+cxx~docs+stl patches=b231fcc4d5cff05e5c3a4814f6a5af0e9a966428dc2176540d2c05aff41de522 arch=linux-amzn2-graviton2
[+]  wjwqncx                              ^gdbm@1.19%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  3zy7kxk                                  ^readline@8.1%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  xb2w5nc                      ^automake@1.16.3%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  z2uysov                      ^libtool@2.4.6%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  4jwrra6                  ^mpfr@4.1.0%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  yutdrfy                      ^autoconf-archive@2019.01.06%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  egfqbtl                      ^texinfo@6.5%gcc@10.3.0 patches=12f6edb0c6b270b8c8dba2ce17998c580db01182d871ee32b7b6e4129bd1d23a,1732115f651cff98989cb0215d8f64da5e0f7911ebf0c13b064920f088f2ffe1 arch=linux-amzn2-graviton2
[+]  vapzblj      ^libxslt@1.1.33%gcc@10.3.0+crypto~python arch=linux-amzn2-graviton2
[+]  zvamksn      ^openmpi@4.1.0%gcc@10.3.0~atomics~cuda~cxx~cxx_exceptions+gpfs~internal-hwloc~java~legacylaunchers~lustre~memchecker+pmi~singularity~sqlite3+static~thread_multiple+vt+wrapper-rpath fabrics=ofi patches=60ce20bc14d98c572ef7883b9fcd254c3f232c2f3a13377480f96466169ac4c8 schedulers=slurm arch=linux-amzn2-graviton2
[+]  cukmqbg          ^hwloc@2.5.0%gcc@10.3.0~cairo~cuda~gl~libudev+libxml2~netloc~nvml+pci+shared arch=linux-amzn2-graviton2
[+]  asgtk6a              ^libpciaccess@0.16%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  4xr3hhh                  ^util-macros@1.19.3%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  tadxrfp          ^libevent@2.1.12%gcc@10.3.0+openssl arch=linux-amzn2-graviton2
[+]  5i3lgfb              ^openssl@1.1.1k%gcc@10.3.0~docs+systemcerts arch=linux-amzn2-graviton2
[+]  72f5gvk          ^libfabric@1.11.1-aws%gcc@10.3.0~debug~kdreg fabrics=sockets,tcp,udp arch=linux-amzn2-graviton2
[+]  mhav5gn          ^numactl@2.0.14%gcc@10.3.0 patches=4e1d78cbbb85de625bad28705e748856033eaafab92a66dffd383a3d7e00cc94,62fc8a8bf7665a60e8f4c93ebbd535647cebf74198f7afafec4c085a8825c006 arch=linux-amzn2-graviton2
[+]  wturp6c          ^openssh@8.5p1%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  ivotdt7              ^libedit@3.1-20210216%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  wqpuvmh          ^slurm@20-02-4-1%gcc@10.3.0~gtk~hdf5~hwloc~mariadb~pmix+readline~restd sysconfdir=PREFIX/etc arch=linux-amzn2-graviton2
[+]  lqb6dym      ^perl-xml-parser@2.44%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  ychdz7l          ^expat@2.4.1%gcc@10.3.0+libbsd arch=linux-amzn2-graviton2
[+]  ourxkez              ^libbsd@0.11.3%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  nssrqfc                  ^libmd@1.0.3%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  f5v6774          ^perl-libwww-perl@6.33%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  7bktzwy              ^perl-encode-locale@1.05%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  ng42qsj              ^perl-file-listing@6.04%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  iel7364                  ^perl-http-date@6.02%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  6c5zqpy              ^perl-html-parser@3.72%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  5356pec                  ^perl-html-tagset@3.20%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  rn72dje              ^perl-http-cookies@6.04%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  lzhpg5e                  ^perl-http-message@6.13%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  cw4yunq                      ^perl-io-html@1.001%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  uwpw4jb                      ^perl-lwp-mediatypes@6.02%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  lbi5zlw                      ^perl-try-tiny@0.28%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  mwjmhxr                      ^perl-uri@1.72%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  ilcgd4p                          ^perl-test-needs@0.002005%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  kqe5fq4              ^perl-http-daemon@6.01%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  n2pgdkj                  ^perl-module-build-tiny@0.039%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  2nu5ktn                      ^perl-extutils-config@0.008%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  oaj7c6l                      ^perl-extutils-helpers@0.026%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  3bmurgv                      ^perl-extutils-installpaths@0.012%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  l3vxnln                      ^perl-module-build@0.4224%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  memap53              ^perl-http-negotiate@6.01%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  jp2quri              ^perl-net-http@6.17%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  ojglnnz              ^perl-www-robotrules@6.02%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  fkruvr4      ^perl-xml-simple@2.24%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  gcliuat      ^python@3.7.10%gcc@10.3.0+bz2+ctypes+dbm~debug+libxml2+lzma+nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tix~tkinter~ucs4+uuid+zlib patches=0d98e93189bc278fbc37a50ed7f183bd8aaf249a8e1670a465f0db6bb4f8cf87 arch=linux-amzn2-graviton2
```

### NVHPC

  - `nvhpc` conflicts with `python`.
    - Can be fixed by using the external `python`.
  - Various dependencies of `libgcrypt` do not compile with `nvhpc`.
    - As a work around, we build them with `gcc`.
  - `libbsd-0.11.3` doesn't build, initially because the current patch included in the package does not apply, but other errors emerge after fixing the patch.
    - Using `libbsd@0.10.0` works.

```
$ spack install meme%nvhpc ^libgcrypt%gcc ^libbsd@0.10.0
```

```
$ spack spec -Il meme%nvhpc ^libgcrypt%gcc ^libbsd@0.10.0
Input spec
--------------------------------
 -   meme%nvhpc
 -       ^libbsd@0.10.0
 -       ^libgcrypt%gcc

Concretized
--------------------------------
[+]  fifpy6p  meme@5.3.0%nvhpc@21.2~image-magick+mpi arch=linux-amzn2-graviton2
[+]  equosbj      ^libgcrypt@1.9.3%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  hjnbovy          ^libgpg-error@1.42%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  23u7l5k              ^gawk@5.1.0%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  klmvhil                  ^gettext@0.21%gcc@10.3.0+bzip2+curses+git~libunistring+libxml2+tar+xz arch=linux-amzn2-graviton2
[+]  wsi7g3j                      ^bzip2@1.0.8%nvhpc@21.2~debug~pic+shared arch=linux-amzn2-graviton2
[+]  s4mb5no                          ^diffutils@3.7%nvhpc@21.2 patches=6e42dc243f17aab29fd167f060f5bc1f08813e03368eb301b43c95d4b1386681 arch=linux-amzn2-graviton2
[+]  r7mmkdp                              ^libiconv@1.16%nvhpc@21.2 arch=linux-amzn2-graviton2
[+]  wo4l72s                      ^libxml2@2.9.10%nvhpc@21.2~python patches=05ff238cf435825ef835c7ae39376b52dc83d8caf19e962f0766c841386a305a,10a88ad47f9797cf7cf2d7d07241f665a3b6d1f31fa026728c8c2ae93e1664e9 arch=linux-amzn2-graviton2
[+]  vtiml6g                          ^pkgconf@1.7.4%nvhpc@21.2 arch=linux-amzn2-graviton2
[+]  br733tn                          ^xz@5.2.5%nvhpc@21.2~pic libs=shared,static arch=linux-amzn2-graviton2
[+]  4js6ect                          ^zlib@1.2.11%nvhpc@21.2+optimize+pic+shared arch=linux-amzn2-graviton2
[+]  asgm7mt                      ^ncurses@6.2%nvhpc@21.2~symlinks+termlib abi=none arch=linux-amzn2-graviton2
[+]  ugpacic                      ^tar@1.34%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  rego5fd                  ^gmp@6.2.1%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  mzhxqyz                      ^autoconf@2.69%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  3mz7xyt                          ^m4@1.4.19%gcc@10.3.0+sigsegv arch=linux-amzn2-graviton2
[+]  ltbv6bk                              ^libsigsegv@2.13%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  gn4fgp5                          ^perl@5.32.1%nvhpc@21.2+cpanm+shared+threads patches=21cf6a73cec16760f8de2e8895ace1299aff2d8e92dc581cd18f1d95a4503048 arch=linux-amzn2-graviton2
[+]  5uyf3k4                              ^berkeley-db@18.1.40%nvhpc@21.2+cxx~docs+stl patches=b231fcc4d5cff05e5c3a4814f6a5af0e9a966428dc2176540d2c05aff41de522 arch=linux-amzn2-graviton2
[+]  m2wdbeo                              ^gdbm@1.19%nvhpc@21.2 arch=linux-amzn2-graviton2
[+]  zori3wf                                  ^readline@8.1%nvhpc@21.2 arch=linux-amzn2-graviton2
[+]  q5y3rsf                      ^automake@1.16.3%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  z2uysov                      ^libtool@2.4.6%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  4jwrra6                  ^mpfr@4.1.0%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  yutdrfy                      ^autoconf-archive@2019.01.06%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  njydrqj                      ^texinfo@6.5%gcc@10.3.0 patches=12f6edb0c6b270b8c8dba2ce17998c580db01182d871ee32b7b6e4129bd1d23a,1732115f651cff98989cb0215d8f64da5e0f7911ebf0c13b064920f088f2ffe1 arch=linux-amzn2-graviton2
[+]  r3qewtm      ^libxslt@1.1.33%nvhpc@21.2+crypto~python arch=linux-amzn2-graviton2
[+]  krxyvbc      ^openmpi@4.1.0%nvhpc@21.2~atomics~cuda~cxx~cxx_exceptions+gpfs~internal-hwloc~java~legacylaunchers~lustre~memchecker+pmi~singularity~sqlite3+static~thread_multiple+vt+wrapper-rpath fabrics=ofi patches=60ce20bc14d98c572ef7883b9fcd254c3f232c2f3a13377480f96466169ac4c8,fba0d3a784a9723338722b48024a22bb32f6a951db841a4e9f08930a93f41d7a schedulers=slurm arch=linux-amzn2-graviton2
[+]  jroqews          ^hwloc@2.5.0%nvhpc@21.2~cairo~cuda~gl~libudev+libxml2~netloc~nvml+pci+shared arch=linux-amzn2-graviton2
[+]  e4m4ued              ^libpciaccess@0.16%nvhpc@21.2 patches=6e08dc445ece06e9e8b1344397f2d3f169005703ddc0f2ae24f366cde78c7377 arch=linux-amzn2-graviton2
[+]  4imdwuy                  ^util-macros@1.19.3%nvhpc@21.2 arch=linux-amzn2-graviton2
[+]  uttaumr          ^libevent@2.1.12%nvhpc@21.2+openssl arch=linux-amzn2-graviton2
[+]  j2qhi7h              ^openssl@1.1.1k%nvhpc@21.2~docs+systemcerts arch=linux-amzn2-graviton2
[+]  xl6zavq          ^libfabric@1.11.1-aws%nvhpc@21.2~debug~kdreg fabrics=sockets,tcp,udp arch=linux-amzn2-graviton2
[+]  5yq4tpw          ^numactl@2.0.14%nvhpc@21.2 patches=4e1d78cbbb85de625bad28705e748856033eaafab92a66dffd383a3d7e00cc94,62fc8a8bf7665a60e8f4c93ebbd535647cebf74198f7afafec4c085a8825c006 arch=linux-amzn2-graviton2
[+]  cl3ohqo          ^openssh@8.5p1%nvhpc@21.2 arch=linux-amzn2-graviton2
[+]  yvqpq74              ^libedit@3.1-20210216%nvhpc@21.2 arch=linux-amzn2-graviton2
[+]  zehhooy          ^slurm@20-02-4-1%nvhpc@21.2~gtk~hdf5~hwloc~mariadb~pmix+readline~restd sysconfdir=PREFIX/etc arch=linux-amzn2-graviton2
[+]  5qlgjmf      ^perl-xml-parser@2.44%nvhpc@21.2 arch=linux-amzn2-graviton2
[+]  ucobzs7          ^expat@2.4.1%nvhpc@21.2+libbsd arch=linux-amzn2-graviton2
[+]  kevfo4m              ^libbsd@0.10.0%nvhpc@21.2 patches=bd4ed3549fde8870ac82cdc5778d91f907131587d31eedcd023dd13594dc39ad arch=linux-amzn2-graviton2
[+]  y2t47lv          ^perl-libwww-perl@6.33%nvhpc@21.2 arch=linux-amzn2-graviton2
[+]  bzw6yvx              ^perl-encode-locale@1.05%nvhpc@21.2 arch=linux-amzn2-graviton2
[+]  liqnsqw              ^perl-file-listing@6.04%nvhpc@21.2 arch=linux-amzn2-graviton2
[+]  7kcrous                  ^perl-http-date@6.02%nvhpc@21.2 arch=linux-amzn2-graviton2
[+]  wq24kah              ^perl-html-parser@3.72%nvhpc@21.2 arch=linux-amzn2-graviton2
[+]  5yqmhos                  ^perl-html-tagset@3.20%nvhpc@21.2 arch=linux-amzn2-graviton2
[+]  wbgtlco              ^perl-http-cookies@6.04%nvhpc@21.2 arch=linux-amzn2-graviton2
[+]  nruhydy                  ^perl-http-message@6.13%nvhpc@21.2 arch=linux-amzn2-graviton2
[+]  hnhjgh2                      ^perl-io-html@1.001%nvhpc@21.2 arch=linux-amzn2-graviton2
[+]  wsgcrtf                      ^perl-lwp-mediatypes@6.02%nvhpc@21.2 arch=linux-amzn2-graviton2
[+]  olvr6os                      ^perl-try-tiny@0.28%nvhpc@21.2 arch=linux-amzn2-graviton2
[+]  hs4cjs3                      ^perl-uri@1.72%nvhpc@21.2 arch=linux-amzn2-graviton2
[+]  lwbdujw                          ^perl-test-needs@0.002005%nvhpc@21.2 arch=linux-amzn2-graviton2
[+]  6iouolg              ^perl-http-daemon@6.01%nvhpc@21.2 arch=linux-amzn2-graviton2
[+]  mevsuod                  ^perl-module-build-tiny@0.039%nvhpc@21.2 arch=linux-amzn2-graviton2
[+]  b2izmfn                      ^perl-extutils-config@0.008%nvhpc@21.2 arch=linux-amzn2-graviton2
[+]  yevyfn2                      ^perl-extutils-helpers@0.026%nvhpc@21.2 arch=linux-amzn2-graviton2
[+]  nnkzejg                      ^perl-extutils-installpaths@0.012%nvhpc@21.2 arch=linux-amzn2-graviton2
[+]  uz3v4ep                      ^perl-module-build@0.4224%nvhpc@21.2 arch=linux-amzn2-graviton2
[+]  s3lbu5y              ^perl-http-negotiate@6.01%nvhpc@21.2 arch=linux-amzn2-graviton2
[+]  7nwrfth              ^perl-net-http@6.17%nvhpc@21.2 arch=linux-amzn2-graviton2
[+]  5cr5u6d              ^perl-www-robotrules@6.02%nvhpc@21.2 arch=linux-amzn2-graviton2
[+]  na6lwdz      ^perl-xml-simple@2.24%nvhpc@21.2 arch=linux-amzn2-graviton2
[+]  6pt5n5r      ^python@3.7.10%nvhpc@21.2+bz2+ctypes+dbm~debug+libxml2+lzma+nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tix~tkinter~ucs4+uuid+zlib patches=0d98e93189bc278fbc37a50ed7f183bd8aaf249a8e1670a465f0db6bb4f8cf87 arch=linux-amzn2-graviton2
```

  - The default `spack` `meme` package generates `xml` link errors.
    - Installing `libxml2` and `libxslt` as `spack` packages and building `meme` against them solves this problem (requires changes to `spack`'s `meme` package).
  - Some of the compilation flags used by `meme` and `libxmlst` are not supported by `nvhpc`, but they can be easily patched out.

```
diff --git a/var/spack/repos/builtin/packages/libxslt/package.py b/var/spack/repos/builtin/packages/libxslt/package.py
index c42240f303..cecd64d477 100644
--- a/var/spack/repos/builtin/packages/libxslt/package.py
+++ b/var/spack/repos/builtin/packages/libxslt/package.py
@@ -57,3 +57,8 @@ def import_module_test(self):
         if '+python' in self.spec:
             with working_dir('spack-test', create=True):
                 python('-c', 'import libxslt')
+
+    def patch(self):
+        # Remove flags not recognized by the NVIDIA compiler
+        if self.spec.satisfies('%nvhpc'):
+            filter_file('-Wmissing-format-attribute', '', 'configure')
```

```
diff --git a/var/spack/repos/builtin/packages/meme/package.py b/var/spack/repos/builtin/packages/meme/package.py
# See Arm's build section for the changes required to this file.
```

## Test Case 1

[ReFrame Test 1](meme-lex0-small.py)

Small test from [MEME](https://meme-suite.org/meme/doc/examples/meme_example_output_files/meme.html) that checkes if the output generated by the local build matches the reference output provided. We use this test to evaluate the correctness of the installation, not to measure performance.

```
reframe -c meme-lex0-small.py -r
```

### Validation

The output of the command
```
meme lex0.fna -oc lex0.fna.d -dna -mod zoops -nmotifs 3 -revcomp
```
is matched against [the reference output from MEME](https://meme-suite.org/meme/doc/examples/meme_example_output_files/meme.txt). This comparison is performed after stripping the output from run/platform specific data, such as timing or hostname information.

### ReFrame Output

#### Arm

```
----------] waiting for spawned checks to finish
[       OK ] ( 1/30) meme_-lex0-small_meme_csigtg7_N_1_MPI_2_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 7.709s total: 7.730s]
[       OK ] ( 2/30) meme_-lex0-small_meme_csigtg7_N_1_MPI_1_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 8.670s total: 8.690s]
[       OK ] ( 3/30) meme_-lex0-small_meme_csigtg7_N_1_MPI_8_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 8.988s total: 9.008s]
[       OK ] ( 4/30) meme_-lex0-small_meme_csigtg7_N_1_MPI_32_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 8.900s total: 8.921s]
[       OK ] ( 5/30) meme_-lex0-small_meme_csigtg7_N_1_MPI_16_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 10.111s total: 10.131s]
[       OK ] ( 6/30) meme_-lex0-small_meme_csigtg7_N_1_MPI_4_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 11.420s total: 11.440s]
[       OK ] ( 7/30) meme_-lex0-small_meme_csigtg7_N_1_MPI_64_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 10.639s total: 10.660s]
[       OK ] ( 8/30) meme_-lex0-small_meme_csigtg7_N_2_MPI_128_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 12.273s total: 12.293s]
[       OK ] ( 9/30) meme_-lex0-small_meme_fifpy6p_N_8_MPI_512_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 16.798s total: 18.739s]
[       OK ] (10/30) meme_-lex0-small_meme_fifpy6p_N_1_MPI_64_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 19.708s total: 24.713s]
[       OK ] (11/30) meme_-lex0-small_meme_fifpy6p_N_2_MPI_128_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 20.934s total: 25.178s]
[       OK ] (12/30) meme_-lex0-small_meme_fifpy6p_N_1_MPI_32_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 20.097s total: 26.112s]
[       OK ] (13/30) meme_-lex0-small_meme_fifpy6p_N_4_MPI_256_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 23.825s total: 26.524s]
[       OK ] (14/30) meme_-lex0-small_meme_fifpy6p_N_1_MPI_16_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 22.953s total: 29.736s]
[       OK ] (15/30) meme_-lex0-small_meme_fifpy6p_N_1_MPI_8_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 22.934s total: 30.508s]
[       OK ] (16/30) meme_-lex0-small_meme_fifpy6p_N_1_MPI_4_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 21.577s total: 31.307s]
[       OK ] (17/30) meme_-lex0-small_meme_fifpy6p_N_1_MPI_2_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 16.944s total: 36.988s]
[       OK ] (18/30) meme_-lex0-small_meme_fifpy6p_N_1_MPI_1_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 12.556s total: 38.256s]
[       OK ] (19/30) meme_-lex0-small_meme_xzjirlu_N_8_MPI_512_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 21.296s total: 47.762s]
[       OK ] (20/30) meme_-lex0-small_meme_xzjirlu_N_1_MPI_32_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 22.054s total: 53.879s]
[       OK ] (21/30) meme_-lex0-small_meme_xzjirlu_N_1_MPI_64_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 23.280s total: 54.345s]
[       OK ] (22/30) meme_-lex0-small_meme_xzjirlu_N_2_MPI_128_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 26.504s total: 54.814s]
[       OK ] (23/30) meme_-lex0-small_meme_xzjirlu_N_4_MPI_256_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 28.785s total: 56.039s]
[       OK ] (24/30) meme_-lex0-small_meme_xzjirlu_N_1_MPI_16_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 25.740s total: 58.355s]
[       OK ] (25/30) meme_-lex0-small_meme_xzjirlu_N_1_MPI_8_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 20.733s total: 59.009s]
[       OK ] (26/30) meme_-lex0-small_meme_xzjirlu_N_1_MPI_4_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 20.381s total: 59.925s]
[       OK ] (27/30) meme_-lex0-small_meme_xzjirlu_N_1_MPI_2_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 12.311s total: 61.370s]
[       OK ] (28/30) meme_-lex0-small_meme_xzjirlu_N_1_MPI_1_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 9.337s total: 64.012s]
[       OK ] (29/30) meme_-lex0-small_meme_csigtg7_N_8_MPI_512_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 18.424s total: 73.884s]
[       OK ] (30/30) meme_-lex0-small_meme_csigtg7_N_4_MPI_256_OMP_1 on aws:c6gn using builtin [compile: 0.005s run: 26.543s total: 82.800s]
[----------] all spawned checks have finished

[  PASSED  ] Ran 30/30 test case(s) from 30 check(s) (0 failure(s), 0 skipped)
[==========] Finished on Fri Jul 16 16:28:11 2021 
```

#### Intel

```
[----------] waiting for spawned checks to finish
[       OK ] ( 1/18) meme_-lex0-small_meme_ylex6xs_N_1_MPI_1_OMP_1 on aws:c5n using builtin [compile: 0.006s run: 10.058s total: 10.079s]
[       OK ] ( 2/18) meme_-lex0-small_meme_ylex6xs_N_1_MPI_9_OMP_1 on aws:c5n using builtin [compile: 0.006s run: 10.536s total: 10.557s]
[       OK ] ( 3/18) meme_-lex0-small_meme_ylex6xs_N_1_MPI_3_OMP_1 on aws:c5n using builtin [compile: 0.005s run: 11.444s total: 11.465s]
[       OK ] ( 4/18) meme_-lex0-small_meme_ylex6xs_N_1_MPI_18_OMP_1 on aws:c5n using builtin [compile: 0.006s run: 13.744s total: 13.764s]
[       OK ] ( 5/18) meme_-lex0-small_meme_ylex6xs_N_1_MPI_36_OMP_1 on aws:c5n using builtin [compile: 0.005s run: 16.376s total: 16.395s]
[       OK ] ( 6/18) meme_-lex0-small_meme_ylex6xs_N_1_MPI_72_OMP_1 on aws:c5n using builtin [compile: 0.005s run: 16.694s total: 16.713s]
[       OK ] ( 7/18) meme_-lex0-small_meme_ylex6xs_N_2_MPI_144_OMP_1 on aws:c5n using builtin [compile: 0.004s run: 23.544s total: 23.563s]
[       OK ] ( 8/18) meme_-lex0-small_meme_ucxv6oz_N_1_MPI_72_OMP_1 on aws:c5n using builtin [compile: 0.006s run: 13.358s total: 24.686s]
[       OK ] ( 9/18) meme_-lex0-small_meme_ucxv6oz_N_2_MPI_144_OMP_1 on aws:c5n using builtin [compile: 0.006s run: 46.702s total: 54.964s]
[       OK ] (10/18) meme_-lex0-small_meme_ucxv6oz_N_1_MPI_36_OMP_1 on aws:c5n using builtin [compile: 0.006s run: 41.446s total: 55.864s]
[       OK ] (11/18) meme_-lex0-small_meme_ucxv6oz_N_1_MPI_3_OMP_1 on aws:c5n using builtin [compile: 0.007s run: 58.899s total: 84.183s]
[       OK ] (12/18) meme_-lex0-small_meme_ucxv6oz_N_1_MPI_18_OMP_1 on aws:c5n using builtin [compile: 0.006s run: 68.734s total: 83.917s]
[       OK ] (13/18) meme_-lex0-small_meme_ucxv6oz_N_1_MPI_9_OMP_1 on aws:c5n using builtin [compile: 0.007s run: 61.846s total: 84.347s]
[       OK ] (14/18) meme_-lex0-small_meme_ylex6xs_N_4_MPI_288_OMP_1 on aws:c5n using builtin [compile: 0.004s run: 103.813s total: 103.830s]
[       OK ] (15/18) meme_-lex0-small_meme_ucxv6oz_N_1_MPI_1_OMP_1 on aws:c5n using builtin [compile: 0.006s run: 58.300s total: 114.149s]
[       OK ] (16/18) meme_-lex0-small_meme_ucxv6oz_N_4_MPI_288_OMP_1 on aws:c5n using builtin [compile: 0.005s run: 107.752s total: 115.267s]
[       OK ] (17/18) meme_-lex0-small_meme_ucxv6oz_N_8_MPI_576_OMP_1 on aws:c5n using builtin [compile: 0.005s run: 130.548s total: 136.818s]
[       OK ] (18/18) meme_-lex0-small_meme_ylex6xs_N_8_MPI_576_OMP_1 on aws:c5n using builtin [compile: 0.006s run: 90.118s total: 146.735s]
[----------] all spawned checks have finished

[  PASSED  ] Ran 18/18 test case(s) from 18 check(s) (0 failure(s), 0 skipped)
[==========] Finished on Fri Jul 16 16:33:40 2021 
```

## Test Case 2

[ReFrame Test 2](meme-Klf1-large.py.py)

A performance-oriented test built by us [using a larger dataset from MEME](https://meme-suite.org/meme/doc/examples/example-datasets/Klf1.fna) [and sample arguments from a Bioinformatics performance question](https://www.biostars.org/p/65594/).

```
reframe -c meme-Klf1-large.py -r --performance-report
```

### Validation

The output of the command
```
meme Klf1.fna -oc Klf1.fa.meme -dna -text -nmotifs 16 -maxsize 100000000 -maxw 25
```
is matched against [reference output generated by us](outputs/Klf1.fna.txt). As
before, this comparison is performed after stripping the output from
run/platform specific data.

### ReFrame Output

#### Arm

```
[  PASSED  ] Ran 30/30 test case(s) from 30 check(s) (0 failure(s), 0 skipped)
[==========] Finished on Fri Jul 16 15:12:42 2021
==============================================================================
PERFORMANCE REPORT
------------------------------------------------------------------------------
meme_-Klf1-large_meme_csigtg7_N_1_MPI_1_OMP_1
- aws:c6gn
   - builtin
      * num_tasks: 1
      * Total Time: 1973.33 s
------------------------------------------------------------------------------
meme_-Klf1-large_meme_csigtg7_N_1_MPI_2_OMP_1
   - builtin
      * num_tasks: 2
      * Total Time: 1003.21 s
------------------------------------------------------------------------------
meme_-Klf1-large_meme_csigtg7_N_1_MPI_4_OMP_1
   - builtin
      * num_tasks: 4
      * Total Time: 498.16 s
------------------------------------------------------------------------------
meme_-Klf1-large_meme_csigtg7_N_1_MPI_8_OMP_1
   - builtin
      * num_tasks: 8
      * Total Time: 253.51 s
------------------------------------------------------------------------------
meme_-Klf1-large_meme_csigtg7_N_1_MPI_16_OMP_1
   - builtin
      * num_tasks: 16
      * Total Time: 133.31 s
------------------------------------------------------------------------------
meme_-Klf1-large_meme_csigtg7_N_1_MPI_32_OMP_1
   - builtin
      * num_tasks: 32
      * Total Time: 73.81 s
------------------------------------------------------------------------------
meme_-Klf1-large_meme_csigtg7_N_1_MPI_64_OMP_1
   - builtin
      * num_tasks: 64
      * Total Time: 44.47 s
------------------------------------------------------------------------------
meme_-Klf1-large_meme_csigtg7_N_2_MPI_128_OMP_1
- aws:c6gn
   - builtin
      * num_tasks: 128
      * Total Time: 33.54 s
------------------------------------------------------------------------------
meme_-Klf1-large_meme_csigtg7_N_4_MPI_256_OMP_1
   - builtin
      * num_tasks: 256
      * Total Time: 30.08 s
------------------------------------------------------------------------------
meme_-Klf1-large_meme_csigtg7_N_8_MPI_512_OMP_1
   - builtin
      * num_tasks: 512
      * Total Time: 29.42 s
------------------------------------------------------------------------------
meme_-Klf1-large_meme_xzjirlu_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Total Time: 1954.61 s
------------------------------------------------------------------------------
meme_-Klf1-large_meme_xzjirlu_N_1_MPI_2_OMP_1
   - builtin
      * num_tasks: 2
      * Total Time: 994.1 s
------------------------------------------------------------------------------
meme_-Klf1-large_meme_xzjirlu_N_1_MPI_4_OMP_1
   - builtin
      * num_tasks: 4
      * Total Time: 499.94 s
------------------------------------------------------------------------------
meme_-Klf1-large_meme_xzjirlu_N_1_MPI_8_OMP_1
   - builtin
      * num_tasks: 8
      * Total Time: 251.54 s
------------------------------------------------------------------------------
meme_-Klf1-large_meme_xzjirlu_N_1_MPI_16_OMP_1
   - builtin
      * num_tasks: 16
      * Total Time: 132.87 s
------------------------------------------------------------------------------
meme_-Klf1-large_meme_xzjirlu_N_1_MPI_32_OMP_1
   - builtin
      * num_tasks: 32
      * Total Time: 74.45 s
------------------------------------------------------------------------------
meme_-Klf1-large_meme_xzjirlu_N_1_MPI_64_OMP_1
   - builtin
      * num_tasks: 64
      * Total Time: 45.0 s
------------------------------------------------------------------------------
meme_-Klf1-large_meme_xzjirlu_N_2_MPI_128_OMP_1
   - builtin
      * num_tasks: 128
      * Total Time: 34.42 s
------------------------------------------------------------------------------
meme_-Klf1-large_meme_xzjirlu_N_4_MPI_256_OMP_1
   - builtin
      * num_tasks: 256
      * Total Time: 32.33 s
------------------------------------------------------------------------------
meme_-Klf1-large_meme_xzjirlu_N_8_MPI_512_OMP_1
   - builtin
      * num_tasks: 512
      * Total Time: 31.34 s
------------------------------------------------------------------------------
meme_-Klf1-large_meme_fifpy6p_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Total Time: 2216.7 s
------------------------------------------------------------------------------
meme_-Klf1-large_meme_fifpy6p_N_1_MPI_2_OMP_1
   - builtin
      * num_tasks: 2
      * Total Time: 1118.03 s
------------------------------------------------------------------------------
meme_-Klf1-large_meme_fifpy6p_N_1_MPI_4_OMP_1
   - builtin
      * num_tasks: 4
      * Total Time: 570.22 s
------------------------------------------------------------------------------
meme_-Klf1-large_meme_fifpy6p_N_1_MPI_8_OMP_1
   - builtin
      * num_tasks: 8
      * Total Time: 296.85 s
------------------------------------------------------------------------------
meme_-Klf1-large_meme_fifpy6p_N_1_MPI_16_OMP_1
   - builtin
      * num_tasks: 16
      * Total Time: 170.7 s
------------------------------------------------------------------------------
meme_-Klf1-large_meme_fifpy6p_N_1_MPI_32_OMP_1
   - builtin
      * num_tasks: 32
      * Total Time: 109.83 s
------------------------------------------------------------------------------
meme_-Klf1-large_meme_fifpy6p_N_1_MPI_64_OMP_1
   - builtin
      * num_tasks: 64
      * Total Time: 81.18 s
------------------------------------------------------------------------------
meme_-Klf1-large_meme_fifpy6p_N_2_MPI_128_OMP_1
   - builtin
      * num_tasks: 128
      * Total Time: 71.62 s
------------------------------------------------------------------------------
meme_-Klf1-large_meme_fifpy6p_N_4_MPI_256_OMP_1
   - builtin
      * num_tasks: 256
      * Total Time: 75.75 s
------------------------------------------------------------------------------
meme_-Klf1-large_meme_fifpy6p_N_8_MPI_512_OMP_1
   - builtin
      * num_tasks: 512
      * Total Time: 78.88 s
------------------------------------------------------------------------------
```

#### Intel

```
[  PASSED  ] Ran 18/18 test case(s) from 18 check(s) (0 failure(s), 0 skipped)
[==========] Finished on Fri Jul 16 15:12:29 2021
==============================================================================
PERFORMANCE REPORT
------------------------------------------------------------------------------
meme_-Klf1-large_meme_ylex6xs_N_1_MPI_1_OMP_1
- aws:c5n
   - builtin
      * num_tasks: 1
      * Total Time: 1416.1 s
------------------------------------------------------------------------------
meme_-Klf1-large_meme_ylex6xs_N_1_MPI_3_OMP_1
- aws:c5n
   - builtin
      * num_tasks: 3
      * Total Time: 484.2 s
------------------------------------------------------------------------------
meme_-Klf1-large_meme_ylex6xs_N_1_MPI_9_OMP_1
   - builtin
      * num_tasks: 9
      * Total Time: 169.09 s
------------------------------------------------------------------------------
meme_-Klf1-large_meme_ylex6xs_N_1_MPI_18_OMP_1
   - builtin
      * num_tasks: 18
      * Total Time: 91.34 s
------------------------------------------------------------------------------
meme_-Klf1-large_meme_ylex6xs_N_1_MPI_36_OMP_1
   - builtin
      * num_tasks: 36
      * Total Time: 54.62 s
------------------------------------------------------------------------------
meme_-Klf1-large_meme_ylex6xs_N_1_MPI_72_OMP_1
   - builtin
      * num_tasks: 72
      * Total Time: 57.42 s
------------------------------------------------------------------------------
meme_-Klf1-large_meme_ylex6xs_N_2_MPI_144_OMP_1
- aws:c5n
   - builtin
      * num_tasks: 144
      * Total Time: 43.35 s
------------------------------------------------------------------------------
meme_-Klf1-large_meme_ylex6xs_N_4_MPI_288_OMP_1
   - builtin
      * num_tasks: 288
      * Total Time: 40.12 s
------------------------------------------------------------------------------
meme_-Klf1-large_meme_ylex6xs_N_8_MPI_576_OMP_1
- aws:c5n
   - builtin
      * num_tasks: 576
      * Total Time: 37.12 s
------------------------------------------------------------------------------
meme_-Klf1-large_meme_ucxv6oz_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Total Time: 1705.14 s
------------------------------------------------------------------------------
meme_-Klf1-large_meme_ucxv6oz_N_1_MPI_3_OMP_1
   - builtin
      * num_tasks: 3
      * Total Time: 588.09 s
------------------------------------------------------------------------------
meme_-Klf1-large_meme_ucxv6oz_N_1_MPI_9_OMP_1
   - builtin
      * num_tasks: 9
      * Total Time: 204.78 s
------------------------------------------------------------------------------
meme_-Klf1-large_meme_ucxv6oz_N_1_MPI_18_OMP_1
   - builtin
      * num_tasks: 18
      * Total Time: 109.71 s
------------------------------------------------------------------------------
meme_-Klf1-large_meme_ucxv6oz_N_1_MPI_36_OMP_1
   - builtin
      * num_tasks: 36
      * Total Time: 64.38 s
------------------------------------------------------------------------------
meme_-Klf1-large_meme_ucxv6oz_N_1_MPI_72_OMP_1
   - builtin
      * num_tasks: 72
      * Total Time: 66.15 s
------------------------------------------------------------------------------
meme_-Klf1-large_meme_ucxv6oz_N_2_MPI_144_OMP_1
   - builtin
      * num_tasks: 144
      * Total Time: 47.92 s
------------------------------------------------------------------------------
meme_-Klf1-large_meme_ucxv6oz_N_4_MPI_288_OMP_1
   - builtin
      * num_tasks: 288
      * Total Time: 39.39 s
------------------------------------------------------------------------------
meme_-Klf1-large_meme_ucxv6oz_N_8_MPI_576_OMP_1
   - builtin
      * num_tasks: 576
      * Total Time: 37.88 s
------------------------------------------------------------------------------
```

### On-node Strong Scaling Study

| Cores |   Arm 21.0 |   Gnu 10.3 | Nvidia 21.2 |
|-------|------------|------------|-------------|
|     1 |  1973.33 s |  1954.61 s |   2216.7  s |
|     2 |  1003.21 s |   994.1  s |   1118.03 s |
|     4 |   498.16 s |   499.94 s |    570.22 s |
|     8 |   253.51 s |   251.54 s |    296.85 s |
|    16 |   133.31 s |   132.87 s |    170.7  s |
|    32 |    73.81 s |    74.45 s |    109.83 s |
|    64 |    44.47 s |    45.0  s |     81.18 s |

### Serial Hot-spot Profile

List of top-10 functions/code locations from a serial profile (C6gn with `meme`
compiled with GCC). Collected with `reframe` by prepending `map --profile
--export-functions=prof.csv` to the job specification.

| Position | Routine                 | Time (%) |
|----------|-------------------------|----------|
|  1       |  next_pY                |   34.6%  |
|  2       |  global_max             |   33.3%  |
|  3       |  align_top_subsequences |    5.2%  |
|  4       |  m_step                 |    5.1%  |
|  5       |  __log_finite           |    4.3%  |
|  6       |  e_step                 |    4.2%  |
|  7       |  exp                    |    3.6%  |
|  8       |  __exp_finite           |    1.8%  |
|  9       |  pY_compare             |    1.6%  |
| 10       |  msort_with_tmp.part    |    1.3%  |

### Full Node Hot-spot Profile

List of top-10 functions/code locations from a full node profile (C6gn with
`meme` compiled with GCC). Collected with `reframe` by prepending `map
--profile --export-functions=prof.csv` to the job specification.

| Position | Routine                | Time (%) | MPI (%) |
|----------|------------------------|----------|---------|
|  1       | next_pY                |   23.7%  |         |
|  2       | global_max             |   23.6%  |         |
|  3       | MPI_Allreduce          |   15.6%  |  15.6%  |
|  4       | m_step                 |    6.8%  |         |
|  5       | align_top_subsequences |    6.5%  |         |
|  6       | e_step                 |    5.3%  |         |
|  7       | __log_finite           |    3.6%  |         |
|  8       | exp                    |    3.3%  |         |
|  9       | __exp_finite           |    2.7%  |         |
| 10       | pY_compare             |    0.8%  |         |

### On-Node Architecture Comparison

#### C6gn instances

| Cores |   Arm 21.0 |   Gnu 10.3 | Nvidia 21.2 |
|-------|------------|------------|-------------|
|     1 |  1973.33 s |  1954.61 s |   2216.7  s |
|     2 |  1003.21 s |   994.1  s |   1118.03 s |
|     4 |   498.16 s |   499.94 s |    570.22 s |
|     8 |   253.51 s |   251.54 s |    296.85 s |
|    16 |   133.31 s |   132.87 s |    170.7  s |
|    32 |    73.81 s |    74.45 s |    109.83 s |
|    64 |    44.47 s |    45.0  s |     81.18 s |

#### C5n instances

| Nodes | Hardware threads |  Gnu 10.3 | Nvidia 21.2 |
|-------|------------------|-----------|-------------|
| 1     |               1  | 1416.1  s |   1705.14 s |
| 1     |               3  |  484.2  s |    588.09 s |
| 1     |               9  |  169.09 s |    204.78 s |
| 1     |              18  |   91.34 s |    109.71 s |
| 1     |              36  |   54.62 s |     64.38 s |
| 1     |              72  |   57.42 s |     66.15 s |

### Off-Node Scaling Study

#### C6gn instances

| Nodes | Cores | Arm 21.0 | Gnu 10.3 | Nvidia 21.2 |
|-------|-------|----------|----------|-------------|
| 1     |    8  | 253.51 s | 251.54 s |    296.85 s |
| 1     |   16  | 133.31 s | 132.87 s |    170.7  s |
| 1     |   32  |  73.81 s |  74.45 s |    109.83 s |
| 1     |   64  |  44.47 s |  45.0  s |     81.18 s |
| 2     |  128  |  33.54 s |  34.42 s |     71.62 s |
| 4     |  256  |  30.08 s |  32.33 s |     75.75 s |
| 8     |  512  |  29.42 s |  31.34 s |     78.88 s |

#### C5n instances

| Nodes | Hardware threads | Gnu 10.3 | Nvidia 21.2 |
|-------|------------------|----------|-------------|
| 1     |               9  | 169.09 s |    204.78 s |
| 1     |              18  |  91.34 s |    109.71 s |
| 1     |              36  |  54.62 s |     64.38 s |
| 1     |              72  |  57.42 s |     66.15 s |
| 2     |             144  |  43.35 s |     47.92 s |
| 4     |             288  |  40.12 s |     39.39 s |
| 8     |             576  |  37.12 s |     37.88 s |

N.B. The last run with 576 MPI processes has to be run without the `map`
profiling, since the Arm licence installed only supported up to 512 processes.

## Report

### Compilation Summary

As expected, building with `gcc` was extremely straightfoward, requiring no
changes to packages whatsoever. The major issues with building `meme` with
compilers other than `gcc` related mostly with ``GNU-isms'' that the Arm and
Nvidia compilers do not implement, or implement differently. More specifically,
the major issue with the Arm compiler was related to the way it deals with
inline functions---in `meme`, several inline functions were declared `extern
inline`, which was causing the Arm compiler to emit multiple definitions of the
same function, which eventually would lead to linkage errors. Changing these
declarations to `static inline` solved the problem. Meanwhile, the major issues
with the Nvidia compiler were related with the lack of support for 128-bit
integers, as well as unrecognised compilation flags. To solve the former issue,
we resorted to compiling the affected dependencies with GCC. To solve the
latter, we had to inspect the flags generating errors one by one, and determine
whether or not it was safe to remove them. Since most of them were warning,
this was a relatively simple procedure.

### Performance Summary

In our experiments, the fastest compilers turned out to be Arm and GCC. The
former is slightly faster for a larger number of nodes, whilst the latter is
faster for smaller runs. Meanwhile, for larger runs on C6gn nodes (e.g. 8 nodes
with 64 MPI processes per node) the Nvidia compiler is more than 2x slower than
Arm and GCC. However, this descrepancy does not emerge on C5n nodes.
