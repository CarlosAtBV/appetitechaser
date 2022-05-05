uniform float timer;

vec4 Process(vec4 color)
{
	const float pi = 3.14;
	
	float newTimer = timer * 12.5;
	newTimer = floor(newTimer);
	newTimer /= 12.5;
	
	const float TEXSIZE = 128.0;
	const float SPEED = 0.5;
	
	vec2 texUV = floor(vTexCoord.st*TEXSIZE) / TEXSIZE;
	
	vec2 baseUV = vec2(0,0);
	baseUV.x = (texUV.y + newTimer * SPEED);
	baseUV.y = (texUV.x + newTimer * SPEED);
	
	vec2 waves = sin(pi * 1.5 * baseUV) * 0.05;
	waves.y += -newTimer / 4;
	vec2 rippleUV = texUV.st + vec2(0, -newTimer);
	
	waves = sin(pi * 2.0 * baseUV) * 0.01;
	vec2 rippleUVUnder = texUV.st + waves;
	
    vec2 p = floor(pixelpos.xz) / 256;
	p.x += newTimer / 8;
	p.y += newTimer / 8;
	p *= 256;
	p = floor(p);
	p /= 256;
	
	//vec4 colorClouds = texture(texClouds, p);
	
	vec4 colorRipples = texture(texRipples, rippleUV);
	vec4 colorDarkBits = texture(texClouds, p);
	vec4 colorDarkWaves = texture(texRipples2, rippleUV);
	//vec4 colorCombined = mix(colorDarkBits/2, vec4(1.0,1.0,1.0,1.0), colorRipples.r);
	vec4 colorCombined = mix(colorDarkWaves, colorRipples, 0.5 + min(colorDarkBits.r, 0.5));
	
	float rampX = clamp(colorCombined.r, 0.01, 0.99);
	vec4 colorRamp = texelFetch(texRamp, ivec2(int(rampX * textureSize(texRamp, 0).x), 0), 0);
	vec4 finalColor = mix(texture(texUnder, rippleUVUnder), colorRamp, max(0.5 + colorCombined.r, 0.5));
	
	return finalColor;
}