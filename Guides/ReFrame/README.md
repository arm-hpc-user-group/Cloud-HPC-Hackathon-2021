# ReFrame

During this workshop we will be using the [ReFrame toolkit](https://github.com/eth-cscs/reframe) to manage code execution, validation and performance logging.

ReFrame is especially useful within this context as it can take a lot of the complexity out of using the HPC resources.
We will tell ReFrame which applications we want to run, and how to run them, and it will generate the appropriate `Slurm` submission scripts, and submit the jobs to the correct queue.

It is worth noting that we will only be using a subset of the full ReFrame functionality.
Whilst ReFrame can be used to build applications (by integrating with system compilers and build systems) we are going to be using `Spack` for building our packages.
This means for the most part we will only ever be using [Run-Only Regression Tests](https://reframe-hpc.readthedocs.io/en/stable/tutorial_advanced.html#writing-a-run-only-regression-test).


## How ReFrame Works

![ReFrame Test Pileline](https://reframe-hpc.readthedocs.io/en/stable/_images/pipeline.svg)

ReFrame has a clear [regression test pipeline](https://reframe-hpc.readthedocs.io/en/stable/pipeline.html), comprised of distinct phases.

* Setup: Create tests for target systems partitions.
* Build: Build the application - not needed with `Run Only` tests.
* Run: Execute the application.
* Sanity: Validate the success of the execution.
* Performance: Extract performance metrics.
* Cleanup: Stage out required files, and delete temp files.

This whole regression test pipeline is automated from the test description, with sections of the test file corresponding to the different phases of the pipeline.


## Our ReFrame Tests

Our ReFrame tests are roughly broken into 3 logical sections:
* Describe the test to run
* Validate the scientific solution
* Extract performance data

When we describe the test to run, we give ReFrame information such as:
* Parameter: Which Spack modules to load
* Parameter: Which systems / partitions (Slurm queues) to run on
* What the binary is called
* How to define the test case
* Parameter: How many MPI ranks / OpenMP tasks to use

When run ReFrame does a parameter expansion - that is to say it generates all combinations of the test case for every parameter option.
So it will generate a test for every Spack module, on every system / partition, for every MPI / OpenMP rank combination.

So say we have a test which can be run on 2 queues (`C6g` and `C6gn`), we have built for 3 compilers (`GCC`, `Arm` and `NVIDIA`) and we want to run 7 MPI data points (1, 2, 4, 8, 16, 32 and 64 cores /node), ReFrame will generate 42 copies of the test case (2*3*7).
For each of these it will create a stage directory, into which it will copy the appropriate files and generate the corresponding Slurm submission script, and submit to the scheduler.

When run, it will collect the appropriate files back and post-process the output for validation and performance.

Very quickly we can see how powerful ReFrame is for managing this process, that would otherwise get very confusing by hand.


## System Integration

ReFrame needs to be configured to work on a specific HPC system, to understand the scheduler and queues etc.
We have done this set-up already, so fear not you should be up and running in no time.

We have also pre-configured ReFrame to use a `Graylog` logging server, this will help us keep track of the progress of the teams.

### Compiler Choice

Compiler choice in ReFrame is done through the Spack module parameter.

We control this by using a Spack spec, this in turn will be passed to the `spack load` command within the job submission script.

```
# Parameters - Compilers - Defined as their Spack specs (use spec or hash)
spec = parameter([
    'cloverleaf@1.1 %gcc@10.3.0',     # CloverLeaf with the GCC compiler
    'cloverleaf@1.1 %arm@21.0.0.879', # CloverLeaf with the Arm compiler
    'cloverleaf@1.1 %nvhpc@21.2'      # CloverLeaf with the NVIDIA compiler
])
```

When working with multiple versions of an application, with a similar spec, we can still use the Spack hash - which we can extract from the `spack find -l` command.
```
$ spack find -l cloverleaf
==> 3 installed packages
-- linux-amzn2-graviton2 / arm@21.0.0.879 -----------------------
po2pm6x cloverleaf@1.1

-- linux-amzn2-graviton2 / gcc@10.3.0 ---------------------------
p4ueuct cloverleaf@1.1

-- linux-amzn2-graviton2 / nvhpc@21.2 ---------------------------
a366d6a cloverleaf@1.1
```

```
# Parameters - Compilers - Defined as their Spack specs (use spec or hash)
spec = parameter([
    'cloverleaf/p4ueuct',     # CloverLeaf with the GCC compiler
    'cloverleaf/po2pm6x',     # CloverLeaf with the Arm compiler
    'cloverleaf/a366d6a'      # CloverLeaf with the NVIDIA compiler
])
```

Internally, we will query the spec (or hash) used to extract meta-data about the package used, this data is then passed to the logging server to document the runs.


## Writing A Test

### Meta-data

The first thing we are going to do when developing our test is to set some appropriate meta-data values.
These help distinguish results, and help automate log processing.
We have set these values as mandatory - so ReFrame will complain if they are not set correctly.

```
# Logging Variables
log_team_name = 'TeamArm'
log_app_name = 'CloverLeaf'
log_test_name = 'BM16_short
```

### Parameters

As mentioned above ReFrame does a parameter combination, specifically the three parameters we are interested in are:
* **Valid Systems:** Where can the test run.
```
valid_systems = ['aws:c6g', 'aws:c6gn'] 
```
* **Spec:** Which Spack modules to use
```
spec = parameter([
    'cloverleaf@1.1 %gcc@10.3.0',
    'cloverleaf@1.1 %arm@21.0.0.879'
])
```
* **Parallelism:** The MPI / OpenMP configurations
```
parallelism = parameter([
    { 'nodes' : 1, 'mpi' : 16, 'omp' : 4},
    { 'nodes' : 1, 'mpi' : 32, 'omp' : 2},
    { 'nodes' : 1, 'mpi' : 64, 'omp' : 1},
])
```

### Application Definition

We need to tell ReFrame what binary to execute.
The Spack module will take care of putting everything in the correct path, so we just need to specify the binary to run, and any parameters to pass to it:

```
executable = 'clover_leaf'
executable_opts = []
```
In this case CloverLeaf doesn't take any parameters, it simply looks for a `clover.in` file in the current directory - we will discuss this in the next section.
With other codes we may want to specify some more complex command line options.

We also want to define any output files that we want to keep:
```
logfile = 'clover.out'
keep_files = [logfile]
```


### Input Data

Defining the input data for a test case can be quite complicated, and there are a number of ways that we can do it.

**Command Line Options:** 

By far the simplest option, for codes which can be controlled this way, is by specifying command line options to the binary.

```
executable_opts = ['-O', '-i', self.input_file]
```

Note: This may need to be used in addition to the other methods below, for example when specifying the location of an input file.


**Pre Run CMDs:** 

This is a predefined variable holding a set of commands to run before the binary is executed.
```
prerun_cmds = ['wget -O clover.in https://raw.githubusercontent.com/UK-MAC/CloverLeaf_ref/master/InputDecks/clover_bm16_short.in']
```
So here we are telling ReFrame to inject the `wget` command into our job submission file, just before the execution phase.
In this case we just grab a single file, and rename it to the expected input file.

This results in the following job submission file:
```
#!/bin/bash
#SBATCH --job-name="rfm_CloverLeafTest_cloverleaf_1_1__gcc_10_3_0___nodes___1___mpi___8___omp___8__job"
#SBATCH --ntasks=8
#SBATCH --ntasks-per-node=8
#SBATCH --cpus-per-task=8
#SBATCH --output=rfm_CloverLeafTest_cloverleaf_1_1__gcc_10_3_0___nodes___1___mpi___8___omp___8__job.out
#SBATCH --error=rfm_CloverLeafTest_cloverleaf_1_1__gcc_10_3_0___nodes___1___mpi___8___omp___8__job.err
#SBATCH -p c6g
spack load cloverleaf@1.1 %gcc@10.3.0
export OMP_NUM_THREADS=8
export OMP_PLACES=cores
wget -O clover.in https://raw.githubusercontent.com/UK-MAC/CloverLeaf_ref/master/InputDecks/clover_bm16_short.in
srun clover_leaf
```

This solution is suitable for fairly simple input files.

**Test Dependencies:**

Another option for curating input cases is to use test dependencies.
The [Using Dependencies Tutorial](https://reframe-hpc.readthedocs.io/en/stable/tutorial_deps.html) provides a great walk-through for those looking to have multi-stage tests.

Simply put, you can define another test - which establishes your input criteria - and then create a dependency link between your execution test and the establishing test.

## Validation / Sanity Checking

A critical component of regression testing, and ReFrame, is correctness checking the solution.

This is without doubt the hardest phase of establishing a regression test, and will vary depending on the application and the test case.

ReFrame has a [number of methods for helping you to validate test](https://reframe-hpc.readthedocs.io/en/stable/sanity_functions_reference.html) cases, and we will discuss a few approaches here.

### Keyword Checking

Some, nice, codes have mechanisms to self validate for certain test cases.
They then may print out a test success status message.

In this case we simply need to ask ReFrame to look for this message.

One such example is Stream, the memory bandwidth benchmark, and is demonstrated in the [ReFrame Stream Example](https://github.com/eth-cscs/reframe/blob/master/cscs-checks/microbenchmarks/cpu/stream/stream.py).

```
self.sanity_patterns = sn.assert_found(
            r'Solution Validates: avg error less than', self.stdout)
```
So for the sanity check we are simply saying "Does the output contain the phrase `Solution Validates`"? 
If so, our job is done, the test has passed, if not the test has failed.

### Single Value

If the code output has a single metric of interest, with a known value for validation, then we can build a sanity check around that.
This is the approach used in [our CloverLeaf example](../../Tutorials/CloverLeaf/cloverleaf_bm16_short.py).

First we need to extract the value of interest, we do this by building a regular expression to apply to the application output.

```
# Regex - Volume   Mass   Density   Pressure   Internal Energy   Kinetic Energy   Total Energy
sol_regex = r'\s+step:\s+87\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)'

# Validate for kinetic energy (6) 
kinetic_energy = sn.extractsingle(sol_regex, self.logfile, 6, float)
```
So here we look for the line beginning ` step: 87` followed by 7 numbers.
We then extract the 6th of these numbers, corresponding to the metric we are interested in (kinetic energy), casting the string value to a float.

**Note:** [Debugging Sanity and Performance Patterns](https://reframe-hpc.readthedocs.io/en/stable/tutorial_tips_tricks.html#debugging-sanity-and-performance-patterns) is a very useful guide for writing and debugging your regular expressions.


We can then set our sanity pattern to an assertion on this value. 
We could simply perform a strict an equals assertion on the exact value:

```
# expected = 0.3075
self.sanity_patterns = sn.assert_eq(kinetic_energy, 0.3075)

```

However, we may want to allow for some tolerance in our check (caused by rounding errors, fast maths, etc), to do this we use a bounded assertion.

```
# expected = 0.3075
expected_lower = 0.30745
expected_upper = 0.30755
       
# Perform a bounded assert
self.sanity_patterns = sn.assert_bounded(kinetic_energy, expected_lower, expected_upper)
```

### Multiple Value

In the previous section we were just applying a sanity check on a single value.

For some more comprehensive checks we may need to apply this to all the values of a figure of merit.

A good example of this is demonstrated in the [ReFrame Tutorials](https://reframe-hpc.readthedocs.io/en/stable/tutorial_advanced.html#applying-a-sanity-function-iteratively).
Here it is shown for a random number checker - where we need to make sure that all 100 values are between the bounds of 90 and 100.

```
@run_before('sanity')
def set_sanity_patterns(self):
    numbers = sn.extractall(
        r'Random: (?P<number>\S+)', self.stdout, 'number', float
    )
    self.sanity_patterns = sn.all([
        sn.assert_eq(sn.count(numbers), 100),
        sn.all(sn.map(lambda x: sn.assert_bounded(x, 90, 100), numbers))
    ])
```

## Performance Extraction

Gathering the performance metrics happens in a very similar way to the sanity checking.
A regular expression is used in conjunction with the same `extractall` and `extractsingle` functions to extract a figure of merit, which is then logged.

Again, looking at the [Stream Benchmark Example](https://github.com/eth-cscs/reframe/blob/master/cscs-checks/microbenchmarks/cpu/stream/stream.py):

```
self.perf_patterns = {
    'triad': sn.extractsingle(r'Triad:\s+(?P<triad>\S+)\s+\S+',
                                      self.stdout, 'triad', float)
}
```

### Reference Performance

Similar to the sanity checking phase ReFrame supports test pass/fail conditions based on expected performance.
This is very useful for regression testing, as it helps spot when a code change or environment configuration hurts performance.

It does however require that an expected value for the test is known for every system / partition and scale the test is run on.

With the case of Stream, our figure of merit is `MB/s`, which we calculate an expected value for the system (or derive one by running Stream first) - and compare our test value to it.

```
self.stream_bw_reference = {
    'PrgEnv-cray': {
        'daint:mc': {'triad': (89000, -0.05, None, 'MB/s')},
        'dom:mc': {'triad': (89000, -0.05, None, 'MB/s')},
    },
    'PrgEnv-gnu': {
        'daint:mc': {'triad': (88500, -0.05, None, 'MB/s')},
        'dom:mc': {'triad': (87500, -0.05, None, 'MB/s')},
    },
    'PrgEnv-intel': {
        'daint:mc': {'triad': (119000, -0.05, None, 'MB/s')},
        'dom:mc': {'triad': (119000, -0.05, None, 'MB/s')},
    },
}
try:
    self.reference = self.stream_bw_reference[self.current_environ.name]
except KeyError:
    self.reference = self.stream_bw_reference['PrgEnv-gnu']
```
In this extract, we see the expected `Triad` performance (extracted with the `perf_patterns` above) for a number of different environs (compilers) for different machines.

The four-tuple used represent the expected value, a lower and upper thresholds and a measurement unit.

**Note:** `None` is used as the upper threshold, signifying that the test will not fail on a good score, only an inferior one.

With our [CloverLeaf Example](../../Tutorials/CloverLeaf/cloverleaf_bm16_short.py), we do not perform sanity checking on the performance value - we simply collect the data for use in the performance report and the logging.

```
self.reference = {
    '*': {'Total Time': (0, None, None, 's'),}
}
```


