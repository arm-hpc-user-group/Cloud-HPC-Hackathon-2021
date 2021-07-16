#!/bin/bash
#SBATCH --job-name="rfm_LaghosTest_laghos_3_1__nvhpc___nodes___4___mpi___256___omp___1__job"
#SBATCH --ntasks=256
#SBATCH --ntasks-per-node=64
#SBATCH --cpus-per-task=1
#SBATCH --output=rfm_LaghosTest_laghos_3_1__nvhpc___nodes___4___mpi___256___omp___1__job.out
#SBATCH --error=rfm_LaghosTest_laghos_3_1__nvhpc___nodes___4___mpi___256___omp___1__job.err
#SBATCH -p c6gn
#SBATCH --exclusive
spack load laghos@3.1 %nvhpc
export OMP_NUM_THREADS=1
export OMP_PLACES=cores
srun laghos -p 0 -dim 2 -rs 3 -tf 0.75 -pa > laghos.out
