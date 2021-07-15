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

Generally, an existing sequencing analysis tool was used to count reads. One of the BAM files is advertised as 20K reads, which will also be 5000000 bases for that sequencing run.

```
spack load samtools

# reads in the "small" BAM
samtools view -c H06HDADXX130110.1.ATCACGAT.20k_reads.bam
20000

# reads in the "medium" BAM
samtools view -c HG00096.mapped.ILLUMINA.bwa.GBR.low_coverage.20120522.bam
145063589

# reads in the "large" BAM
samtools view -c HG00096.wgs.ILLUMINA.bwa.GBR.high_cov_pcr_free.20140203.bam
652944493
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
      * Total Time: 408.0 s
------------------------------------------------------------------------------
GATK_gatk_countreads_1000_genomes_low_coverage_gatk_4_1_8_1_arm_21_0_0_879_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Total Time: 408.0 s
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
      * Total Time: 390.0 s
------------------------------------------------------------------------------
```

### On-node Compiler Comparison

Performance comparison of two compilers.

| Cores | gcc        | arm        |
|-------|------------|------------|
| All   |  408.0     |   408.0    |



## Test Case 2

This confirms that GATK is working by doing a common read analysis of a BAM file using the `ReadCountsSpark` tool that was added in GATK4. This is run against the small, medium and large sequencing runs noted in the description. This is run on both the ARM and x86 HPC. This tool is used in a similar way as `ReadCount` but it is distinct and has distinct output.

```
reframe -c gatk_countbases.py -r --performance-report
```

### Validation

This is a public BAM file from an Illumina HiSeq 2500 and is known to have 20K reads and 5000000 bases in it.

Running GATK by hand (same commands) lets you inspect stats and work with this file. It is small enough that it should always process in a fraction of a second.

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
      * Total Time: 0.549795 s
------------------------------------------------------------------------------
GATK_gatk_countreadsspark_hiseq_2500_20k_gatk_4_1_8_1_arm_21_0_0_879_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Total Time: 0.501399 s
------------------------------------------------------------------------------
GATK_gatk_countreadsspark_1000_genomes_low_coverage_gatk_4_1_8_1_gcc_10_3_0_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Total Time: 299.037115 s
------------------------------------------------------------------------------
GATK_gatk_countreadsspark_1000_genomes_low_coverage_gatk_4_1_8_1_arm_21_0_0_879_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Total Time: 299.195437 s
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
      * Total Time: 0.380283 s
------------------------------------------------------------------------------
GATK_gatk_countreadsspark_1000_genomes_low_coverage_gatk_4_1_8_1_gcc_10_3_0_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Total Time: 301.929988 s
------------------------------------------------------------------------------
```

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
      * Total Time: 402.0 s
------------------------------------------------------------------------------
```

x86 HPC output after `gcc` compile.

```
```

## Test Case 4

[ReFrame Benchmark 4](#)

This confirms that GATK is working by doing a common read analysis of base counts from a BAM file using the `BaseCountsSpark` tool that was added in GATK4. This is run against the small, medium and large sequencing runs noted in the description. This is run on both the ARM and x86 HPC. This tool is used in a similar way as `BaseCount` but it is distinct and has distinct output.

```
reframe -c gatk_countbases.py -r --performance-report
```

### Validation

Expected base counts were manually collected using samtools.

### ReFrame Output

```
==============================================================================
PERFORMANCE REPORT
------------------------------------------------------------------------------
GATK_gatk_countbasesspark_hiseq_2500_20k_gatk_4_1_8_1_gcc_10_3_0_N_1_MPI_1_OMP_1
- aws:c6gn
   - builtin
      * num_tasks: 1
      * Total Time: 0.656905 s
------------------------------------------------------------------------------
GATK_gatk_countbasesspark_hiseq_2500_20k_gatk_4_1_8_1_arm_21_0_0_879_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Total Time: 0.676111 s
------------------------------------------------------------------------------
GATK_gatk_countbasesspark_1000_genomes_low_coverage_gatk_4_1_8_1_gcc_10_3_0_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Total Time: 451.688856 s
------------------------------------------------------------------------------
GATK_gatk_countbasesspark_1000_genomes_low_coverage_gatk_4_1_8_1_arm_21_0_0_879_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Total Time: 458.258934 s
------------------------------------------------------------------------------
```

### On-node Compiler Comparison

Performance comparison of two compilers.

| Cores | gcc@10.3.0 | arm@ |
|-------|------------|------------|
| All   |            |            |


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

GATK compiles and runs on the new ARM HPC as well as it does on the x86 HPC. One of the main requirements is an updated JVM and this was out of date. Updates to the spack package were made to update to the latest OpenJDK release.

### Performance Summary

GATK is able to process genomics data on both HPCs. The new GATK Sparck-based tools appear to be notably faster than the legacy GATK3 implementations. Since the JVM is used for many of these applications, it did seem to make sense to do performance sweeps using MPI and OpenMP. The JVM is already threading efficiently to take advantage of multiple processing cores and the Spark tools are capable of doing map/reduce-style processing.

OpenJDK appears to be notably faster on the x86.


### Optimisation Summary

The biggest optimizations appear to come from using the latest JVM (OpenJDK 16) and using the `--java-opts "-Xm60G ..."` style argument in JDK to leverage the full resources of the HPC nodes. The ReFrame tests includes examples of these Java perf options.
