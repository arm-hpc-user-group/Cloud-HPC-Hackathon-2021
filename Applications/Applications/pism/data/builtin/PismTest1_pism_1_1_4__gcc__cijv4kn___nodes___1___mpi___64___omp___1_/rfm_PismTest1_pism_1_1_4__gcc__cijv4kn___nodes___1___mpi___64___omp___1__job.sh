#!/bin/bash
#SBATCH --job-name="rfm_PismTest1_pism_1_1_4__gcc__cijv4kn___nodes___1___mpi___64___omp___1__job"
#SBATCH --ntasks=64
#SBATCH --ntasks-per-node=64
#SBATCH --cpus-per-task=1
#SBATCH --output=rfm_PismTest1_pism_1_1_4__gcc__cijv4kn___nodes___1___mpi___64___omp___1__job.out
#SBATCH --error=rfm_PismTest1_pism_1_1_4__gcc__cijv4kn___nodes___1___mpi___64___omp___1__job.err
#SBATCH -p c6gn
#SBATCH --exclusive
spack load pism@1.1.4 %gcc /cijv4kn
export OMP_NUM_THREADS=1
export OMP_PLACES=cores
srun /usr/bin/time -f "real:%e" pismv -test B -Mx 61 -Mz 11 -ys 422.45 -y 25000 &> pismv.out
