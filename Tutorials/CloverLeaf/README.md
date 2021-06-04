# CloverLeaf

## Compilation

### Spack Package Modification

The existing Spack package removes the compiler flags for GCC, and has no explicit support for the Arm compiler.

```
diff --git a/var/spack/repos/builtin/packages/cloverleaf/package.py b/var/spack/repos/builtin/packages/cloverleaf/package.py
index a4a0c43d3a..589229a73b 100644
--- a/var/spack/repos/builtin/packages/cloverleaf/package.py
+++ b/var/spack/repos/builtin/packages/cloverleaf/package.py
@@ -57,8 +57,8 @@ def build_targets(self):
 
         if '%gcc' in self.spec:
             targets.append('COMPILER=GNU')
-            targets.append('FLAGS_GNU=')
-            targets.append('CFLAGS_GNU=')
+            targets.append('FLAGS_GNU=-O3 -march=native -funroll-loops')
+            targets.append('CFLAGS_GNU=-O3 -march=native -funroll-loops')
         elif '%cce' in self.spec:
             targets.append('COMPILER=CRAY')
             targets.append('FLAGS_CRAY=')
@@ -75,6 +75,10 @@ def build_targets(self):
             targets.append('COMPILER=XLF')
             targets.append('FLAGS_XLF=')
             targets.append('CFLAGS_XLF=')
+        elif '%arm' in self.spec:
+            targets.append('COMPILER=ARM')
+            targets.append('FLAGS_ARM=-O3 -mcpu=native -funroll-loops')
+            targets.append('CFLAGS_ARM=-O3 -mcpu=native -funroll-loops')
 
         return targets
```

### Building CloverLeaf

Now we can simply build CloverLeaf with the desired compilers, with a dependency on the exisiting OpenMPI (identified by their hashes)

```
spack install cloverleaf@1.1%gcc@10.3.0 ^openmpi/ehtcdbv
spack install cloverleaf@1.1%arm@21.0.0.879 ^openmpi/6bfbjqd
```

## ReFrame BM16_short (single node)

[ReFrame Benchmark](cloverleaf_bm16_short.py)

```
../bin/reframe -c CloverLeaf/cloverleaf_bm16_short.py -r --performance-report
```

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

| Cores | Arm 21.0 | GCC 10.3 |
| ----- |:--------:|:--------:|
| 1     | 233.44   | 201.08   |
| 2     | 109.27   | 101.62   |
| 4     | 56.79    | 52.70    |
| 8     | 30.92    | 29.14    |
| 16    | 20.12    | 19.61    |
| 32    | 17.02    | 17.12    |
| 64    | 17.82    | 17.93    |
