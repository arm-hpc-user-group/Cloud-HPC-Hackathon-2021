#!/bin/bash
#SBATCH --job-name="rfm_BransonTest0_branson_0_82__arm___nodes___1___mpi___1___omp___1__job"
#SBATCH --ntasks=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --output=rfm_BransonTest0_branson_0_82__arm___nodes___1___mpi___1___omp___1__job.out
#SBATCH --error=rfm_BransonTest0_branson_0_82__arm___nodes___1___mpi___1___omp___1__job.err
#SBATCH -p c6gn
#SBATCH --exclusive
spack load arm-forge
spack load branson@0.82 %arm
export OMP_NUM_THREADS=1
export OMP_PLACES=cores
cp /home/iman/rfms/branson/proxy_small.xml ./branson.in
map --profile --export-functions=profile.csv srun BRANSON ./branson.in > branson.out
