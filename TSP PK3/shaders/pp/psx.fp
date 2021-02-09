void main()
{
	vec2 coord = TexCoord;
	
	vec4 screenTex = texture(InputTexture, coord);
	vec2 res = textureSize(InputTexture, 0) / 2;
	
	float fadeLevel = (1.0 + fadeAmount * 2);
	
	ivec2 texSize = textureSize(loadingText, 0);
	vec2 texCoord = coord * vec2(res.x / (res.y * 1.333), 1.0);// * (res / texSize);
	texCoord.y *= -1;
	
	vec4 texColor = textureLod(loadingText, texCoord, 0);
	
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
