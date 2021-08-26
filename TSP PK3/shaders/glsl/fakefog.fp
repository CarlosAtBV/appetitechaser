float easeOutCirc ( float newInput )
{
	//if ( newInput > 1.0 ) return 1.0;
	
	//return sqrt(1 - pow(newInput - 1, 2));
	if ( newInput >= 1.0 )
	{
		return 1.0;
	}
	
	return 1 - pow(2, -10 * newInput);
}

void SetupMaterial( inout Material mat )
{
	float doMix1 = easeOutCirc(distance(pixelpos.xyz, uCameraPos.xyz) / 16768.);
	float doMix2 = easeOutCirc(distance(pixelpos.xyz, uCameraPos.xyz) / 32768.);
	//vec4 fogColor = vec4(0.902, 0.102, 0.267, 1.0);
	vec4 fogColor = vec4(0.357, 0.078, 0.149, 1.0);
	vec4 baseColor = getTexel(vTexCoord.st);
	
	vec4 altColor = mix(baseColor, mix(vec4(0.0, 0.0, 0.0, 1.0), fogColor, baseColor.r), doMix1);
	
	mat.Base = mix(altColor, fogColor, clamp(doMix2, 0.0, 1.0));
}

vec4 ProcessLight( Material mat, vec4 color )
{
	return vec4(1.0, 1.0, 1.0, 1.0);
}