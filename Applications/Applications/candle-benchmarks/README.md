# CANDLE-benchmarks

**Description:** ECP-CANDLE Benchmarks

**URL:** https://github.com/ECP-CANDLE/Benchmarks

**Team:** DeepNeuron-Blue


NOTE: At the time of submission, we are still trying to compile the applications (or more percisely its py-tensorflow dependencies). This application as well as a lot of its dependencies need modification in order to be compatible with arm arch.


## Compilation

```
candle-benchmarks%gcc +mpi ^openblas ^binutils+gold+ld  ^automake@1.15: ^py-scipy@1.6.3 ^py-gast@0.3.3 ^py-pybind11@2.6.2 ^openjdk@11: ^protobuf@:3.15
```

The latest version of candle-benchmarks depends on py-numba, which depends on llvm that needs binutils+gold. The external binutils is configured with ~gold therefore need to be rebuild.

Blas need to be provided in order to build py-torch, unfortunately, py-torch does not recognize armpl as a valid blas provider.

The latest py-scipy version depends on py-pythran, which in turn depends on `py-gast@0.4.0:0.4.999`, and py-tensorflow explictly requires `py-gast@0.3.3`. See thread in https://github.com/spack/spack/pull/24897.

Bazel does not like the default openjdk, See https://github.com/spack/spack/issues/14234

The latest protobuf does not build with tensorflow. Its likely an error from tensorflow code base. Specifically, protobuf removed error_message() method and replaced it with message() in Status class of `protobuf/src/google/stubs/status.h` from 3.16 onwards, however `tensorflow/tensorflow/core/kernels/example_parsing_ops.cc` is still trying to access `error_message()` methods all the way from v2 to latest.


### Spack Package Modification

We encountered several issues during the installation of candle-benchmarks. We had to refactor most parts of the package recipe as well as fixing a number of bugs in a few dependencies.

A list of pull requests:

* Candle-benchmarks: https://github.com/spack/spack/pull/24896
* CuDNN: https://github.com/spack/spack/pull/24882
* py-tensorflow: https://github.com/spack/spack/pull/24923

#### dependencies

The original recipe only has parts of dependencies specified in README file.

#### version

We applied git version scheme instead of using raw checksum, the origin recipe only has v0.1 and the updated recipe includs v0.1-master.

#### bug fix in recipe

* `+gpu` is an invalid boolean variant for py-theano package as appeared in candle-benchmarks script, which is correted to be `+cuda`.
* `+highgui` is flaged as conflicted with `imgproc`, therefore we removed `+highgui`, in addition, opencv either does not have `+python` or `+zlib` option.
* the expected arch argument in `cudnn` is set to `aarch64sbsa`, which does not align with spack convention.