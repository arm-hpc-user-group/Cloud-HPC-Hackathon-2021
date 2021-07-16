#!/bin/bash
#SBATCH --job-name="rfm_LaghosTest0_branson_0_82__arm___nodes___1___mpi___32___omp___1__job"
#SBATCH --ntasks=32
#SBATCH --ntasks-per-node=32
#SBATCH --cpus-per-task=1
#SBATCH --output=rfm_LaghosTest0_branson_0_82__arm___nodes___1___mpi___32___omp___1__job.out
#SBATCH --error=rfm_LaghosTest0_branson_0_82__arm___nodes___1___mpi___32___omp___1__job.err
#SBATCH -p c6gn
#SBATCH --exclusive
spack load arm-forge
spack load branson@0.82 %arm
export OMP_NUM_THREADS=1
export OMP_PLACES=cores
wget -O branson.in https://raw.githubusercontent.com/lanl/branson/develop/inputs/proxy_small.xml
map --profile --output=profile.map srun BRANSON ./branson.in > branson.out
