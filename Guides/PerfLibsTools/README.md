# Perf Libs Tools

[Perf-libs-tools](https://github.com/ARM-software/perf-libs-tools) is logging library designed to measure the calls to maths library functions.
This is used to count the number and type of calls to common BLAS / LAPACK and FFT routines.

This information is collected to help improve maths library performance in the future, by identifying the characteristics of different applications.


## Prerequisites

Perf-libs-tools assumes that you have linked your application with a shared library, any library will do (`armpl`, `openblas`, etc).

### Building the Code

Building Perf-libs-tools is easy, just clone the repo and run make.

```
git clone https://github.com/ARM-software/perf-libs-tools.git
cd perf-libs-tools
make
```

However, there are some steps for 'known issues' you may want to follow:
* Set the `CC=` entry in `Makefile` to your compiler of choice
* Remove the `#include <xblas>` in `src/armpl.h`
* Remove the first 4 lines from `src/PROTOTYPES`

### Building with Spack

On the clusters a Spack package has been provided.

```
spack install perf-libs-tools-git
```

## Using Perf-libs-tools

Perf-libs tools is simple to use, you simply `LD_PRELOAD` the library on the execution line.

We have two main considerations for which library to use:
* Is the package using OpenMP: `libarmpl_mp-summarylog.so`
* Or no OpenMP: `libarmpl-summarylog.so`

Then we simply load the library before our run:
```
export LD_PRELOAD=/<path to install>/lib/libarmpl_mp-summarylog.so
export OMP_NUM_THREADS=8
mpirun -np 4 --map-by slot:PE=8 ./app
```

### Output

This will generate a number of files (default location is `/tmp/armplsummary_<pid>.apl`) with the trace information.

The location can be controlled via the `ARMPL_LOGGING_FILEROOT` environment variable.

These files on their own are very useful.

Examples can be seen in the following two files for a 2 rank MPI run:
* [06422.apl](plt_out/06422.apl)
* [06423.apl](plt_out/06423.apl)


**Note:** Perf-libs-tools will generate one file per process, if you are using only MPI then one file per rank, however with OpenMP this is one file per thread.

### Summary

Whilst these individual files are useful we can also summarize them.

```
python3 tools/process_summary.py *.apl > summary.log
```

This will output merged analysis from all of the files provided.

An example of this output is provided for [06422.apl](plt_out/06422.apl) and [06423.apl](plt_out/06423.apl).

```
Process full dataset for BLAS, LAPACK and FFT function usage.
Opening file plt_out/06422.apl
Opening file plt_out/06423.apl
BLAS level 1     : count      52867    total time       0.0216  user count      47106  user time       0.0203
BLAS level 2     : count      19892    total time       0.0118  user count      16146  user time       0.0108
BLAS level 3     : count      16059    total time       0.0196  user count      16059  user time       0.0196
LAPACK           : count      69601    total time       0.1396  user count      13708  user time       0.0759
FFT              : count        152    total time       0.0035  user count        136  user time       0.0026
 
Double precision : count     158383    total time       0.1893  user count      92975  user time       0.1229
Single precision : count          0    total time       0.0000  user count          0  user time       0.0000
Double complex   : count        112    total time       0.0050  user count        112  user time       0.0050
Single complex   : count          0    total time       0.0000  user count          0  user time       0.0000
 ```

## Perf-Libs-Tools inside ReFrame

All of this process can be automated within a ReFrame job.

We do this via the following steps:
* Load the spack module
* Configure the pre-run commands for an output directory
* Tell ReFrame to save the output directory
* Add the `LD_PRELOAD` to srun
* Configure the post-run commands to run the `process_summary.py`
* Tell ReFrame to save the summary file

```
# Profiling
@run_before('run')
def perf_libs_tools(self):

    # Load perf-libs-tools-module
    self.modules.append('perf-libs-tools-git')

    # Make folder to save results to 
    apl_dir = 'plt_out'
    # Create the folder in pre_run cmd
    self.prerun_cmds.append('mkdir {0}'.format(apl_dir))
    # Set the Fileroot to the new folder
    self.variables['ARMPL_SUMMARY_FILEROOT'] = '$PWD/{0}/'.format(apl_dir)
    # Tell reframe to keep the folder after cleanup
    self.keep_files.append(apl_dir)

    # Add the LD_PRELOAD to srun
    self.job.launcher.options = ['--export=ALL,LD_PRELOAD=libarmpl-summarylog.so']
        
    # Make summary file
    apl_file = '{0}_{1}_apl_summary.log'.format(self.log_app_name, self.log_test_name)
    # Run post process
    self.postrun_cmds.append('process_summary.py {0}/*.apl > {1}'.format(apl_dir, apl_file))

    # Keep the summary file
    self.keep_files.append(apl_file)

```

When ReFrame finishes we should have a directory `plt_out` containing our `<pid>.apl` files and our summary file - named based on the application and test case.

We have demonstrated this with a simple [CP2K test case](cp2k_sibulk8.py) - to show the whole procedure.
