#!/bin/bash
#SBATCH --job-name="rfm_PismTest0HS_pism_1_1_4__gcc___nodes___1___mpi___64___omp___1__job"
#SBATCH --ntasks=64
#SBATCH --ntasks-per-node=64
#SBATCH --cpus-per-task=1
#SBATCH --output=rfm_PismTest0HS_pism_1_1_4__gcc___nodes___1___mpi___64___omp___1__job.out
#SBATCH --error=rfm_PismTest0HS_pism_1_1_4__gcc___nodes___1___mpi___64___omp___1__job.err
#SBATCH -p c6gn
#SBATCH --exclusive
spack load arm-forge
spack load pism@1.1.4 %gcc
export OMP_NUM_THREADS=1
export OMP_PLACES=cores
map --profile --export-functions=profile.csv srun /usr/bin/time -f "real:%e" pismv -test A -Mx 61 -Mz 11 -y 25000 &> pismv.out
