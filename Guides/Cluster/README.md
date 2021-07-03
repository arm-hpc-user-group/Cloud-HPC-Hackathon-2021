# Parallel Cluster

The clusters you have access to are created using AWS [Parallel Cluster](https://aws.amazon.com/hpc/parallelcluster/).
This builds a virtual cluster on top of EC2 instances, and handles all of the cluster configuration for you.

In many ways these clusters will behave exactly as an on-prem cluster would.

## Connecting to the Cluster

As part of the sign-up process you will have provided us with a public SSH key, and a username.
On your cluster an account has been created with this username and authenticated with the public key. 
No passwords are used to connect to the cluster, all you need is:
* Your cluster User Name
* Your private SSH key to match the public key you provided us
* The IP address of the cluster head-node (we provide this)

For example:

```
ssh operks@100.27.44.170
```

For simplicity we suggest updating your `~/.ssh/config` with the details to allow for a shortcut.
```
Host ArmCluster
  Hostname 100.27.44.170
  User operks
  IdentityFile ~/.ssh/id_rsa
```
Now we can simply:
```
ssh ArmCluster
```

## Cluster Description

Now that you have connected to the cluster, what is there?

Firstly, we classify the nodes as:
* **Head Node:** This is where you connect into, and build your software.
* **Compute Node:** This is where you will run the jobs.

For this workshop we will be using 3 different AWS instance types:
* [C6gn.16xlarge](https://aws.amazon.com/ec2/instance-types/c6/) Arm based Graviton 2 instance
* [C5n.18xlarge](https://aws.amazon.com/ec2/instance-types/c5/) Intel Xeon Platinum based instance

| Attribute      | C6gn.16xlarge | C5n.18xlarge |
| -------------- | ------------- | ------------ |
| Cores          | 64            | 36 (72 vCPU) |
| Speed (GHz)    | 2.5           | 3.0          |
| Memory (GiB)   | 128           | 192          |
| Network (Gbps) | 100           | 100          |




## Job Scheduler

The clusters are configured to run the `Slurm` scheduler, a common HPC scheduler that many will already be familiar with.
For those new to `Slurm` this [Quick Start User Guide](https://slurm.schedmd.com/quickstart.html) may be useful.


The Arm Cluster has only queue configured - `c6gn`.
```
$ sinfo
PARTITION AVAIL  TIMELIMIT  NODES  STATE NODELIST 
c6gn*         up   infinite      4  idle~ c6gn-dy-c6gn16xlarge-[1-4]
```

### Job Submission

There are multiple options of job submission, but our simpliest option is via the `srun` command.
This command takes as arguement a script, which it will execute on the desired resource.

```
srun -N 1 -n 64 -l hostname 
```
This will submit a job, that will spin up a compute node instance and run the `hostname` command.
This command will perform this as an interactive command, and will not return until the job has finished.

For longer lasting jobs, or queuing, then a batch submission is more appropriate.

```
$ cat example.sh
#!/bin/bash

srun -l hostname
```

```
chmod +x example.sh
sbatch -N 1 -n 64 -P c6gn example.sh
```

This command tells `Slurm` to run our `example.sh` script on 1 Node, with 64 cores, on partition "c6g".
This will generate output files (`*.err` and `*.out`) in the current directory, named by the job ID, e.g. `slurm-7.out`.

If your job is queued then you can use the `squeue` command to view its status.

```
$ squeue
             JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON) 
                10      c6gn example.   operks CF       0:01      2 c6gn-dy-c6gn16xlarge-[1-2]
```


### Interactive Jobs

In addition to the commands above we can use `srun` to provide us an interactive bash shell, this allows us to run multiple commands all within the same environment of a job, without the need for a job submission script. 
This can be very usefull for debugging purposes.

```
srun -N 1 -n 64 --pty bash
```


### Idle Nodes

For those already familiar with clusters this will be a very similar experience.
All of the same commands are available to you.

However, there is one main difference - resource is not provisioned ahead of time.
In a traditional cluster your jobs may have to queue to wait for resource to become available.
With these clusters the compute nodes do not sit idle, they are dynamically created and destroyed as and when they are needed.
This means on job submission there may be a wait of a few minutes whilst new compute nodes are provisioned.



## File System

Navigating the file system is key to understanding how best to use the cluster.

```
/
├─ home (500 GB)                
|  ├─ user1
|  ├─ user2
|  ├─ user3
|  └─ user4
|
├─ software (20 GB)
|  ├─ ACFL
|  ├─ arm-forge-21.0
|  ├─ binutils
|  ├─ gcc
|  ├─ spack
|  ├─ reframe
|  └─ nvhpc
|
├─ scratch (1200 GB)
|  └─ opt
|     └─ spack
|
└─ tmp
```

On the clusters we have a number of file systems mounted in different folders, for different purposes.

* **`/home`:** Home folders of the users, NFS export mounted on the compute nodes
* **`/software`:** Software installs, NFS export mounted on the compute nodes
* **`/scratch`:** High performance Lustre FS for Spack installs and user runs
* **`/tmp`:** Node local temp storage
