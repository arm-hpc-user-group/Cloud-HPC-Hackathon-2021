# meme 

**Description:** The MEME Suite allows the biologist to discover novel motifs in collections of unaligned nucleotide or protein sequences, and to perform a wide variety of other motif-based analyses.

**URL:** http://meme-suite.org

**Team:**  

## Compilation

### Modifications

  - `meme` has to be patched for `arm`
    - https://github.com/spack/spack/pull/24883/files#diff-765aeff1784028c4b0d57514f10e8ddf9357fb3153f93b6823e4f9c9027c1620
    - We'll try to get this included upstream.
  - `spack meme` has to be patched for `arm` and `nvhpc`
    - https://github.com/spack/spack/pull/24883
  - `spack libxslt` has to be patched for `nvhpc`
    - https://github.com/spack/spack/pull/24873

These patches are also included below.

### Building meme

#### Arm

  - `meme` does not build due to the way some inline functions are declared, so we patched it as below (probably will try to get this included upstream).

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

  - Here's the patched `spack meme` package, including the changes required to compile `nvhpc` (see below).

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

  - `perl@5.32.1` was used as suggested on slack.
  - We used external `python` to speedup the compilation.

```
spack external find python
```

```
$ spack spec -Il meme%arm ^perl@5.32.1
Input spec
--------------------------------
 -   meme%arm
 -       ^perl@5.32.1

Concretized
--------------------------------
==> Warning: arm@21.0.0.879 cannot build optimized binaries for "graviton2". Using best target possible: "aarch64"
[+]  425o2yr  meme@5.3.0%arm@21.0.0.879~image-magick+mpi patches=5007c0d69900e6bfcb06fce5385670ab153f01de1aea9f62220c20e0497a2ba2 arch=linux-amzn2-aarch64
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
[+]  eqxgd55      ^openmpi@4.1.1%arm@21.0.0.879~atomics~cuda~cxx~cxx_exceptions+gpfs~internal-hwloc~java~legacylaunchers~lustre~memchecker~pmi~singularity~sqlite3+static~thread_multiple+vt+wrapper-rpath fabrics=none schedulers=none arch=linux-amzn2-aarch64
[+]  xl6anaa          ^hwloc@2.5.0%arm@21.0.0.879~cairo~cuda~gl~libudev+libxml2~netloc~nvml+pci+shared arch=linux-amzn2-aarch64
[+]  jueqz7p              ^libpciaccess@0.16%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  uwcxkin                  ^util-macros@1.19.3%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  gonqskn          ^libevent@2.1.12%arm@21.0.0.879+openssl arch=linux-amzn2-aarch64
[+]  vc3waha              ^openssl@1.1.1k%arm@21.0.0.879~docs+systemcerts arch=linux-amzn2-aarch64
[+]  mv2g7r5          ^numactl@2.0.14%arm@21.0.0.879 patches=4e1d78cbbb85de625bad28705e748856033eaafab92a66dffd383a3d7e00cc94,62fc8a8bf7665a60e8f4c93ebbd535647cebf74198f7afafec4c085a8825c006 arch=linux-amzn2-aarch64
[+]  6vvthuo          ^openssh@8.5p1%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  xe4evc4              ^libedit@3.1-20210216%arm@21.0.0.879 arch=linux-amzn2-aarch64
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
[+]  ck4dsab      ^python@3.7.10%arm@21.0.0.879+bz2+ctypes+dbm~debug+libxml2+lzma+nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tix~tkinter~ucs4+uuid+zlib patches=0d98e93189bc278fbc37a50ed7f183bd8aaf249a8e1670a465f0db6bb4f8cf87 arch=linux-amzn2-aarch64
```

```
$ spack install meme%arm ^perl@5.32.1
==> Warning: arm@21.0.0.879 cannot build optimized binaries for "graviton2". Using best target possible: "aarch64"
[+] /home/rjj/spack/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/libiconv-1.16-7vnthznb6f3xn2hyykrin45yeymts6fb
[+] /home/rjj/spack/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/pkgconf-1.7.4-zpuzm23bl335qaqoszzhkd6wep7i4ml2
[+] /home/rjj/spack/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/xz-5.2.5-zqsab4fq32x3k7df6idvkhvceugzp4gq
[+] /home/rjj/spack/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/zlib-1.2.11-puuxvg25icc6pdyssc4sgi5oskrliz4k
[+] /home/rjj/spack/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/libsigsegv-2.13-6jhzlulucoiy7gufglfbwhx7rki775wx
[+] /home/rjj/spack/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/berkeley-db-18.1.40-33wiajjxmksgrm2umgyrld5olisskwdz
[+] /home/rjj/spack/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/autoconf-archive-2019.01.06-36hcfzw3xddhyrf3exbf5jrs2akskocu
[+] /home/rjj/spack/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/util-macros-1.19.3-uwcxkinw2672z53papss7tm74wtwlab7
[+] /home/rjj/spack/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/libmd-1.0.3-srfepw2slm577yf3ndnqfvegxd5wc47s
[+] /usr (external python-3.7.10-ck4dsablke42vizpgmkx33s47yewaxkd)
[+] /home/rjj/spack/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/tar-1.34-fohku26jzkjq5gkbgcu6t6vikmnflf4g
[+] /home/rjj/spack/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/diffutils-3.7-adtc6ycofvxn36pnti4rjpbvpqpy7zzq
[+] /home/rjj/spack/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/ncurses-6.2-uhtqtlbyo7yigh35us6kaqq3f5vgshyf
[+] /home/rjj/spack/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/libxml2-2.9.10-dypqz2im5bj62zkyxk7ahsm7z4yqslle
[+] /home/rjj/spack/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/m4-1.4.19-lnai6aqtcgccuundb6iszo6lsfe5ingi
[+] /home/rjj/spack/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/libbsd-0.11.3-5q4lmygjonvmdncgynk2sxv2irlx5ehf
[+] /home/rjj/spack/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/bzip2-1.0.8-z4ybgriwwt7xs5ous57y47rne7dx7jvb
[+] /home/rjj/spack/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/libedit-3.1-20210216-xe4evc4smpyo4hr6wb4ykjzgufoavn4u
[+] /home/rjj/spack/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/readline-8.1-3haw5gtwq4xn5uftetwf74ykypck3ttj
[+] /home/rjj/spack/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/libtool-2.4.6-e4ssqx6phoexdyix2ffpbperalwklkuo
[+] /home/rjj/spack/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/expat-2.4.1-oyfuwk3dgqeglx4xk5q3qtwwf4orsbrq
[+] /home/rjj/spack/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/gettext-0.21-rl3qj47kiajnxqhdfoaqsewha3hj5bvv
[+] /home/rjj/spack/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/gdbm-1.19-645q4qjl2yh5azskbbng3ev4ok5py7cz
[+] /home/rjj/spack/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/libpciaccess-0.16-jueqz7pr2i5327di7dtfgnss7xj5bdgo
[+] /home/rjj/spack/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/perl-5.32.1-vv6txro26vz6rei7rfene7djrlddrll2
[+] /home/rjj/spack/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/hwloc-2.5.0-xl6anaasg27j4uw672jn7z5pvibb4qfg
[+] /home/rjj/spack/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/perl-try-tiny-0.28-63xetxbh3jkgddtpv6pygikfqjklryf3
[+] /home/rjj/spack/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/perl-extutils-helpers-0.026-nmupwpidxxq56tvqltkzeucodaxw2v4t
[+] /home/rjj/spack/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/perl-lwp-mediatypes-6.02-2p4t5hi7knbopc3f2k2o4kmdcr32oxfq
[+] /home/rjj/spack/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/perl-test-needs-0.002005-hlpexymfjgaqazpgotf4nmyzhq5zbsm7
[+] /home/rjj/spack/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/perl-html-tagset-3.20-plc6lno7wezhxenwlro4ieo3yhncrbxj
[+] /home/rjj/spack/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/perl-extutils-installpaths-0.012-e7eeriokslvqicpw5pndx4gibcyihn3f
[+] /home/rjj/spack/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/perl-http-date-6.02-gnnb256fp7shtixenpnw3syoy3yybfbg
[+] /home/rjj/spack/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/autoconf-2.69-par2wrm6wxctmbtzbz7yqshoqaozofec
[+] /home/rjj/spack/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/perl-extutils-config-0.008-h5t34a42it6qceye3hg4hwadtc4zvsof
[+] /home/rjj/spack/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/openssl-1.1.1k-vc3wahacaffdv4csjq5enxyyqtzfppxj
[+] /home/rjj/spack/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/perl-io-html-1.001-fbhtyzq22mubjmdstq4x3fdkq7jgvwsq
[+] /home/rjj/spack/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/texinfo-6.5-wqpjcrwgau4ashd3rgykstsvsp5vb66y
[+] /home/rjj/spack/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/perl-module-build-0.4224-ec7ahmpc2tq7qfq3soqqmpwlgzexp5hs
[+] /home/rjj/spack/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/perl-encode-locale-1.05-miszmcndqoaqt6i4wckypjw3o44aqpx2
[+] /home/rjj/spack/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/perl-uri-1.72-ardflxywajjrqwc56x3qg6wmupdl5rej
[+] /home/rjj/spack/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/perl-html-parser-3.72-pkjgw5vjbyt7lrpq4stcanf5exaxtui2
[+] /home/rjj/spack/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/perl-file-listing-6.04-qppjxlcf2msuzhqdhmnkndqbrhbmgsgg
[+] /home/rjj/spack/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/automake-1.16.3-edezkz3kir457u7yc554afjbfd42oveb
[+] /home/rjj/spack/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/openssh-8.5p1-6vvthuodratjaerhyrjlkmoz722xt575
[+] /home/rjj/spack/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/libevent-2.1.12-gonqskn2pxdwfefom4uxlgy6qgxxtmsf
[+] /home/rjj/spack/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/perl-module-build-tiny-0.039-d6j4vei2k4uolbiwi7tvalf5za74xmdj
[+] /home/rjj/spack/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/perl-http-message-6.13-tjhb3pitkhqe5qchmwq2hfhd5zihj52s
[+] /home/rjj/spack/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/perl-net-http-6.17-gzm6crbpaw46p5luzkk6rjp4hdc5mjuv
[+] /home/rjj/spack/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/perl-www-robotrules-6.02-kwobb4g7qolx2xvlabnhotk6ceisnhu7
[+] /home/rjj/spack/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/gmp-6.2.1-y7o4xcemclbfe77vaqo3mu7vaanorkji
[+] /home/rjj/spack/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/numactl-2.0.14-mv2g7r5fxdbopfvogpibbaqdgnbrcedc
[+] /home/rjj/spack/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/perl-http-negotiate-6.01-f7wxi23k63wkt64rbcqd7kcjngenyame
[+] /home/rjj/spack/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/perl-http-daemon-6.01-zrmw65nybzqdqcj5jdidvzhx6xja4f5p
[+] /home/rjj/spack/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/perl-http-cookies-6.04-dwuwymubilhdsiyhamshd7zgzac3jmgs
[+] /home/rjj/spack/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/mpfr-4.1.0-s55efueyvfqhnctcgmwtu4zr6vlfrnst
[+] /home/rjj/spack/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/openmpi-4.1.1-eqxgd55t743v4nns6wf5ionyie2iioaj
[+] /home/rjj/spack/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/perl-libwww-perl-6.33-yigrrtoybywma5z52pizdgzyspb4lc33
[+] /home/rjj/spack/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/gawk-5.1.0-r5sadrnilf7xvmf5oomuhugopdmdy7cu
[+] /home/rjj/spack/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/perl-xml-parser-2.44-abuse3azatsv3azyoksyptg7gzforhw5
[+] /home/rjj/spack/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/libgpg-error-1.42-45e7cf62wlkleklnwmtfq3r73w4phxib
[+] /home/rjj/spack/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/libgcrypt-1.9.3-xc6udazenhyeaitpxdnb4wvg52winodb
[+] /home/rjj/spack/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/libxslt-1.1.33-jaizlxa53c45c4wcvjof2psbqbqu5446
==> Installing meme-5.3.0-425o2yrunny2fimknk2gf4axdf7p7mic
==> No binary for meme-5.3.0-425o2yrunny2fimknk2gf4axdf7p7mic found: installing from source
==> Using cached archive: /home/rjj/spack/var/spack/cache/_source-cache/archive/b2/b2ddec9db972fcf77b29c7deb62df8b1dd8a6638c13c1aa06a5d563c4a7ff756.tar.gz
==> Applied patch /home/rjj/spack/var/spack/repos/builtin/packages/meme/arm.patch
==> Ran patch() for meme
==> meme: Executing phase: 'autoreconf'
==> meme: Executing phase: 'configure'
==> meme: Executing phase: 'build'
==> meme: Executing phase: 'install'
==> meme: Successfully installed meme-5.3.0-425o2yrunny2fimknk2gf4axdf7p7mic
  Fetch: 0.04s.  Build: 17.37s.  Total: 17.41s.
[+] /home/rjj/spack/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/meme-5.3.0-425o2yrunny2fimknk2gf4axdf7p7mic
==> Updating view at /home/rjj/meme-arm/.spack-env/view
==> Warning: [/home/rjj/meme-arm/.spack-env/._view/62zg2tww4xe4wgpwihg2zzhx3k2qtgsu] Skipping external package: python@3.7.10%arm@21.0.0.879+bz2+ctypes+dbm~debug+libxml2+lzma+nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tix~tkinter~ucs4+uuid+zlib patches=0d98e93189bc278fbc37a50ed7f183bd8aaf249a8e1670a465f0db6bb4f8cf87 arch=linux-amzn2-aarch64/ck4dsab
```

#### GCC

  - No major errors were detected when building with `gcc`.
  - We use `perl@5.32.1` as suggested on slack.
  - We use external `python` to speedup the compilation.

```
spack external find python
```

```
$ spack spec -Il meme%gcc ^perl@5.32.1
Input spec
--------------------------------
 -   meme%gcc
 -       ^perl@5.32.1

Concretized
--------------------------------
[+]  gl7hp6y  meme@5.3.0%gcc@10.3.0~image-magick+mpi arch=linux-amzn2-graviton2
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
[+]  l7oony6      ^openmpi@4.1.1%gcc@10.3.0~atomics~cuda~cxx~cxx_exceptions+gpfs~internal-hwloc~java~legacylaunchers~lustre~memchecker~pmi~singularity~sqlite3+static~thread_multiple+vt+wrapper-rpath fabrics=none schedulers=none arch=linux-amzn2-graviton2
[+]  cukmqbg          ^hwloc@2.5.0%gcc@10.3.0~cairo~cuda~gl~libudev+libxml2~netloc~nvml+pci+shared arch=linux-amzn2-graviton2
[+]  asgtk6a              ^libpciaccess@0.16%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  4xr3hhh                  ^util-macros@1.19.3%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  tadxrfp          ^libevent@2.1.12%gcc@10.3.0+openssl arch=linux-amzn2-graviton2
[+]  5i3lgfb              ^openssl@1.1.1k%gcc@10.3.0~docs+systemcerts arch=linux-amzn2-graviton2
[+]  mhav5gn          ^numactl@2.0.14%gcc@10.3.0 patches=4e1d78cbbb85de625bad28705e748856033eaafab92a66dffd383a3d7e00cc94,62fc8a8bf7665a60e8f4c93ebbd535647cebf74198f7afafec4c085a8825c006 arch=linux-amzn2-graviton2
[+]  wturp6c          ^openssh@8.5p1%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  ivotdt7              ^libedit@3.1-20210216%gcc@10.3.0 arch=linux-amzn2-graviton2
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
[+]  gcliuat      ^python@3.7.10%gcc@10.3.0+bz2+ctypes+dbm~debug+libxml2+lzma+nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tix~tkinter~ucs4+uuid+zlib patches=0d98e93189bc278fbc37a50ed7f183bd8aaf249a8e1670a465f0db6bb4f8cf87 arch=linux-amzn2-graviton2
```

```
$ spack install meme%gcc ^perl@5.32.1
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/gcc-10.3.0/libiconv-1.16-y5ei3cmj2tgxpgnr6igh5fziwnnbi7a3
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/gcc-10.3.0/pkgconf-1.7.4-s4pw7zmcaf2rh6xuc22jp66cg3npx4nz
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/gcc-10.3.0/xz-5.2.5-ye3kcvvokl2a3pdn6lkab7j7rzpxggpi
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/gcc-10.3.0/zlib-1.2.11-qepjcvjpz2nwtm4zbaz2br33bwvy23tx
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/gcc-10.3.0/libsigsegv-2.13-ltbv6bkcmvubbgixriiwzbqudh6fkazl
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/gcc-10.3.0/berkeley-db-18.1.40-y42m6yrtdnsuoh45fi5jfx4yerisdxrk
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/gcc-10.3.0/autoconf-archive-2019.01.06-yutdrfyi3gkgdz7gmqa5efgofx5ozdfn
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/gcc-10.3.0/util-macros-1.19.3-4xr3hhh6aikjhwk5woa5uhbaro6srjbg
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/gcc-10.3.0/libmd-1.0.3-nssrqfcpfcpomxqfhbdr3ptjjp2nd6xd
[+] /usr (external python-3.7.10-gcliuatsk3ithegvhwy4ifly5m3y6vtz)
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/gcc-10.3.0/tar-1.34-v6cutkhxah5zju5ndfmzq465bdptkgo6
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/gcc-10.3.0/diffutils-3.7-2w7bert4g2o7lucct63fowxxj2vsqkvt
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/gcc-10.3.0/ncurses-6.2-iwzirqcp76atpg62xlcu46dh2yjddw3j
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/gcc-10.3.0/libxml2-2.9.10-iyhm3wilqssofsggowwbfxun7niccvhf
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/gcc-10.3.0/m4-1.4.19-3mz7xytiqgkfu67nm2ebstep6sgkzxwb
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/gcc-10.3.0/libbsd-0.11.3-ourxkez44ksg5ciapptjeaxjzrulu5hy
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/gcc-10.3.0/bzip2-1.0.8-rqrpmaprfygdmjxct4442op7bbj5e56h
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/gcc-10.3.0/readline-8.1-3zy7kxkw67essppq4knw2gvklra5ygs4
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/gcc-10.3.0/libedit-3.1-20210216-ivotdt7lhwaqswzxiytqy6doasslbljt
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/gcc-10.3.0/libtool-2.4.6-z2uysov7wn6lxgyfytyhgulaaz6zijfm
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/gcc-10.3.0/expat-2.4.1-ychdz7licpqsyebds6d3dbxquxz2ew7r
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/gcc-10.3.0/gettext-0.21-fqlpcslnophdmhn2lhhqlvjxnguwzlpb
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/gcc-10.3.0/gdbm-1.19-wjwqncxnsbjbrwsvfedxdtxinvrmjryv
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/gcc-10.3.0/libpciaccess-0.16-asgtk6aydbyop2sv7wornerzw6y4mjre
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/gcc-10.3.0/perl-5.32.1-4m7exgbhfvcb5wlifx6o4ngpphbjjphb
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/gcc-10.3.0/hwloc-2.5.0-cukmqbgswpp2d2a6yftqywlujkorlpbq
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/gcc-10.3.0/perl-module-build-0.4224-l3vxnlnqyoatmq5zw3t2aa7c27cjxc5w
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/gcc-10.3.0/perl-lwp-mediatypes-6.02-uwpw4jbqjhsicxv4jicqpmoxcjnjzu23
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/gcc-10.3.0/autoconf-2.69-djnylognarbxzwpvmlp6yoqnx2sklt2l
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/gcc-10.3.0/perl-test-needs-0.002005-ilcgd4pnf32x367kj5rncepi27pbqcuz
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/gcc-10.3.0/perl-extutils-installpaths-0.012-3bmurgvfx65rj4ussctrlijedbl5rv5x
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/gcc-10.3.0/perl-io-html-1.001-cw4yunqrs6kkyvwjn4f2vrjfet2u4vf4
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/gcc-10.3.0/perl-http-date-6.02-iel7364fqqw34marxs2bhiz2ryp3wfo7
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/gcc-10.3.0/perl-try-tiny-0.28-lbi5zlwstshiobnfkih7fh6y6azogyui
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/gcc-10.3.0/perl-html-tagset-3.20-5356pecizzclskqxkgx2rtzjelkhzkdu
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/gcc-10.3.0/perl-extutils-helpers-0.026-oaj7c6lrawhr3i6lv7ew3iwilvh5zfvl
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/gcc-10.3.0/perl-encode-locale-1.05-7bktzwyklvwp557nru2vwv5owpngzlxg
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/gcc-10.3.0/perl-extutils-config-0.008-2nu5ktnrxzmegyellhxckwssg3eaub64
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/gcc-10.3.0/texinfo-6.5-egfqbtluucpkgtbqrvo5j3fcf6c5l4pj
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/gcc-10.3.0/openssl-1.1.1k-5i3lgfbcbweivvoiqxg4jckshtmlyhkb
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/gcc-10.3.0/automake-1.16.3-xb2w5ncoqrjpbhbdnilr4uxm34q6mu4i
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/gcc-10.3.0/perl-uri-1.72-mwjmhxr4xsunndhk2ujqb7tdy7m6xio2
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/gcc-10.3.0/perl-file-listing-6.04-ng42qsj7uptj6flp3q45thamvk2673ga
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/gcc-10.3.0/perl-html-parser-3.72-6c5zqpyelmbdyj5jl22qcueul3xvy2dk
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/gcc-10.3.0/perl-module-build-tiny-0.039-n2pgdkj5b6uruq3xvpr46xibfvmuepsl
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/gcc-10.3.0/openssh-8.5p1-wturp6cp4ypasvbcyn7qx7rgagdak7kc
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/gcc-10.3.0/libevent-2.1.12-tadxrfpeo27q5qow6wzvlsmyhv6kud4q
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/gcc-10.3.0/gmp-6.2.1-rego5fd26ydvr4nmx6kgf73kysxinrz5
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/gcc-10.3.0/numactl-2.0.14-mhav5gnwdad3th2hgidiuzepv7tmdekn
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/gcc-10.3.0/perl-net-http-6.17-jp2quripysc2jg3hsxct5ttyaurxddez
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/gcc-10.3.0/perl-www-robotrules-6.02-ojglnnz65ifhxqo42qo36bfnclklu5yo
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/gcc-10.3.0/perl-http-message-6.13-lzhpg5e3ksypt4gqxus3yumb7ysftaqw
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/gcc-10.3.0/mpfr-4.1.0-4jwrra6yu5p4megbbvklajihvfhzln44
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/gcc-10.3.0/openmpi-4.1.1-l7oony6qix6xuddtdfcjeeeyrh5x536d
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/gcc-10.3.0/perl-http-negotiate-6.01-memap537wakso4d467fb2fg3om7nyk3g
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/gcc-10.3.0/perl-http-cookies-6.04-rn72djeoblr6bgm3glkxizssluph5t7b
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/gcc-10.3.0/perl-http-daemon-6.01-kqe5fq4uxoz7eg3ou35uttcbcbenvjv3
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/gcc-10.3.0/gawk-5.1.0-wbcp5owlgdkqftwpad3epklp6t7auhfp
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/gcc-10.3.0/perl-libwww-perl-6.33-f5v6774ieoy4kpgciwqsoj4745lgmhv4
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/gcc-10.3.0/libgpg-error-1.42-hjnbovy4wzj4vwpvb3zjldambls2sri4
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/gcc-10.3.0/perl-xml-parser-2.44-lqb6dymrnsfobtx44rfpvdvy5ppo2hdj
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/gcc-10.3.0/libgcrypt-1.9.3-equosbjd7u25gi5ytpzyge37uxiqwlcn
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/gcc-10.3.0/libxslt-1.1.33-vapzbljmokpq4jwaavjxip3tfnsd3e7w
==> Installing meme-5.3.0-gl7hp6ygegwney5mpaestizwmpptva3t
==> No binary for meme-5.3.0-gl7hp6ygegwney5mpaestizwmpptva3t found: installing from source
==> Using cached archive: /home/rjj/spack/var/spack/cache/_source-cache/archive/b2/b2ddec9db972fcf77b29c7deb62df8b1dd8a6638c13c1aa06a5d563c4a7ff756.tar.gz
==> Ran patch() for meme
==> meme: Executing phase: 'autoreconf'
==> meme: Executing phase: 'configure'
==> meme: Executing phase: 'build'
==> meme: Executing phase: 'install'
==> meme: Successfully installed meme-5.3.0-gl7hp6ygegwney5mpaestizwmpptva3t
  Fetch: 0.04s.  Build: 17.71s.  Total: 17.74s.
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/gcc-10.3.0/meme-5.3.0-gl7hp6ygegwney5mpaestizwmpptva3t
==> Updating view at /home/rjj/meme-gcc/.spack-env/view
==> Warning: [/home/rjj/meme-gcc/.spack-env/._view/thngqlmneanmqdvj3otgio4rjbr4ndlb] Skipping external package: python@3.7.10%gcc@10.3.0+bz2+ctypes+dbm~debug+libxml2+lzma+nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tix~tkinter~ucs4+uuid+zlib patches=0d98e93189bc278fbc37a50ed7f183bd8aaf249a8e1670a465f0db6bb4f8cf87 arch=linux-amzn2-graviton2/gcliuat
```

#### NVHPC

  - `nvhpc` conflicts with `python`.
    - Can be fixed by using the external `python`.

```
spack external find python
```

  - Various dependencies of `libgcrypt` do not compile with `nvhpc`. As a work around, we build them with `gcc`.
  - `libbsd-0.11.3` doesn't build, initially because the current patch included in the package does not apply, but other errors emerge after fixing the patch.
    - Using `libbsd@0.10.0` works.
  - `perl@5.34.0` hangs during compilation, so we use `perl@5.32.1`.

```
$ spack spec -Il meme%nvhpc ^libgcrypt%gcc ^libbsd@0.10.0 ^perl@5.32.1
Input spec
--------------------------------
 -   meme%nvhpc
 -       ^libbsd@0.10.0
 -       ^libgcrypt%gcc
 -       ^perl@5.32.1

Concretized
--------------------------------
[+]  k63vfh6  meme@5.3.0%nvhpc@21.2~image-magick+mpi arch=linux-amzn2-graviton2
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
[+]  oof4r4k      ^openmpi@4.1.1%nvhpc@21.2~atomics~cuda~cxx~cxx_exceptions+gpfs~internal-hwloc~java~legacylaunchers~lustre~memchecker~pmi~singularity~sqlite3+static~thread_multiple+vt+wrapper-rpath fabrics=none patches=fba0d3a784a9723338722b48024a22bb32f6a951db841a4e9f08930a93f41d7a schedulers=none arch=linux-amzn2-graviton2
[+]  jroqews          ^hwloc@2.5.0%nvhpc@21.2~cairo~cuda~gl~libudev+libxml2~netloc~nvml+pci+shared arch=linux-amzn2-graviton2
[+]  e4m4ued              ^libpciaccess@0.16%nvhpc@21.2 patches=6e08dc445ece06e9e8b1344397f2d3f169005703ddc0f2ae24f366cde78c7377 arch=linux-amzn2-graviton2
[+]  4imdwuy                  ^util-macros@1.19.3%nvhpc@21.2 arch=linux-amzn2-graviton2
[+]  uttaumr          ^libevent@2.1.12%nvhpc@21.2+openssl arch=linux-amzn2-graviton2
[+]  j2qhi7h              ^openssl@1.1.1k%nvhpc@21.2~docs+systemcerts arch=linux-amzn2-graviton2
[+]  5yq4tpw          ^numactl@2.0.14%nvhpc@21.2 patches=4e1d78cbbb85de625bad28705e748856033eaafab92a66dffd383a3d7e00cc94,62fc8a8bf7665a60e8f4c93ebbd535647cebf74198f7afafec4c085a8825c006 arch=linux-amzn2-graviton2
[+]  cl3ohqo          ^openssh@8.5p1%nvhpc@21.2 arch=linux-amzn2-graviton2
[+]  yvqpq74              ^libedit@3.1-20210216%nvhpc@21.2 arch=linux-amzn2-graviton2
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
[+]  6pt5n5r      ^python@3.7.10%nvhpc@21.2+bz2+ctypes+dbm~debug+libxml2+lzma+nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tix~tkinter~ucs4+uuid+zlib patches=0d98e93189bc278fbc37a50ed7f183bd8aaf249a8e1670a465f0db6bb4f8cf87 arch=linux-amzn2-graviton2
```

  - The default `spack meme` package generates `xml` link errors.
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

```
$ spack install meme%nvhpc ^libgcrypt%gcc ^libbsd@0.10.0 ^perl@5.32.1
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/nvhpc-21.2/libiconv-1.16-r7mmkdpt4wbubln5d2qfg3gnwoa7jwup
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/nvhpc-21.2/pkgconf-1.7.4-vtiml6gd4tq2n2weyfyyxl75p76fso36
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/nvhpc-21.2/xz-5.2.5-br733tn7u7m7bkzoqki4t6mkwqe37kcc
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/nvhpc-21.2/zlib-1.2.11-4js6ectch4sma7o6s4c3wdnknse53stu
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/gcc-10.3.0/libsigsegv-2.13-ltbv6bkcmvubbgixriiwzbqudh6fkazl
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/nvhpc-21.2/berkeley-db-18.1.40-5uyf3k42277wtheux4xkcqetv52ifecq
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/gcc-10.3.0/autoconf-archive-2019.01.06-yutdrfyi3gkgdz7gmqa5efgofx5ozdfn
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/nvhpc-21.2/util-macros-1.19.3-4imdwuyb6nnch2eduhl7mfdb5awa6sgl
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/nvhpc-21.2/libbsd-0.10.0-kevfo4mlgq6aehvphjgobdmxv2nalusd
[+] /usr (external python-3.7.10-6pt5n5r5czl5gduqyhnpd6birqvvyjgg)
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/gcc-10.3.0/tar-1.34-ugpacicagphjnlzbpvrznxd5emylwlmn
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/nvhpc-21.2/diffutils-3.7-s4mb5noxg5nn4i6x22fcjugursbtxgxo
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/nvhpc-21.2/ncurses-6.2-asgm7mtatrjw36ttfk3g5vxfxz5ybj7h
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/nvhpc-21.2/libxml2-2.9.10-wo4l72sljq27vlflhhnbftrnwo6qfuph
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/gcc-10.3.0/m4-1.4.19-3mz7xytiqgkfu67nm2ebstep6sgkzxwb
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/nvhpc-21.2/expat-2.4.1-ucobzs7xoo25m4j4yopd2qplgs22o7xg
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/nvhpc-21.2/bzip2-1.0.8-wsi7g3j4vytltkoudzfoghkb5v7wwnel
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/nvhpc-21.2/readline-8.1-zori3wfcaqyec26duh45loktzyovwj6b
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/nvhpc-21.2/libedit-3.1-20210216-yvqpq74ewuievw5qv774ce4ctb2aop5v
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/gcc-10.3.0/libtool-2.4.6-z2uysov7wn6lxgyfytyhgulaaz6zijfm
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/gcc-10.3.0/gettext-0.21-klmvhilfcfswnm2vkekesjx6aquoadwx
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/nvhpc-21.2/gdbm-1.19-m2wdbeocflxsyohvv3mppfhnp2fzoklm
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/nvhpc-21.2/libpciaccess-0.16-e4m4uedp2o6ltanfegdoaa4a3c4mv6qv
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/nvhpc-21.2/perl-5.32.1-gn4fgp5ygy6wuv3wmnarrir5vwtwauw7
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/nvhpc-21.2/hwloc-2.5.0-jroqewsmhchutjwtj7fl4pfphrbletj3
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/nvhpc-21.2/openssl-1.1.1k-j2qhi7harygj5remm5a37zqehpj5uqzm
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/nvhpc-21.2/perl-extutils-config-0.008-b2izmfns55z6qhogxlctjwyzgkvjxonh
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/gcc-10.3.0/autoconf-2.69-mzhxqyz6om765zbxioydxy4x2ichxt5r
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/nvhpc-21.2/perl-module-build-0.4224-uz3v4epjz7xksyix4gntgatgg66743zy
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/nvhpc-21.2/perl-extutils-helpers-0.026-yevyfn2oidprezjex74zyu4k6ilfkvue
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/nvhpc-21.2/perl-test-needs-0.002005-lwbdujw3qfikbsjszbmgwmr54tujp7pb
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/nvhpc-21.2/perl-http-date-6.02-7kcrousikltzvyqssz7mfbyjyi4tbrze
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/nvhpc-21.2/perl-io-html-1.001-hnhjgh2q6rquikhsa7htg2foldelhdxc
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/nvhpc-21.2/perl-lwp-mediatypes-6.02-wsgcrtfuiizht5ws5slgzruo6hwhvzvb
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/nvhpc-21.2/perl-encode-locale-1.05-bzw6yvxcx6gqbkppthsqgvqjf4yzjhba
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/nvhpc-21.2/perl-try-tiny-0.28-olvr6oso5bcjwagm2adpufuw5msjaldn
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/gcc-10.3.0/texinfo-6.5-njydrqj6o7gg4liuotwmwdswdqz5adwp
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/nvhpc-21.2/perl-html-tagset-3.20-5yqmhosygagckbumadyyqdvhdvocjtbn
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/nvhpc-21.2/perl-extutils-installpaths-0.012-nnkzejgr6yxdxusmpnomqkz3wjg5g52n
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/nvhpc-21.2/openssh-8.5p1-cl3ohqoeab4gbj7wlk3pvlyaawkykq3m
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/nvhpc-21.2/libevent-2.1.12-uttaumroxxwuv2nkijr3cabjygz3vw5q
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/gcc-10.3.0/automake-1.16.3-q5y3rsfftyeso67bw64e5t7liqqpenja
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/nvhpc-21.2/perl-uri-1.72-hs4cjs3gzrldtachwypihikta2f7vnnz
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/nvhpc-21.2/perl-file-listing-6.04-liqnsqwwgozvhoa4nl7cup6dvnpxj4pp
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/nvhpc-21.2/perl-html-parser-3.72-wq24kahn4i6eonetkl7d574cradpacvi
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/nvhpc-21.2/perl-module-build-tiny-0.039-mevsuodqjqhu4kpqnakaawdovparf4cr
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/nvhpc-21.2/numactl-2.0.14-5yq4tpwoq3pckv44wbxc4bauau7pictt
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/gcc-10.3.0/gmp-6.2.1-rego5fd26ydvr4nmx6kgf73kysxinrz5
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/nvhpc-21.2/perl-net-http-6.17-7nwrfth5va3n3xtxdn46b3grnjxf2c73
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/nvhpc-21.2/perl-http-message-6.13-nruhydygzszlz7jcqoealeww3rnt6kvf
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/nvhpc-21.2/perl-www-robotrules-6.02-5cr5u6dgx23c7lyrk3vdmwbf3xmlykoa
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/nvhpc-21.2/openmpi-4.1.1-oof4r4k2xcglcuutsmzkimahaf6npgnd
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/gcc-10.3.0/mpfr-4.1.0-4jwrra6yu5p4megbbvklajihvfhzln44
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/nvhpc-21.2/perl-http-cookies-6.04-wbgtlcou2fm462kufmvlf6lgp4udtkxy
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/nvhpc-21.2/perl-http-daemon-6.01-6iouolgdb73oure5mhc64ewdumtvkunb
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/nvhpc-21.2/perl-http-negotiate-6.01-s3lbu5ym44uwlcgmciyxx4b4mrskbzow
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/gcc-10.3.0/gawk-5.1.0-23u7l5kfg7tceadziqilrttxkoarvuym
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/nvhpc-21.2/perl-libwww-perl-6.33-y2t47lvvdq7vfulx3mc72tf6zddzwkgi
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/gcc-10.3.0/libgpg-error-1.42-hjnbovy4wzj4vwpvb3zjldambls2sri4
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/nvhpc-21.2/perl-xml-parser-2.44-5qlgjmfmjqojelc2ptxzfgru5rhmpw6a
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/gcc-10.3.0/libgcrypt-1.9.3-equosbjd7u25gi5ytpzyge37uxiqwlcn
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/nvhpc-21.2/libxslt-1.1.33-r3qewtmebps5w7yowpgb34rqyego4rz4
==> Installing meme-5.3.0-k63vfh6k5iavtvb3vzwzhxobd7t6c5g3
==> No binary for meme-5.3.0-k63vfh6k5iavtvb3vzwzhxobd7t6c5g3 found: installing from source
==> Using cached archive: /home/rjj/spack/var/spack/cache/_source-cache/archive/b2/b2ddec9db972fcf77b29c7deb62df8b1dd8a6638c13c1aa06a5d563c4a7ff756.tar.gz
==> Ran patch() for meme
==> meme: Executing phase: 'autoreconf'
==> meme: Executing phase: 'configure'
==> meme: Executing phase: 'build'
==> meme: Executing phase: 'install'
==> meme: Successfully installed meme-5.3.0-k63vfh6k5iavtvb3vzwzhxobd7t6c5g3
  Fetch: 0.04s.  Build: 31.63s.  Total: 31.67s.
[+] /home/rjj/spack/opt/spack/linux-amzn2-graviton2/nvhpc-21.2/meme-5.3.0-k63vfh6k5iavtvb3vzwzhxobd7t6c5g3
==> Updating view at /home/rjj/meme-nvhpc/.spack-env/view
==> Warning: [/home/rjj/meme-nvhpc/.spack-env/._view/ha6aeh7czi6oapnfqunxtrmn4lep3z24] Skipping external package: python@3.7.10%nvhpc@21.2+bz2+ctypes+dbm~debug+libxml2+lzma+nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tix~tkinter~ucs4+uuid+zlib patches=0d98e93189bc278fbc37a50ed7f183bd8aaf249a8e1670a465f0db6bb4f8cf87 arch=linux-amzn2-graviton2/6pt5n5r
```

## Test Case 1

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
