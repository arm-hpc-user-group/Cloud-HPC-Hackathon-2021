# meme 

**Description:** The MEME Suite allows the biologist to discover novel motifs in collections of unaligned nucleotide or protein sequences, and to perform a wide variety of other motif-based analyses.

**URL:** http://meme-suite.org

**Team:**  

## Compilation

### Spack Package Modification

Details of any changes to the Spack recipe used.

Git commit hash of checkout for pacakage:

Pull request for Spack recipe changes:

### Building meme



#### Compiler 1

```
spack install <app>%<compiler1>
```

```
$ spack spec -Il <app>%<compiler1>

```

#### NVHPC

  - `nvhpc` conflicts with `python`, which can be fixed by using the external `python`.

```
spack external find python
```

  - Various dependencies of `libgcrypt` do not compile with `nvhpc`. As a work around, we can build them with `gcc`.
  - `libbsd-0.11.3` doesn't build, initially because the current patch included in the package does not apply, but other errors emerge after fixing the patch. Using `libbsd@0.10.0` works.
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
[+]  uayb6j2  meme@5.3.0%nvhpc@21.2~image-magick+mpi dev_path=/home/rjj/meme-nvhpc/meme arch=linux-amzn2-graviton2
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

  - The default `spack meme` package generates `xml` link errors. Installing `libxml2` and `libxslt` as `spack packages` and building `meme` against them solves this problem.
  - Some of the compilation flags used by `meme` and `libxmlst` are not supported by `nvhpc`, but these flags can be easily patched out.

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
index 78e21ca595..205c91c811 100644
--- a/var/spack/repos/builtin/packages/meme/package.py
+++ b/var/spack/repos/builtin/packages/meme/package.py
@@ -31,6 +31,8 @@ class Meme(AutotoolsPackage):
     depends_on('mpi', when='+mpi')
     depends_on('imagemagick', type=('build', 'run'), when='+image-magick')
     depends_on('perl-xml-parser', type=('build', 'run'))
+    depends_on('libxml2', type=('build', 'run'))
+    depends_on('libxslt', type=('build', 'run'))
 
     def url_for_version(self, version):
         url = 'http://meme-suite.org/meme-software/{0}/meme{1}{2}.tar.gz'
@@ -40,7 +42,14 @@ def url_for_version(self, version):
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
