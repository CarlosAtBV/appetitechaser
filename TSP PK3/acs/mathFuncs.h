function int arcsin(int x)
{
  return VectorAngle(FixedSqrt(1.0 - FixedMul(x,x)), x);
}

function int arccos(int x)
{
  return VectorAngle(x, FixedSqrt(1.0 - FixedMul(x,x)));
}

function int arctan(int x)
{
  return VectorAngle(1.0, x);
}

function int sq(int x)
{
  return FixedMul(x, x);
}

function int t_ang(int x)
{
  return abs(x % 0.5);
}

function int FixedAngMod(int fAngle)
{
  if (fAngle > 1.0){
    fAngle %= 65536; }
  else if (fAngle < 0){
    fAngle %= (-65536);
    fAngle = fAngle + 65536;}
  return fAngle;
}