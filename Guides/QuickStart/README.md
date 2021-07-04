# Quick Start Guide

Based on the other user guides and Tutorial examples.

## Building CloverLeaf

`spack install cloverleaf@arm`

## ReFrame Example

```
cd /shared/home/$USER
git clone https://github.com/arm-hpc-user-group/Cloud-HPC-Hackathon-2021.git

cd Cloud-HPC-Hackathon-2021/Tutorials/CloverLeaf/
```

### Edit the File

`vim cloverleaf_bm16_short.py`


Add your team name:
```
# Logging Variables
log_team_name = '<<TEAM NAME>>'
```

Set the right compiler spec:

```
 # Parameters - Compilers - Defined as their Spack specs (use spec or hash)
    spec = parameter([
        'cloverleaf@1.1 %arm@21.0.0.879' # CloverLeaf with the Arm compiler
    ])
```

Set the desired core counts:

```
# Parameters - MPI / Threads - Used for scaling studies
    parallelism = parameter([
        { 'nodes' : 1, 'mpi' : 16, 'omp' : 1},
        { 'nodes' : 1, 'mpi' : 32, 'omp' : 1},
        { 'nodes' : 1, 'mpi' : 64, 'omp' : 1},
    ])
```

### Run ReFrame

```
reframe -c cloverleaf_bm16_short.py -r --performance-report
```

Now just check that the test passed.

### Next Steps

Build CloverLeaf for the other compilers and test again.