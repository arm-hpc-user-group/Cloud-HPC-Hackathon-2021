#!/bin/bash
#SBATCH --job-name="rfm_MiniTriTest_amg2013__gcc_10_3_0___nodes___1___mpi___16___omp___1___extra_cmd____1_4_4___job"
#SBATCH --ntasks=16
#SBATCH --ntasks-per-node=16
#SBATCH --cpus-per-task=1
#SBATCH --output=rfm_MiniTriTest_amg2013__gcc_10_3_0___nodes___1___mpi___16___omp___1___extra_cmd____1_4_4___job.out
#SBATCH --error=rfm_MiniTriTest_amg2013__gcc_10_3_0___nodes___1___mpi___16___omp___1___extra_cmd____1_4_4___job.err
#SBATCH -p c6gn
#SBATCH --exclusive=user
spack load amg2013 %gcc@10.3.0
export OMP_NUM_THREADS=1
export OMP_PLACES=cores
wget https://asc.llnl.gov/sites/asc/files/2021-01/amg2013_0.tgz
tar xzf amg2013_0.tgz
srun time amg2013 ./AMG2013/test/sstruct.in.MG.FD
