uniform float timer;

vec4 Process(vec4 color)
{
	vec2 texScanSize = textureSize(texScanline, 0);
	vec2 scanlinePos = mod(gl_FragCoord.st, texScanSize);
	//scanlinePos = ;mod(scanlinePos, texScanSize) / texScanSize;
	
	float scanlineReal = mod(gl_FragCoord.t - timer * 16, 64) / 64;//, 8);
	
	vec4 baseColor = texture( tex, vTexCoord.st );
	vec4 scanColor = texelFetch( texScanline, ivec2(scanlinePos), 0 );
	baseColor.rgb = baseColor.rgb * mix(1.0, 1.0+scanlineReal/4, 1.0-scanColor.a);
	//baseColor.rgb += scanlineReal * (scanColor.a/8);
	vec4 borderColor = texture( texBorder, vTexCoord.st );
	
	return mix(baseColor, borderColor, borderColor.a);//mix(tex1, tex2, maskColor.r);
	//return vec4(pixelpos.xyz, 1.0);//mix(tex1, tex2, .r);// mask);
}