# NuT 

**Description:** NuT is Monte Carlo code for neutrino transport and is a C++ analog to the Haskell McPhD code. NuT is principally aimed at exploring on-node parallelism and performance issues.

**URL:** https://github.com/lanl/NuT

**Team:** Iman

## Compilation

### Spack Package Modification

Details of any changes to the Spack recipe used.

Spack pull request to add _random123_ conflict with nvhpc: https://github.com/spack/spack/pull/24921

Git commit hash of checkout for pacakage:

Pull request for Spack recipe changes:

### Building NuT

**note** NuT is not parallel, so don't look for parallel stuff.

#### Compiler 1: ARM

```
spack install nut %arm
```

```
$ spack spec -Il nut %arm
Input spec
--------------------------------
 -   nut%arm

Concretized
--------------------------------
==> Warning: arm@21.0.0.879 cannot build optimized binaries for "graviton2". Using best target possible: "aarch64"
[+]  ziqvr3w  nut@0.1.1%arm@21.0.0.879~ipo build_type=RelWithDebInfo arch=linux-amzn2-aarch64
[+]  fqvybaf      ^cmake@3.20.5%arm@21.0.0.879~doc+ncurses+openssl+ownlibs~qt build_type=Release arch=linux-amzn2-aarch64
[+]  uhtqtlb          ^ncurses@6.2%arm@21.0.0.879~symlinks+termlib abi=none arch=linux-amzn2-aarch64
[+]  zpuzm23              ^pkgconf@1.7.4%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  vc3waha          ^openssl@1.1.1k%arm@21.0.0.879~docs+systemcerts arch=linux-amzn2-aarch64
[+]  vv6txro              ^perl@5.32.1%arm@21.0.0.879+cpanm+shared+threads arch=linux-amzn2-aarch64
[+]  33wiajj                  ^berkeley-db@18.1.40%arm@21.0.0.879+cxx~docs+stl patches=b231fcc4d5cff05e5c3a4814f6a5af0e9a966428dc2176540d2c05aff41de522 arch=linux-amzn2-aarch64
[+]  z4ybgri                  ^bzip2@1.0.8%arm@21.0.0.879~debug~pic+shared arch=linux-amzn2-aarch64
[+]  adtc6yc                      ^diffutils@3.7%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  7vnthzn                          ^libiconv@1.16%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  645q4qj                  ^gdbm@1.19%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  3haw5gt                      ^readline@8.1%arm@21.0.0.879 arch=linux-amzn2-aarch64
[+]  puuxvg2                  ^zlib@1.2.11%arm@21.0.0.879+optimize+pic+shared arch=linux-amzn2-aarch64
[+]  wlwyzhw      ^random123@1.13.2%arm@21.0.0.879 patches=ceda9371f95401922515a1acd35891079cdbaa825ee1d998d6f31995e96aa282 arch=linux-amzn2-aarch64
```

#### Compiler 2: GCC

```
spack install nut %gcc
```

```
$ spack spec -Il nut %gcc
Input spec
--------------------------------
 -   nut%gcc

Concretized
--------------------------------
[+]  ihypvrj  nut@0.1.1%gcc@10.3.0~ipo build_type=RelWithDebInfo arch=linux-amzn2-graviton2
[+]  m7325ee      ^cmake@3.20.5%gcc@10.3.0~doc+ncurses+openssl+ownlibs~qt build_type=Release arch=linux-amzn2-graviton2
[+]  iwzirqc          ^ncurses@6.2%gcc@10.3.0~symlinks+termlib abi=none arch=linux-amzn2-graviton2
[+]  s4pw7zm              ^pkgconf@1.7.4%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  5i3lgfb          ^openssl@1.1.1k%gcc@10.3.0~docs+systemcerts arch=linux-amzn2-graviton2
[+]  4m7exgb              ^perl@5.32.1%gcc@10.3.0+cpanm+shared+threads arch=linux-amzn2-graviton2
[+]  y42m6yr                  ^berkeley-db@18.1.40%gcc@10.3.0+cxx~docs+stl patches=b231fcc4d5cff05e5c3a4814f6a5af0e9a966428dc2176540d2c05aff41de522 arch=linux-amzn2-graviton2
[+]  rqrpmap                  ^bzip2@1.0.8%gcc@10.3.0~debug~pic+shared arch=linux-amzn2-graviton2
[+]  2w7bert                      ^diffutils@3.7%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  y5ei3cm                          ^libiconv@1.16%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  wjwqncx                  ^gdbm@1.19%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  3zy7kxk                      ^readline@8.1%gcc@10.3.0 arch=linux-amzn2-graviton2
[+]  qepjcvj                  ^zlib@1.2.11%gcc@10.3.0+optimize+pic+shared arch=linux-amzn2-graviton2
[+]  uwifijy      ^random123@1.13.2%gcc@10.3.0 patches=ceda9371f95401922515a1acd35891079cdbaa825ee1d998d6f31995e96aa282 arch=linux-amzn2-graviton2
```

#### Compiler 3: NVHPC
**slight hitch here nvhpc cannot compile cmake** and there is also a slightly trickier curve ball here: random123 uses neon intriscics that nvhpc doesn't support but spack doesn't throw a helpful error like it does with cmake. I fixed it in spack repo: https://github.com/spack/spack/pull/24921

**But** still it wasn't the ultimate solution, this random123 is a header library and a file of that was included into nut, so even though I had random123 (apparently) it still couldn't work, the header was using '__uint128_t' something that nvhpc cannot handle, this is partly weird because 'spack install random123' is sucessfull and there is some expectation that it works, but the installation is copying a bunch of header files around, so the '%nvhpc' there is meaningless.

So what to do? This is the most daring thing I attempted during this hackaton, because well, if not here and now, where else do really bad practicies, hastily put together stitched together improvisations? And it is also a competition, so why not. Firstly, if uint128\_t is not made into fast hw instructions, it is pointless because it would be very _slow_ if you emulate that through good 'ol C code, but just to make this compile on nvhpc, I grabbed this: https://github.com/calccrypto/uint128_t which is basically an implementation of that slow solution, and here is where it gets worse: I 'cd' ed into the directory where the include file was using uint128_t, and I "manually" patched it by adding these lines: 

```
#include "uint128_t.h"
#define __uint128_t uint128_t 
```

And then I wget'ed all the files from https://github.com/calccrypto/uint128_t into that same directory (btw it is: /scratch/opt/spack/linux-amzn2-graviton2/gcc-10.3.0/random123-1.13.2-uwifijyjey3dibeaf77spxtcjtc2coqo/include/Random123/philox.h) this is the philox.h from random123 library. There is a good way to do all of this, just don't compile it with nvhpc :) But anyway, it compiles now and I'm good.

** so the next part worked on my machine because of the patch I discussed, and due to time constraints I don't have the bandwidth to do this in a nice way. **


```
spack install nut %nvhpc ^cmake%gcc ^random123%gcc
```

** again: this spec is not ok, unless you do the patch I described **
```
$ spack spec -Il nut %nvhpc ^cmake%gcc ^random123%gcc
Input spec
--------------------------------
nut%nvhpc
    ^cmake%gcc
    ^random123%gcc

Concretized
--------------------------------
nut@0.1.1%nvhpc@21.2~ipo build_type=RelWithDebInfo arch=linux-amzn2-graviton2
    ^cmake@3.20.5%gcc@10.3.0~doc+ncurses+openssl+ownlibs~qt build_type=Release arch=linux-amzn2-graviton2
        ^ncurses@6.2%gcc@10.3.0~symlinks+termlib abi=none arch=linux-amzn2-graviton2
            ^pkgconf@1.7.4%gcc@10.3.0 arch=linux-amzn2-graviton2
        ^openssl@1.1.1k%gcc@10.3.0~docs+systemcerts arch=linux-amzn2-graviton2
            ^perl@5.32.1%gcc@10.3.0+cpanm+shared+threads arch=linux-amzn2-graviton2
                ^berkeley-db@18.1.40%gcc@10.3.0+cxx~docs+stl patches=b231fcc4d5cff05e5c3a4814f6a5af0e9a966428dc2176540d2c05aff41de522 arch=linux-amzn2-graviton2
                ^bzip2@1.0.8%gcc@10.3.0~debug~pic+shared arch=linux-amzn2-graviton2
                    ^diffutils@3.7%gcc@10.3.0 arch=linux-amzn2-graviton2
                        ^libiconv@1.16%gcc@10.3.0 arch=linux-amzn2-graviton2
                ^gdbm@1.19%gcc@10.3.0 arch=linux-amzn2-graviton2
                    ^readline@8.1%gcc@10.3.0 arch=linux-amzn2-graviton2
                ^zlib@1.2.11%gcc@10.3.0+optimize+pic+shared arch=linux-amzn2-graviton2
    ^random123@1.13.2%gcc@10.3.0 patches=ceda9371f95401922515a1acd35891079cdbaa825ee1d998d6f31995e96aa282 arch=linux-amzn2-graviton2
```

## Validation

I go over the description once as it is similar for all test cases:

NuT has three particle type, nu_e, nu_e_bar and nu_x, each of this should be conserved meaning that the total particles we started with, would either escape or be absorbed so for each: total_i = absorbed_i + escaped_i and this conservation is used in validation. The test case sends in 10000 particles and the medium data comes from the files in the repository, this one is: https://raw.githubusercontent.com/lanl/NuT/master/test/data/

## Test Case 1 P1 medium with N = 1000

[ReFrame Benchmark 1](#)

```
../bin/reframe -c t0.py -r --performance-report
```

### Validation

N = 10000 particles 
medium spec: p1

### ReFrame Output

Time is measured in seconds (I later fixed it in the code) but the (s) is umited in the above.

```
==============================================================================
PERFORMANCE REPORT
------------------------------------------------------------------------------
nut_test0_2P_nut_0_1_1__arm_N_1_MPI_1_OMP_1
- aws:c6gn
   - builtin
      * num_tasks: 1
      * MC/s: 954579.2861695348 
      * T: 15.69 s
------------------------------------------------------------------------------
nut_test0_2P_nut_0_1_1__gcc__ihypvrj_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * MC/s: 1104524.262536873 
      * T: 13.56 s
------------------------------------------------------------------------------
nut_test0_2P_nut_0_1_1__nvhpc_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * MC/s: 961936.3519588953 
      * T: 15.57 s
------------------------------------------------------------------------------
```

### On-node Compiler Comparison

Performance comparison of two compilers. Measure is monte carlo steps per second.

| Cores | ARM       | GCC        | NCHPC     |
|-------|-----------|------------|-----------|
| 1     | 954579    | 1104524    |  961936   |

## Test Case 1 P1 medium with N = 1000

[ReFrame Benchmark 2](#)

```
../bin/reframe -c t1.py -r --performance-report
```

### Validation TC2

N = 20000 particles 
medium spec: p2

### ReFrame Output TC2

Time is measured in seconds (I later fixed it in the code) but the (s) is umited in the above.

```
==============================================================================
PERFORMANCE REPORT
------------------------------------------------------------------------------
nut_test1_2_nut_0_1_1__arm_N_1_MPI_1_OMP_1
- aws:c6gn
   - builtin
      * num_tasks: 1
      * MC/s: 965815.2710940005 
      * T: 31.17 s
------------------------------------------------------------------------------
nut_test1_2_nut_0_1_1__gcc__ihypvrj_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * MC/s: 1111275.8213362864 
      * T: 27.09 s
------------------------------------------------------------------------------
nut_test1_2_nut_0_1_1__nvhpc_N_1_MPI_1_OMP_1
   - builtin
      * num_tasks: 1
      * MC/s: 966125.2246469833 
      * T: 31.16 s
------------------------------------------------------------------------------
```

### On-node Compiler Comparison TC2

Performance comparison of two compilers. Measure is monte carlo steps per second. The results being similar to previous is MC/T is nice because it means that it scales well with number of particles, as you can see with x2 particles the total times are roughly doubled as we expect. Also surprisingly nvhpc is not so broken after all :)

| Cores | ARM       | GCC        | NCHPC     |
|-------|-----------|------------|-----------|
| 1     | 965815    | 1111275    |  966125   |


### Compilation Summary

Only nvhpc had issues and boy was it hefty! Full, long discussion is there in that section. 
