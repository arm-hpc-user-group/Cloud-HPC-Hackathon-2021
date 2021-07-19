#!/bin/bash
#SBATCH --job-name="rfm_PismTest2REDO_pism_1_1_4__arm___nodes___1___mpi___1___omp___1__job"
#SBATCH --ntasks=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --output=rfm_PismTest2REDO_pism_1_1_4__arm___nodes___1___mpi___1___omp___1__job.out
#SBATCH --error=rfm_PismTest2REDO_pism_1_1_4__arm___nodes___1___mpi___1___omp___1__job.err
#SBATCH -p c6gn
#SBATCH --exclusive
spack load pism@1.1.4 %arm
export OMP_NUM_THREADS=1
export OMP_PLACES=cores
srun /usr/bin/time -f "real:%e" pismv -test C -Mx 61 -Mz 11 -y 15208.0 &> pismv.out
