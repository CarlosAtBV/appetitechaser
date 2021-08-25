mat3 GetTBN()
{
    vec3 n = normalize(vWorldNormal.xyz);
    vec3 p = pixelpos.xyz;
    vec2 uv = vTexCoord.st;

    // get edge vectors of the pixel triangle
    vec3 dp1 = dFdx(p);
    vec3 dp2 = dFdy(p);
    vec2 duv1 = dFdx(uv);
    vec2 duv2 = dFdy(uv);

    // solve the linear system
    vec3 dp2perp = cross(n, dp2); // cross(dp2, n);
    vec3 dp1perp = cross(dp1, n); // cross(n, dp1);
    vec3 t = dp2perp * duv1.x + dp1perp * duv2.x;
    vec3 b = dp2perp * duv1.y + dp1perp * duv2.y;

    // construct a scale-invariant frame
    float invmax = inversesqrt(max(dot(t,t), dot(b,b)));
    return mat3(t * invmax, b * invmax, n);
}

vec2 ParallaxMap(mat3 tbn, float dist)
{
	ivec2 texSize = textureSize(tex, 0);
	float newDist = dist / texSize.x;
	
    mat3 invTBN = transpose(tbn);
    vec3 V = normalize(invTBN * (uCameraPos.xyz - pixelpos.xyz));

    vec2 texCoords = vTexCoord.st;
    vec2 p = V.xy / abs(V.z) * newDist;// * parallaxScale;
    return texCoords - p;
}

vec4 Process(vec4 color)
{
    mat3 tbn = GetTBN();
	
	vec3 balls = vec3(0,0,0);
	
	for ( int i = 32; i > 0; i-- )
	{
		vec2 texCoord = ParallaxMap(tbn, i);
		vec4 colorFinal = getTexel(texCoord);
		
		float getAmt = (balls.r + balls.g + balls.b) / 3.;
		balls = mix(balls, colorFinal.rgb, (1.0 - getAmt) * 0.25);
	}
	
	return vec4(balls, 1.0);
}