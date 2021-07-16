#!/bin/bash
#SBATCH --job-name="rfm_Amg2013Test_amg2013__arm_21_0_0_879___nodes___2___mpi___2___omp___1__job"
#SBATCH --ntasks=2
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --output=rfm_Amg2013Test_amg2013__arm_21_0_0_879___nodes___2___mpi___2___omp___1__job.out
#SBATCH --error=rfm_Amg2013Test_amg2013__arm_21_0_0_879___nodes___2___mpi___2___omp___1__job.err
#SBATCH -p c6gn
#SBATCH --exclusive=user
spack load amg2013 %arm@21.0.0.879
export OMP_NUM_THREADS=1
export OMP_PLACES=cores
wget https://asc.llnl.gov/sites/asc/files/2021-01/amg2013_0.tgz
tar xzf amg2013_0.tgz
srun time amg2013 -in ./AMG2013/test/sstruct.in.MG.FD
