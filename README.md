# A-HUG Cloud HPC Hackathon

![A-HUG Hackathon Logo](https://a-hug.org/wp-content/uploads/2021/05/arm-aws-hackathon.png)

**Team Sign-Up:** [Sign-up Form](https://docs.google.com/forms/d/e/1FAIpQLScQ5Kq3pNgtZVJrKdLQHTOp2xKu0ILyzlgmoGB6pdFZ62uyfg/viewform)

**Dates:** Week of July 12th 2021

**Website:** [A-HUG Hackathon](https://a-hug.org/hackathons/aws-hackathon/)


## Description

Teams will undertake application porting and performance tuning of key HPC applications using virtual clusters on the AWS cloud – powered by their Arm Neoverse-N1 based Graviton2 processor. Using the Spack package manager teams will have to control the installation of their codes – and tune compiler, library and optimization flag choice to ensure a robust and performance tuned installation. 

Teams must then undertake performance and scalability studies and to compare against other processor architectures. Amassing points for successful builds, tests, performance analysis and tuning – the team with the most points will take the prizes (winning team get M1 Macbooks each).


Take a look at our example mini-app [CloverLeaf](Tutorials/CloverLeaf/).

Teams can be made up of up to 4 students, for registration please go to this [sign-up form](https://docs.google.com/forms/d/e/1FAIpQLScQ5Kq3pNgtZVJrKdLQHTOp2xKu0ILyzlgmoGB6pdFZ62uyfg/viewform).

## Gamification

Whilst the objective of this hackathon is serious, we want to keep it as fun and competitive as possible. 
There are multiple ways of scoring points – which will allow teams to employ different tactics to best utilise their skills.

Teams might choose to go broad – and enable as many codes with a light touch as possible, or to go deep and work on benchmarking and optimising a few key applications for the best gains.

How ever teams choose to play, the end result will be a comprehensive set of applications and benchmarks in the cloud.

## Codes

We have readied a list of over 100 HPC applications (already available in Spack). Some of these will be kept secret to surprise teams, others will be announced in advance.

### Bidding for a Code

Before the event we will allow teams to bid (using their initial points) for any specific codes (max 2 codes) they wish to work on – from our list of revealed codes. Other codes will be available as the event progresses.

### Free Mini-App

To get all of the teams started they will be provided with a ‘free’ mini-app. Something simple and known to work on a variety of platforms. This is designed to help teams get up to speed with the different tools we will be using throughout the event (ParallelCluster, Spack, ReFrame).

## Points Scoring

Teams can earn points through a variety of different tasks. Simply speaking they are broken down into the following categories:

### Compilation and Validation
Here teams can gain points for successfully building the codes. Extra points will be available for building with different compilers.
To prove that the build actually work teams will need to demonstrate validation test cases.

### Benchmarking
This is where things get a bit more interesting. Points will be available here for different types of performance analysis and benchmarking. Think scaling studies, compiler comparisons, network comparisons, architecture comparisons, hot-spot analysis.

### Optimisation
Now for the most open-ended of topics – performance optimisation. Here teams are invited to get involved with the nitty gritty of application performance tuning, for big points. From the simplistic compiler flags and dependency libraries all the way up to code modifications, we really want to see what you can do. Just remember – your code still needs to validate.

### Documentation 
Lastly, we want to hear about what you have done. Points will be awarded for writing up the experience, and lessons learnt along the way. 

## Resources

### Hardware
This event will take place on virtual clusters hosted on AWS. The main focus will be the Arm based Graviton2 instances. You will have a cluster of the 64-core (C6gn.16xlarge) nodes, with enhanced (EFA) networking.
Teams will also have access to an Intel based clusters (C5n.18xlarge) – for performance comparisons and validation purposes.

### Software

#### Utility
* [Spack](https://github.com/spack/spack) – For controlling the installation of the applications.
* [ReFrame](https://github.com/eth-cscs/reframe) – For controlling the validation and performance.
* [GrayLog](https://www.graylog.org/) – Logging server for all of the validation and performance data.

#### System Software
* Compilers – GCC, [Arm (ACFL)](https://developer.arm.com/tools-and-software/server-and-hpc/compile/arm-compiler-for-linux/resources), [NVIDIA (NVHPC)](https://developer.nvidia.com/hpc-sdk)
* MPI – Open MPI
* Maths Libraries – [ArmPL](https://developer.arm.com/tools-and-software/server-and-hpc/downloads/arm-performance-libraries), OpenBLAS, Bliss, BYO!
* Profilers / Debuggers – [Arm Forge (DDT / MAP)](https://developer.arm.com/tools-and-software/server-and-hpc/downloads/arm-forge), BYO!
