# miniAero 

**Description:** Mini-application for the evaulation of programming models and hardware for next generation platforms, kokkos, unstructured finite volume code that solves the compressibl Navier-Stokes equations

**URL:** https://github.com/Mantevo/miniAero 

**Team:**  Team Joe

## Compilation
I had to modify the miniAero source code in order to add MPI support in Spack. The updated code is hosted in `https://github.com/ghe-asu/miniAero.git` for the moment.

### Code Changes
1. Remove depreciated `kokkos::experimental` namesapce.
2. Update depreciated `view::dimention_0` to `view::extent(0)`
3. Update depreciated `ptr_on_device` to `data`
4. Replace `-Isrc` to `-I.` in `Makefile`.

### Spack Package Modification
The updated recipe is under the folder `spack`.

Details of any changes to the Spack recipe used:
1. Replaced `kokkos-legacy` dependency with `kokkos`.
2. Updated compiling and linking flags.
3. Added an MPI variant for miniAero.

Git commit hash of checkout for pacakage:
`2ee751b3bd5c5c3516d6de33bacd2e1f0f3b752c`

Pull request for Spack recipe changes: 

### Building miniAero



#### Compiler 1: GCC

```
spack install miniaero@v1.0.1%gcc@10.3.0+mpi
```

#### Compiler 2: Arm

```
spack install miniaero@1.0.1%arm@21.0.0.879+mpi
```

## Test Case 1: Fine Ramp

[ReFrame Benchmark 1](#)
In folder `reframe`:
```
reframe -c miniaero_fine_ramp.py -r --performance-report
```

### Validation

Details of the validation for `Test Case 1: Fine Ramp`.


### ReFrame Output
`pgcn3wa` is Arm with optimized compiler flags. `qdrynal` is Arm without.

```
==============================================================================
PERFORMANCE REPORT
------------------------------------------------------------------------------
miniAero_fine-ramp_miniaero_v1_0_1__gcc_10_3_0_N_1_MPI_1_OMP_1
- aws:c6gn
   - builtin
      * num_tasks: 1
      * Total Time: 159.09 s
------------------------------------------------------------------------------
miniAero_fine-ramp_miniaero_v1_0_1__gcc_10_3_0_N_1_MPI_2_OMP_1
   - builtin
      * num_tasks: 2
      * Total Time: 75.85 s
------------------------------------------------------------------------------
miniAero_fine-ramp_miniaero_v1_0_1__gcc_10_3_0_N_1_MPI_4_OMP_1
   - builtin
      * num_tasks: 4
      * Total Time: 35.88 s
------------------------------------------------------------------------------
miniAero_fine-ramp_miniaero_v1_0_1__gcc_10_3_0_N_1_MPI_8_OMP_1
   - builtin
      * num_tasks: 8
      * Total Time: 18.26 s
------------------------------------------------------------------------------
miniAero_fine-ramp_miniaero_v1_0_1__gcc_10_3_0_N_1_MPI_16_OMP_1
   - builtin
      * num_tasks: 16
      * Total Time: 9.79 s
------------------------------------------------------------------------------
miniAero_fine-ramp_miniaero_v1_0_1__gcc_10_3_0_N_1_MPI_32_OMP_1
   - builtin
      * num_tasks: 32
      * Total Time: 4.79 s
------------------------------------------------------------------------------
miniAero_fine-ramp_miniaero_v1_0_1__gcc_10_3_0_N_1_MPI_64_OMP_1
   - builtin
      * num_tasks: 64
      * Total Time: 2.23 s
------------------------------------------------------------------------------
miniAero_fine-ramp_miniaero_v1_0_1_qdrynal_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Total Time: 188.01 s
------------------------------------------------------------------------------
miniAero_fine-ramp_miniaero_v1_0_1_qdrynal_N_1_MPI_2_OMP_1
   - builtin
      * num_tasks: 2
      * Total Time: 73.64 s
------------------------------------------------------------------------------
miniAero_fine-ramp_miniaero_v1_0_1_qdrynal_N_1_MPI_4_OMP_1
   - builtin
      * num_tasks: 4
      * Total Time: 38.64 s
------------------------------------------------------------------------------
miniAero_fine-ramp_miniaero_v1_0_1_qdrynal_N_1_MPI_8_OMP_1
   - builtin
      * num_tasks: 8
      * Total Time: 19.41 s
------------------------------------------------------------------------------
miniAero_fine-ramp_miniaero_v1_0_1_qdrynal_N_1_MPI_16_OMP_1
   - builtin
      * num_tasks: 16
      * Total Time: 9.7 s
------------------------------------------------------------------------------
miniAero_fine-ramp_miniaero_v1_0_1_qdrynal_N_1_MPI_32_OMP_1
   - builtin
      * num_tasks: 32
      * Total Time: 4.47 s
------------------------------------------------------------------------------
miniAero_fine-ramp_miniaero_v1_0_1_qdrynal_N_1_MPI_64_OMP_1
   - builtin
      * num_tasks: 64
      * Total Time: 2.61 s
------------------------------------------------------------------------------
miniAero_fine-ramp_miniaero_v1_0_1_pgcn3wa_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Total Time: 144.82 s
------------------------------------------------------------------------------
miniAero_fine-ramp_miniaero_v1_0_1_pgcn3wa_N_1_MPI_2_OMP_1
   - builtin
      * num_tasks: 2
      * Total Time: 73.16 s
------------------------------------------------------------------------------
miniAero_fine-ramp_miniaero_v1_0_1_pgcn3wa_N_1_MPI_4_OMP_1
   - builtin
      * num_tasks: 4
      * Total Time: 32.84 s
------------------------------------------------------------------------------
miniAero_fine-ramp_miniaero_v1_0_1_pgcn3wa_N_1_MPI_8_OMP_1
   - builtin
      * num_tasks: 8
      * Total Time: 15.35 s
------------------------------------------------------------------------------
miniAero_fine-ramp_miniaero_v1_0_1_pgcn3wa_N_1_MPI_16_OMP_1
   - builtin
      * num_tasks: 16
      * Total Time: 7.91 s
------------------------------------------------------------------------------
miniAero_fine-ramp_miniaero_v1_0_1_pgcn3wa_N_1_MPI_32_OMP_1
   - builtin
      * num_tasks: 32
      * Total Time: 4.26 s
------------------------------------------------------------------------------
miniAero_fine-ramp_miniaero_v1_0_1_pgcn3wa_N_1_MPI_64_OMP_1
   - builtin
      * num_tasks: 64
      * Total Time: 2.24 s
------------------------------------------------------------------------------
```


### Serial Hot-spot Profile

List of top-10 functions / code locations from a serial profile.

Profiling command used:
In reframe, example from https://github.com/arm-hpc-user-group/Cloud-HPC-Hackathon-2021/blob/main/Guides/Profiling/cloverleaf_BM16_short_hotspot.py

|Position|Routine                                                                                                                                                                   |Time (%)|
|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
|1       |roe_flux<Kokkos::Serial>::compute_flux(double const* const&, double const* const&, double* const&, double const* const&, double const* const&, double const* const&) const|27.9%   |
|2       |Kokkos::View<double const* [inlined]                                                                                                                                      |18.3%   |
|3       |limiter_face<Kokkos::Serial, true>::operator()(int const&) const [inlined]                                                                                                |10.7%   |
|4       |compute_face_flux<Kokkos::Serial, true, roe_flux<Kokkos::Serial>, no_viscous_flux<Kokkos::Serial> >::operator()(int const&) const [inlined]                               |33.2%   |
|5       |Kokkos::atomic_fetch_add<double>(double volatile*, std::add_const<double>::type) [inlined]                                                                                |5.5%    |
|6       |green_gauss_face<Kokkos::Serial>::operator()(int const&) const [inlined]                                                                                                  |3.8%    |
|7       |compute_face_flux<Kokkos::Serial, true, roe_flux<Kokkos::Serial>, no_viscous_flux<Kokkos::Serial> >::operator()(int const&) const [inlined]                               |3.4%    |
|8       |Kokkos::atomic_compare_exchange<double>(double volatile*, double, double) [inlined]                                                                                       |2.9%    |
|9       |min_max_face<Kokkos::Serial, true>::operator()(int const&) const [inlined]                                                                                                |2.1%    |
|10      |MathTools<Kokkos::Serial>::MatVec5(double, double const*, double const*, double, double*) [inlined]                                                                       |1.5%    |



### Full Node Hot-spot Profile

List of top-10 functions / code locations from a full node profile.

Profiling command used:
Same as above.

|Position|Routine                                                                                                                                                                   |Time (%)|
|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
|1       |MPI_Waitall                                                                                                                                                               |29.4%   |
|2       |roe_flux<Kokkos::Serial>::compute_flux(double const* const&, double const* const&, double* const&, double const* const&, double const* const&, double const* const&) const|14.8%   |
|3       |Kokkos::atomic_fetch_add<double>(double volatile*, std::add_const<double>::type) [inlined]                                                                                |5.5%    |
|4       |limiter_face<Kokkos::Serial, true>::operator()(int const&) const [inlined]                                                                                                |5.2%    |
|5       |Kokkos::atomic_compare_exchange<double>(double volatile*, double, double) [inlined]                                                                                       |4.7%    |
|6       |compute_face_flux<Kokkos::Serial, true, roe_flux<Kokkos::Serial>, no_viscous_flux<Kokkos::Serial> >::operator()(int const&) const [inlined]                               |4.3%    |
|7       |MPI_Allgather                                                                                                                                                             |3.3%    |
|8       |VenkatLimiter<Kokkos::Serial>::limit(double, double, double, double) [inlined]                                                                                            |2.6%    |
|9       |MPI_Finalize                                                                                                                                                              |2.4%    |
|10      |min_max_face<Kokkos::Serial, true>::operator()(int const&) const [inlined]                                                                                                |2.3%    |


### Strong Scaling Study

On-node scaling study for two compilers.

|Cores|GCC (seconds)|Arm (seconds)|
|-----|-------------|-------------|
|1    |159.09       |188.01       |
|2    |75.85        |73.64        |
|4    |35.88        |38.64        |
|8    |18.26        |19.41        |
|16   |9.79         |9.7          |
|32   |4.79         |4.47         |
|64   |2.23         |2.61         |




## Optimisation
A compiler flag tunning for Arm compiler is done.

### Compiler Flag Tuning

Compiler flags before:
```
CFLAGS=-O3
```

Compiler flags after:
```
CFLAGS=-Ofast -ffast-math -armpl -Rpass=loop
```

#### Compiler Flag Performance

| Cores | Original Flags | New Flags |
|-------|----------------|-----------|
|1    |188.01              |144.82             |
|2    |73.64               |73.16              |
|4    |38.64               |32.84              |
|8    |19.41               |15.35              |
|16   |9.7                 |7.91               |
|32   |4.47                |4.26               |
|64   |2.61                |2.24               |



### Performance Regression

From slowest case, Arm compiler with 1 core, 188.01 seconds to 2.24 seconds, Arm compiler with 64 cores and updated compiler flags.



## Report

### Compilation Summary
I made the code from not compiling to compiling. It is like the biggest speed up one could ever made:)

### Performance Summary

For mini application based on well maintained numerical library (kokkos), the scaling is almost perfect.


### Optimisation Summary

A small tune on the compiler flags for Arm led to very decent speed up, from 188.01 seconds to 144.82 seconds for 1 core case.
