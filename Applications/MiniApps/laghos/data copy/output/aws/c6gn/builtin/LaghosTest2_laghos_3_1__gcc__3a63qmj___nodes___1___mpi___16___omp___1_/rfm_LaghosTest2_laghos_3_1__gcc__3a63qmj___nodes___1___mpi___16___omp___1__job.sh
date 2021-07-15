#!/bin/bash
#SBATCH --job-name="rfm_LaghosTest2_laghos_3_1__gcc__3a63qmj___nodes___1___mpi___16___omp___1__job"
#SBATCH --ntasks=16
#SBATCH --ntasks-per-node=16
#SBATCH --cpus-per-task=1
#SBATCH --output=rfm_LaghosTest2_laghos_3_1__gcc__3a63qmj___nodes___1___mpi___16___omp___1__job.out
#SBATCH --error=rfm_LaghosTest2_laghos_3_1__gcc__3a63qmj___nodes___1___mpi___16___omp___1__job.err
#SBATCH -p c6gn
#SBATCH --exclusive
spack load laghos@3.1 %gcc /3a63qmj
export OMP_NUM_THREADS=1
export OMP_PLACES=cores
srun laghos -p 1 -dim 2 -rs 3 -tf 0.8 -pa > laghos.out
