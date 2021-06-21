# CloverLeaf

Proxy Application. CloverLeaf is a miniapp that solves the compressible Euler equations on a Cartesian grid, using an explicit, second-order accurate method.

## Compilation

The only dependency for CloverLeaf is MPI. 
By default we want to use Open MPI, so we look at what is available:

```
$ spack find -l openmpi
==> 3 installed packages
-- linux-amzn2-graviton2 / arm@21.0.0.879 -----------------------
6bfbjqd openmpi@4.1.0

-- linux-amzn2-graviton2 / gcc@10.3.0 ---------------------------
ehtcdbv openmpi@4.1.0

-- linux-amzn2-graviton2 / nvhpc@21.2 ---------------------------
jmzsjsv openmpi@4.1.0
```

Great, we have an Open MPI install for all 3 compilers of interest.

### Spack Package Modification

The existing Spack package removes the compiler flags for GCC, and has no explicit support for the Arm compiler or NVHPC.
Note we have not added the corresponding flags for other compilers as this is out of scope for now.

```
         if '%gcc' in self.spec:
             targets.append('COMPILER=GNU')
-            targets.append('FLAGS_GNU=')
-            targets.append('CFLAGS_GNU=')
+            targets.append('OMP_GNU=-fopenmp')
+            targets.append('FLAGS_GNU=-O3 -march=native -funroll-loops')
+            targets.append('CFLAGS_GNU=-O3 -march=native -funroll-loops')
         elif '%cce' in self.spec:
             targets.append('COMPILER=CRAY')
             targets.append('FLAGS_CRAY=')
@@ -75,6 +76,16 @@ def build_targets(self):
             targets.append('COMPILER=XLF')
             targets.append('FLAGS_XLF=')
             targets.append('CFLAGS_XLF=')
+        elif '%arm' in self.spec:
+            targets.append('COMPILER=ARM')
+            targets.append('OMP_ARM=-fopenmp')
+            targets.append('FLAGS_ARM=-O3 -mcpu=native -funroll-loops')
+            targets.append('CFLAGS_ARM=-O3 -mcpu=native -funroll-loops')
+        elif '%nvhpc' in self.spec:
+            targets.append('COMPILER=NVHPC')
+            targets.append('OMP_NVHPC=-mp=multicore')
+            targets.append('FLAGS_NVHPC=-O3 -fast')
+            targets.append('CFLAGS_NVHPC=-O3 -fast')

```

### Building CloverLeaf

Now we can simply build CloverLeaf with the desired compilers, with a dependency on the exisiting OpenMPI (identified by their hashes)


#### GCC 10.3.0

```
spack install cloverleaf@1.1%gcc@10.3.0 ^openmpi/ehtcdbv
```

```
$ spack spec -Il cloverleaf@1.1%gcc@10.3.0 ^openmpi/ehtcdbv

[+]  zqcxt5p  cloverleaf@1.1%gcc@10.3.0 build=ref arch=linux-amzn2-graviton2
[+]  ehtcdbv      ^openmpi@4.1.0%gcc@10.3.0~atomics~cuda~cxx~cxx_exceptions+gpfs~internal-hwloc~java~legacylaunchers~lustre~memchecker+pmi~singularity~sqlite3+static~thread_multiple+vt+wrapper-rpath fabrics=ofi patches=60ce20bc14d98c572ef7883b9fcd254c3f232c2f3a13377480f96466169ac4c8 schedulers=slurm arch=linux-amzn2-graviton2
[+]  czkhgoa          ^hwloc@2.4.1%gcc@10.3.0~cairo~cuda~gl~libudev+libxml2~netloc~nvml+pci+shared arch=linux-amzn2-graviton2
[+]  asgtk6a              ^libpciaccess@0.16%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  iyhm3wi              ^libxml2@2.9.10%gcc@10.3.0~python arch=linux-amzn2-graviton2
[+]  y5ei3cm                  ^libiconv@1.16%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  ye3kcvv                  ^xz@5.2.5%gcc@10.3.0~pic libs=shared,static arch=linux-amzn2-graviton2
[+]  qepjcvj                  ^zlib@1.2.11%gcc@10.3.0+optimize+pic+shared arch=linux-amzn2-graviton2
[+]  iwzirqc              ^ncurses@6.2%gcc@10.3.0~symlinks+termlib abi=none arch=linux-amzn2-graviton2
[+]  tadxrfp          ^libevent@2.1.12%gcc@10.3.0+openssl arch=linux-amzn2-graviton2
[+]  5i3lgfb              ^openssl@1.1.1k%gcc@10.3.0~docs+systemcerts arch=linux-amzn2-graviton2
[+]  ts5lqeg          ^libfabric@1.11.1-aws%gcc@10.3.0~kdreg fabrics=sockets,tcp,udp arch=linux-amzn2-graviton2
[+]  mhav5gn          ^numactl@2.0.14%gcc@10.3.0 patches=4e1d78cbbb85de625bad28705e748856033eaafab92a66dffd383a3d7e00cc94,62fc8a8bf7665a60e8f4c93ebbd535647cebf74198f7afafec4c085a8825c006 arch=linux-amzn2-graviton2
[+]  wturp6c          ^openssh@8.5p1%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  ivotdt7              ^libedit@3.1-20210216%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  wqpuvmh          ^slurm@20-02-4-1%gcc@10.3.0~gtk~hdf5~hwloc~mariadb~pmix+readline~restd sysconfdir=PREFIX/etc arch=linux-amzn2-graviton2
```

#### Arm 21.0.879

```
spack install cloverleaf@1.1%arm@21.0.0.879 ^openmpi/6bfbjqd
```

```
$ spack spec -Il cloverleaf@1.1%arm@21.0.0.879 ^openmpi/6bfbjqd

[+]  3fq5vz4  cloverleaf@1.1%arm@21.0.0.879 build=ref arch=linux-amzn2-graviton2
[+]  6bfbjqd      ^openmpi@4.1.0%arm@21.0.0.879~atomics~cuda~cxx~cxx_exceptions+gpfs~internal-hwloc~java~legacylaunchers~lustre~memchecker+pmi~singularity~sqlite3+static~thread_multiple+vt+wrapper-rpath fabrics=ofi patches=60ce20bc14d98c572ef7883b9fcd254c3f232c2f3a13377480f96466169ac4c8 schedulers=slurm arch=linux-amzn2-graviton2
[+]  eulyxmx          ^hwloc@2.4.1%arm@21.0.0.879~cairo~cuda~gl~libudev+libxml2~netloc~nvml+pci+shared arch=linux-amzn2-graviton2
[+]  heo5xlh              ^libpciaccess@0.16%arm@21.0.0.879 arch=linux-amzn2-graviton2
[+]  7og6524              ^libxml2@2.9.10%arm@21.0.0.879~python arch=linux-amzn2-graviton2
[+]  4fpawwk                  ^libiconv@1.16%arm@21.0.0.879 arch=linux-amzn2-graviton2
[+]  3uhexv5                  ^xz@5.2.5%arm@21.0.0.879~pic libs=shared,static arch=linux-amzn2-graviton2
[+]  kfhtmo3                  ^zlib@1.2.11%arm@21.0.0.879+optimize+pic+shared arch=linux-amzn2-graviton2
[+]  5fshnbc              ^ncurses@6.2%arm@21.0.0.879~symlinks+termlib abi=none arch=linux-amzn2-graviton2
[+]  hj5l7x5          ^libevent@2.1.12%arm@21.0.0.879+openssl arch=linux-amzn2-graviton2
[+]  b6rhpqo              ^openssl@1.1.1k%arm@21.0.0.879~docs+systemcerts arch=linux-amzn2-graviton2
[+]  tr5jdui          ^libfabric@1.11.1-aws%arm@21.0.0.879~kdreg fabrics=sockets,tcp,udp arch=linux-amzn2-graviton2
[+]  325gh7i          ^numactl@2.0.14%arm@21.0.0.879 patches=4e1d78cbbb85de625bad28705e748856033eaafab92a66dffd383a3d7e00cc94,62fc8a8bf7665a60e8f4c93ebbd535647cebf74198f7afafec4c085a8825c006 arch=linux-amzn2-graviton2
[+]  7cmi2lb          ^openssh@8.5p1%arm@21.0.0.879 arch=linux-amzn2-graviton2
[+]  qytqrqe              ^libedit@3.1-20210216%arm@21.0.0.879 arch=linux-amzn2-graviton2
[+]  uxllonc          ^slurm@20-02-4-1%arm@21.0.0.879~gtk~hdf5~hwloc~mariadb~pmix+readline~restd sysconfdir=PREFIX/etc arch=linux-amzn2-graviton2
```

#### NVHPC 21.2

```
spack install cloverleaf@1.1%nvhpc@21.2 ^openmpi/jmzsjsv
```

```
$ spack spec -Il cloverleaf@1.1%nvhpc@21.2 ^openmpi/jmzsjsv

[+]  mfwj3xb  cloverleaf@1.1%nvhpc@21.2 build=ref arch=linux-amzn2-graviton2
[+]  jmzsjsv      ^openmpi@4.1.0%nvhpc@21.2~atomics~cuda~cxx~cxx_exceptions+gpfs~internal-hwloc~java~legacylaunchers~lustre~memchecker+pmi~singularity~sqlite3+static~thread_multiple+vt+wrapper-rpath fabrics=ofi patches=60ce20bc14d98c572ef7883b9fcd254c3f232c2f3a13377480f96466169ac4c8,fba0d3a784a9723338722b48024a22bb32f6a951db841a4e9f08930a93f41d7a schedulers=slurm arch=linux-amzn2-graviton2
[+]  k6nxff3          ^hwloc@2.4.1%nvhpc@21.2~cairo~cuda~gl~libudev+libxml2~netloc~nvml+pci+shared arch=linux-amzn2-graviton2
[+]  e4m4ued              ^libpciaccess@0.16%nvhpc@21.2 patches=6e08dc445ece06e9e8b1344397f2d3f169005703ddc0f2ae24f366cde78c7377 arch=linux-amzn2-graviton2
[+]  wo4l72s              ^libxml2@2.9.10%nvhpc@21.2~python patches=05ff238cf435825ef835c7ae39376b52dc83d8caf19e962f0766c841386a305a,10a88ad47f9797cf7cf2d7d07241f665a3b6d1f31fa026728c8c2ae93e1664e9 arch=linux-amzn2-graviton2
[+]  r7mmkdp                  ^libiconv@1.16%nvhpc@21.2 arch=linux-amzn2-graviton2
[+]  br733tn                  ^xz@5.2.5%nvhpc@21.2~pic libs=shared,static arch=linux-amzn2-graviton2
[+]  4js6ect                  ^zlib@1.2.11%nvhpc@21.2+optimize+pic+shared arch=linux-amzn2-graviton2
[+]  asgm7mt              ^ncurses@6.2%nvhpc@21.2~symlinks+termlib abi=none arch=linux-amzn2-graviton2
[+]  uttaumr          ^libevent@2.1.12%nvhpc@21.2+openssl arch=linux-amzn2-graviton2
[+]  j2qhi7h              ^openssl@1.1.1k%nvhpc@21.2~docs+systemcerts arch=linux-amzn2-graviton2
[+]  nnmvqus          ^libfabric@1.11.1-aws%nvhpc@21.2~kdreg fabrics=sockets,tcp,udp arch=linux-amzn2-graviton2
[+]  5yq4tpw          ^numactl@2.0.14%nvhpc@21.2 patches=4e1d78cbbb85de625bad28705e748856033eaafab92a66dffd383a3d7e00cc94,62fc8a8bf7665a60e8f4c93ebbd535647cebf74198f7afafec4c085a8825c006 arch=linux-amzn2-graviton2
[+]  cl3ohqo          ^openssh@8.5p1%nvhpc@21.2 arch=linux-amzn2-graviton2
[+]  yvqpq74              ^libedit@3.1-20210216%nvhpc@21.2 arch=linux-amzn2-graviton2
[+]  zehhooy          ^slurm@20-02-4-1%nvhpc@21.2~gtk~hdf5~hwloc~mariadb~pmix+readline~restd sysconfdir=PREFIX/etc arch=linux-amzn2-graviton2
```


## ReFrame BM16_short (single node)

[ReFrame Benchmark](cloverleaf_bm16_short.py)

```
../bin/reframe -c CloverLeaf/cloverleaf_bm16_short.py -r --performance-report
```

### Validation

For this test case we want to look at the `Kinetic Energy` after 87 steps (defined in the `clover.in` file).

The sample output for the end of the calculation, gives us a number of validation criteria.
```
 Step      87 time   0.1242811 control    sound    timestep   1.46E-03       1,       1 x  1.30E-03 y  1.30E-03

 Time   0.12574308920817368
                       Volume            Mass         Density        Pressure Internal Energy  Kinetic Energy    Total Energy
 step:     87      0.1000E+03      0.2800E+02      0.2800E+00      0.1707E+00      0.4269E+02      0.3075E+00      0.4299E+02


 Calculation complete
 Clover is finishing
 Wall clock    166.40373587608337
 First step overhead   1.6100406646728516E-003
```

We could check for `Calculation complete`, however as there is no internal validation this is insufficient. 
So we look at the output variables.
CloverLeaf conserves Volume, Mass and Density, so for validation we should use Kinetric Energy, and for this test we are looking for a value of 0.307j.
In the ReFrame test we have allowed for some tolerance on this value for rounding and machine precision.


### ReFrame Output

```
==============================================================================
PERFORMANCE REPORT
------------------------------------------------------------------------------
CloverLeaf_BM16_short_cloverleaf_1_1__gcc_10_3_0_N_1_MPI_1_OMP_1
- aws:c6g
   - builtin
      * num_tasks: 1
      * Total Time: 233.44770884513855 s
------------------------------------------------------------------------------
CloverLeaf_BM16_short_cloverleaf_1_1__gcc_10_3_0_N_1_MPI_2_OMP_1
   - builtin
      * num_tasks: 2
      * Total Time: 109.2751829624176 s
------------------------------------------------------------------------------
CloverLeaf_BM16_short_cloverleaf_1_1__gcc_10_3_0_N_1_MPI_4_OMP_1
   - builtin
      * num_tasks: 4
      * Total Time: 56.79921007156372 s
------------------------------------------------------------------------------
CloverLeaf_BM16_short_cloverleaf_1_1__gcc_10_3_0_N_1_MPI_8_OMP_1
   - builtin
      * num_tasks: 8
      * Total Time: 30.928933143615723 s
------------------------------------------------------------------------------
CloverLeaf_BM16_short_cloverleaf_1_1__gcc_10_3_0_N_1_MPI_16_OMP_1
   - builtin
      * num_tasks: 16
      * Total Time: 20.127499103546143 s
------------------------------------------------------------------------------
CloverLeaf_BM16_short_cloverleaf_1_1__gcc_10_3_0_N_1_MPI_32_OMP_1
   - builtin
      * num_tasks: 32
      * Total Time: 17.02335500717163 s
------------------------------------------------------------------------------
CloverLeaf_BM16_short_cloverleaf_1_1__gcc_10_3_0_N_1_MPI_64_OMP_1
   - builtin
      * num_tasks: 64
      * Total Time: 17.82581901550293 s
------------------------------------------------------------------------------
```

### On-node Compiler Scaling Study

| Cores | GCC 10.3 | Arm 21.0 | NVHPC 21.2 |
| ----- |:--------:|:--------:|:----------:|
| 1     | 233.44   | 201.08   | 198.18     |
| 2     | 109.27   | 101.62   | 119.11     |
| 4     | 56.79    | 52.70    | 56.38      |
| 8     | 30.92    | 29.14    | 32.71      |
| 16    | 20.12    | 19.61    | 20.54      |
| 32    | 17.02    | 17.12    | 18.20      |
| 64    | 17.82    | 17.93    | 17.61      |

## ReFrame BM512_short (multi node)

[ReFrame Benchmark](cloverleaf_bm512_short.py)

```
../bin/reframe -c cloverleaf_bm512_short.py -r --performance-report
```

### Validation

```
 Time    1.5737050254218295E-002
                       Volume            Mass         Density        Pressure Internal Energy  Kinetic Energy    Total Energy
 step:     87      0.1000E+03      0.2800E+02      0.2800E+00      0.1718E+00      0.4296E+02      0.3861E-01      0.4300E+02
```

Here we are looking for a Kinetic Energy value of 0.0386j.


### Off-Node Scaling Study

| Nodes | Cores | GCC 10.3 - C6g | Arm 21.0 - C6g | GCC 10.3 - C6gn | Arm 21.0 - C6gn |
|-------|-------|----------------|----------------|-----------------|-----------------|
| 1     | 32    | 522.76         | 511.13         | 522.41          | 511.28          |
| 1     | 64    | 519.70         | 515.96         | 519.45          | 515.84          |
| 2     | 128   | 263.97         | 262.94         | 263.86          | 262.91          |
| 4     | 256   | 132.81         | 131.96         | 132.08          | 131.81          |

## Report

### Compilation Summary

CloverLeaf compilers fairly simply 'out-of-the-box' and so no modifications were required.
As stated the Spack recipy strips out the necessary compiler flags, so we needed to set them back to the minimal recommendation.
We also added support for the Arm Compiler and NVHPC, with comparable flags to that of GCC.

Otherwise no modifications were needed. CloverLeaf only has one dependency - MPI, so for this we used Open MPI, specifying the hash of the preinstalled versions.


### Performance Summary

From our performance study we see that the Arm compiler outperforms the GCC compiler for our smaller test case at a number of core counts. 
Single core the NVHPC build is actually fastest. 
However, there is very little difference at higher core counts, where CloverLeaf becomes memory bound.

Our scaling study for `BM_16_short` shows that we saturate memory bandwidth at about 16 cores, and the use of a full node could be detrimental.

Our larger scaling study `BM_512_short` shows some similar on-node behaviour, but good scaling off node - with near perfect parallel efficiency. 
Again, no difference between compilers is evident. 
We also note that there is no performance gain from utilising the faster network on the C6gn instance types, as we are still memory bound rather than network bound.

### Optimisation Summary

We have not undertaken an optimisation exercise.

