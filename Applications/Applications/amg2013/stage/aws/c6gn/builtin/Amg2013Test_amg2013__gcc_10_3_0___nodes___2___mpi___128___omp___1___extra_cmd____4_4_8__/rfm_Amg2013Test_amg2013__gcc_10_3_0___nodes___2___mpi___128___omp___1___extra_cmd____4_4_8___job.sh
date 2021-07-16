#!/bin/bash
#SBATCH --job-name="rfm_Amg2013Test_amg2013__gcc_10_3_0___nodes___2___mpi___128___omp___1___extra_cmd____4_4_8___job"
#SBATCH --ntasks=128
#SBATCH --ntasks-per-node=64
#SBATCH --cpus-per-task=1
#SBATCH --output=rfm_Amg2013Test_amg2013__gcc_10_3_0___nodes___2___mpi___128___omp___1___extra_cmd____4_4_8___job.out
#SBATCH --error=rfm_Amg2013Test_amg2013__gcc_10_3_0___nodes___2___mpi___128___omp___1___extra_cmd____4_4_8___job.err
#SBATCH -p c6gn
#SBATCH --exclusive=user
spack load amg2013 %gcc@10.3.0
export OMP_NUM_THREADS=1
export OMP_PLACES=cores
wget https://asc.llnl.gov/sites/asc/files/2021-01/amg2013_0.tgz
tar xzf amg2013_0.tgz
ln -sf ./AMG2013/test/sstruct.in.MG.FD .
srun time amg2013
