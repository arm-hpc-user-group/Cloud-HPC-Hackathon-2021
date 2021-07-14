# mpiP

[mpiP](https://github.com/LLNL/mpiP) is a light-weight profiling library for MPI applications. Because it only collects statistical information about MPI functions, mpiP generates considerably less overhead and much less data than tracing tools. All the information captured by mpiP is task-local. It only uses communication during report generation, typically at the end of the experiment, to merge results from all of the tasks into one output file.


## Prerequisites

mpiP intercepts MPI calls at link time.  You can either compile your code with mpiP, or set the `LD_PRELOAD` environment variable at runtime.
In any case, it is recommended to build your code with debugging symbols.

### Installing mpiP with Spack

```
spack install mpip
```

## Using mpiP

mpiP is simple to use. Simply `LD_PRELOAD` the library on the execution line.
You pass options to mpiP by setting the `MPIP` environment variable.
Example:

```
export MPIP="-f output_dir"
export LD_PRELOAD=/<path to install>/lib/libmpiP.so
export OMP_NUM_THREADS=8
mpirun -np 4 --map-by slot:PE=8 ./app
```

### Output

mpiP will generate a report in a text file. Here's an example [clover_leaf.64.5895.1.mpiP](clover_leaf.64.5895.1.mpiP) 


## mpiP inside ReFrame

All of this process can be automated within a ReFrame job.

We do this via the following steps:
* Load the spack module
* Configure the pre-run commands for an output directory
* Tell ReFrame to save the output directory
* Add the `LD_PRELOAD` to srun

```
    # Profiling
    @run_before('run')
    def preload_mpiP(self):
        # Load mpiP module
        self.modules.append('mpip')

        # Store output in a folder
        mpip_output = 'mpip_output'
        self.prerun_cmds.append('mkdir "%s"' % mpip_output)
        # Configure mpiP
        self.variables['MPIP'] = '"-f %s"' % mpip_output
        # Tell reframe to keep the folder after cleanup
        self.keep_files.append(mpip_output)

        # Add the LD_PRELOAD to srun
        self.job.launcher.options = ['--export=ALL,LD_PRELOAD=libmpiP.so']
```

When ReFrame finishes we should have a directory `mpip_output` containing a report file named based on the application and test case.

