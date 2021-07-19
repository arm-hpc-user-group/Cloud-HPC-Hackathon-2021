# Additional details on MemXCT 
(TODO: cleanup pending) 

## All work based off of this [SC19 paper](http://impact.crhc.illinois.edu/Shared/Papers/MemXCT_SC19.pdf)

## Compile

**Make Sure Dependencies are Installed**

1. C++ Compiler
2. MPI Compiler

**Modify Makefile**

There are Makefiles for ALCF Theta (Intel KNL) and OLCF Summit (IBM POWER9) and TACC Frontera (Intel Cascade Lake) systems. You should use one of these to modify according to your system.

## Download Datasets

We provide the challenge datasets over Box. Dimensions (Theta x Rho) and corresponding application memory footprints are given below.

**Test Datasest:**

* ADS1 (360x256): 512 MB
* ADS2 (750x512): 3.6 GB
* ADS3 (1500x1024): 28 GB
* ADS4 (2400x2048): 180 GB

**Challenge Datasets:**
TBA

Each dataset requires a theta file and a sinogram file. Use the code below to directly download datasets to your cluster.

```bash
wget https://uofi.box.com/shared/static/ql76fxfrnec1jdl8dc4f2g4ihwekn9oj -O ADS1_theta.bin
wget https://uofi.box.com/shared/static/zmt3vq5k0jaqgcay4a7yscv2a0viyxlc -O ADS1_sinogram.bin

wget https://uofi.box.com/shared/static/yrsr9brzl6q03bmnunfk65k33ykvfr8o -O ADS2_theta.bin
wget https://uofi.box.com/shared/static/wssrib7ud9na1k5zxxjm3kabd2bcrjwu -O ADS2_sinogram.bin

wget https://uofi.box.com/shared/static/vi1uiecpqqiz7rjtty6fbxxwn1feoib0 -O ADS3_theta.bin
wget https://uofi.box.com/shared/static/icxtknbrndv8i2d83mc87ppjxepty8jz -O ADS3_sinogram.bin

wget https://uofi.box.com/shared/static/tbjk9dksog7qqick66nbcnq4ngais1yd -O ADS4_theta.bin
wget https://uofi.box.com/shared/static/ki7smuurh34cleayvwfxhjfn9mgsnega -O ADS4_sinogram.bin
```
## Compile
```
make -f Makefile.<arch/machine>
```
## Run 

Edit input parameters and run the application using run script. Update one of the run scripts for your system.

```bash
#DOMAIN INFORMATION
export NUMTHE= #Number of Rotations (according to the input dataset)
export NUMRHO= #Number of Channels (according to the input dataset)
export PIXSIZE= #Pixel Size (should be 1)
#SOLVER DATA
export NUMITER= #Number of Iterations (should be 24)
#TILE SIZE (MUST BE POWER OF TWO)
export SPATSIZE= #Spatial Tile Size (tuning parameter)
export SPECSIZE= #Spectral Tile Size (tuning parameter)
#BLOCK SIZE
export PROJBLOCK= #Projection Partition Block Size (tuning parameter)
export BACKBLOCK= #Backprojection Partition Block Size (tuning parameter)
#BUFFER SIZE
export PROJBUFF= #Projection Buffer Size in KB (tuning parameter)
export BACKBUFF= #Backprojection Buffer Size in KB (tuning parameter)
#I/O FILES
export THEFILE= #input theta file path
export SINFILE= #input sinogram file path
export OUTFILE= #output image file path

#RUN COMMAND COMES HERE
```

You should see residual error drops in each iteration.

## Verify

Download [Fiji](https://fiji.sc) open source, lightweight, standalone scientific visualization tool. Import the raw image file and inspect the image to verify the code. Sinogram (input) and tomogram (output) test data should look as below.

<table>
  <tr>
    <th>ADS1 Sinogram (360x256)</th>
    <th>ADS1 Tomogram (256x256)</th>
  </tr>
  <tr valign="top">
    <td style="text-align:center"><img src="https://user-images.githubusercontent.com/15988772/91278602-0e326000-e74a-11ea-8d64-37dd8ce307e3.png" width="256" title="ADS1 Sinogram"></td>
    <td style="text-align:center"><img src="https://user-images.githubusercontent.com/15988772/91278668-22765d00-e74a-11ea-8e41-867c3ee286d6.png" width="256" title="ADS1 Tomogram" ></td>
  </tr>
</table>

<table>
  <tr>
    <th>ADS2 Sinogram (750x512)</th>
    <th>ADS2 Tomogram (512x512)</th>
  </tr>
  <tr valign="top">
    <td style="text-align:center"><img src="https://user-images.githubusercontent.com/15988772/91278678-2609e400-e74a-11ea-8fd0-e789b2427c44.png" width="256" title="ADS2 Sinogram"></td>
    <td style="text-align:center"><img src="https://user-images.githubusercontent.com/15988772/91278685-286c3e00-e74a-11ea-9238-9ffb6c12699e.png" width="256" title="ADS2 Tomogram" ></td>
  </tr>
</table>

<table>
  <tr>
    <th>ADS3 Sinogram (1500x1024)</th>
    <th>ADS3 Tomogram (1024x1024)</th>
  </tr>
  <tr valign="top">
    <td style="text-align:center"><img src="https://user-images.githubusercontent.com/15988772/91278696-2ace9800-e74a-11ea-8bcc-17be6f63e693.png" width="256" title="ADS3 Sinogram"></td>
    <td style="text-align:center"><img src="https://user-images.githubusercontent.com/15988772/91278705-2d30f200-e74a-11ea-9563-bad5bb6e2e48.png" width="256" title="ADS3 Tomogram" ></td>
  </tr>
</table>

<table>
  <tr>
    <th>ADS4 Sinogram (2400x2048)</th>
    <th>ADS4 Tomogram (2048x2048)</th>
  </tr>
  <tr valign="top">
    <td style="text-align:center"><img src="https://user-images.githubusercontent.com/15988772/91278713-2efab580-e74a-11ea-8b6d-e4265b96c8ab.png" width="256" title="ADS4 Sinogram"></td>
    <td style="text-align:center"><img src="https://user-images.githubusercontent.com/15988772/91278912-7123f700-e74a-11ea-8908-dbcfbb2e4dd7.png" width="256" title="ADS4 Tomogram" ></td>
  </tr>
</table>
