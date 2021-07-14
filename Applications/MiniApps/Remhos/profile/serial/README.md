#### Serial Hot-spot Profile
The 12 tables below are the serial hot-spot profiling results across 3 compilers and 4 test cases. The raw profiles can be found at the current directory.

Profiling command used:
```
export OMP_NUM_THREADS=1
map --profile -o profile/serial/<test case>_<compiler>.map srun -N 1 -n 1 remhos <executable opts based on the test case>
```

##### Test Case 1: 2DRemap x Compiler 1: `gcc@10.3.0`
| Position | Routine                                                           | Time (s) | Time (%) |
|----------|-------------------------------------------------------------------|----------|----------|
| 1        | mfem::AddMult_a_VVt                                               |    2.39  |   13.40  |
| 2        | mfem::AddMultVWt                                                  |    2.01  |   11.30  |
| 3        | mfem::SparseMatrix::AddSubMatrix                                  |    1.60  |    9.00  |
| 4        | mfem::Mult                                                        |    1.42  |    8.00  |
| 5        | mfem::Poly_1D::Basis::Eval(double, mfem::Vector&, mfem::Vector&)  |    1.19  |    6.70  |
| 6        | mfem::SparseMatrix::AddMult                                       |    1.10  |    6.20  |
| 7        | mfem::Poly_1D::CalcBinomTerms                                     |    0.84  |    4.70  |
| 8        | mfem::Poly_1D::Basis::Eval(double, mfem::Vector&)                 |    0.50  |    2.80  |
| 9        | mfem::SparseMatrix::SearchRow                                     |    0.43  |    2.40  |
| 10       | mfem::L2Pos_QuadrilateralElement::CalcDShape                      |    0.37  |    2.10  |

##### Test Case 1: 2DRemap x Compiler 1: `gcc@10.3.0`
| Position | Routine                                                           | Time (s) | Time (%) |
|----------|-------------------------------------------------------------------|----------|----------|
| 1        | mfem::AddMult_a_VVt                                               |    2.39  |   13.40  |
| 2        | mfem::AddMultVWt                                                  |    2.01  |   11.30  |
| 3        | mfem::Mult                                                        |    1.42  |    8.00  |
| 4        | mfem::Poly_1D::Basis::Eval(double, mfem::Vector&, mfem::Vector&)  |    1.19  |    6.70  |
| 5        | mfem::SparseMatrix::AddSubMatrix                                  |    1.60  |    9.00  |
| 6        | mfem::SparseMatrix::AddMult                                       |    1.10  |    6.20  |
| 7        | mfem::L2Pos_QuadrilateralElement::CalcShape                       |    0.84  |    4.70  |
| 8        | mfem::Poly_1D::CalcBinomTerms                                     |    0.50  |    2.80  |
| 9        | mfem::L2Pos_QuadrilateralElement::CalcDShape                      |    0.37  |    2.10  |
| 10       | mfem::Poly_1D::Basis::Eval(double, mfem::Vector&)                 |    0.43  |    2.40  |

##### Test Case 1: 2DRemap x Compiler 2: `arm@21.0.0.879`
| Position | Routine                                                           | Time (s) | Time (%) |
|----------|-------------------------------------------------------------------|----------|----------|
| 1        | mfem::AddMult_a_VVt                                               | 3.33     | 16.80    |
| 2        | mfem::AddMultVWt                                                  | 2.24     | 11.30    |
| 3        | mfem::Mult                                                        | 1.47     | 7.40     |
| 4        | mfem::Poly_1D::Basis::Eval(double, mfem::Vector&, mfem::Vector&)  | 1.45     | 7.30     |
| 5        | mfem::SparseMatrix::AddSubMatrix                                  | 1.39     | 7.00     |
| 6        | mfem::SparseMatrix::AddMult                                       | 1.03     | 5.20     |
| 7        | mfem::L2Pos_QuadrilateralElement::CalcShape                       | 0.81     | 4.10     |
| 8        | mfem::Poly_1D::CalcBinomTerms                                     | 0.56     | 2.80     |
| 9        | mfem::L2Pos_QuadrilateralElement::CalcDShape                      | 0.52     | 2.60     |
| 10       | mfem::Poly_1D::Basis::Eval(double, mfem::Vector&)                 | 0.50     | 2.50     |

##### Test Case 1: 2DRemap x Compiler 2: `arm@21.0.0.879`
| Position | Routine                                                           | Time (s) | Time (%) |
|----------|-------------------------------------------------------------------|----------|----------|
| 1        | mfem::AddMult_a_VVt                                               | 3.33     | 16.80    |
| 2        | mfem::AddMultVWt                                                  | 2.24     | 11.30    |
| 3        | mfem::Mult                                                        | 1.47     | 7.40     |
| 4        | mfem::Poly_1D::Basis::Eval(double, mfem::Vector&, mfem::Vector&)  | 1.45     | 7.30     |
| 5        | mfem::SparseMatrix::AddSubMatrix                                  | 1.39     | 7.00     |
| 6        | mfem::SparseMatrix::AddMult                                       | 1.03     | 5.20     |
| 7        | mfem::L2Pos_QuadrilateralElement::CalcShape                       | 0.81     | 4.10     |
| 8        | mfem::Poly_1D::CalcBinomTerms                                     | 0.56     | 2.80     |
| 9        | mfem::L2Pos_QuadrilateralElement::CalcDShape                      | 0.52     | 2.60     |
| 10       | mfem::Poly_1D::Basis::Eval(double, mfem::Vector&)                 | 0.50     | 2.50     |

##### Test Case 1: 2DRemap x Compiler 3: `nvhpc@21.2`
| Position | Routine                                                          | Time (s) | Time (%) |
|----------|------------------------------------------------------------------|----------|----------|
| 1        | mfem::AddMultVWt                                                 | 4.44     | 20.10    |
| 2        | mfem::AddMult_a_VVt                                              | 4.05     | 18.30    |
| 3        | mfem::Mult                                                       | 1.59     | 7.20     |
| 4        | mfem::SparseMatrix::AddSubMatrix                                 | 1.48     | 6.70     |
| 5        | mfem::SparseMatrix::AddMult                                      | 1.26     | 5.70     |
| 6        | mfem::L2Pos_QuadrilateralElement::CalcShape                      | 1.02     | 4.60     |
| 7        | mfem::Poly_1D::Basis::Eval(double, mfem::Vector&, mfem::Vector&) | 0.84     | 3.80     |
| 8        | mfem::H1_QuadrilateralElement::CalcDShape                        | 0.82     | 3.70     |
| 9        | mfem::L2Pos_QuadrilateralElement::CalcDShape                     | 0.80     | 3.60     |
| 10       | mfem::Poly_1D::Basis::Eval(double, mfem::Vector&)                | 0.51     | 2.30     |

##### Test Case 2: 3DRemap x Compiler 1: `gcc@10.3.0`
| Position | Routine                                                          | Time (s) | Time (%) |
|----------|------------------------------------------------------------------|----------|----------|
| 1        | mfem::Mult                                                       | 2.33     | 24.50    |
| 2        | mfem::AddMult_a_VVt                                              | 1.59     | 16.70    |
| 3        | mfem::AddMultVWt                                                 | 1.47     | 15.50    |
| 4        | mfem::SparseMatrix::AddSubMatrix                                 | 0.53     | 5.60     |
| 5        | mfem::Poly_1D::Basis::Eval(double, mfem::Vector&, mfem::Vector&) | 0.48     | 5.00     |
| 6        | mfem::L2Pos_HexahedronElement::CalcShape                         | 0.48     | 5.00     |
| 7        | mfem::H1_HexahedronElement::CalcDShape                           | 0.31     | 3.30     |
| 8        | mfem::Assembly::ComputeFluxTerms                                 | 0.29     | 3.10     |
| 9        | mfem::Vector::operator*                                          | 0.22     | 2.30     |
| 10       | mfem::H1_HexahedronElement::CalcShape                            | 0.22     | 2.30     |

##### Test Case 2: 3DRemap x Compiler 2: `arm@21.0.0.879`
| Position | Routine                                                          | Time (s) | Time (%) |
|----------|------------------------------------------------------------------|----------|----------|
| 1        | mfem::AddMult_a_VVt                                              | 2.25     | 20.70    |
| 2        | mfem::Mult                                                       | 1.97     | 18.10    |
| 3        | mfem::AddMultVWt                                                 | 1.41     | 13.00    |
| 4        | mfem::Poly_1D::Basis::Eval(double, mfem::Vector&, mfem::Vector&) | 0.76     | 7.00     |
| 5        | mfem::L2Pos_HexahedronElement::CalcDShape                        | 0.62     | 5.70     |
| 6        | mfem::L2Pos_HexahedronElement::CalcShape                         | 0.53     | 4.90     |
| 7        | mfem::SparseMatrix::AddSubMatrix                                 | 0.36     | 3.30     |
| 8        | mfem::H1_HexahedronElement::CalcDShape                           | 0.36     | 3.30     |
| 9        | mfem::Vector::operator*                                          | 0.36     | 3.30     |
| 10       | mfem::Poly_1D::Basis::Eval(double, mfem::Vector&)                | 0.28     | 2.60     |

##### Test Case 2: 3DRemap x Compiler 3: `nvhpc@21.2`
| Position | Routine                                                          | Time (s) | Time (%) |
|----------|------------------------------------------------------------------|----------|----------|
| 1        | mfem::Mult                                                       | 2.65     | 21.30    |
| 2        | mfem::AddMult_a_VVt                                              | 2.61     | 21.00    |
| 3        | mfem::AddMultVWt                                                 | 2.08     | 16.70    |
| 4        | mfem::Assembly::ComputeFluxTerms                                 | 0.76     | 6.10     |
| 5        | mfem::Poly_1D::Basis::Eval(double, mfem::Vector&, mfem::Vector&) | 0.63     | 5.10     |
| 6        | mfem::H1_HexahedronElement::CalcDShape                           | 0.60     | 4.80     |
| 7        | mfem::H1_HexahedronElement::CalcShape                            | 0.48     | 3.90     |
| 8        | mfem::L2Pos_HexahedronElement::CalcDShape                        | 0.37     | 3.00     |
| 9        | mfem::L2Pos_HexahedronElement::CalcShape                         | 0.30     | 2.40     |
| 10       | mfem::Poly_1D::Binom                                             | 0.24     | 1.90     |

##### Test Case 3: 2DTransport x Compiler 1: `gcc@10.3.0`
| Position | Routine                                    | Time (s) | Time (%) |
|----------|--------------------------------------------|----------|----------|
| 1        | mfem::SparseMatrix::AddMult                | 3.53     | 54.80    |
| 2        | mfem::NeumannHOSolver::CalcHOSolution      | 0.75     | 11.70    |
| 3        | mfem::ResidualDistribution::CalcLOSolution | 0.63     | 9.80     |
| 4        | mfem::Assembly::LinearFluxLumping          | 0.44     | 6.80     |
| 5        | mfem::Vector::Norml2()                     | 0.40     | 6.20     |
| 6        | mfem::ClipScaleSolver::CalcFCTSolution     | 0.16     | 2.50     |
| 7        | _int_free                                  | 0.08     | 1.20     |
| 8        | __GI__IO_file_close_it                     | 0.06     | 0.90     | 
| 9        | mfem::DofInfo::ComputeBounds               | 0.06     | 0.90     |
| 10       | mfem::Vector::operator-=                   | 0.06     | 0.90     |

##### Test Case 3: 2DTransport x Compiler 2: `arm@21.0.0.879`
| Position | Routine                                    | Time (s) | Time (%) |
|----------|--------------------------------------------|----------|----------|
| 1        | mfem::SparseMatrix::AddMult                | 3.59     | 54.90    |
| 2        | mfem::Vector::Norml2                       | 0.54     | 8.20     |
| 3        | mfem::NeumannHOSolver::CalcHOSolution      | 0.50     | 7.60     |
| 4        | mfem::ResidualDistribution::CalcLOSolution | 0.50     | 7.60     |
| 5        | mfem::Assembly::LinearFluxLumping          | 0.38     | 5.80     |
| 6        | mfem::Vector::operator=                    | 0.14     | 2.10     |
| 7        | mfem::ClipScaleSolver::CalcFCTSolution     | 0.14     | 2.10     |
| 8        | mfem::Vector::operator-=                   | 0.12     | 1.80     |
| 9        | malloc                                     | 0.10     | 1.50     |
| 10       | mfem::DofInfo::ComputeBounds               | 0.10     | 1.50     |

##### Test Case 3: 2DTransport x Compiler 3: `nvhpc@21.2`
| Position | Routine                                    | Time (s) | Time (%) |
|----------|--------------------------------------------|----------|----------|
| 1        | mfem::SparseMatrix::AddMult                | 3.46     | 50.30    |
| 2        | mfem::Assembly::LinearFluxLumping          | 1.09     | 15.90    |
| 3        | mfem::ResidualDistribution::CalcLOSolution | 0.63     | 9.20     |
| 4        | mfem::NeumannHOSolver::CalcHOSolution      | 0.56     | 8.10     |
| 5        | mfem::Vector::Norml2                       | 0.34     | 4.90     |
| 6        | mfem::ClipScaleSolver::CalcFCTSolution     | 0.22     | 3.20     |
| 7        | mfem::Vector::operator-=                   | 0.12     | 1.70     |
| 8        | mfem::Vector::operator=                    | 0.06     | 0.90     |
| 9        | malloc                                     | 0.06     | 0.90     |
| 10       | mfem::Mult                                 | 0.04     | 0.60     |

##### Test Case 4: 3DTransport x Compiler 1: `gcc@10.3.0`
| Position | Routine                                    | Time (s) | Time (%) |
|----------|--------------------------------------------|----------|----------|
| 1        | mfem::SparseMatrix::AddMult                | 5.17     | 58.70    |
| 2        | mfem::Assembly::LinearFluxLumping          | 1.09     | 12.40    |
| 3        | mfem::NeumannHOSolver::CalcHOSolution      | 0.62     | 7.00     |
| 4        | mfem::ResidualDistribution::CalcLOSolution | 0.55     | 6.30     |
| 5        | mfem::Vector::Norml2                       | 0.40     | 4.50     |
| 6        | mfem::ClipScaleSolver::CalcFCTSolution     | 0.16     | 1.80     |
| 7        | _int_free                                  | 0.08     | 0.90    |
| 8        | mfem::Vector::operator-=                   | 0.08     | 0.90     |
| 9        | mfem::DofInfo::ComputeBounds               | 0.08     | 0.90     |
| 10       | mfem::Mult                                 | 0.06     | 0.70     |

##### Test Case 4: 3DTransport x Compiler 2: `arm@21.0.0.879`
| Position | Routine                                    | Time (s) | Time (%) |
|----------|--------------------------------------------|----------|----------|
| 1        | mfem::SparseMatrix::AddMult                | 5.66     | 61.10    |
| 2        | mfem::Assembly::LinearFluxLumping          | 1.61     | 17.40    |
| 3        | mfem::Vector::Norml2                       | 0.50     | 5.40     |
| 4        | mfem::ResidualDistribution::CalcLOSolution | 0.48     | 5.20     |
| 5        | mfem::NeumannHOSolver::CalcHOSolution      | 0.42     | 4.50     |
| 6        | mfem::L2_HexahedronElement::CalcDShape     | 0.06     | 0.60     |
| 7        | mfem::ClipScaleSolver::CalcFCTSolution     | 0.06     | 0.60     |
| 8        | mfem::Mult                                 | 0.04     | 0.40     |
| 9        | mfem::AddMultVWt                           | 0.04     | 0.40     |
| 10       | mfem::Vector::operator-=                   | 0.04     | 0.40     |

##### Test Case 4: 3DTransport x Compiler 3: `nvhpc@21.2`
| Position | Routine                                    | Time (s) | Time (%) |
|----------|--------------------------------------------|----------|----------|
| 1        | mfem::SparseMatrix::AddMult                | 5.58     | 53.00    |
| 2        | mfem::Assembly::LinearFluxLumping          | 2.85     | 27.10    |
| 3        | mfem::ResidualDistribution::CalcLOSolution | 0.54     | 5.10     |
| 4        | mfem::Vector::Norml2                       | 0.46     | 4.40     |
| 5        | mfem::Vector::operator-=                   | 0.26     | 2.50     |
| 6        | mfem::AddMult_a_VVt                        | 0.12     | 1.10     |
| 7        | mfem::NeumannHOSolver::CalcHOSolution      | 0.12     | 1.10     |
| 8        | mfem::ClipScaleSolver::CalcFCTSolution     | 0.09     | 0.90     |
| 9        | mfem::Vector::operator=(double)()          | 0.06     | 0.60     |
| 10       | MPI_Allreduce                              | 0.06     | 0.60     |


