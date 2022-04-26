uniform float timer;

vec4 Process(vec4 color)
{
	const float pi = 3.14;
	
	float newTimer = timer * 8;
	newTimer = floor(newTimer);
	newTimer /= 8;
	
	const float TEXSIZE = 128.0;
	const float SPEED = 0.25;//0.25;
	
	vec2 texUV = floor(vTexCoord.st*TEXSIZE) / TEXSIZE;
	
	vec2 baseUV = vec2(0,0);
	baseUV.x = (texUV.y + newTimer * SPEED);
	baseUV.y = (texUV.x + newTimer * SPEED);
	
	vec2 waves = sin(pi * 3.0 * baseUV) * 0.05;
	waves.y += -newTimer / 4;
	
	vec2 rippleUV = texUV.st + waves;
	
    vec2 p = floor(pixelpos.xz) / 512;
	p.x += newTimer / 30;
	p.y += newTimer / 30;
	p *= 512;
	p = floor(p);
	p /= 512;
	
	vec4 colorClouds = texture(texClouds, p);
	
	vec4 colorRipples = mix(texture(texRipples2, rippleUV), texture(texRipples, rippleUV), colorClouds.r);
	
	vec4 colorRamp = texelFetch(texRamp, ivec2(int((colorRipples.r) * textureSize(texRamp, 0).x), 0), 0);
	
	return colorRamp;
}