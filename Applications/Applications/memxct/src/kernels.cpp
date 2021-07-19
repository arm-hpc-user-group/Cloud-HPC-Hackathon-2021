#include "vars.h"

extern float *raypart;
extern float *raybuff;

extern int raynuminc;
extern int raynumout;
extern int mynumray;
extern int mynumpix;

extern int *raysendstart;
extern int *rayrecvstart;
extern int *raysendcount;
extern int *rayrecvcount;

extern int *rayraystart;
extern int *rayrayind;
extern int *rayrecvlist;

extern double ftime;
extern double btime;
extern double fktime;
extern double frtime;
extern double bktime;
extern double brtime;
extern double aftime;
extern double abtime;
extern int numproj;
extern int numback;

extern int proj_blocksize;
extern int proj_numblocks;
extern int *proj_blockdispl;
extern int proj_buffsize;
extern long *proj_buffdispl;
extern int *proj_buffmap;
extern int *proj_buffmapnz;
extern long *proj_buffmapdispl;
extern long proj_rownztot;
extern unsigned short *proj_buffindex;
extern float *proj_buffvalue;
extern int back_blocksize;
extern int back_numblocks;
extern int *back_blockdispl;
extern int back_buffsize;
extern long *back_buffdispl;
extern int *back_buffmap;
extern int *back_buffmapnz;
extern long *back_buffmapdispl;
extern unsigned short *back_buffindex;
extern float *back_buffvalue;

void projection(float *mes, float *obj){
  MPI_Barrier(MPI_COMM_WORLD);
  double timef = MPI_Wtime();
  {
    double time = MPI_Wtime();
    int blocksize = proj_blocksize;
    int numblocks = proj_numblocks;
    int *blockdispl = proj_blockdispl;
    int buffsize = proj_buffsize;
    long *buffdispl = proj_buffdispl;
    int *buffmap = proj_buffmap;
    long *buffmapdispl = proj_buffmapdispl;
    int *buffmapnz = proj_buffmapnz;
    unsigned short *index = proj_buffindex;
    float *value = proj_buffvalue;
    #pragma omp parallel
    {
      float output[blocksize];
      float input[buffsize];
      int start;
      #pragma omp for schedule(dynamic)
      for(int block = 0; block < numblocks; block++){
        for(int n = 0; n < blocksize; n++)
          output[n] = 0;
        for(int buff = blockdispl[block]; buff < blockdispl[block+1]; buff++){
          for(int n = 0; n < buffmapnz[buff]; n++)
            input[n] = obj[buffmap[buffmapdispl[buff]+n]];
          start = buff*blocksize;
          for(int m = 0; m < blocksize; m++)
            for(long n = buffdispl[start+m]; n < buffdispl[start+m+1]; n++)
              output[m] += input[index[n]]*value[n];
        }
        start = block*blocksize;
        for(int n = 0; n < blocksize; n++){
          if(start+n < raynumout)
            raypart[start+n] = output[n];
        }
      }
    }
    MPI_Barrier(MPI_COMM_WORLD);
    fktime = fktime + MPI_Wtime()-time;
  }
  {
    double time = MPI_Wtime();
    MPI_Alltoallv(raypart,raysendcount,raysendstart,MPI_FLOAT,raybuff,rayrecvcount,rayrecvstart,MPI_FLOAT,MPI_COMM_WORLD);
    MPI_Barrier(MPI_COMM_WORLD);
    aftime = aftime + MPI_Wtime()-time;
  }
  {
    double  time = MPI_Wtime();
    #pragma omp parallel for
    for(int k = 0; k < mynumray; k++){
      float reduce = 0;
      for(int kk = rayraystart[k]; kk < rayraystart[k+1]; kk++)
        reduce = reduce + raybuff[rayrayind[kk]];
      mes[k] = reduce;
    }
    MPI_Barrier(MPI_COMM_WORLD);
    frtime = frtime + MPI_Wtime()-time;
  }
  ftime = ftime + MPI_Wtime()-timef;
  numproj++;
}

void backprojection(float *gra, float *res){
  MPI_Barrier(MPI_COMM_WORLD);
  double timeb = MPI_Wtime();
  {
    double time = timeb;
    #pragma omp parallel for
    for(int k = 0; k < raynuminc; k++)
      raybuff[k] = res[rayrecvlist[k]];
    MPI_Barrier(MPI_COMM_WORLD);
    brtime = brtime + MPI_Wtime()-time;
  }
  {
    double time = MPI_Wtime();
    MPI_Alltoallv(raybuff,rayrecvcount,rayrecvstart,MPI_FLOAT,raypart,raysendcount,raysendstart,MPI_FLOAT,MPI_COMM_WORLD);
    MPI_Barrier(MPI_COMM_WORLD);
    abtime = abtime + MPI_Wtime()-time;
  }
  {
    double time = MPI_Wtime();
    int blocksize = back_blocksize;
    int numblocks = back_numblocks;
    int *blockdispl = back_blockdispl;
    int buffsize = back_buffsize;
    long *buffdispl = back_buffdispl;
    int *buffmap = back_buffmap;
    long *buffmapdispl = back_buffmapdispl;
    int *buffmapnz = back_buffmapnz;
    unsigned short *index = back_buffindex;
    float *value = back_buffvalue;
    #pragma omp parallel
    {
      float output[blocksize];
      float input[buffsize];
      int start;
      #pragma omp for schedule(dynamic)
      for(int block = 0; block < numblocks; block++){
        for(int n = 0; n < blocksize; n++)
          output[n] = 0;
        for(int buff = blockdispl[block]; buff < blockdispl[block+1]; buff++){
          for(int n = 0; n < buffmapnz[buff]; n++)
            input[n] = raypart[buffmap[buffmapdispl[buff]+n]];
          start = buff*blocksize;
          for(int m = 0; m < blocksize; m++)
            for(long n = buffdispl[start+m]; n < buffdispl[start+m+1]; n++)
              output[m] += input[index[n]]*value[n];
        }
        start = block*blocksize;
        for(int n = 0; n < blocksize; n++){
          if(start+n < raynumout)
            gra[start+n] = output[n];
        }
      }
    }
    MPI_Barrier(MPI_COMM_WORLD);
    bktime = bktime + MPI_Wtime()-time;
  }
  btime = btime + MPI_Wtime()-timeb;
  numback++;
}
