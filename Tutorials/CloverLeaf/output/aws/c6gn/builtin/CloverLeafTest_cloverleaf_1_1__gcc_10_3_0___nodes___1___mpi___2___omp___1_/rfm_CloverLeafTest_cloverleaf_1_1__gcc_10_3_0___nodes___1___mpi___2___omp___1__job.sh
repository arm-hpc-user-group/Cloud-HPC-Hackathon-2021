#!/bin/bash
#SBATCH --job-name="rfm_CloverLeafTest_cloverleaf_1_1__gcc_10_3_0___nodes___1___mpi___2___omp___1__job"
#SBATCH --ntasks=2
#SBATCH --ntasks-per-node=2
#SBATCH --cpus-per-task=1
#SBATCH --output=rfm_CloverLeafTest_cloverleaf_1_1__gcc_10_3_0___nodes___1___mpi___2___omp___1__job.out
#SBATCH --error=rfm_CloverLeafTest_cloverleaf_1_1__gcc_10_3_0___nodes___1___mpi___2___omp___1__job.err
#SBATCH -p c6gn
#SBATCH --exclusive
spack load cloverleaf@1.1 %gcc@10.3.0
export OMP_NUM_THREADS=1
export OMP_PLACES=cores
wget -O clover.in https://raw.githubusercontent.com/UK-MAC/CloverLeaf_ref/master/InputDecks/clover_bm16_short.in
srun clover_leaf
