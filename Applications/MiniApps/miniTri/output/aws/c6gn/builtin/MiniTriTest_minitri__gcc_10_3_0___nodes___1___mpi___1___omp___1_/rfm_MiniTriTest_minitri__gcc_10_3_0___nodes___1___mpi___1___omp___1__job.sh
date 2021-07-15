#!/bin/bash
#SBATCH --job-name="rfm_MiniTriTest_minitri__gcc_10_3_0___nodes___1___mpi___1___omp___1__job"
#SBATCH --ntasks=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --output=rfm_MiniTriTest_minitri__gcc_10_3_0___nodes___1___mpi___1___omp___1__job.out
#SBATCH --error=rfm_MiniTriTest_minitri__gcc_10_3_0___nodes___1___mpi___1___omp___1__job.err
#SBATCH -p c6gn
spack load minitri %gcc@10.3.0
export OMP_NUM_THREADS=1
export OMP_PLACES=cores
wget https://sparse.tamu.edu/MM/SNAP/ca-GrQc.tar.gz
tar xzf ca-GrQc.tar.gz
srun time miniTri.exe ./ca-GrQc/ca-GrQc.mtx
