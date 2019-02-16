
function int ProjInt_Brute(int stid, int ttid, int spd, int ptid, int xoff, int yoff, int zoff, str ptype, int axoff, int ayoff, int azoff, int angoff, int rand, int input_t)
{
  int sX, sY, sZ, s_ang, tX, tY, tZ, tVelX, tVelY, tVelZ;
  int tXf, tYf, tZf;
  int T_S_z, Z_spd_t, X_spd_t, Y_spd_t, XY_spd_t, spd_t, p_ang;
  int t, tt, t_inc, sml_t, n, nmax, i, diff, smldiff;
  int X_spd, Y_spd, Z_spd, XY_spd;
  int check = 1, check2 = 1;
  int oldstid, oldttid, stid_z, ttid_z;

  if(!stid || ThingCount(T_NONE,stid) > 1){
    stid_z = 1;
    oldstid = ActivatorTID();
    stid = UniqueTID();
    Thing_ChangeTID(0, stid); }
  else{ oldstid = stid; }

  sX = GetActorX(stid);
  sY = GetActorY(stid);
  sZ = GetActorZ(stid);
  s_ang = GetActorAngle(stid);
  
  sZ += zoff;

  if(xoff > 0){
    sX += FixedMul(cos(FixedAngMod(s_ang - 0.25)),xoff); 
    sY += FixedMul(sin(FixedAngMod(s_ang - 0.25)),xoff); }
  else if(xoff < 0){
    sX += FixedMul(cos(FixedAngMod(s_ang + 0.25)),xoff); 
    sY += FixedMul(sin(FixedAngMod(s_ang + 0.25)),xoff); }
 
 if(yoff > 0){
    sX += FixedMul(cos(s_ang),yoff); 
    sY += FixedMul(sin(s_ang),yoff); }
  else if(yoff < 0){
    sX -= FixedMul(cos(s_ang),yoff); 
    sY -= FixedMul(sin(s_ang),yoff); }

  if(!ttid || ThingCount(T_NONE,ttid) > 1){
    ttid_z = 1;
    SetActivator(0, AAPTR_TARGET);
    oldttid = ActivatorTID();
    ttid = UniqueTID();
    Thing_ChangeTID(0, ttid); }
  else{ oldttid = ttid; }

  tX = GetActorX(ttid);
  tY = GetActorY(ttid);
  tZ = GetActorZ(ttid);
  tZ += 36.0;
  //tZ += 26.5; for comparison with Thing_ProjectileIntercept
  
  tVelX = GetActorVelX(ttid);
  tVelY = GetActorVelY(ttid);
  tVelZ = GetActorVelZ(ttid);
  
  if(!CheckFlag(ttid,"NOGRAVITY")){ tVelZ = 0; }

  while(check){
    t = sml_t - (t_inc / 2);
    if(!i){
      t = 1.0;
      t_inc = 10.0;
      nmax = 40; }
    else if(i == 1){
      if(sml_t > 400.0){ check = 0; } //stop trying to get closer if it's out of range, it's just a waste
      else{
        t_inc = 1.0;
        nmax = 10; }}  
    else if(i == 2){
      t_inc = 0.1;
      nmax = 10; }       
    else if(i == 3){
      t_inc = 0.01;
      nmax = 10; }             
    else if(i == 4){
      t_inc = 0.001;
      nmax = 10; }           
    else if(i == 5){
      t_inc = 1;
      nmax = 66; }         
    else if(i == 6){ check = 0; }      
    ++i;
    n = 0;
    check2 = 1; 

    while(check && check2){
      tXf = tX + FixedMul(t,tVelX);
      tYf = tY + FixedMul(t,tVelY);
      tZf = tZ + FixedMul(t,tVelZ);
      Z_spd_t = FixedDiv(tZf - sZ, t);
      X_spd_t = FixedDiv(tXf - sX, t);
      Y_spd_t = FixedDiv(tYf - sY, t);
      XY_spd_t = VectorLength(X_spd_t, Y_spd_t);
      spd_t = VectorLength(XY_spd_t, Z_spd_t);
      diff = abs(spd - spd_t);
      if((diff < smldiff) || n == 0){
        smldiff = diff;
        sml_t = t; }
      ++n;
      t += t_inc;
      if(n > nmax){ check2 = 0; }}}

  if(input_t){ t = input_t; }
  else{ 
    if(rand){ random(1, sml_t); }
    else{ t = sml_t; }}
  tt = sml_t;
  tXf = tX + FixedMul(t,tVelX);
  tYf = tY + FixedMul(t,tVelY);
  tZf = tZ + FixedMul(t,tVelZ);
  
  if(rand || input_t){
    Z_spd = FixedDiv(tZf - sZ, tt);
    p_ang = VectorAngle(tXf - sX, tYf - sY);
    XY_spd = FixedSqrt(sq(spd) - sq(Z_spd));
    X_spd = FixedMul(cos(p_ang), XY_spd);
    Y_spd = FixedMul(sin(p_ang), XY_spd); }
  else{
    Z_spd = FixedDiv(tZf - sZ, t);
    X_spd = FixedDiv(tXf - sX, t);
    Y_spd = FixedDiv(tYf - sY, t);
    p_ang = VectorAngle(tXf - sX, tYf - sY); }
  
  SetActorAngle(stid, p_ang);
  
  sZ += azoff;

  if(axoff > 0){
    sX -= FixedMul(cos(FixedAngMod(s_ang - 0.25)),axoff); 
    sY -= FixedMul(sin(FixedAngMod(s_ang - 0.25)),axoff); }
  else if(axoff < 0){
    sX += FixedMul(cos(FixedAngMod(s_ang + 0.25)),axoff); 
    sY += FixedMul(sin(FixedAngMod(s_ang + 0.25)),axoff); }
 
  if(ayoff > 0){
    sX += FixedMul(cos(s_ang),ayoff); 
    sY += FixedMul(sin(s_ang),ayoff); }
  else if(ayoff < 0){
    sX -= FixedMul(cos(s_ang),ayoff); 
    sY -= FixedMul(sin(s_ang),ayoff); }

  if(angoff != 0){
    p_ang = FixedAngMod(p_ang + angoff);
    XY_spd = FixedSqrt(sq(X_spd) + sq(Y_spd));
    X_spd = FixedMul(cos(FixedAngMod(p_ang + angoff)), XY_spd);
    Y_spd = FixedMul(sin(FixedAngMod(p_ang + angoff)), XY_spd); }

  if(!ptid || ThingCount(T_NONE,stid) > 1){ ptid = UniqueTID(); }

  SpawnProjectile (stid, ptype, 0, 0, 0, 0, ptid); 
  SetActivator(ptid); 
  SetPointer(AAPTR_TARGET, stid); //so doesn't collide with it
  SetPointer(AAPTR_TRACER, ttid);
  SetActorPosition(ptid, sX, sY, sZ, 0);
  SetActorAngle(ptid, p_ang);
  SetActorVelocity(ptid,X_spd,Y_spd,Z_spd,0,0);

  SetActivator(stid); 
  if(stid_z){ Thing_ChangeTID(stid, oldstid); }
  if(ttid_z){ Thing_ChangeTID(ttid, oldttid); }
  return t;
}
    
/* This below script doesn't work, because I'm dumb, and since I don't know 
C++ yet I can't copy the code Thing_ProjectileIntercept uses. (Here it is on 
the ZDoom git (https://github.com/rheit/zdoom/blob/master/src/p_things.cpp) 
I've tried to comment this code well enough to explain what I'm trying to do 
here, so if you're reading this and can figure out what I'm doing wrong please 
help me. */

function int ProjectileInterceptNoWork(int stid, int ttid, int spd, int ptid)
{
  /* stid is the shooter tid, ttid is the target tid, spd is the speed of the projectile in fixed point, ptid is the tid the projectile will have */

  int t, last_t, sml_t, n, diff, lastdiff, smldiff, check;
  
  int a, b, c, t1, t2;
  
  int sX = GetActorX(stid);
  int sY = GetActorY(stid);
  int sZ = GetActorZ(stid);

  int tX = GetActorX(ttid);
  int tY = GetActorY(ttid);
  int tZ = GetActorZ(ttid);
  
  //tZ = tZ + 26.5;  This was just here for comparison with Thing_ProjectileIntercept, which fires above the target's Z approximately 26.5 map units. 
  
  int tVelX = GetActorVelX(ttid);
  int tVelY = GetActorVelY(ttid);
  int tVelZ = GetActorVelZ(ttid);

  //Triangle STI, where S is shooter position, T is target position and I is where the target and fired projectile will intercept

  int S_T_len = FixedSqrt(sq(sX - tX) + sq(sY - tY) + sq(sZ - tZ)); //Distance between shooter and target, or S_T
  int tVel_len = FixedSqrt(sq(tVelX) + sq(tVelY) + sq(tVelZ));  //Vector length for the shooter's velocity

  int alg_dot_STI = FixedMul(sX-tX, tVelX) + FixedMul(sY-tY, tVelY) + FixedMul(sZ-tZ, tVelZ);  /* The algebraic dot product, which is:
  //log(s: "alg_dot_STI:", f: alg_dot_STI);
  
  http://en.wikipedia.org/wiki/Dot_product
  http://math.oregonstate.edu/home/programs/undergrad/CalculusQuestStudyGuides/vcalc/dotprod/dotprod.html
  
   Vector0   *  Vector1 =
  [x0,y0,z0] * [x1,y1,z1] =
   (x0 * x1) + (y0 * y1) + (z0 * z1)
  
  which is equal to the geometric dot product, which is:
  
  Vector0 * Vector1 =
  |V0| * |V1| * cos(###)   where ### is the angle between the vectors and |x| denotes "length of x"
  
  so
  
  sqrt(x0*x0 + y0*y0 + z0*z0) * sqrt(x1*x1 + y1*y1 + z1*z1) * cos(###) = (x0 * x1 ) + (y0 * y1) + (z0 * z1)
  
  so
  
  cos(###) = [(x0 * x1 ) + (y0 * y1) + (z0 * z1)] / [sqrt(x0*x0 + y0*y0 + z0*z0) * sqrt(x1*x1 + y1*y1 + z1*z1)]
   
  */

  int cos_STI = FixedDiv(alg_dot_STI, FixedMul(S_T_len, tVel_len)); 

  /*
  Then using the Law of Cosines, 
  http://en.wikipedia.org/wiki/Law_of_cosines
  which is:
  
  c*c = a*a + b*b - 2*a*b*cos(C),   where a, b, and c are sides of a triangle and C is the angle opposite side c.
  
  in this case 
  
  a = S_T = S_T_len   | S_T_len = FixedSqrt(sq(sX - tX) + sq(sY - tY) + sq(sZ - tZ));
  
  b = T_I = target veloctiy * t = tVel_len * t   | tVel_len  = FixedSqrt(sq(tVelX) + sq(tVelY) + sq(tVelZ));
  
  c = S_I = projectile veloctiy * t = spd * t   | function argument
  
  C = angle S_T_I = arccos(cos_STI)   | cos_STI = FixedDiv(alg_dot_STI, FixedMul(S_T_len, tVel_len)); 
  
  where t is time to impact, in tics. 
  
  We can then substitute
  
  c*c = a*a + b*b - 2*a*b*cos(C)

  (spd * t)*(spd * t) = (S_T_len)*(S_T_len) + (tVel_len * t)*(tVel_len * t) - 2*(S_T_len)*(tVel_len * t)*(cos_STI)

  set it equal to zero by subtracting from the left
  
  0 = (S_T_len)*(S_T_len) + (tVel_len * t)*(tVel_len * t) - 2*(S_T_len)*(tVel_len * t)*(cos_STI) - (spd * t)*(spd * t)

  then factor for t
  
  0 = (tVel_len * t)*(tVel_len * t) - (spd * t)*(spd * t) + (S_T_len)*(S_T_len) - 2*(S_T_len)*(tVel_len * t)*(cos_STI)  
  
  0 = (tVel_len * t)*(tVel_len * t) - (spd * t)*(spd * t) + (S_T_len)*(S_T_len) - 2*(S_T_len)*(tVel_len * t)*(cos_STI) 
  
  0 = (t*t)*(tVel_len)*(tVel_len) - (t*t)*(spd)*(spd) - (t)*2*(S_T_len)*(tVel_len)*(cos_STI) + (S_T_len)*(S_T_len)
  
  0 = (t^2)*((tVel_len)*(tVel_len) - (spd)*(spd)) + (t)*(-2*(S_T_len)*(tVel_len)*(cos_STI)) + (S_T_len)*(S_T_len)
  
  since the expression is now in the form 
  
  y = ax^2 + bx + c = 0
  
  we can use the quadratic formula 
  http://en.wikipedia.org/wiki/Quadratic_formula
  
  [-b +/- sqrt(b^2 - 4*a*c)] / (2*a)
  
  to find when the two paths intersect
  
  to make it easier, isolate a, b, and c from the expression
  
  0 = (t^2)*((tVel_len)*(tVel_len) - (spd)*(spd)) + (t)*(-2*(S_T_len)*(tVel_len)*(cos_STI)) + (S_T_len)*(S_T_len)
  
  a = (tVel_len)*(tVel_len) - (spd)*(spd)
  
  b = -2*(S_T_len)*(tVel_len)*(cos_STI)
  
  c = (S_T_len)*(S_T_len)
  
  */
  
  a = sq(tVel_len) - sq(spd);
  b = -2 * FixedMul(FixedMul(S_T_len, tVel_len), cos_STI);
  c = sq(S_T_len);
  
  t1 = FixedDiv( (-b + FixedSqrt(sq(b) - (4 * FixedMul(a,c)))) , (2 * a) );
  
  t2 = FixedDiv( (-b - FixedSqrt(sq(b) - (4 * FixedMul(a,c)))) , (2 * a) );

  log(s: "t1 = ", f: t1);
  log(s: "t2 = ", f: t2);

  /* in this case only positive values for t can be used, so */

  if(t1 > t2 && t1 > 0){ t = t1; }
  else if (t2 > 0){ t = t2; }
  else{ t = 99.0; }

  log(s: "t = ", f: t);
 
  int tVelX_t = FixedMul(t,tVelX);
  int tVelY_t = FixedMul(t,tVelY);
  int tVelZ_t = FixedMul(t,tVelZ);
  int tXf = tX + tVelX_t;
  int tYf = tY + tVelY_t;
  int tZf = tZ + tVelZ_t;

  int Z_spd = FixedDiv(tZf - sZ, t);
  int X_spd = FixedDiv(tXf - sX, t);
  int Y_spd = FixedDiv(tYf - sY, t);
  
  /* below is only used to have the firing actor be the firer of the projectile
  and allow assigning of a tid to that projectile */
  
  Thing_ProjectileIntercept (stid, 201, 0, ttid, ptid);
  
  SetActorAngle(ptid,VectorAngle(tXf - sX, tYf - sY));
  SetActorVelocity(ptid,X_spd,Y_spd,Z_spd,0,0);
  
  return t;
}