#!/bin/bash
#SBATCH --job-name="rfm_MiniTriTest_amg2013__nvhpc_21_2___nodes___4___mpi___256___omp___1___extra_cmd____4_8_8___job"
#SBATCH --ntasks=256
#SBATCH --ntasks-per-node=64
#SBATCH --cpus-per-task=1
#SBATCH --output=rfm_MiniTriTest_amg2013__nvhpc_21_2___nodes___4___mpi___256___omp___1___extra_cmd____4_8_8___job.out
#SBATCH --error=rfm_MiniTriTest_amg2013__nvhpc_21_2___nodes___4___mpi___256___omp___1___extra_cmd____4_8_8___job.err
#SBATCH -p c6gn
#SBATCH --exclusive=user
spack load amg2013 %nvhpc@21.2
export OMP_NUM_THREADS=1
export OMP_PLACES=cores
wget https://asc.llnl.gov/sites/asc/files/2021-01/amg2013_0.tgz
tar xzf amg2013_0.tgz
srun time amg2013 ./AMG2013/test/sstruct.in.MG.FD
