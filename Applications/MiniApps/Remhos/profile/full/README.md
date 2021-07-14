### Full Node Hot-spot Profile
The 12 tables below are the full node hot-spot profiling results across 3 compilers and 4 test cases. The raw profiles can be found at the current directory.

Profiling command used:
```
map --profile -o profile/full/<test case>_<compiler>.map srun -N 1 -n 64 remhos <executable opts based on the test case>
```

#### Test Case 1: 2DRemap x Compiler 1: `gcc@10.3.0`
| Position | Routine             | Time (s) | Time (%) | MPI (%) |
|----------|---------------------|----------|----------|---------|
| 1        | MPI_Allreduce       | 4.78     | 80.30    | 80.30   |
| 2        | MPI_Waitall         | 0.33     | 5.50     | 5.50    |
| 3        | MPI_Waitany         | 0.15     | 2.60     | 2.60    |
| 4        | MPI_Bcast           | 0.10     | 1.70     | 1.70    |
| 5        | MPI_Isend           | 0.10     | 1.70     | 1.70    |
| 6        | MPI_Finalize        | 0.07     | 1.10     | 1.10    |
| 7        | MPI_Irecv           | 0.06     | 1.00     | 1.00    |
| 8        | mfem::AddMult_a_VVt | 0.04     | 0.60     | 0.00    |
| 9        | mfem::AddMultVWt    | 0.04     | 0.60     | 0.00    |
| 10       | mfem::Mult          | 0.02     | 0.40     | 0.00    |

#### Test Case 1: 2DRemap x Compiler 2: `arm@21.0.0.879`
| Position | Routine                          | Time (s) | Time (%) | MPI (%) |
|----------|----------------------------------|----------|----------|---------|
| 1        | MPI_Allreduce                    | 4.87     | 80.40    | 80.40   |
| 2        | MPI_Waitall                      | 0.35     | 5.80     | 5.80    |
| 3        | MPI_Waitany                      | 0.17     | 2.80     | 2.80    |
| 4        | MPI_Isend                        | 0.10     | 1.70     | 1.70    |
| 5        | MPI_Bcast                        | 0.08     | 1.30     | 1.30    |
| 6        | MPI_Irecv                        | 0.06     | 1.00     | 1.00    |
| 7        | mfem::AddMult_a_VVt              | 0.05     | 0.80     | 0.00    |
| 8        | mfem::AddMultVWt                 | 0.04     | 0.60     | 0.00    |
| 9        | mfem::Mult                       | 0.02     | 0.40     | 0.00    |
| 10       | mfem::SparseMatrix::AddSubMatrix | 0.02     | 0.40     | 0.00    |

#### Test Case 1: 2DRemap x Compiler 3: `nvhpc@21.2`
```
Maximum backtrace size in sampler exceeded, stack too deep.
```
| Position | Routine                         | Time (s) | Time (%) | MPI (%) |
|----------|---------------------------------|----------|----------|---------|
| 1        | MPI_Allreduce                   | 5.82     | 48.80    | 48.80   |
| 2        | ompi_mtl_ofi_iprobe_true        | 1.54     | 12.90    | 12.90   |
| 3        | ompi_mtl_ofi_progress_no_inline | 1.41     | 11.80    | 11.80   |
| 4        | MPI_Bcast                       | 1.20     | 10.10    | 10.10   |
| 5        | PMPI_Iprobe                     | 0.85     | 7.10     | 7.10    |
| 6        | MPI_Waitall                     | 0.39     | 3.30     | 3.30    |
| 7        | MPI_Isend                       | 0.08     | 0.70     | 0.70    |
| 8        | mfem::AddMult_a_VVt             | 0.08     | 0.70     | 0.00    |
| 9        | MPI_Irecv                       | 0.08     | 0.70     | 0.70    |
| 10       | mfem::DenseMatrix::Mult         | 0.06     | 0.50     | 0.00    |

#### Test Case 2: 3DRemap x Compiler 1: `gcc@10.3.0`
| Position | Routine             | Time (s) | Time (%) | MPI (%) |
|----------|---------------------|----------|----------|---------|
| 1        | MPI_Allreduce       | 0.24     | 39.10    | 39.10   |
| 2        | MPI_Finalize        | 0.06     | 9.00     | 9.00    |
| 3        | MPI_Waitany         | 0.04     | 6.70     | 6.70    |
| 4        | MPI_Waitall         | 0.03     | 5.60     | 5.60    |
| 5        | mfem::Mult          | 0.03     | 4.80     | 0.00    |
| 6        | MPI_Isend           | 0.02     | 3.80     | 3.80    |
| 7        | mfem::AddMultVWt    | 0.02     | 3.70     | 0.00    |
| 8        | mfem::AddMult_a_VVt | 0.02     | 3.50     | 0.00    |
| 9        | MPI_Barrier         | 0.02     | 2.90     | 2.90    |
| 10       | MPI_Scan            | 0.01     | 2.20     | 2.20    |

#### Test Case 2: 3DRemap x Compiler 2: `arm@21.0.0.879`
| Position | Routine             | Time (s) | Time (%) | MPI (%) |
|----------|---------------------|----------|----------|---------|
| 1        | MPI_Allreduce       | 0.24     | 37.80    | 37.80   |
| 2        | MPI_Finalize        | 0.05     | 7.60     | 7.60    |
| 3        | MPI_Waitall         | 0.04     | 6.40     | 6.40    |
| 4        | MPI_Bcast           | 0.03     | 5.40     | 5.40    |
| 5        | mfem::Mult          | 0.03     | 5.30     | 0.00    |
| 6        | mfem::AddMult_a_VVt | 0.03     | 4.40     | 0.00    |
| 7        | MPI_Waitany         | 0.02     | 3.80     | 3.80    |
| 8        | mfem::AddMultVWt    | 0.02     | 3.50     | 0.00    |
| 9        | MPI_Isend           | 0.02     | 3.40     | 3.40    |
| 10       | MPI_Barrier         | 0.02     | 3.30     | 3.30    |

#### Test Case 2: 3DRemap x Compiler 3: `nvhpc@21.2`
```
Maximum backtrace size in sampler exceeded, stack too deep.
```
| Position | Routine                         | Time (s) | Time (%) | MPI (%) |
|----------|---------------------------------|----------|----------|---------|
| 1        | ompi_mtl_ofi_progress_no_inline | 2.10     | 38.20    | 38.20   |
| 2        | MPI_Bcast                       | 0.86     | 15.70    | 15.70   |
| 3        | ompi_mtl_ofi_iprobe_true        | 0.74     | 13.50    | 13.50   |
| 4        | MPI_Isend                       | 0.68     | 12.40    | 12.40   |
| 5        | <unknown>                       | 0.25     | 4.50     | 16.90   |
| 6        | ompi_request_default_test_all   | 0.25     | 4.50     | 4.50    |
| 7        | MPI_Allreduce                   | 0.19     | 3.40     | 3.40    |
| 8        | mfem::AddMult_a_VVt             | 0.12     | 2.20     | 0.00    |
| 9        | mfem::Mult                      | 0.12     | 2.20     | 0.00    |
| 10       | MPI_Waitall                     | 0.12     | 2.20     | 2.20    |

#### Test Case 3: 2DTransport x Compiler 1: `gcc@10.3.0`
| Position | Routine                     | Time (s) | Time (%) | MPI (%) |
|----------|-----------------------------|----------|----------|---------|
| 1        | MPI_Allreduce               | 2.00     | 73.30    | 73.30   |
| 2        | MPI_Waitall                 | 0.22     | 8.20     | 8.20    |
| 3        | MPI_Isend                   | 0.07     | 2.50     | 2.50    |
| 4        | MPI_Waitany                 | 0.07     | 2.50     | 2.50    |
| 5        | mfem::SparseMatrix::AddMult | 0.07     | 2.40     | 0.00    |
| 6        | MPI_Finalize                | 0.05     | 2.00     | 2.00    |
| 7        | MPI_Send                    | 0.04     | 1.60     | 1.60    |
| 8        | MPI_Irecv                   | 0.04     | 1.30     | 1.30    |
| 9        | MPI_Bcast                   | 0.03     | 1.00     | 1.00    |
| 10       | MPI_Scan                    | 0.03     | 1.00     | 1.00    |

#### Test Case 3: 2DTransport x Compiler 2: `arm@21.0.0.879`
| Position | Routine                     | Time (s) | Time (%) | MPI (%) |
|----------|-----------------------------|----------|----------|---------|
| 1        | MPI_Allreduce               | 1.99     | 74.90    | 74.90   |
| 2        | MPI_Waitall                 | 0.18     | 6.60     | 6.60    |
| 3        | MPI_Waitany                 | 0.07     | 2.70     | 2.70    |
| 4        | MPI_Isend                   | 0.06     | 2.30     | 2.30    |
| 5        | mfem::SparseMatrix::AddMult | 0.06     | 2.20     | 0.00    |
| 6        | MPI_Finalize                | 0.05     | 1.70     | 1.70    |
| 7        | MPI_Send                    | 0.05     | 1.70     | 1.70    |
| 8        | MPI_Bcast                   | 0.04     | 1.50     | 1.50    |
| 9        | MPI_Irecv                   | 0.03     | 1.30     | 1.30    |
| 10       | MPI_Scan                    | 0.03     | 1.10     | 1.10    |

#### Test Case 3: 2DTransport x Compiler 3: `nvhpc@21.2`
```
Maximum backtrace size in sampler exceeded, stack too deep.
```
| Position | Routine                         | Time (s) | Time (%) | MPI (%) |
|----------|---------------------------------|----------|----------|---------|
| 1        | MPI_Allreduce                   | 2.23     | 38.50    | 38.50   |
| 2        | MPI_Bcast                       | 1.35     | 23.30    | 23.30   |
| 3        | <unknown>                       | 1.21     | 21.00    | 0.80    |
| 4        | MPI_Waitall                     | 0.27     | 4.60     | 4.60    |
| 5        | MPI_Isend                       | 0.22     | 3.80     | 3.80    |
| 6        | mfem::SparseMatrix::AddMult     | 0.13     | 2.30     | 0.00    |
| 7        | ompi_mtl_ofi_progress_no_inline | 0.09     | 1.50     | 1.50    |
| 8        | MPI_Reduce                      | 0.05     | 0.80     | 0.80    |
| 9        | __mpn_mul_1                     | 0.05     | 0.80     | 0.00    |
| 10       | libmetis__FM_2WayRefine         | 0.05     | 0.80     | 0.00    |

#### Test Case 4: 3DTransport x Compiler 1: `gcc@10.3.0`
| Position | Routine                     | Time (s) | Time (%) | MPI (%) |
|----------|-----------------------------|----------|----------|---------|
| 1        | MPI_Allreduce               | 2.92     | 65.20    | 65.20   |
| 2        | MPI_Waitall                 | 0.53     | 11.80    | 11.80   |
| 3        | MPI_Waitany                 | 0.28     | 6.30     | 6.30    |
| 4        | MPI_Isend                   | 0.21     | 4.80     | 4.80    |
| 5        | MPI_Irecv                   | 0.10     | 2.30     | 2.30    |
| 6        | mfem::SparseMatrix::AddMult | 0.08     | 1.80     | 0.00    |
| 7        | MPI_Finalize                | 0.07     | 1.60     | 1.60    |
| 8        | MPI_Bcast                   | 0.06     | 1.30     | 1.30    |
| 9        | MPI_Send                    | 0.05     | 1.20     | 1.20    |
| 10       | MPI_Scan                    | 0.04     | 1.00     | 1.00    |

#### Test Case 4: 3DTransport x Compiler 2: `arm@21.0.0.879`
| Position | Routine                           | Time (s) | Time (%) | MPI (%) |
|----------|-----------------------------------|----------|----------|---------|
| 1        | MPI_Allreduce                     | 2.79     | 63.90    | 63.90   |
| 2        | MPI_Waitall                       | 0.51     | 11.60    | 11.60   |
| 3        | MPI_Waitany                       | 0.35     | 8.10     | 8.10    |
| 4        | MPI_Isend                         | 0.22     | 5.10     | 5.10    |
| 5        | MPI_Irecv                         | 0.11     | 2.60     | 2.60    |
| 6        | mfem::SparseMatrix::AddMult       | 0.09     | 2.00     | 0.00    |
| 7        | MPI_Send                          | 0.06     | 1.30     | 1.30    |
| 8        | MPI_Bcast                         | 0.04     | 1.00     | 1.00    |
| 9        | MPI_Finalize                      | 0.04     | 0.90     | 0.90    |
| 10       | mfem::Assembly::LinearFluxLumping | 0.03     | 0.60     | 0.00    |

#### Test Case 4: 3DTransport x Compiler 3: `nvhpc@21.2`
```
Maximum backtrace size in sampler exceeded, stack too deep.
```
| Position | Routine                         | Time (s) | Time (%) | MPI (%) |
|----------|---------------------------------|----------|----------|---------|
| 1        | MPI_Allreduce                   | 3.75     | 33.40    | 33.40   |
| 2        | <unknown>                       | 1.84     | 16.40    | 4.90    |
| 3        | ompi_mtl_ofi_progress_no_inline | 1.82     | 16.20    | 16.20   |
| 4        | ompi_mtl_ofi_iprobe_true        | 0.99     | 8.80     | 8.80    |
| 5        | MPI_Bcast                       | 0.90     | 8.00     | 8.00    |
| 6        | MPI_Isend                       | 0.55     | 4.90     | 4.90    |
| 7        | MPI_Waitall                     | 0.55     | 4.90     | 4.90    |
| 8        | PMPI_Testall                    | 0.25     | 2.20     | 2.20    |
| 9        | MPI_Waitany                     | 0.17     | 1.50     | 1.50    |
| 10       | mfem::SparseMatrix::AddMult     | 0.12     | 1.10     | 0.00    |
