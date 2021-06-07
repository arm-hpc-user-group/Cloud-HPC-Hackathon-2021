# Tutorials


## How to play

Upon being assigned a code, teams should fork this github repo.

They can then navigate to the corresponding `Application` directory.
Here they will find an existing `README.md` template file.
As teams work on a code, they should up date this file with thier commands and results.

To build and run a code teams will be asked to use Spack and ReFrame.

We have put together a walkthrough using the [CloverLeaf mini-app](CloverLeaf/).
This example is based around ReFrame Python job files. The additional steps are documented in the `README.md`.

This process determines a number of actions:
* Building the application with spack
* Which spack modules to load
* How many cores to run on (and how many nodes)
* How to validate the solution
* How to extract performance data

Throughout the event exterts will be on-hand from both Spack and ReFrame to help guide you through.

## Spack

[Spack](https://spack.readthedocs.io/en/latest/) is a common HPC package manager.
We will use Spack in this workshop to manage the instalation of our codes, and manage the dependency tracking.

### Compilers / MPI

We have made a number of compilers and MPI installations available on the system.

```
$ spack compiler list
==> Available compilers
-- arm amzn2-aarch64 --------------------------------------------
arm@21.0.0.879

-- gcc amzn2-aarch64 --------------------------------------------
gcc@10.3.0  gcc@7.3.1
```

You can then use a specific compiler to build a package by specifying it in the spec:

```
$ spack install cloverleaf%arm@21.0.0.879
```

We also have a number of MPI installs to use:

```
$ spack find -vl openmpi
==> 2 installed packages
-- linux-amzn2-graviton2 / arm@21.0.0.879 -----------------------
6bfbjqd openmpi@4.1.0~atomics~cuda~cxx~cxx_exceptions+gpfs~internal-hwloc~java~legacylaunchers~lustre~memchecker+pmi~singularity~sqlite3+static~thread_multiple+vt+wrapper-rpath fabrics=ofi patches=60ce20bc14d98c572ef7883b9fcd254c3f232c2f3a13377480f96466169ac4c8 schedulers=slurm

-- linux-amzn2-graviton2 / gcc@10.3.0 ---------------------------
ehtcdbv openmpi@4.1.0~atomics~cuda~cxx~cxx_exceptions+gpfs~internal-hwloc~java~legacylaunchers~lustre~memchecker+pmi~singularity~sqlite3+static~thread_multiple+vt+wrapper-rpath fabrics=ofi patches=60ce20bc14d98c572ef7883b9fcd254c3f232c2f3a13377480f96466169ac4c8 schedulers=slurm
```


For this we can then look at the dependencies to install CloverLeaf with the Arm compiler, using the preinstalled Open MPI (specified by the hash `6bfbjqd`).

```
$ spack install cloverleaf%arm@21.0.0.879 ^openmpi/6bfbjqd
```


## ReFrame

[ReFrame](https://reframe-hpc.readthedocs.io/en/stable/index.html) is used as a build and test harness for HPC applications.
For this workshop we will just be doing 'Run only' tests, as we will be using Spack to manage the installs.

We ask students to develop their own ReFrame files, an example is presented in the CloverLeaf folder (CloverLeaf BM16 Short)[CloverLeaf/cloverleaf_bm16_short.py].
Follow this template to harness the power of ReFrame to drive the job submission and validation of your test cases.

ReFrame has also been configured to pass the performance logs to a GrayLog server, allowing us to analyse the output and automatically visualise the results.

The ReFrame website contains a number of useful [tutorials](https://reframe-hpc.readthedocs.io/en/stable/tutorials.html).

## GrayLog

To visualise the progress of teams we will be using dynamic dashboards in GrayLog to plot progress.

Below is an example of one of the dashboards generated for our CloverLeaf tutorial, showing how many test cases we have ported, and the scaling data for them.


![GrayLog](Images/GrayLog_CloverLeaf.png)
