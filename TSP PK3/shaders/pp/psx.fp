void main()
{
	vec2 coord = TexCoord;
	
	vec4 screenTex = texture(InputTexture, coord);
	vec2 res = textureSize(InputTexture, 0) / 2;
	
	float fadeLevel = (1.0 + fadeAmount * 2);
	
	ivec2 texSize = textureSize(loadingText, 0);
	vec2 texCoord = coord * vec2(res.x / (res.y * 1.333), 1.0);// * (res / texSize);
	texCoord.y *= -1;
	texCoord.y += 1.0;
	ivec2 texiCoord = ivec2(int(texCoord.x * 320), int(texCoord.y * 240));
	
	vec4 texColor = vec4(texelFetch(loadingText, texiCoord, 0).rgb, 1.0);
	
	vec4 fadedOut = ((screenTex - 0.5) * fadeLevel) + 0.5;
	
	if ( fadeAmount == 1.0 )
	{
		FragColor = texColor;
	}
	else
	{
		FragColor = mix(fadedOut, vec4(0.0,0.0,0.0,1.0), fadeAmount);
	}
}
