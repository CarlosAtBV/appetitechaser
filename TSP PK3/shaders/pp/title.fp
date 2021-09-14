void main()
{
	vec2 coord = TexCoord;
	vec4 screenTex = texture(InputTexture, coord);
	
	vec2 titleCoord = vec2(TexCoord.s, 1.0-TexCoord.t);
	
	vec4 textTex = texture(texText, titleCoord);
	vec4 textMaskTex = texture(texTextMask, titleCoord);
	
	float textGradX = clamp((textTex.r / 4.) + (1.0 - text_fadeAmount), 0.01, 0.99);
	
	vec4 gradTex = textureLod(texGradient, vec2(textGradX, 0.0), 0);
	
	FragColor = mix(screenTex, vec4(1.0, 1.0, 1.0, 1.0), (gradTex.r * textMaskTex.r));
}