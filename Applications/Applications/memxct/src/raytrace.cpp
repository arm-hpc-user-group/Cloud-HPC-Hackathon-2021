#include "vars.h"

extern float raylength;
extern float pixsize;
extern int numx;
extern int numy;
extern int spatsize;
extern int spatindexing;

void findlength(float theta, float rho, float *d, float *length){
  //RAY'S VECTOR REPRESENTAION
  float x = rho*cos(theta)+0.5*raylength*sin(theta);
  float y = rho*sin(theta)-0.5*raylength*cos(theta);
  float dx = -raylength*sin(theta);
  float dy = +raylength*cos(theta);
  //TOP LEVEL
  float p[4] = {-dx,dx,-dy,dy};
  float q[4] = {x-d[0],d[1]-x,y-d[2],d[3]-y};
  float u1 = 0;
  float u2 = 1;
  bool pass = true;
  int inid = 0;
  for(int k = 0; k < 4; k++)
    if(p[k] == 0){
      if(q[k] < 0){
        pass = false;
        break;
      }
    }else{
      float t = q[k]/p[k];
      if(p[k] < 0 && u1 < t){
        u1 = t;
        inid = k;
      }
      else if(p[k] > 0 && u2 > t)
        u2 = t;
    }
  if(u1 > u2 || u1 > 1 || u1 < 0) pass = false;
  if(pass)if(u2>u1)*length = *length+(u2-u1)*raylength;
}

void findnumpix(float theta, float rho, float *d, int *numpix){

  int numproc;
  int myid;
  MPI_Comm_size(MPI_COMM_WORLD,&numproc);
  MPI_Comm_rank(MPI_COMM_WORLD,&myid);

  //RAY'S VECTOR REPRESENTAION
  float x = rho*cos(theta)+0.5*raylength*sin(theta);
  float y = rho*sin(theta)-0.5*raylength*cos(theta);
  float dx = -raylength*sin(theta);
  float dy = +raylength*cos(theta);

  //TOP LEVEL
  float p[4] = {-dx,dx,-dy,dy};
  float q[4] = {x-d[0],d[1]-x,y-d[2],d[3]-y};
  float u1 = 0;
  float u2 = 1;
  bool pass = true;
  int inid = 0;
  for(int k = 0; k < 4; k++)
    if(p[k] == 0){
      if(q[k] < 0){
        pass = false;
        break;
      }
    }else{
      float t = q[k]/p[k];
      if(p[k] < 0 && u1 < t){
        u1 = t;
        inid = k;
      }
      else if(p[k] > 0 && u2 > t)
        u2 = t;
    }
  if(u1 > u2 || u1 > 1 || u1 < 0) pass = false;
  //IF RAY COLLIDES WITH DOMAIN
  if(pass){
    //FIND THE INITIAL PIXEL
    int init = 0;
    int initx = 0;
    int inity = 0;
    if(inid == 0){ //LEFT
      initx = 0;
      inity = (int)((y+u1*dy-d[2])/pixsize);
    }
    if(inid == 1){ //RIGHT
      initx = (int)((d[1]-d[0]-pixsize/2)/pixsize);
      inity = (int)((y+u1*dy-d[2])/pixsize);
    }
    if(inid == 2){ //BOTTOM
      initx = (int)((x+u1*dx-d[0])/pixsize);
      inity = 0;
    }
    if(inid == 3){ //TOP
      initx = (int)((x+u1*dx-d[0])/pixsize);
      inity = (int)((d[3]-d[2]-pixsize/2)/pixsize);
    }
    float px = d[0]+initx*pixsize+pixsize/2;
    float py = d[2]+inity*pixsize+pixsize/2;
    //TRACE RAY WHILE IT IS IN THE DOMAIN
    while(px > d[0] && px < d[1] && py < d[3] && py > d[2]){
      int exid = 0;
      q[0] = x-(px-pixsize/2);
      q[1] = (px+pixsize/2)-x;
      q[2] = y-(py-pixsize/2);
      q[3] = (py+pixsize/2)-y;
      u1 = 0;
      u2 = 1;
      for(int k = 0; k < 4; k++){
        float t = q[k]/p[k];
        if(p[k] < 0 && u1 < t)
          u1 = t;
        else if(p[k] > 0 && u2 > t){
          u2 = t;
          exid = k;
        }
      }
      //INCREMENT NUMBER OF PIXELS
      if(u2 > u1)
        *numpix = *numpix + 1;
      //FIND NEXT PIXEL
      if(exid == 0){
        initx = initx-1;
        px = px - pixsize;
      }
      if(exid == 1){
        initx = initx+1;
        px = px + pixsize;
      }
      if(exid == 2){
        inity = inity-1;
        py = py - pixsize;
      }
      if(exid == 3){
        inity = inity+1;
        py = py + pixsize;
      }
    }
  }
}

void findpixind(float theta, float rho, float *d, int *numpix, int offset, int *pixind){

  int numproc;
  int myid;
  MPI_Comm_size(MPI_COMM_WORLD,&numproc);
  MPI_Comm_rank(MPI_COMM_WORLD,&myid);

  //RAY'S VECTOR REPRESENTAION
  float x = rho*cos(theta)+0.5*raylength*sin(theta);
  float y = rho*sin(theta)-0.5*raylength*cos(theta);
  float dx = -raylength*sin(theta);
  float dy = +raylength*cos(theta);

  //TOP LEVEL
  float p[4] = {-dx,dx,-dy,dy};
  float q[4] = {x-d[0],d[1]-x,y-d[2],d[3]-y};
  float u1 = 0;
  float u2 = 1;
  bool pass = true;
  int inid = 0;
  for(int k = 0; k < 4; k++)
    if(p[k] == 0){
      if(q[k] < 0){
        pass = false;
        break;
      }
    }else{
      float t = q[k]/p[k];
      if(p[k] < 0 && u1 < t){
        u1 = t;
        inid = k;
      }
      else if(p[k] > 0 && u2 > t)
        u2 = t;
    }
  if(u1 > u2 || u1 > 1 || u1 < 0) pass = false;
  //IF RAY COLLIDES WITH DOMAIN
  if(pass){
    //FIND THE INITIAL PIXEL
    int init = 0;
    int initx = 0;
    int inity = 0;
    if(inid == 0){ //LEFT
      initx = 0;
      inity = (int)((y+u1*dy-d[2])/pixsize);
    }
    if(inid == 1){ //RIGHT
      initx = (int)((d[1]-d[0]-pixsize/2)/pixsize);
      inity = (int)((y+u1*dy-d[2])/pixsize);
    }
    if(inid == 2){ //BOTTOM
      initx = (int)((x+u1*dx-d[0])/pixsize);
      inity = 0;
    }
    if(inid == 3){ //TOP
      initx = (int)((x+u1*dx-d[0])/pixsize);
      inity = (int)((d[3]-d[2]-pixsize/2)/pixsize);
    }
    float px = d[0]+initx*pixsize+pixsize/2;
    float py = d[2]+inity*pixsize+pixsize/2;
    //TRACE RAY WHILE IT IS IN THE DOMAIN
    while(px > d[0] && px < d[1] && py < d[3] && py > d[2]){
      int exid = 0;
      q[0] = x-(px-pixsize/2);
      q[1] = (px+pixsize/2)-x;
      q[2] = y-(py-pixsize/2);
      q[3] = (py+pixsize/2)-y;
      u1 = 0;
      u2 = 1;
      for(int k = 0; k < 4; k++){
        float t = q[k]/p[k];
        if(p[k] < 0 && u1 < t)
          u1 = t;
        else if(p[k] > 0 && u2 > t){
          u2 = t;
          exid = k;
        }
      }
      //ADD CONTRIBUTION FROM CURRENT PIXEL
      int z = 0;
      if(spatindexing==1)
        z = inity*spatsize+initx;
      if(spatindexing==2)
        z = initx*spatsize+inity;
      if(spatindexing==3)
        z = encode(initx,inity);
      if(spatindexing==4)
        z = encode(inity,initx);
      if(spatindexing==5)
        z = xy2d(spatsize,initx,inity);
        //z = encode(initx,inity);
      if(u2 > u1){
        pixind[*numpix] = offset+z;
        //pixlen[*numpix] = (u2-u1)*raylength;
        *numpix = *numpix + 1;
      }
      //FIND NEXT PIXEL
      if(exid == 0){
        initx = initx-1;
        px = px - pixsize;
      }
      if(exid == 1){
        initx = initx+1;
        px = px + pixsize;
      }
      if(exid == 2){
        inity = inity-1;
        py = py - pixsize;
      }
      if(exid == 3){
        inity = inity+1;
        py = py + pixsize;
      }
    }
  }
}


int encode(unsigned short x, unsigned short y){
  unsigned int z = 0; // z gets the resulting Morton Number.
  for (int i = 0; i < sizeof(x)*8; i++)
    z |= (x & 1U << i) << i | (y & 1U << i) << (i + 1);
  return z;
}

//rotate/flip a quadrant appropriately
void rot(int n, int *x, int *y, int rx, int ry) {
    if (ry == 0) {
        if (rx == 1) {
            *x = n-1 - *x;
            *y = n-1 - *y;
        }

        //Swap x and y
        int t  = *x;
        *x = *y;
        *y = t;
    }
}
//convert (x,y) to d
int xy2d (int n, int x, int y) {
    int rx, ry, s, d=0;
    for (s=n/2; s>0; s/=2) {
        rx = (x & s) > 0;
        ry = (y & s) > 0;
        d += s * s * ((3 * rx) ^ ry);
        rot(s, &x, &y, rx, ry);
    }
    return d;
}
//convert d to (x,y)
void d2xy(int n, int d, int *x, int *y) {
    int rx, ry, s, t=d;
    *x = *y = 0;
    for (s=1; s<n; s*=2) {
        rx = 1 & (t/2);
        ry = 1 & (t ^ rx);
        rot(s, x, y, rx, ry);
        *x += s * rx;
        *y += s * ry;
        t /= 4;
    }
}
