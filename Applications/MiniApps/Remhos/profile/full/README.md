#### Full Node Hot-spot Profile
The 12 tables below are the full node hot-spot profiling results across 3 compilers and 4 test cases. The raw profiles can be found at the current directory.

Profiling command used:
```
map --profile -o profile/full/<test case>_<compiler>.map srun -N 1 -n 64 remhos <executable opts based on the test case>
```

##### Test Case 1: 2DRemap x Compiler 1: `gcc@10.3.0`
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

##### Test Case 1: 2DRemap x Compiler 2: `arm@21.0.0.879`
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

##### Test Case 1: 2DRemap x Compiler 3: `nvhpc@21.2`
```
Maximum backtrace size in sampler exceeded, stack too deep.
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

##### Test Case 2: 3DRemap x Compiler 1: `gcc@10.3.0`
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

##### Test Case 2: 3DRemap x Compiler 2: `arm@21.0.0.879`
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

##### Test Case 2: 3DRemap x Compiler 3: `nvhpc@21.2`
```
Maximum backtrace size in sampler exceeded, stack too deep.
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

##### Test Case 3: 2DTransport x Compiler 1: `gcc@10.3.0`
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

##### Test Case 3: 2DTransport x Compiler 2: `arm@21.0.0.879`
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

##### Test Case 3: 2DTransport x Compiler 3: `nvhpc@21.2`
```
Maximum backtrace size in sampler exceeded, stack too deep.
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

##### Test Case 4: 3DTransport x Compiler 1: `gcc@10.3.0`
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

##### Test Case 4: 3DTransport x Compiler 2: `arm@21.0.0.879`
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

##### Test Case 4: 3DTransport x Compiler 3: `nvhpc@21.2`
```
Maximum backtrace size in sampler exceeded, stack too deep.
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
