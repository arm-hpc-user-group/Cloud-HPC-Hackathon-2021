# GATK 

**Description:** GATK (pronounced "Gee-ay-tee-kay", not "Gat-kay"), stands for GenomeAnalysisToolkit. It is a collection of command-line tools for analyzing high-throughput sequencing data with a primary focus on variant discovery. The tools can be used individually or chained together into complete workflows.

GATK is a very large set of tools with ~100 different distinct tools to test. Several are tested here. GATK also relies on genomics data to work, including reference genomes and sequencing output (aka "BAM" files). The current standard reference human genome is used for testing here. BAM files from the [famous 1000 Genomes Project](https://www.nature.com/articles/nature15393) that characterized genomic differences amongst the human sub-populataions is also used. Three [publically available BAM files](https://console.cloud.google.com/storage/browser/genomics-public-data/1000-genomes) are used representing small, medium and large sequencing output.

* `H06HDADXX130110.1.ATCACGAT.20k_reads.bam` is a small Illumina HiSeq 25000 20k read, 5000000 base pair run from [Google's copy of Broad/GATK data](https://storage.googleapis.com/genomics-public-data/test-data/dna/wgs/hiseq2500/NA12878/H06HDADXX130110.1.ATCACGAT.20k_reads.bam)
* `HG00096.mapped.ILLUMINA.bwa.GBR.low_coverage.20120522.bam` is a medium sized "low coverage" Illumina sequencer data set from the initial 1000 Genomes Project
* `HG00096.wgs.ILLUMINA.bwa.GBR.high_cov_pcr_free.20140203.bam` is a large sized "high coverage" Illumina sequencer data from Phase 3 updates to the 1000 Genomes Project

The above files represent real, large genomics files and have been saved to `/scratch/home/jayson/gatk-data` since they are so large (100GB+ for the last one!). These represent one sequencing run of one sample. The full 1000 Genome Project data set has closer to 3,000 total files of this size. Results here help show how well these types of files can be handled.

**URL:** https://software.broadinstitute.org/gatk/

**Team:** Falkners 

## Compilation

GATK has three requirements:
* JDK 1.8+
* [BWA](http://bio-bwa.sourceforge.net/)
* [SAMTools](http://samtools.sourceforge.net/)

BWA and SAMTools are not strictly required for some of the GATK tools; however, GATK's documentation says they should be installed.

### Spack Package Modification

The default spack package will mostly work; however, GATK has several Java-based tools and it needs `bwa` and `samtools`.

##### Add OpenJDK to spack

Upgrading to the latest JVM was done to use the latest updated. The default spack package has OpenJDK11 and the changes below will use OpenJDK16, which is several years worth of improvements.

Diff of interest is shown below.

```
--- a/var/spack/repos/builtin/packages/openjdk/package.py
+++ b/var/spack/repos/builtin/packages/openjdk/package.py
@@ -17,6 +17,9 @@
 #    format returned by platform.system() and 'arch' by platform.machine()

 _versions = {
+    '16.0.1': {
+        'Linux-x86_64': ('b1198ffffb7d26a3fdedc0fa599f60a0d12aa60da1714b56c1defbce95d8b235', 'https://download.java.net/java/GA/jdk16.0.1/7147401fd7354114ac51ef3e1328291f/9/GPL/openjdk-16.0.1_linux-x64_bin.tar.gz'),
+        'Linux-aarch64': ('602b005074777df2a0b4306e20152a6446803edd87ccbab95b2f313c4d9be6ba', 'https://download.java.net/java/GA/jdk16.0.1/7147401fd7354114ac51ef3e1328291f/9/GPL/openjdk-16.0.1_linux-aarch64_bin.tar.gz')},
     '11.0.9.1_1': {
         'Linux-ppc64le': ('d94b6b46a14ab0974b1c1b89661741126d8cf8a0068b471b8f5fa286a71636b1', 'https://github.com/AdoptOpenJDK/openjdk11-binaries/releases/download/jdk-11.0.9.1%2B1/OpenJDK11U-jdk_ppc64le_linux_hotspot_11.0.9.1_1.tar.gz')},
     '11.0.8_10': {
@@ -55,6 +58,7 @@ class Openjdk(Package):
         if pkg:
             version(ver, sha256=pkg[0], url=pkg[1])

+    provides('java@16', when='@16.0:16.99')
     provides('java@11', when='@11.0:11.99')
```

Git commit hash of checkout for pacakage: `667ab501996058b1f89f1763d1791befa455b1f8`

Pull request for Spack recipe changes: https://github.com/spack/spack/pull/24870

##### Require `bwa` and `samtools` via spack package

`bwa` and `samtools` are also needed for some GATK functionality and according to [GATK's best practices](https://gatk.broadinstitute.org/hc/en-us/articles/360041320571--How-to-Install-all-software-packages-required-to-follow-the-GATK-Best-Practices). Below is a diff that adds them to the `spack` package for GATK.

```
diff --git a/var/spack/repos/builtin/packages/gatk/package.py b/var/spack/repos/builtin/packages/gatk/package.py
index f83ead3d2d..6a5348ff49 100644
--- a/var/spack/repos/builtin/packages/gatk/package.py
+++ b/var/spack/repos/builtin/packages/gatk/package.py
@@ -100,6 +100,8 @@ class Gatk(Package):
     # output.
     variant('r', default=False, description='Use R for plotting')

+    depends_on("samtools", type="run")
+    depends_on("bwa", type="run")
     depends_on("java@8", type="run")
     depends_on("python@2.6:2.8,3.6:", type="run", when="@4.0:")
     depends_on("r@3.2:", type="run", when="@4.0: +r")
```

Git commit hash of checkout for pacakage: `667ab501996058b1f89f1763d1791befa455b1f8`

Pull request for Spack recipe changes: https://github.com/spack/spack/pull/24902


### Building GATK

GATK compiled fine with `gcc` on the x86 HPC and with both `gcc` and `arm` on the ARM HPC.

#### Compiler 1

`gcc` on the ARM HPC.
```
spack install gatk@4.1.8.1 %gcc@10.3.0
```

`gcc` dependencies used.
```
[+]  dryvlws  gatk@4.1.8.1%gcc@10.3.0~r arch=linux-amzn2-graviton2
[+]  763lrfl      ^openjdk@1.8.0_191-b12%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  62czasr      ^python@3.8.11%gcc@10.3.0+bz2+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tix~tkinter~ucs4+uuid+zlib patches=0d98e93189bc278fbc37a50ed7f183bd8aaf249a8e1670a465f0db6bb4f8cf87 arch=linux-amzn2-graviton2
[+]  rqrpmap          ^bzip2@1.0.8%gcc@10.3.0~debug~pic+shared arch=linux-amzn2-graviton2
[+]  2w7bert              ^diffutils@3.7%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  y5ei3cm                  ^libiconv@1.16%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  ychdz7l          ^expat@2.4.1%gcc@10.3.0+libbsd arch=linux-amzn2-graviton2
[+]  ourxkez              ^libbsd@0.11.3%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  nssrqfc                  ^libmd@1.0.3%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  wjwqncx          ^gdbm@1.19%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  3zy7kxk              ^readline@8.1%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  iwzirqc                  ^ncurses@6.2%gcc@10.3.0~symlinks+termlib abi=none arch=linux-amzn2-graviton2
[+]  s4pw7zm                      ^pkgconf@1.7.4%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  fqlpcsl          ^gettext@0.21%gcc@10.3.0+bzip2+curses+git~libunistring+libxml2+tar+xz arch=linux-amzn2-graviton2
[+]  iyhm3wi              ^libxml2@2.9.10%gcc@10.3.0~python arch=linux-amzn2-graviton2
[+]  ye3kcvv                  ^xz@5.2.5%gcc@10.3.0~pic libs=shared,static arch=linux-amzn2-graviton2
[+]  qepjcvj                  ^zlib@1.2.11%gcc@10.3.0+optimize+pic+shared arch=linux-amzn2-graviton2
[+]  v6cutkh              ^tar@1.34%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  35cffos          ^libffi@3.3%gcc@10.3.0 patches=26f26c6f29a7ce9bf370ad3ab2610f99365b4bdd7b82e7c31df41a3370d685c0 arch=linux-amzn2-graviton2
[+]  5i3lgfb          ^openssl@1.1.1k%gcc@10.3.0~docs+systemcerts arch=linux-amzn2-graviton2
[+]  4m7exgb              ^perl@5.32.1%gcc@10.3.0+cpanm+shared+threads arch=linux-amzn2-graviton2
[+]  y42m6yr                  ^berkeley-db@18.1.40%gcc@10.3.0+cxx~docs+stl patches=b231fcc4d5cff05e5c3a4814f6a5af0e9a966428dc2176540d2c05aff41de522 arch=linux-amzn2-graviton2
[+]  2q753q6          ^sqlite@3.35.5%gcc@10.3.0+column_metadata+fts~functions~rtree arch=linux-amzn2-graviton2
[+]  2non7qx          ^util-linux-uuid@2.36.2%gcc@10.3.0 arch=linux-amzn2-graviton2```
```

#### Compiler 2

`arm` on the ARM HPC.
```
spack install gatk@4.1.8.1 %arm@21.0.0.879
```

`arm` dependencies used.

```
$ spack spec -Il gatk@4.1.8.1%arm@21.0.0.879

[+]  352aeok  gatk@4.1.8.1%arm@21.0.0.879~r arch=linux-amzn2-aarch64
[+]  pp2djek      ^openjdk@1.8.0_191-b12%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  jk7wv5q      ^python@3.8.11%arm@21.0.0.879+bz2+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tix~tkinter~ucs4+uuid+zlib patches=0d98e93189bc278fbc37a50ed7f183bd8aaf249a8e1670a465f0db6bb4f8cf87 arch=linux-amzn2-aarch64
[+]  z4ybgri          ^bzip2@1.0.8%arm@21.0.0.879~debug~pic+shared arch=linux-amzn2-aarch64
[+]  adtc6yc              ^diffutils@3.7%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  7vnthzn                  ^libiconv@1.16%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  oyfuwk3          ^expat@2.4.1%arm@21.0.0.879+libbsd arch=linux-amzn2-aarch64
[+]  5q4lmyg              ^libbsd@0.11.3%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  srfepw2                  ^libmd@1.0.3%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  645q4qj          ^gdbm@1.19%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  3haw5gt              ^readline@8.1%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  uhtqtlb                  ^ncurses@6.2%arm@21.0.0.879~symlinks+termlib abi=none arch=linux-amzn2-aarch64
[+]  zpuzm23                      ^pkgconf@1.7.4%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  rl3qj47          ^gettext@0.21%arm@21.0.0.879+bzip2+curses+git~libunistring+libxml2+tar+xz arch=linux-amzn2-aarch64
[+]  dypqz2i              ^libxml2@2.9.10%arm@21.0.0.879~python arch=linux-amzn2-aarch64
[+]  zqsab4f                  ^xz@5.2.5%arm@21.0.0.879~pic libs=shared,static arch=linux-amzn2-aarch64
[+]  puuxvg2                  ^zlib@1.2.11%arm@21.0.0.879+optimize+pic+shared arch=linux-amzn2-aarch64
[+]  fohku26              ^tar@1.34%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  far5l4e          ^libffi@3.3%arm@21.0.0.879 patches=26f26c6f29a7ce9bf370ad3ab2610f99365b4bdd7b82e7c31df41a3370d685c0 arch=linux-amzn2-aarch64
[+]  vc3waha          ^openssl@1.1.1k%arm@21.0.0.879~docs+systemcerts arch=linux-amzn2-aarch64
[+]  vv6txro              ^perl@5.32.1%arm@21.0.0.879+cpanm+shared+threads arch=linux-amzn2-aarch64
[+]  33wiajj                  ^berkeley-db@18.1.40%arm@21.0.0.879+cxx~docs+stl patches=b231fcc4d5cff05e5c3a4814f6a5af0e9a966428dc2176540d2c05aff41de522 arch=linux-amzn2-aarch64
[+]  zj3dbdy          ^sqlite@3.35.5%arm@21.0.0.879+column_metadata+fts~functions~rtree arch=linux-amzn2-aarch64
[+]  uflz3t5          ^util-linux-uuid@2.36.2%arm@21.0.0.879 arch=linux-amzn2-aarch64
```


#### Compiler 3

`gcc` was used on the x86 HPC.
```
spack install gatk@4.1.8.1 %gcc@10.3.0
```

x86 `gcc` dependencies used.
```
pack spec -Il gatk@4.1.8.1%gcc@10.3.0

gatk@4.1.8.1%gcc@10.3.0~r arch=linux-amzn2-skylake_avx512
    ^openjdk@1.8.0_265-b01%gcc@10.3.0 arch=linux-amzn2-skylake_avx512
    ^python@3.8.11%gcc@10.3.0+bz2+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tix~tkinter~ucs4+uuid+zlib patches=0d98e93189bc278fbc37a50ed7f183bd8aaf249a8e1670a465f0db6bb4f8cf87 arch=linux-amzn2-skylake_avx512
        ^bzip2@1.0.8%gcc@10.3.0~debug~pic+shared arch=linux-amzn2-skylake_avx512
            ^diffutils@3.7%gcc@10.3.0 arch=linux-amzn2-skylake_avx512
                ^libiconv@1.16%gcc@10.3.0 arch=linux-amzn2-skylake_avx512
        ^expat@2.4.1%gcc@10.3.0+libbsd arch=linux-amzn2-skylake_avx512
            ^libbsd@0.11.3%gcc@10.3.0 arch=linux-amzn2-skylake_avx512
                ^libmd@1.0.3%gcc@10.3.0 arch=linux-amzn2-skylake_avx512
        ^gdbm@1.19%gcc@10.3.0 arch=linux-amzn2-skylake_avx512
            ^readline@8.1%gcc@10.3.0 arch=linux-amzn2-skylake_avx512
                ^ncurses@6.2%gcc@10.3.0~symlinks+termlib abi=none arch=linux-amzn2-skylake_avx512
                    ^pkgconf@1.7.4%gcc@10.3.0 arch=linux-amzn2-skylake_avx512
        ^gettext@0.21%gcc@10.3.0+bzip2+curses+git~libunistring+libxml2+tar+xz arch=linux-amzn2-skylake_avx512
            ^libxml2@2.9.10%gcc@10.3.0~python arch=linux-amzn2-skylake_avx512
                ^xz@5.2.5%gcc@10.3.0~pic libs=shared,static arch=linux-amzn2-skylake_avx512
                ^zlib@1.2.11%gcc@10.3.0+optimize+pic+shared arch=linux-amzn2-skylake_avx512
            ^tar@1.34%gcc@10.3.0 arch=linux-amzn2-skylake_avx512
        ^libffi@3.3%gcc@10.3.0 patches=26f26c6f29a7ce9bf370ad3ab2610f99365b4bdd7b82e7c31df41a3370d685c0 arch=linux-amzn2-skylake_avx512
        ^openssl@1.1.1k%gcc@10.3.0~docs+systemcerts arch=linux-amzn2-skylake_avx512
            ^perl@5.32.1%gcc@10.3.0+cpanm+shared+threads arch=linux-amzn2-skylake_avx512
                ^berkeley-db@18.1.40%gcc@10.3.0+cxx~docs+stl patches=b231fcc4d5cff05e5c3a4814f6a5af0e9a966428dc2176540d2c05aff41de522 arch=linux-amzn2-skylake_avx512
        ^sqlite@3.35.5%gcc@10.3.0+column_metadata+fts~functions~rtree arch=linux-amzn2-skylake_avx512
        ^util-linux-uuid@2.36.2%gcc@10.3.0 arch=linux-amzn2-skylake_avx512
```

## Test Case 1

This confirms that GATK is working by doing a common read analysis of a BAM file using the `ReadCounts` tool that has always been available in GATK. This is run against the small, medium and large sequencing runs noted in the description. This is run on both the ARM and x86 HPC.

```
reframe -c gatk_countreads.py -r --performance-report
```

### Validation

An existing sequencing analysis tool was used to count reads. One of the BAM files is advertised as 20K reads, which will also be 5000000 bases for that sequencing run.

```
spack load samtools

# reads in the "small" BAM
samtools view -c H06HDADXX130110.1.ATCACGAT.20k_reads.bam
20,000
5,000,000 bases

# reads in the "medium" BAM
samtools view -c HG00096.mapped.ILLUMINA.bwa.GBR.low_coverage.20120522.bam
145,063,589
14,506,358,900 bases

# reads in the "large" BAM
samtools view -c HG00096.wgs.ILLUMINA.bwa.GBR.high_cov_pcr_free.20140203.bam
652,944,493 reads
161,506,906,064 bases
```

### ReFrame Output

ARM HPC output 
```
==============================================================================
PERFORMANCE REPORT
------------------------------------------------------------------------------
GATK_gatk_countreads_hiseq_2500_20k_gatk_4_1_8_1_gcc_10_3_0_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Total Time: 0.0 s
------------------------------------------------------------------------------
GATK_gatk_countreads_hiseq_2500_20k_gatk_4_1_8_1_arm_21_0_0_879_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Total Time: 0.0 s
------------------------------------------------------------------------------
GATK_gatk_countreads_1000_genomes_low_coverage_gatk_4_1_8_1_gcc_10_3_0_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Total Time: 414.0 s
------------------------------------------------------------------------------
GATK_gatk_countreads_1000_genomes_low_coverage_gatk_4_1_8_1_arm_21_0_0_879_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Total Time: 408.0 s
------------------------------------------------------------------------------
GATK_gatk_countreads_1000_genomes_high_coverage_gatk_4_1_8_1_gcc_10_3_0_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Total Time: 4488.0 s
------------------------------------------------------------------------------
GATK_gatk_countreads_1000_genomes_high_coverage_gatk_4_1_8_1_arm_21_0_0_879_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Total Time: 4488.0 s
------------------------------------------------------------------------------
```

x86 HPC output

```
==============================================================================
PERFORMANCE REPORT
------------------------------------------------------------------------------
GATK_gatk_countreads_hiseq_2500_20k_gatk_4_1_8_1_gcc_10_3_0_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Total Time: 0.0 s
------------------------------------------------------------------------------
GATK_gatk_countreads_1000_genomes_low_coverage_gatk_4_1_8_1_gcc_10_3_0_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Total Time: 384.0 s
------------------------------------------------------------------------------
GATK_gatk_countreads_1000_genomes_high_coverage_gatk_4_1_8_1_gcc_10_3_0_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Total Time: 3630.0 s
------------------------------------------------------------------------------
```

### On-node Compiler Comparison

Performance comparison of two compilers. 

| BAM | gcc        | arm        |
|-------|------------|------------|
| small   | < sec      |   < sec    |
| medium   |  414 s    |   408 s   |
| large   |   4488 s     |  4488 s  |


### Serial Hot-spot Profile

List of top-10 functions / code locations from a serial profile.

For the C6gn (ARM) here are the top ten application routines, with associated % of runtime for arm. `taskset` is used to limit the JVM to one core. It by default will use and GATK didn't otherwise have a great way to constrain resources.

For the C6gn (ARM) with `arm` compiler, here are the top ten application routines, with associated % of runtime. `taskset` is used to limit JVM/GATK to one core.

Profiling command used:
```
SPACK_DIR=': SPACK_DIR="/scratch/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/gperftoo
ls-2.8.1-nlcrjyzchw37gafuffie7h5vapyl5uhg"
env LD_PRELOAD=$SPACK_DIR/lib/libprofiler.so CPUPROFILE=gatk_arm_countreads_serial.profile taskset --cpu-list 0 gatk --java-options "-Xmx60g" CountReads -I /scratch/home/jayson/gatk-data/H06HDADXX130110.1.ATCACGAT.20k_reads.bam

# its just the JVM!
which gatk
GATK_DIR="/scratch/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/gatk-4.1.8.1
-352aeokyfru4jfjog2pbfwyljkapm5e6/bin/gatk"

JDIR="/scratch/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/openjdk-1.8.0_191-b12-pp2djekneggf2gz7rejcjtdy67ejkuq6"


pprof --text $JDIR/bin/java gatk_arm_countreads.profile | head -n 15

Total: 398 samples
      13   3.3%   3.3%       15   3.8% PhaseChaitin::Split
      10   2.5%   5.8%       10   2.5% SymbolTable::lookup_only
       7   1.8%   7.5%        7   1.8% ContiguousSpace::prepare_for_compaction
       7   1.8%   9.3%        7   1.8% IndexSetIterator::advance_and_next
       7   1.8%  11.1%        7   1.8% inflate_fast
       5   1.3%  12.3%       10   2.5% PhaseChaitin::gather_lrg_masks [clone .constprop.229]
       4   1.0%  13.3%        5   1.3% PhaseIdealLoop::build_loop_late
       4   1.0%  14.3%        4   1.0% __libc_read
       4   1.0%  15.3%        4   1.0% inflate_table
       3   0.8%  16.1%        3   0.8% 0x0000ffff70212ec0
       3   0.8%  16.8%        3   0.8% Arena::contains
       3   0.8%  17.6%       10   2.5% ClassFileParser::parse_method
       3   0.8%  18.3%        3   0.8% ClassFileParser::skip_over_field_signature
       3   0.8%  19.1%        3   0.8% NodeHash::hash_delete
```


### Full Node Hot-spot Profile

List of top-10 functions / code locations from a full node profile.

For the C6gn (ARM) with `arm` compiler, here are the top ten application routines, with associated % of runtime. By default the JVM uses all cores for GATK.

Profiling command used:
```
SPACK_DIR=': SPACK_DIR="/scratch/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/gperftoo
ls-2.8.1-nlcrjyzchw37gafuffie7h5vapyl5uhg"
env LD_PRELOAD=$SPACK_DIR/lib/libprofiler.so CPUPROFILE=gatk_arm_countreads_full.profile gatk --java-options "-Xmx60g" CountReads -I /scratch/home/jayson/gatk-data/H06HDADXX130110.1.ATCACGAT.20k_reads.bam

# its just the JVM!
which gatk
GATK_DIR="/scratch/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/gatk-4.1.8.1
-352aeokyfru4jfjog2pbfwyljkapm5e6/bin/gatk"

JDIR="/scratch/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/openjdk-1.8.0_191-b12-pp2djekneggf2gz7rejcjtdy67ejkuq6"

pprof --text $JDIR/bin/java gatk_arm_countreads_full.profile | head -n 15

Total: 287 samples
       9   3.1%   3.1%       10   3.5% SymbolTable::lookup_only
       9   3.1%   6.3%        9   3.1% __pthread_cond_signal
       6   2.1%   8.4%        6   2.1% inflate_fast
       5   1.7%  10.1%        9   3.1% PhaseChaitin::Split
       4   1.4%  11.5%        4   1.4% readCEN
       3   1.0%  12.5%        3   1.0% 0x0000ffff904feb04
       3   1.0%  13.6%        3   1.0% 0x0000ffffa1c4d48c
       3   1.0%  14.6%        3   1.0% Compile::identify_useful_nodes
       3   1.0%  15.7%        3   1.0% IndexSetIterator::advance_and_next
       3   1.0%  16.7%        3   1.0% NTarjan::DFS
       3   1.0%  17.8%        8   2.8% PhaseChaitin::build_ifg_physical
       3   1.0%  18.8%        3   1.0% PhaseChaitin::elide_copy
       3   1.0%  19.9%        3   1.0% PhaseChaitin::interfere_with_live
       3   1.0%  20.9%        3   1.0% RegMask::Size

```

### Strong Scaling Study

No strong study was done for GATK.


### Off-Node Scaling Study

Off-node scaling study was not performed.

### On-Node Architecture Comparison

On-node scaling study for two architectures.

| Cores | C6gn (Aarch64) | C5n (X86) |
|-------|------------|------------|
| small   | < sec      |   < sec    |
| medium   |  414 s    |  384 s   |
| large   |   4488 s     |  3630 s  |

WIP: can also hacky test scaling JVM with `taskset --cpu-list 0 gatk <tool ... >` etc

| Cores | C6gn (Aarch64) | C5n (X86) |
|-------|----------------|-----------|
| 1     |                |           |
| 2     |                |           |
| 4     |                |           |
| 8     |                |           |
| 16    |                |           |
| 32    |                |           |
| 64    |                |           |


## Test Case 2

This confirms that GATK is working by doing a common read analysis of a BAM file using the `ReadCountsSpark` tool that was added in GATK4. This is run against the small, medium and large sequencing runs noted in the description. This is run on both the ARM and x86 HPC. This tool is used in a similar way as `ReadCount` but it is distinct and has distinct output.

```
reframe -c gatk_countbases.py -r --performance-report
```

### Validation

Expected base counts were manually collected using samtools.

### ReFrame Output

ARM HPC output after `gcc` compile.
```
==============================================================================
PERFORMANCE REPORT
------------------------------------------------------------------------------
GATK_gatk_countreadsspark_hiseq_2500_20k_gatk_4_1_8_1_gcc_10_3_0_N_1_MPI_1_OMP_1
- aws:c6gn
   - builtin
      * num_tasks: 1
      * Total Time: 0.545348 s
------------------------------------------------------------------------------
GATK_gatk_countreadsspark_hiseq_2500_20k_gatk_4_1_8_1_arm_21_0_0_879_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Total Time: 0.512613 s
------------------------------------------------------------------------------
GATK_gatk_countreadsspark_1000_genomes_low_coverage_gatk_4_1_8_1_gcc_10_3_0_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Total Time: 302.355639 s
------------------------------------------------------------------------------
GATK_gatk_countreadsspark_1000_genomes_low_coverage_gatk_4_1_8_1_arm_21_0_0_879_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Total Time: 302.264508 s
------------------------------------------------------------------------------
GATK_gatk_countreadsspark_1000_genomes_high_coverage_gatk_4_1_8_1_gcc_10_3_0_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Total Time: 3231.738226 s
------------------------------------------------------------------------------
GATK_gatk_countreadsspark_1000_genomes_high_coverage_gatk_4_1_8_1_arm_21_0_0_879_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Total Time: 3234.871644 s
------------------------------------------------------------------------------
```

x86 HPC output after `gcc` compile.

```
==============================================================================
PERFORMANCE REPORT
------------------------------------------------------------------------------
GATK_gatk_countreadsspark_hiseq_2500_20k_gatk_4_1_8_1_gcc_10_3_0_N_1_MPI_1_OMP_1
- aws:c5n
   - builtin
      * num_tasks: 1
      * Total Time: 0.399857 s
------------------------------------------------------------------------------
GATK_gatk_countreadsspark_1000_genomes_low_coverage_gatk_4_1_8_1_gcc_10_3_0_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Total Time: 281.917648 s
------------------------------------------------------------------------------
GATK_gatk_countreadsspark_1000_genomes_high_coverage_gatk_4_1_8_1_gcc_10_3_0_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Total Time: 2835.658355 s
------------------------------------------------------------------------------
```

### On-node Compiler Comparison

`gcc@10.3.0` was compared against `arm@21.0.0.879`. 

| BAM | gcc        | arm        |
|-------|------------|------------|
| small   | 0.54 s      |   0.51 s    |
| medium   |  302.35 s  |   302.26 s   |
| large   |  3231.73 s  | 3234.87 s   |


### Serial Hot-spot Profile

List of top-10 functions / code locations from a serial profile.

For the C6gn (ARM) with `arm` compiler, here are the top ten application routines, with associated % of runtime. `taskset` is used to limit JVM/GATK to one core.

Profiling command used:
```
SPACK_DIR=': SPACK_DIR="/scratch/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/gperftoo
ls-2.8.1-nlcrjyzchw37gafuffie7h5vapyl5uhg"
env LD_PRELOAD=$SPACK_DIR/lib/libprofiler.so CPUPROFILE=gatk_arm_countreadsspark_serial.profile taskset --cpu-list 0 gatk --java-options "-Xmx60g" CountReadsSpark -I /scratch/home/jayson/gatk-data/H06HDADXX130110.1.ATCACGAT.20k_reads.bam

# its just the JVM!
which gatk
GATK_DIR="/scratch/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/gatk-4.1.8.1
-352aeokyfru4jfjog2pbfwyljkapm5e6/bin/gatk"

JDIR="/scratch/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/openjdk-1.8.0_191-b12-pp2djekneggf2gz7rejcjtdy67ejkuq6"

pprof --text $JDIR/bin/java gatk_arm_countreadsspark_serial.profile | h
ead -n 15

Total: 849 samples
      28   3.3%   3.3%       28   3.3% inflate_fast
      26   3.1%   6.4%       34   4.0% SymbolTable::lookup_only
      21   2.5%   8.8%       25   2.9% PhaseChaitin::Split
      14   1.6%  10.5%       14   1.6% __GI___clone
      10   1.2%  11.7%       10   1.2% IndexSetIterator::advance_and_next
       9   1.1%  12.7%        9   1.1% ContiguousSpace::prepare_for_compaction
       9   1.1%  13.8%       13   1.5% PhaseChaitin::interfere_with_live
       8   0.9%  14.7%       30   3.5% PhaseChaitin::build_ifg_physical
       8   0.9%  15.7%       13   1.5% PhaseIdealLoop::build_loop_early
       8   0.9%  16.6%        8   0.9% __libc_read
       7   0.8%  17.4%        8   0.9% SymbolTable::lookup@8db5f0
       6   0.7%  18.1%        6   0.7% Node_Backward_Iterator::next
       6   0.7%  18.8%        6   0.7% PhaseChaitin::elide_copy
       6   0.7%  19.6%       18   2.1% PhaseIdealLoop::build_loop_late
```


### Full Node Hot-spot Profile

List of top-10 functions / code locations from a full node profile.

For the C6gn (ARM) with `arm` compiler, here are the top ten application routines, with associated % of runtime. By default the JVM uses all cores for GATK.

Profiling command used:
```
SPACK_DIR=': SPACK_DIR="/scratch/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/gperftoo
ls-2.8.1-nlcrjyzchw37gafuffie7h5vapyl5uhg"
env LD_PRELOAD=$SPACK_DIR/lib/libprofiler.so CPUPROFILE=gatk_arm_countreadsspark_full.profile gatk --java-options "-Xmx60g" CountReadsSpark -I /scratch/home/jayson/gatk-data/H06HDADXX130110.1.ATCACGAT.20k_reads.bam

# its just the JVM!
which gatk
GATK_DIR="/scratch/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/gatk-4.1.8.1
-352aeokyfru4jfjog2pbfwyljkapm5e6/bin/gatk"

JDIR="/scratch/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/openjdk-1.8.0_191-b12-pp2djekneggf2gz7rejcjtdy67ejkuq6"

pprof --text $JDIR/bin/java gatk_arm_countreadsspark_full.profile | head -n 15

Total: 589 samples
      18   3.1%   3.1%       21   3.6% PhaseChaitin::Split
      18   3.1%   6.1%       22   3.7% SymbolTable::lookup_only
      15   2.5%   8.7%       15   2.5% inflate_fast
      10   1.7%  10.4%       10   1.7% IndexSetIterator::advance_and_next
       8   1.4%  11.7%        9   1.5% __pthread_cond_signal
       7   1.2%  12.9%        7   1.2% PhaseChaitin::elide_copy
       7   1.2%  14.1%        7   1.2% ThreadStateTransition::transition_from_native [clone .constprop.235]
       7   1.2%  15.3%        7   1.2% binary_search
       7   1.2%  16.5%       25   4.2% inflate
       5   0.8%  17.3%        5   0.8% Symbol::equals
       5   0.8%  18.2%        5   0.8% SymbolTable::lookup@8db5f0
       5   0.8%  19.0%        5   0.8% __GI_memset
       5   0.8%  19.9%        5   0.8% _int_free
       4   0.7%  20.5%        4   0.7% ClassFileParser::verify_legal_utf8
```

### Strong Scaling Study

Strong scaling study was not performed.

### Off-Node Scaling Study

Off-node scaling study was not performed.

### On-Node Architecture Comparison

On-node scaling study for two architectures.

| Cores | C6gn (Aarch64) | C5n (X86) |
|-------|------------|------------|
| small   | 0.54 s      |  0.39 s    |
| medium   |  302.35 s  |  281.91 s    |
| large   |  3231.73 s  |  2835.65 s  |

WIP: can also test scaling JVM with `taskset --cpu-list 0 gatk <tool ... >` etc

| Cores | C6gn (Aarch64) | C5n (X86) |
|-------|----------------|-----------|
| 1     |                |           |
| 2     |                |           |
| 4     |                |           |
| 8     |                |           |
| 16    |                |           |
| 32    |                |           |
| 64    |                |           |


## Test Case 3

This confirms that GATK is working by doing a common read analysis of base pairs in a BAM file using the `BaseCounts` tool that has been in all versions of GATK. This is run against the small, medium and large sequencing runs noted in the description. This is run on both the ARM and x86 HPC.

```
reframe -c gatk_countbases.py -r --performance-report
```

### Validation

Expected base counts were manually collected using samtools.

### ReFrame Output

ARM HPC output after `gcc` compile.
```
==============================================================================
PERFORMANCE REPORT
------------------------------------------------------------------------------
GATK_gatk_countbases_hiseq_2500_20k_gatk_4_1_8_1_gcc_10_3_0_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Total Time: 0.0 s
------------------------------------------------------------------------------
GATK_gatk_countbases_hiseq_2500_20k_gatk_4_1_8_1_arm_21_0_0_879_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Total Time: 0.0 s
------------------------------------------------------------------------------
GATK_gatk_countbases_1000_genomes_low_coverage_gatk_4_1_8_1_gcc_10_3_0_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Total Time: 408.0 s
------------------------------------------------------------------------------
GATK_gatk_countbases_1000_genomes_low_coverage_gatk_4_1_8_1_arm_21_0_0_879_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Total Time: 408.0 s
------------------------------------------------------------------------------
GATK_gatk_countbases_1000_genomes_high_coverage_gatk_4_1_8_1_gcc_10_3_0_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Total Time: 4488.0 s
------------------------------------------------------------------------------
GATK_gatk_countbases_1000_genomes_high_coverage_gatk_4_1_8_1_arm_21_0_0_879_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Total Time: 4488.0 s
------------------------------------------------------------------------------
```

x86 HPC output after `gcc` compile.

```
==============================================================================
PERFORMANCE REPORT
------------------------------------------------------------------------------
GATK_gatk_countbases_hiseq_2500_20k_gatk_4_1_8_1_gcc_10_3_0_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Total Time: 0.0 s
------------------------------------------------------------------------------
GATK_gatk_countbases_1000_genomes_low_coverage_gatk_4_1_8_1_gcc_10_3_0_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Total Time: 486.0 s
------------------------------------------------------------------------------
GATK_gatk_countbases_1000_genomes_high_coverage_gatk_4_1_8_1_gcc_10_3_0_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Total Time: 4374.0 s
------------------------------------------------------------------------------
```

### On-node Compiler Comparison

`gcc@10.3.0` was compared against `arm@21.0.0.879`.

| BAM | gcc        | arm        |
|-------|------------|------------|
| small   | < 1 s     | < 1 s    |
| medium   | 408 s  |   408 s   |
| large   |  4488 s  | 4488 s   |

### Serial Hot-spot Profile

List of top-10 functions / code locations from a serial profile.

For the C6gn (ARM) with `arm` compiler, here are the top ten application routines, with associated % of runtime. `taskset` is used to limit JVM/GATK to one core.

Profiling command used:
```
SPACK_DIR=': SPACK_DIR="/scratch/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/gperftoo
ls-2.8.1-nlcrjyzchw37gafuffie7h5vapyl5uhg"
env LD_PRELOAD=$SPACK_DIR/lib/libprofiler.so CPUPROFILE=gatk_arm_countbases_serial.profile taskset --cpu-list 0 gatk --java-options "-Xmx60g" CountBasesSpark -I /scratch/home/jayson/gatk-data/H06HDADXX130110.1.ATCACGAT.20k_reads.bam

# its just the JVM!
which gatk
GATK_DIR="/scratch/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/gatk-4.1.8.1
-352aeokyfru4jfjog2pbfwyljkapm5e6/bin/gatk"

JDIR="/scratch/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/openjdk-1.8.0_191-b12-pp2djekneggf2gz7rejcjtdy67ejkuq6"

pprof --text $JDIR/bin/java gatk_arm_countbases_serial.profile | head -n 15

Total: 866 samples
      30   3.5%   3.5%       33   3.8% SymbolTable::lookup_only
      22   2.5%   6.0%       22   2.5% inflate_fast
      20   2.3%   8.3%       28   3.2% PhaseChaitin::Split
      15   1.7%  10.0%       15   1.7% __GI___clone
      13   1.5%  11.5%       13   1.5% IndexSetIterator::advance_and_next
      11   1.3%  12.8%       13   1.5% PhaseChaitin::elide_copy
      10   1.2%  14.0%       10   1.2% __GI_memset
      10   1.2%  15.1%       10   1.2% inflate_table
       9   1.0%  16.2%       20   2.3% PhaseIdealLoop::build_loop_late
       9   1.0%  17.2%        9   1.0% resource_allocate_bytes
       8   0.9%  18.1%       23   2.7% PhaseChaitin::build_ifg_physical
       8   0.9%  19.1%       11   1.3% PhaseIdealLoop::build_loop_early
       7   0.8%  19.9%        9   1.0% ContiguousSpace::prepare_for_compaction
       7   0.8%  20.7%       39   4.5% inflate
```


### Full Node Hot-spot Profile

List of top-10 functions / code locations from a full node profile.

For the C6gn (ARM) with `arm` compiler, here are the top ten application routines, with associated % of runtime. By default the JVM uses all cores for GATK.

Profiling command used:
```
SPACK_DIR=': SPACK_DIR="/scratch/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/gperftoo
ls-2.8.1-nlcrjyzchw37gafuffie7h5vapyl5uhg"
env LD_PRELOAD=$SPACK_DIR/lib/libprofiler.so CPUPROFILE=gatk_arm_countbases_full.profile gatk --java-options "-Xmx60g" CountBasesSpark -I /scratch/home/jayson/gatk-data/H06HDADXX130110.1.ATCACGAT.20k_reads.bam

# its just the JVM!
which gatk
GATK_DIR="/scratch/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/gatk-4.1.8.1
-352aeokyfru4jfjog2pbfwyljkapm5e6/bin/gatk"

JDIR="/scratch/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/openjdk-1.8.0_191-b12-pp2djekneggf2gz7rejcjtdy67ejkuq6"

pprof --text $JDIR/bin/java gatk_arm_countbases_full.profile | head -n 15

Total: 599 samples
      23   3.8%   3.8%       25   4.2% SymbolTable::lookup_only
      17   2.8%   6.7%       17   2.8% inflate_fast
      15   2.5%   9.2%       21   3.5% PhaseChaitin::Split
      10   1.7%  10.9%       10   1.7% IndexSetIterator::advance_and_next
      10   1.7%  12.5%       11   1.8% __pthread_cond_signal
       9   1.5%  14.0%       33   5.5% inflate
       8   1.3%  15.4%        9   1.5% Dictionary::find
       8   1.3%  16.7%       12   2.0% SymbolTable::lookup@8db5f0
       8   1.3%  18.0%        8   1.3% __memcpy_simd
       8   1.3%  19.4%        9   1.5% resource_allocate_bytes
       7   1.2%  20.5%        7   1.2% ClassFileParser::verify_legal_utf8
       7   1.2%  21.7%        7   1.2% Symbol::equals
       6   1.0%  22.7%        6   1.0% ClassFileParser::skip_over_field_signature
       6   1.0%  23.7%       18   3.0% PhaseChaitin::build_ifg_physical
```


### Strong Scaling Study

On-node scaling was not done.

### Off-Node Scaling Study

Off-node scaling study was not performed.

### On-Node Architecture Comparison

On-node scaling study for two architectures.

| Cores | C6gn (Aarch64) | C5n (X86) |
|-------|------------|------------|
| small   | < 1 s     | < 1 s    |
| medium   | 408 s  |  486 s   |
| large   |  4488 s  | 4374 s   |

WIP: can also test scaling JVM with `taskset --cpu-list 0 gatk <tool ... >` etc

| Cores | C6gn (Aarch64) | C5n (X86) |
|-------|----------------|-----------|
| 1     |                |           |
| 2     |                |           |
| 4     |                |           |
| 8     |                |           |
| 16    |                |           |
| 32    |                |           |
| 64    |                |           |



## Test Case 4

[ReFrame Benchmark 4](#)

This confirms that GATK is working by doing a common read analysis of base counts from a BAM file using the `BaseCountsSpark` tool that was added in GATK4. This is run against the small, medium and large sequencing runs noted in the description. This is run on both the ARM and x86 HPC. This tool is used in a similar way as `BaseCount` but it is distinct and has distinct output.

```
reframe -c gatk_countbases.py -r --performance-report
```

### Validation

Expected base counts were manually collected using samtools.

### ReFrame Output

Output from the ARM HPC
```
==============================================================================
PERFORMANCE REPORT
------------------------------------------------------------------------------
GATK_gatk_countbasesspark_hiseq_2500_20k_gatk_4_1_8_1_gcc_10_3_0_N_1_MPI_1_OMP_1
- aws:c6gn
   - builtin
      * num_tasks: 1
      * Total Time: 0.689159 s
------------------------------------------------------------------------------
GATK_gatk_countbasesspark_hiseq_2500_20k_gatk_4_1_8_1_arm_21_0_0_879_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Total Time: 0.68249 s
------------------------------------------------------------------------------
GATK_gatk_countbasesspark_1000_genomes_low_coverage_gatk_4_1_8_1_gcc_10_3_0_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Total Time: 454.830457 s
------------------------------------------------------------------------------
GATK_gatk_countbasesspark_1000_genomes_low_coverage_gatk_4_1_8_1_arm_21_0_0_879_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Total Time: 461.68703 s
------------------------------------------------------------------------------
GATK_gatk_countbases_1000_genomes_high_coverage_gatk_4_1_8_1_gcc_10_3_0_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Total Time: 4488.0 s
------------------------------------------------------------------------------
GATK_gatk_countbases_1000_genomes_high_coverage_gatk_4_1_8_1_arm_21_0_0_879_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Total Time: 4488.0 s
------------------------------------------------------------------------------
```

Output from the ARM HPC

```
==============================================================================
PERFORMANCE REPORT
------------------------------------------------------------------------------
GATK_gatk_countbasesspark_hiseq_2500_20k_gatk_4_1_8_1_gcc_10_3_0_N_1_MPI_1_OMP_1
- aws:c5n
   - builtin
      * num_tasks: 1
      * Total Time: 0.544623 s
------------------------------------------------------------------------------
GATK_gatk_countbasesspark_1000_genomes_low_coverage_gatk_4_1_8_1_gcc_10_3_0_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Total Time: 505.129401 s
------------------------------------------------------------------------------
GATK_gatk_countbasesspark_1000_genomes_high_coverage_gatk_4_1_8_1_gcc_10_3_0_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Total Time: 78.0 m
------------------------------------------------------------------------------
```

### On-node Compiler Comparison

`gcc@10.3.0` was compared against `arm@21.0.0.879`.

| BAM | gcc        | arm        |
|-------|------------|------------|
| small   | < 0.69 s     | < 0.68 s    |
| medium   | 454.83 s  |   461.68 s   |
| large   |  4488 s  | 4488 s   |


### Serial Hot-spot Profile

List of top-10 functions / code locations from a serial profile.

For the C6gn (ARM) with `arm` compiler, here are the top ten application routines, with associated % of runtime. `taskset` is used to limit JVM/GATK to one core.

Profiling command used:
```
SPACK_DIR=': SPACK_DIR="/scratch/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/gperftoo
ls-2.8.1-nlcrjyzchw37gafuffie7h5vapyl5uhg"
env LD_PRELOAD=$SPACK_DIR/lib/libprofiler.so CPUPROFILE=gatk_arm_countbasesspark_serial.profile taskset --cpu-list 0 gatk --java-options "-Xmx60g" CountBasesSpark -I /scratch/home/jayson/gatk-data/H06HDADXX130110.1.ATCACGAT.20k_reads.bam

# its just the JVM!
which gatk
GATK_DIR="/scratch/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/gatk-4.1.8.1
-352aeokyfru4jfjog2pbfwyljkapm5e6/bin/gatk"

JDIR="/scratch/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/openjdk-1.8.0_191-b12-pp2djekneggf2gz7rejcjtdy67ejkuq6"

pprof --text $JDIR/bin/java gatk_arm_countbasesspark_serial.profile | head -n 15

Total: 849 samples
      30   3.5%   3.5%       33   3.9% SymbolTable::lookup_only
      22   2.6%   6.1%       22   2.6% inflate_fast
      20   2.4%   8.5%       20   2.4% __GI___clone
      15   1.8%  10.2%       19   2.2% PhaseChaitin::Split
      12   1.4%  11.7%       12   1.4% IndexSetIterator::advance_and_next
      11   1.3%  13.0%       15   1.8% PhaseChaitin::gather_lrg_masks [clone .constprop.229]
      10   1.2%  14.1%       13   1.5% PhaseIdealLoop::build_loop_early
       9   1.1%  15.2%       22   2.6% PhaseChaitin::build_ifg_physical
       9   1.1%  16.3%       12   1.4% PhaseChaitin::interfere_with_live
       8   0.9%  17.2%        8   0.9% SymbolTable::lookup@8db5f0
       8   0.9%  18.1%       35   4.1% inflate
       7   0.8%  19.0%        7   0.8% ContiguousSpace::prepare_for_compaction
       7   0.8%  19.8%       14   1.6% PhaseChaitin::post_allocate_copy_removal
       7   0.8%  20.6%       17   2.0% PhaseLive::compute
```


### Full Node Hot-spot Profile

List of top-10 functions / code locations from a full node profile.

For the C6gn (ARM) with `arm` compiler, here are the top ten application routines, with associated % of runtime. By default the JVM uses all cores for GATK.

Profiling command used:
```
SPACK_DIR=': SPACK_DIR="/scratch/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/gperftoo
ls-2.8.1-nlcrjyzchw37gafuffie7h5vapyl5uhg"
env LD_PRELOAD=$SPACK_DIR/lib/libprofiler.so CPUPROFILE=gatk_arm_countbasesspark_full.profile gatk --java-options "-Xmx60g" CountBasesSpark -I /scratch/home/jayson/gatk-data/H06HDADXX130110.1.ATCACGAT.20k_reads.bam

# its just the JVM!
which gatk
GATK_DIR="/scratch/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/gatk-4.1.8.1
-352aeokyfru4jfjog2pbfwyljkapm5e6/bin/gatk"

JDIR="/scratch/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/openjdk-1.8.0_191-b12-pp2djekneggf2gz7rejcjtdy67ejkuq6"

pprof --text $JDIR/bin/java gatk_arm_countbasesspark_full.profile | head -n 15

Total: 592 samples
      24   4.1%   4.1%       30   5.1% SymbolTable::lookup_only
      15   2.5%   6.6%       15   2.5% inflate_fast
      10   1.7%   8.3%       12   2.0% PhaseChaitin::Split
       8   1.4%   9.6%        8   1.4% IndexSetIterator::advance_and_next
       8   1.4%  11.0%        8   1.4% __GI_memset
       8   1.4%  12.3%        8   1.4% __pthread_mutex_unlock_usercnt
       7   1.2%  13.5%        7   1.2% PhaseIdealLoop::is_dominator
       7   1.2%  14.7%        7   1.2% RelocIterator::set_limits
       7   1.2%  15.9%        7   1.2% __pthread_cond_signal
       7   1.2%  17.1%        7   1.2% binary_search
       6   1.0%  18.1%        6   1.0% Dictionary::find
       6   1.0%  19.1%        6   1.0% Symbol::equals
       6   1.0%  20.1%       26   4.4% inflate
       5   0.8%  20.9%        5   0.8% SignatureVerifier::is_valid_type
```

### Strong Scaling Study

On-node scaling study for two compilers was not done for this test.

### Off-Node Scaling Study

Off-node scaling study comparing C6g and C6gn instances was not done for this test.

### On-Node Architecture Comparison

On-node scaling study for two architectures.
| BAM size | C6gn (Aarch64) | C5n (X86) |
|-------|------------|------------|
| small   | < 0.69 s     | < 0.54 s    |
| medium   | 454.83 s  |   505.12 s   |
| large   |  4488 s  | 4680 s   |

WIP: can scale using taskset

| Cores | C6gn (Aarch64) | C5n (X86) |
|-------|----------------|-----------|
| 1     |                |           |
| 2     |                |           |
| 4     |                |           |
| 8     |                |           |
| 16    |                |           |
| 32    |                |           |
| 64    |                |           |

## Test Case 5

This confirms that GATK is working by doing a common quality control cleanup of a BAM file using the `MarkDuplicatesSpark` tool that has always been available in GATK. This is run against the small, medium and large sequencing runs noted in the description. This is run on both the ARM and x86 HPC. Both C5n and C6gn.

```
reframe -c gatk_dedup_small.py -r --performance-report
reframe -c gatk_dedup_medium.py -r --performance-report
reframe -c gatk_dedup_large.py -r --performance-report
```

### Validation

The ReFrame test looks for the sucess status of the de-duplication run. Manual analysis was also done to verify that metrics files are produced correctly.

### ReFrame Output

ARM HPC output 
```
# from "small" dataset
==============================================================================
PERFORMANCE REPORT
------------------------------------------------------------------------------
GATK_gatk_dedup_small_gatk_4_1_8_1_gcc_10_3_0_N_1_MPI_1_OMP_1
- aws:c6gn
   - builtin
      * num_tasks: 1
      * Total Time: 0.2 m
------------------------------------------------------------------------------
GATK_gatk_dedup_small_gatk_4_1_8_1_arm_21_0_0_879_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Total Time: 0.22 m
------------------------------------------------------------------------------

# from "medium"
==============================================================================
PERFORMANCE REPORT
------------------------------------------------------------------------------
GATK_gatk_dedup_medium_gatk_4_1_8_1_gcc_10_3_0_N_1_MPI_1_OMP_1
- aws:c6gn
   - builtin
      * num_tasks: 1
      * Total Time: 12.29 m
------------------------------------------------------------------------------
GATK_gatk_dedup_medium_gatk_4_1_8_1_arm_21_0_0_879_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Total Time: 12.28 m
------------------------------------------------------------------------------

# from "large" dataset
==============================================================================
PERFORMANCE REPORT
------------------------------------------------------------------------------
GATK_gatk_dedup_large_gatk_4_1_8_1_gcc_10_3_0_N_1_MPI_1_OMP_1
- aws:c6gn
   - builtin
      * num_tasks: 1
      * Total Time: 59.54 m
------------------------------------------------------------------------------
GATK_gatk_dedup_large_gatk_4_1_8_1_arm_21_0_0_879_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Total Time: 59.55 m
------------------------------------------------------------------------------
```

x86 HPC output

```
# from "small" dataset
==============================================================================
PERFORMANCE REPORT
------------------------------------------------------------------------------
GATK_gatk_dedup_small_gatk_4_1_8_1_gcc_10_3_0_N_1_MPI_1_OMP_1
- aws:c5n
   - builtin
      * num_tasks: 1
      * Total Time: 0.18 m
------------------------------------------------------------------------------

# from "medium" dataset
==============================================================================
PERFORMANCE REPORT
------------------------------------------------------------------------------
GATK_gatk_dedup_medium_gatk_4_1_8_1_gcc_10_3_0_N_1_MPI_1_OMP_1
- aws:c5n
   - builtin
      * num_tasks: 1
      * Total Time: 18.97 m
------------------------------------------------------------------------------

# from "large" dataset
==============================================================================
PERFORMANCE REPORT
------------------------------------------------------------------------------
GATK_gatk_dedup_large_gatk_4_1_8_1_gcc_10_3_0_N_1_MPI_1_OMP_1
- aws:c5n
   - builtin
      * num_tasks: 1
      * Total Time: 45.81 s
------------------------------------------------------------------------------
```

### On-node Compiler Comparison

Performance comparison of two compilers. 

TODO
| BAM | gcc        | arm        |
|-------|------------|------------|
| small   | 0.2 m      |  0.22 m     |
| medium   |  12.29 m    |  12.28 m     |
| large   |   59.54 m     |  59.55 m  |


### Serial Hot-spot Profile

List of top-10 functions / code locations from a serial profile.

For the C6gn (ARM) here are the top ten application routines, with associated % of runtime for arm. `taskset` is used to limit the JVM to one core. It by default will use and GATK didn't otherwise have a great way to constrain resources.

Profiling command used:
```
SPACK_DIR=': SPACK_DIR="/scratch/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/gperftoo
ls-2.8.1-nlcrjyzchw37gafuffie7h5vapyl5uhg"
env LD_PRELOAD=$SPACK_DIR/lib/libprofiler.so CPUPROFILE=gatk_arm.profile taskset --cpu-list 0 gatk --java-options "-Xmx60g" MarkDuplicatesSpark -I /scratch/home/jayson/gatk-data/H06HDADXX130110.1.ATCACGAT.20k_reads.bam -O test.bam -M test_metrics.txt

# its just the JVM!
which gatk
GATK_DIR="/scratch/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/gatk-4.1.8.1
-352aeokyfru4jfjog2pbfwyljkapm5e6/bin/gatk"

JDIR="/scratch/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/openjdk-1.8.0_191-b12-pp2djekneggf2gz7rejcjtdy67ejkuq6"

pprof --text $JDIR/bin/java gatk_arm.profile | head -n 15

Total: 1225 samples
      32   2.6%   2.6%       42   3.4% SymbolTable::lookup_only
      31   2.5%   5.1%       31   2.5% __GI___clone
      27   2.2%   7.3%       27   2.2% PhaseIdealLoop::is_dominator
      27   2.2%   9.6%       27   2.2% inflate_fast
      25   2.0%  11.6%       34   2.8% PhaseChaitin::Split
      23   1.9%  13.5%       23   1.9% IndexSetIterator::advance_and_next
      16   1.3%  14.8%       43   3.5% PhaseChaitin::build_ifg_physical
      16   1.3%  16.1%       19   1.6% PhaseChaitin::interfere_with_live
      16   1.3%  17.4%       16   1.3% Symbol::equals
      15   1.2%  18.6%       17   1.4% PhaseChaitin::elide_copy
      12   1.0%  19.6%       13   1.1% PhaseIdealLoop::build_loop_early
      11   0.9%  20.5%       20   1.6% PhaseLive::compute
      10   0.8%  21.3%       10   0.8% __GI_memset
      10   0.8%  22.1%       10   0.8% longest_match
```


### Full Node Hot-spot Profile

List of top-10 functions / code locations from a full node profile.

For the C6gn (ARM) here are the top ten application routines, with associated % of runtime for arm. By default the JVM uses all cores for GATK.

Profiling command used:
```
SPACK_DIR=': SPACK_DIR="/scratch/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/gperftoo
ls-2.8.1-nlcrjyzchw37gafuffie7h5vapyl5uhg"
env LD_PRELOAD=$SPACK_DIR/lib/libprofiler.so CPUPROFILE=gatk_arm.profile gatk --java-options "-Xmx60g" MarkDuplicatesSpark -I /scratch/home/jayson/gatk-data/H06HDADXX130110.1.ATCACGAT.20k_reads.bam -O test.bam -M test_metrics.txt

# its just the JVM!
which gatk
GATK_DIR="/scratch/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/gatk-4.1.8.1
-352aeokyfru4jfjog2pbfwyljkapm5e6/bin/gatk"

JDIR="/scratch/opt/spack/linux-amzn2-aarch64/arm-21.0.0.879/openjdk-1.8.0_191-b12-pp2djekneggf2gz7rejcjtdy67ejkuq6"

pprof --text $JDIR/bin/java gatk_arm.profile | head -n 15

Total: 835 samples
      34   4.1%   4.1%       37   4.4% SymbolTable::lookup_only
      20   2.4%   6.5%       34   4.1% PhaseChaitin::Split
      20   2.4%   8.9%       22   2.6% __pthread_cond_signal
      17   2.0%  10.9%       17   2.0% IndexSetIterator::advance_and_next
      13   1.6%  12.5%       13   1.6% inflate_fast
      12   1.4%  13.9%       12   1.4% PhaseIdealLoop::is_dominator
      10   1.2%  15.1%       12   1.4% PhaseChaitin::elide_copy
       9   1.1%  16.2%        9   1.1% __GI_memset
       8   1.0%  17.1%       11   1.3% PhaseIdealLoop::build_loop_early
       8   1.0%  18.1%       10   1.2% PhaseLive::compute
       8   1.0%  19.0%        8   1.0% RegMask::Size
       8   1.0%  20.0%        8   1.0% RelocIterator::set_limits
       7   0.8%  20.8%       10   1.2% PhaseChaitin::interfere_with_live
       7   0.8%  21.7%       21   2.5% PhaseChaitin::post_allocate_copy_removal
```

### Strong Scaling Study

No strong study was done for GATK.


### Off-Node Scaling Study

Off-node scaling study was not performed.

### On-Node Architecture Comparison

On-node scaling study for two architectures with `gcc` as the compiler.

| Cores | C6gn (Aarch64) | C5n (X86) |
|-------|------------|------------|
| small   | 0.2 m      |  0.18 m     |
| medium   | 18.97 m     |   12.28 m   |
| large   |   59.54 m     |  45.81 m  |


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

Two targets were identified for optimization: OpenJDK and the hardware accelerated deflater replacement (aka "IntelDeflator"). Time only permitted to focus on one. OpenJDK was picked and the goal was to test using the latest ARM compile of Java. Time permitted, test out compile options for it too.

Initial install of OpenJDK16 (note the existing spack install is OpenJDK11 -- several years old!) is the first task. ARM is targeted since it can potentially speed up the most and is a focus of the a-hug event. After install, testing compiler flags, namely `–mcpu=native`.

```
# install ARM with the latest JDK
spack install gatk%arm ^openjdk@16.0.1%arm

# check the dependencies are now for OpenJDK
spack spec -Il gatk@4.1.8.1%arm
Input spec
--------------------------------
 -   gatk@4.1.8.1%arm

Concretized
--------------------------------
==> Warning: arm@21.0.0.879 cannot build optimized binaries for "graviton2". Using best target possible: "aarch64"
[+]  six5xcj  gatk@4.1.8.1%arm@21.0.0.879~r arch=linux-amzn2-aarch64
[+]  ssljwi4      ^openjdk@16.0.1%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  jk7wv5q      ^python@3.8.11%arm@21.0.0.879+bz2+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tix~tkinter~ucs4+uuid+zlib patches=0d98e93189bc278fbc37a50ed7f183bd8aaf249a8e1670a465f0db6bb4f8cf87 arch=linux-amzn2-aarch64
[+]  z4ybgri          ^bzip2@1.0.8%arm@21.0.0.879~debug~pic+shared arch=linux-amzn2-aarch64
[+]  adtc6yc              ^diffutils@3.7%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  7vnthzn                  ^libiconv@1.16%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  oyfuwk3          ^expat@2.4.1%arm@21.0.0.879+libbsd arch=linux-amzn2-aarch64
[+]  5q4lmyg              ^libbsd@0.11.3%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  srfepw2                  ^libmd@1.0.3%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  645q4qj          ^gdbm@1.19%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  3haw5gt              ^readline@8.1%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  uhtqtlb                  ^ncurses@6.2%arm@21.0.0.879~symlinks+termlib abi=none arch=linux-amzn2-aarch64
[+]  zpuzm23                      ^pkgconf@1.7.4%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  rl3qj47          ^gettext@0.21%arm@21.0.0.879+bzip2+curses+git~libunistring+libxml2+tar+xz arch=linux-amzn2-aarch64
[+]  dypqz2i              ^libxml2@2.9.10%arm@21.0.0.879~python arch=linux-amzn2-aarch64
[+]  zqsab4f                  ^xz@5.2.5%arm@21.0.0.879~pic libs=shared,static arch=linux-amzn2-aarch64
[+]  puuxvg2                  ^zlib@1.2.11%arm@21.0.0.879+optimize+pic+shared arch=linux-amzn2-aarch64
[+]  fohku26              ^tar@1.34%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  far5l4e          ^libffi@3.3%arm@21.0.0.879 patches=26f26c6f29a7ce9bf370ad3ab2610f99365b4bdd7b82e7c31df41a3370d685c0 arch=linux-amzn2-aarch64
[+]  vc3waha          ^openssl@1.1.1k%arm@21.0.0.879~docs+systemcerts arch=linux-amzn2-aarch64
[+]  vv6txro              ^perl@5.32.1%arm@21.0.0.879+cpanm+shared+threads arch=linux-amzn2-aarch64
[+]  33wiajj                  ^berkeley-db@18.1.40%arm@21.0.0.879+cxx~docs+stl patches=b231fcc4d5cff05e5c3a4814f6a5af0e9a966428dc2176540d2c05aff41de522 arch=linux-amzn2-aarch64
[+]  zj3dbdy          ^sqlite@3.35.5%arm@21.0.0.879+column_metadata+fts~functions~rtree arch=linux-amzn2-aarch64
[+]  uflz3t5          ^util-linux-uuid@2.36.2%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  7wpcn2q      ^samtools@1.12%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  ir7dg6z          ^htslib@1.12%arm@21.0.0.879+libcurl arch=linux-amzn2-aarch64
[+]  2ycz6hz              ^curl@7.76.1%arm@21.0.0.879~darwinssl~gssapi~libssh~libssh2~nghttp2 arch=linux-amzn2-aarch64
[+]  tgj327p                  ^libidn2@2.3.0%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  6onwa6i                      ^libunistring@0.9.10%arm@21.0.0.879 arch=linux-amzn2-aarch64
```


### Maths Library Report

Report on use of maths library calls generated by (Perf Lib Tools)[https://github.com/ARM-software/perf-libs-tools].
Please attach the corresponding apl files.


### Maths Library Optimisation

Was not done as part of this test.


### Performance Regression

The spack package for GATK runs relatively optimally as-is becauase it relies mainly on the JVM. For example, not a custom C binary where compiler flags may substantially help.

It is unclear if/how to add these commands to the spack package, but all of the `--java-opts` can substantially speed up a single HPC node. In particular, using `-Xmx60g` to make sure RAM is limited by the JVM.

GATK also uses Spark for some of its new tooling, which is based on a scatter/gather strategy. It appears that it may be possible to try to run this cross-node; however, it also will default to trying to optimize on same node. The strategy appears to work as expected. The Spark runs above shows that the new GATK Spark-based tool replacements will work on an HPC and likely be faster regardless of architecture.

The best strategy for replicating large-scale genomics work such as 1000 Genomes is to rely moreso on Slurm to fan out analyses of the many (3000ish) very large (150GB+) files and store results in `/scratch`. GATK can then combine the results.


## Report

Below reports on the GATK tools tested above. Many more GATK tools were also tested including generally samtools, bwa, BwaSpark (aka alignment) and HaplotypeCaller/HaplotypeCallerSpark. They all worked as expected; however, required much more processing/setup and ended up taking too long to fully write-up as part of this 1-week event.

### Compilation Summary

GATK compiles and runs on the new ARM HPC as well as it does on the x86 HPC. One of the main requirements is an updated JVM and this was out of date. Updates to the spack package were made to update to the latest OpenJDK release.

### Performance Summary

GATK is able to process genomics data on both HPCs. The new GATK Sparck-based tools appear to be notably faster than the legacy GATK3 implementations. Since the JVM is used for many of these applications, it didn't make sense to do performance sweeps using MPI and OpenMP. The JVM is already threading efficiently to take advantage of multiple processing cores and the Spark tools are capable of doing map/reduce-style processing.

Several of the tests appear to be IO bound. The C5n (x86) architecture appeared to have a clear advantage here for unknown reasons. It may be due to IO setup on the node and merits further x86 vs ARM comparisons. One related factor noticed in logs is a custom "IntelDeflator" that Java uses to speed up decompression of files. Checking/making an ARM equivalent of this may be helpful. This observation was consistent in both the counting tests (higher IO/lower CPU) and the dedup test (more CPU) with 59.54 m vs 45.81 m, respectively ARM, Intel.

GATK appears to be marginally faster on C6gn (Aarch64) compared to C5n (X86) for the tasks tested.


### Optimisation Summary

The biggest optimizations appear to come from using the latest JVM (OpenJDK 16) and using the `--java-opts "-Xm60G ..."` style argument in JDK to leverage the full resources of the HPC nodes. The ReFrame tests includes examples of these Java perf options.
