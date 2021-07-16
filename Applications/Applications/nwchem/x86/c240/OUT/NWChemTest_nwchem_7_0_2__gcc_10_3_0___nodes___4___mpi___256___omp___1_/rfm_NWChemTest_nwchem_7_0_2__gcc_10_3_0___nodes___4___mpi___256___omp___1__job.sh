#!/bin/bash
#SBATCH --job-name="rfm_NWChemTest_nwchem_7_0_2__gcc_10_3_0___nodes___4___mpi___256___omp___1__job"
#SBATCH --ntasks=256
#SBATCH --ntasks-per-node=64
#SBATCH --cpus-per-task=1
#SBATCH --output=rfm_NWChemTest_nwchem_7_0_2__gcc_10_3_0___nodes___4___mpi___256___omp___1__job.out
#SBATCH --error=rfm_NWChemTest_nwchem_7_0_2__gcc_10_3_0___nodes___4___mpi___256___omp___1__job.err
#SBATCH -p c5n
#SBATCH --exclusive
spack load nwchem@7.0.2 %gcc@10.3.0
export OMP_NUM_THREADS=1
export OMP_PLACES=cores
wget -O nwchem.nw https://nwchemgit.github.io/c240_631gs.nw
srun nwchem nwchem.nw > nwchem.out
