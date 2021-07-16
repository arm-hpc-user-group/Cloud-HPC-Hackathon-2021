# cosmoflow-benchmark 

**Description:** This is a an implementation of the CosmoFlow 3D convolutional neural network for benchmarking. It is written in TensorFlow with the Keras API and uses Horovod for distributed training.

**URL:** https://github.com/sparticlesteve/cosmoflow-benchmark

**Team:**  SGHackers

## Compilation

### Spack Package Modification

We have modified the spack package inplace and did not manage to come up with a patch and other reasonable constraint rules, as the building of Tensorflow and Horovod itself is quite
challenging for us and making spack modifications haphazardly would most probabily result in more trouble than goods. The outline of out build process is explained in the later sections.

### Building cosmoflow-benchmark

#### Compiler 1: GCC@10.3.0

From what we understand, the spack receipe for this application is mainly to 
install all the necessary python libraries, such as TensorFlow and Horovod, while 
the main application is a python script to begin TensorFlow training. 

It seems like there is no good solution yet as to building py-tensorflow from spack and the
existing approach to interface with a bazel build scripts. There are a couple of places
where bazel build fails and we have to manually go in and modify bazel scripts, as well as the
source code. There is also mishandled environment variables as bazel could not find ARM compiler's 
license, which unfortunately we did not have time to debug that.


The first step is to build Tensorflow package
```
spack fetch py-tensorflow@2.4.1%gcc@10.3.0~cuda~nccl # download source code
spack stage py-tensorflow@2.4.1%gcc@10.3.0~cuda~nccl # decompress source code
```
After these two commands, we made two hacks to the source code to fix some problems during building.
1. At Tensorflow/core/kernels/example_parsing_ops.cc:1221, we modified function call from error_message()
to message(). This seems like some versioning is not handled correctly and there was an API interface mismatch.
We have checked the source code and made sure they are functionally equivalent.

2. At Tensorflow/lite/build_def.bzl:tflite_copts, we added two compiler flags `-flax-vector-conversions` and 
`-fomit-frame-pointer`, as otherwise there was error complaining about implicit type conversion between int32x2 and int8x8.

After we patched up these two places, then the installation should process successfully with the following command
```
spack install --keep-stage --dont-restage py-tensorflow@2.4.1%gcc@10.3.0~cuda~nccl
```

Now we have built Tensorflow, we will continue with horovod. Note that horovod accepts pytorch as its default
framework, we do not want that and should append `frameworks=tensorflow`. We can then reuse the py-tensorflow just 
built by specifying its hash version. (spack magic)
```
spack install py-horovod@0.20.3~cuda%gcc@10.3.0 tensor_ops=mpi frameworks=tensorflow ^openmpi ^openblas ^py-tensorflow/ltx4nx5
```

Lastly, we just link everything together to fulfill spack receipe for cosmoflow-benchmark.
```
spack install -j32 cosmoflow-benchmark~cuda%gcc@10.3.0 ^openmpi ^openblas ^py-tensorflow/ltx4nx5 ^py-horovod/vucll5c
```

However, it looks like the spack receipe is coarsely written and there were some missing constraints that are required
to run the application. These are
```
spack install py-tensorflow-estimator%gcc@10.3.0 ^py-tensorflow/ltx4nx5 ^bazel/xluon34
spack spec py-wandb%gcc@9.3.0 ^py-setuptools/tuknvv2
spack install py-promise%gcc@9.3.0 ^py-setuptools/7wan6v2
pathtools
```
Note that there was not a spack script for pathtools, we generated the script via pip2spack.
```
pip2spack install pathtools
spack install py-pathtools
```
After all these steps, we could finally run the benchmark successfully.


```
spack spec  cosmoflow-benchmark~cuda%gcc@10.3.0 ^openmpi ^openblas ^py-tensorflow/ltx4nx5 ^py-horovod/vucll5c
cosmoflow-benchmark@master%gcc@10.3.0~cuda cuda_arch=none arch=linux-amzn2-graviton2
    ^py-h5py@3.2.1%gcc@9.3.0~mpi patches=b4b285397ff55ac015bdbd06dfad774bf6bfff11b4d5b0a25d94887f0a12c35e arch=linux-amzn2-graviton2
        ^hdf5@1.10.7%gcc@9.3.0~cxx~fortran+hl~ipo~java~mpi+shared~szip~threadsafe+tools api=default build_type=RelWithDebInfo arch=linux-amzn2-graviton2
            ^cmake@3.20.5%gcc@9.3.0~doc+ncurses+openssl+ownlibs~qt build_type=Release arch=linux-amzn2-graviton2
                ^ncurses@6.2%gcc@9.3.0~symlinks+termlib abi=none arch=linux-amzn2-graviton2
                    ^pkgconf@1.7.4%gcc@9.3.0 arch=linux-amzn2-graviton2
                ^openssl@1.1.1k%gcc@9.3.0~docs+systemcerts arch=linux-amzn2-graviton2
                    ^perl@5.32.1%gcc@9.3.0+cpanm+shared+threads arch=linux-amzn2-graviton2
                        ^berkeley-db@18.1.40%gcc@9.3.0+cxx~docs+stl patches=b231fcc4d5cff05e5c3a4814f6a5af0e9a966428dc2176540d2c05aff41de522 arch=linux-amzn2-graviton2
                        ^bzip2@1.0.8%gcc@9.3.0~debug~pic+shared arch=linux-amzn2-graviton2
                            ^diffutils@3.7%gcc@9.3.0 arch=linux-amzn2-graviton2
                                ^libiconv@1.16%gcc@9.3.0 arch=linux-amzn2-graviton2
                        ^gdbm@1.19%gcc@9.3.0 arch=linux-amzn2-graviton2
                            ^readline@8.1%gcc@9.3.0 arch=linux-amzn2-graviton2
                        ^zlib@1.2.11%gcc@9.3.0+optimize+pic+shared arch=linux-amzn2-graviton2
        ^py-cython@0.29.22%gcc@9.3.0 arch=linux-amzn2-graviton2
            ^py-setuptools@50.3.2%gcc@9.3.0 arch=linux-amzn2-graviton2
                ^python@3.8.11%gcc@9.3.0+bz2+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tix~tkinter~ucs4+uuid+zlib patches=0d98e93189bc278fbc37a50ed7f183bd8aaf249a8e1670a465f0db6bb4f8cf87 arch=linux-amzn2-graviton2
                    ^expat@2.4.1%gcc@9.3.0+libbsd arch=linux-amzn2-graviton2
                        ^libbsd@0.11.3%gcc@9.3.0 arch=linux-amzn2-graviton2
                            ^libmd@1.0.3%gcc@9.3.0 arch=linux-amzn2-graviton2
                    ^gettext@0.21%gcc@9.3.0+bzip2+curses+git~libunistring+libxml2+tar+xz arch=linux-amzn2-graviton2
                        ^libxml2@2.9.10%gcc@9.3.0~python arch=linux-amzn2-graviton2
                            ^xz@5.2.5%gcc@9.3.0~pic libs=shared,static arch=linux-amzn2-graviton2
                        ^tar@1.34%gcc@9.3.0 arch=linux-amzn2-graviton2
                    ^libffi@3.3%gcc@9.3.0 patches=26f26c6f29a7ce9bf370ad3ab2610f99365b4bdd7b82e7c31df41a3370d685c0 arch=linux-amzn2-graviton2
                    ^sqlite@3.35.5%gcc@9.3.0+column_metadata+fts~functions~rtree arch=linux-amzn2-graviton2
                    ^util-linux-uuid@2.36.2%gcc@9.3.0 arch=linux-amzn2-graviton2
        ^py-numpy@1.21.0%gcc@9.3.0+blas+lapack patches=873745d7b547857fcfec9cae90b09c133b42a4f0c23b6c2d84cf37e2dd816604 arch=linux-amzn2-graviton2
            ^openblas@0.3.15%gcc@9.3.0~bignuma~consistent_fpcsr~ilp64+locking+pic+shared threads=none arch=linux-amzn2-graviton2
        ^py-pkgconfig@1.5.1%gcc@9.3.0 arch=linux-amzn2-graviton2
        ^py-wheel@0.36.2%gcc@9.3.0 arch=linux-amzn2-graviton2
    ^py-horovod@0.20.3%gcc@9.3.0~cuda~rocm controllers=mpi cuda_arch=none frameworks=tensorflow tensor_ops=mpi arch=linux-amzn2-graviton2
        ^openmpi@4.1.0%gcc@9.3.0~atomics~cuda~cxx~cxx_exceptions+gpfs~internal-hwloc~java~legacylaunchers~lustre~memchecker+pmi~singularity~sqlite3+static~thread_multiple+vt+wrapper-rpath fabrics=ofi patches=60ce20bc14d98c572ef7883b9fcd254c3f232c2f3a13377480f96466169ac4c8 schedulers=slurm arch=linux-amzn2-graviton2
            ^hwloc@2.5.0%gcc@9.3.0~cairo~cuda~gl~libudev+libxml2~netloc~nvml+pci+shared arch=linux-amzn2-graviton2
                ^libpciaccess@0.16%gcc@9.3.0 arch=linux-amzn2-graviton2
                    ^libtool@2.4.6%gcc@9.3.0 arch=linux-amzn2-graviton2
                        ^m4@1.4.18%gcc@9.3.0+sigsegv patches=3877ab548f88597ab2327a2230ee048d2d07ace1062efe81fc92e91b7f39cd00,fc9b61654a3ba1a8d6cd78ce087e7c96366c290bc8d2c299f09828d793b853c8 arch=linux-amzn2-graviton2
                            ^libsigsegv@2.13%gcc@9.3.0 arch=linux-amzn2-graviton2
                    ^util-macros@1.19.3%gcc@9.3.0 arch=linux-amzn2-graviton2
            ^libevent@2.1.12%gcc@9.3.0+openssl arch=linux-amzn2-graviton2
            ^libfabric@1.11.1-aws%gcc@9.3.0~debug~kdreg fabrics=sockets,tcp,udp arch=linux-amzn2-graviton2
            ^numactl@2.0.14%gcc@9.3.0 patches=4e1d78cbbb85de625bad28705e748856033eaafab92a66dffd383a3d7e00cc94,62fc8a8bf7665a60e8f4c93ebbd535647cebf74198f7afafec4c085a8825c006 arch=linux-amzn2-graviton2
                ^autoconf@2.69%gcc@9.3.0 arch=linux-amzn2-graviton2
                ^automake@1.16.3%gcc@9.3.0 arch=linux-amzn2-graviton2
            ^openssh@8.5p1%gcc@9.3.0 arch=linux-amzn2-graviton2
                ^libedit@3.1-20210216%gcc@9.3.0 arch=linux-amzn2-graviton2
            ^slurm@20-02-4-1%gcc@9.3.0~gtk~hdf5~hwloc~mariadb~pmix+readline~restd sysconfdir=PREFIX/etc arch=linux-amzn2-graviton2
        ^py-cloudpickle@1.6.0%gcc@9.3.0 arch=linux-amzn2-graviton2
        ^py-psutil@5.7.2%gcc@9.3.0 arch=linux-amzn2-graviton2
        ^py-pyyaml@5.3.1%gcc@9.3.0+libyaml arch=linux-amzn2-graviton2
            ^libyaml@0.2.5%gcc@9.3.0 arch=linux-amzn2-graviton2
        ^py-tensorflow@2.4.1%gcc@9.3.0~android~aws~computecpp~cuda~dynamic_kernels~gcp~gdr~hdfs~ignite~ios~jemalloc~kafka~mkl~monolithic~mpi~nccl~ngraph~numa~opencl~rocm~tensorrt~verbs~xla cuda_arch=none arch=linux-amzn2-graviton2
            ^bazel@3.7.2%gcc@9.3.0+nodepfail patches=0f6940d1cb5dc44630c9e845704da6d5188683eb706e280dafc84f5f0f76999e,3e6448a0dde42bbd72568d29c5646d370dd62ca300cdd10a630908c086844167,604423c717a5e58cdd76ba8a9ce1d313faf13885be838f4e33dd37845b3940cb,dbbf38bd17c63aa923f2433a2013d302739f8043ca427c816e8737dab05ac528 arch=linux-amzn2-graviton2
                ^openjdk@11.0.0-2020-01-01%gcc@9.3.0 arch=linux-amzn2-graviton2
                ^zip@3.0%gcc@9.3.0 patches=14dc88014812a896e5697553025f451435f69b1b541743f853b8dcae6b4dfe27,3bc30bafdfd29f1d26d1e0c4c7217def2ff5b37a715e482f83c5fefa2aa0ecb6,5068e7cb188e520da3cced095292ace13ad5e8321419127bf2ca095e148ab65a,51f48db588b17790aaf6b901d6ca737abdb20124210cf8def17d81841c013d13,66ab4ce03f342c6624aa14be5fa43b90e5608a4f6babcc9c3680828f2c246a74,a92fc4e4f59aa2ca3e8059c6b355ecce8c8c7802cb4f118756bf06eb51455549,a95ed93de9284ff68e835387ddb9ff62414712f9b95ec8e120f02cef8f26faca,eb83fc886ded7101ad8ddf10c025b1bd4d33b594766816cce65397d4f5c6a7b9,f7d0bc42e1db9564732ae0aa1ad238b7278a3e68eb0b05e16f1cb6507df2668d,fa8312c722a1cf774af588d5534745f2231130da0f40a44bba5b394eb13a5c64 arch=linux-amzn2-graviton2
            ^flatbuffers@1.12.0%gcc@9.3.0~ipo+python+shared build_type=RelWithDebInfo arch=linux-amzn2-graviton2
            ^protobuf@3.17.3%gcc@9.3.0+shared build_type=Release arch=linux-amzn2-graviton2
            ^py-absl-py@0.10.0%gcc@9.3.0 arch=linux-amzn2-graviton2
                ^py-six@1.15.0%gcc@9.3.0 arch=linux-amzn2-graviton2
            ^py-astunparse@1.6.3%gcc@9.3.0 arch=linux-amzn2-graviton2
            ^py-gast@0.3.3%gcc@9.3.0 arch=linux-amzn2-graviton2
            ^py-google-pasta@0.2.0%gcc@9.3.0 arch=linux-amzn2-graviton2
            ^py-grpcio@1.32.0%gcc@9.3.0 arch=linux-amzn2-graviton2
                ^c-ares@1.15.0%gcc@9.3.0~ipo build_type=RelWithDebInfo arch=linux-amzn2-graviton2
            ^py-keras-preprocessing@1.1.2%gcc@9.3.0 arch=linux-amzn2-graviton2
            ^py-opt-einsum@3.3.0%gcc@9.3.0 arch=linux-amzn2-graviton2
            ^py-protobuf@3.12.2%gcc@9.3.0~cpp arch=linux-amzn2-graviton2
            ^py-termcolor@1.1.0%gcc@9.3.0 arch=linux-amzn2-graviton2
            ^py-typing-extensions@3.7.4%gcc@9.3.0 arch=linux-amzn2-graviton2
            ^py-wrapt@1.12.1%gcc@9.3.0 arch=linux-amzn2-graviton2
            ^swig@4.0.2%gcc@9.3.0 arch=linux-amzn2-graviton2
                ^pcre@8.44%gcc@9.3.0~jit+multibyte+utf arch=linux-amzn2-graviton2
    ^py-mpi4py@3.0.3%gcc@9.3.0 arch=linux-amzn2-graviton2
    ^py-pandas@1.3.0%gcc@9.3.0 arch=linux-amzn2-graviton2
        ^py-bottleneck@1.3.2%gcc@9.3.0 arch=linux-amzn2-graviton2
        ^py-numexpr@2.7.2%gcc@9.3.0 arch=linux-amzn2-graviton2
        ^py-python-dateutil@2.8.1%gcc@9.3.0 arch=linux-amzn2-graviton2
            ^py-setuptools-scm@6.0.1%gcc@9.3.0+toml arch=linux-amzn2-graviton2
                ^py-toml@0.10.2%gcc@9.3.0 arch=linux-amzn2-graviton2
        ^py-pytz@2020.1%gcc@9.3.0 arch=linux-amzn2-graviton2
    ^py-torch@1.9.0%gcc@9.3.0+caffe2~cuda~cudnn+distributed+fbgemm+gloo+kineto~magma~metal~mkldnn+mpi~nccl+nnpack+numa+numpy+onnx_ml+openmp+qnnpack~rocm+tensorpipe+valgrind+xnnpack cuda_arch=none patches=e37afffe45cf7594c22050109942370e49983ad772d12ebccf508377dc9dcfc9 arch=linux-amzn2-graviton2
        ^benchmark@1.5.5%gcc@9.3.0~ipo build_type=RelWithDebInfo arch=linux-amzn2-graviton2
        ^eigen@3.3.9%gcc@9.3.0~ipo build_type=RelWithDebInfo patches=55daee880b7669807efc0dcbeda2ae3b659e6dd4df3932f3573c8778bf5f8a42 arch=linux-amzn2-graviton2
        ^fp16@2020-05-14%gcc@9.3.0~ipo build_type=RelWithDebInfo arch=linux-amzn2-graviton2
            ^ninja@1.10.2%gcc@9.3.0 arch=linux-amzn2-graviton2
        ^fxdiv@2020-04-17%gcc@9.3.0~ipo build_type=RelWithDebInfo arch=linux-amzn2-graviton2
        ^psimd@2020-05-17%gcc@9.3.0~ipo build_type=RelWithDebInfo arch=linux-amzn2-graviton2
        ^pthreadpool@2021-04-13%gcc@9.3.0~ipo build_type=RelWithDebInfo arch=linux-amzn2-graviton2
        ^py-future@0.18.2%gcc@9.3.0 arch=linux-amzn2-graviton2
        ^py-pybind11@2.6.2%gcc@9.3.0~ipo build_type=RelWithDebInfo arch=linux-amzn2-graviton2
        ^py-tqdm@4.59.0%gcc@9.3.0~notebook~telegram arch=linux-amzn2-graviton2
        ^sleef@3.5.1_2020-12-22%gcc@9.3.0~ipo build_type=Release arch=linux-amzn2-graviton2
        ^valgrind@3.17.0%gcc@9.3.0+boost+mpi+only64bit+ubsan arch=linux-amzn2-graviton2
            ^boost@1.76.0%gcc@9.3.0+atomic+chrono~clanglibcpp~container~context~coroutine+date_time~debug+exception~fiber+filesystem+graph~icu+iostreams+locale+log+math~mpi+multithreaded~numpy~pic+program_options~python+random+regex+serialization+shared+signals~singlethreaded+system~taggedlayout+test+thread+timer~versionedlayout+wave cxxstd=98 visibility=hidden arch=linux-amzn2-graviton2
```

## Test Case 1

[ReFrame Benchmark 1](#)

```
reframe -c cosmoflow.py -r --performance-report
```

### Validation

This reframe script runs the cosmoflow benchmark using a 32 test and 32 validation inputs for TensorFlow training. 
Validation is done by checking the final model loss is below a certain margin.

### ReFrame Output

```
==============================================================================
PERFORMANCE REPORT
------------------------------------------------------------------------------
cosmoflow-benchmark_short_test_cosmoflow_benchmark_cuda_gcc_10_3_0_N_1_MPI_32_OMP_1
- aws:c5n
   - builtin
      * num_tasks: 32
      * Total Time: 224.0208 s
------------------------------------------------------------------------------
cosmoflow-benchmark_short_test_cosmoflow_benchmark_cuda_gcc_10_3_0_N_1_MPI_16_OMP_1
   - builtin
      * num_tasks: 16
      * Total Time: 400.7628 s
------------------------------------------------------------------------------
cosmoflow-benchmark_short_test_cosmoflow_benchmark_cuda_gcc_10_3_0_N_1_MPI_8_OMP_1
   - builtin
      * num_tasks: 8
      * Total Time: 771.6113 s
------------------------------------------------------------------------------
cosmoflow-benchmark_short_test_cosmoflow_benchmark_cuda_gcc_10_3_0_N_1_MPI_4_OMP_1
   - builtin
      * num_tasks: 4
      * Total Time: 1483.0482 s
------------------------------------------------------------------------------
cosmoflow-benchmark_short_test_cosmoflow_benchmark_cuda_gcc_10_3_0_N_1_MPI_2_OMP_1
   - builtin
      * num_tasks: 2
      * Total Time: 2565.0004 s
------------------------------------------------------------------------------
cosmoflow-benchmark_short_test_cosmoflow_benchmark_cuda_gcc_10_3_0_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * Total Time: 3311.0096 s
------------------------------------------------------------------------------
```

### On-node Compiler Comparison

As the underlying bazel script has some problem locating the licence of arm compiler, we are not able to conduct any compiler comparisons.

### Serial Hot-spot Profile

List of top-10 functions / code locations from a serial profile.
Profiling is done using the arm-forge toolchain.

Profiling command used:
```
:map -profile /opt/amazon/openmpi/bin/mpirun -np 1 -bind-to none -map-by slot  -x NCCL_DEBUG=INFO -x LD_LIBRARY_PATH -x PATH     -mca pml ob1 -mca btl ^openib     python train.py -d
```

| Position | Routine | Time (s) | Time (%) |
|----------|---------|----------|----------|
| 1        |   tensors = pywrap_tfe.TFE_Py_Execute(ctx._handle, device_name, op_name,inputs, attrs, num_outputs)      |          |      97.8%    |
| 2        |  PYTHON_IO_WRITE       |          |    0.5%      |
| 3        |   pthread_cond_wait      |          |   0.4%       |
| 4        |  PYTHON_IO_READ       |          |     0.3%     |
| 5        |   open64      |          |    0.2%      |
| 6        |   distributions_from_metadata      |          |   0.2%       |
| 7        |  __xstat64       |          |    0.1%      |
| 8        |   _fill_cache      |          |    0.1%      |
| 9        |  malloc       |          |    0.1%      |
| 10       |    DecodeVarint     |          |   0.1%       |


### Full Node Hot-spot Profile

List of top-10 functions / code locations from a full node profile.

Profiling command used:
```
:map -profile /opt/amazon/openmpi/bin/mpirun -np 8 -bind-to none -map-by slot  -x NCCL_DEBUG=INFO -x LD_LIBRARY_PATH -x PATH     -mca pml ob1 -mca btl ^openib     python train.py -d
```

| Position | Routine | Time (s) | Time (%) | MPI (%) |
|----------|---------|----------|----------|---------|
| 1        |  MPI_Allreduce       |          |   95.9%       |    95.9%     |
| 2        |  nanosleep       |          |     4%     |         |
| 3        |   MPI_Finalize      |          |   <0.1%       |    <0.1%       |
| 4        |   MPI_Bcast      |          |    <0.1%        |    <0.1%       |
| 5        |   malloc      |          |    <0.1%        |         |
| 6        |   thread_start      |          |     <0.1%       |    96%     |
| 7        |    start_thread     |          |        <0.1%    |     96%    |
| 8        |   std::execute_native_thread_routine(void*)      |          |     <0.1%     |  96%       |

### Strong Scaling Study

On-node scaling study for two compilers.
Due to time constraint, performance of 1 and 2 cores are projected by performing a single epoch and projected
to a four epoch performance, while others perform full four epoch training. From some empirical observation, runtime
of each epoch is consistantly similar.

| Cores | gcc@10.3.0 |
|-------|------------|
| 1      |   1388(projected)   |          
| 2      |    1770.1830  |  
| 4      |    947.2417      |    
| 8      |    489.2307      |
| 16      |   256.7789      | 
| 32      |   141.5865      |


### Off-Node Scaling Study

Unfortunately, we didn't have time to do scaling analysis due to time constraint, as tensorflow training is quite time consuming.

### On-Node Architecture Comparison

On-node scaling study for two architectures.

| Cores | C6gn (Aarch64) | C5n (X86) |
|-------|----------------|-----------|
| 1      |   1388(projected)   |   3311.0096        |
| 2      |    1770.1830  |   2565.0004       |
| 4      |      947.2417      |    1483.0482        |
| 8      |    489.2307        |   771.6113        |
| 16      |   256.7789      |   400.7628        |
| 32      |   141.5865      |   224.0208        |


## Optimisation

Since the main application is a python script to execute tensorflow model training, the optimization has 
to be done at the library level. Due to time constraint, we were not able to tune libraries like numpy or
tensorflow, as large amount of time is spent on building and performance analysis.

However, we see some good scaling behaviour for ARM architecture, with almost linear performance scaling as core count increases above four.


## Report

### Compilation Summary

Compilation of python applications in our experience is quite challenging, especially for big projects like Tensorflow. Since Python does not 
enforce explicit build system and dependencies, it is hard to make a good spack receipe as stating every constraint can be challenging, and we do encounter a few 
packages that require us to install separately, even as spack installation is successful. Moreover, in this particular build, spack feels more like
a wrapper on bazel build system, which increases the level of indirection and make some configurations and bug fixes convoluted(at least for inexperienced spack 
developers like us). Moreover, since TensorFlow has so many dependencies, it can trigger an explosion of dependencies and with each slight modification to the 
constraints. However, we do recognise the challenges of developing a smart concretizer that knows when to reuse packages, ignore redundant packages while satisfies all
constraints. Nonetheless, we still greatly appreciate the work to put into this amazing package manager.


### Performance Summary

For this application, we see good linear scaling as number of cores increases. This is probabily due to the proper partitioning of workloads by Tensorflow and hence the 
runtime decreases linearly with increase core count. Moreover, Aarch64 outperforms x86 Skylake by >= 40%, exciting results!

### Optimisation Summary

We did not manage to perform fine tuning of python libraries, such as building numpy with Openblas and other math libraries due to time constraint. Such a pity :(.
