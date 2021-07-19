#!/bin/bash
#SBATCH --job-name="rfm_BransonTest0_branson_0_82__arm___nodes___1___mpi___32___omp___2__job"
#SBATCH --ntasks=32
#SBATCH --ntasks-per-node=32
#SBATCH --cpus-per-task=2
#SBATCH --output=rfm_BransonTest0_branson_0_82__arm___nodes___1___mpi___32___omp___2__job.out
#SBATCH --error=rfm_BransonTest0_branson_0_82__arm___nodes___1___mpi___32___omp___2__job.err
#SBATCH -p c6gn
#SBATCH --exclusive
spack load arm-forge
spack load branson@0.82 %arm
export OMP_NUM_THREADS=2
export OMP_PLACES=cores
cp /home/iman/rfms/branson/proxy_small.xml ./branson.in
map --profile --output=profile.map srun BRANSON ./branson.in > branson.out
