#!/bin/bash
#SBATCH --job-name="rfm_PismTest2_pism_1_1_4__gcc__cijv4kn___nodes___1___mpi___16___omp___1__job"
#SBATCH --ntasks=16
#SBATCH --ntasks-per-node=16
#SBATCH --cpus-per-task=1
#SBATCH --output=rfm_PismTest2_pism_1_1_4__gcc__cijv4kn___nodes___1___mpi___16___omp___1__job.out
#SBATCH --error=rfm_PismTest2_pism_1_1_4__gcc__cijv4kn___nodes___1___mpi___16___omp___1__job.err
#SBATCH -p c6gn
#SBATCH --exclusive
spack load pism@1.1.4 %gcc /cijv4kn
export OMP_NUM_THREADS=1
export OMP_PLACES=cores
srun /usr/bin/time -f "real:%e" pismv -test C -Mx 61 -Mz 11 -y 15208.0 &> pismv.out
