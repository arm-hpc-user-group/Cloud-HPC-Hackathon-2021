#!/bin/bash

#SBATCH --job-name=SWFFT.ARMFORGE
#SBATCH --nodes=1
#SBATCH --ntasks=64
#SBATCH --cpus-per-task=1
#SBATCH -p c6gn
#SBATCH --exclusive

spack load swfft@1.0%gcc@10.3.0
spack load arm-forge@21.0

export OMP_NUM_THREADS=1

map --profile srun TestDfft 5 512
