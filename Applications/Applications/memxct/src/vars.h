#include <mpi.h>
#include <stdio.h>
#include <cmath>
#include <complex>
#include <limits>
#include <omp.h>

using namespace std;

void findnumpix(float, float, float*, int*);
void findpixind(float, float, float*, int*, int, int*);
void findlength(float, float, float*, float*);

void projection(float*, float*);
void backprojection(float*, float*);

int encode(unsigned short, unsigned short);
int xy2d (int n, int x, int y);
void d2xy(int n, int d, int *x, int *y);
float norm_kernel(float*, int);
float dot_kernel(float*, float*, int);
void copy_kernel(float*, float*, int);
void subtract_kernel(float*, float*, float*, int);
void saxpy_kernel(float*, float*, float, float*, int);
