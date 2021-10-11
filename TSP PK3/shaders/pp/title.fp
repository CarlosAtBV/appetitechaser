void main()
{
	vec2 coord = TexCoord;
	vec4 screenTex = mix(vec4(0.0, 0.0, 0.0, 0.0), texture(InputTexture, coord), bg_fadeAmount);
	
	vec2 titleCoord = vec2(TexCoord.s, 1.0-TexCoord.t);
	
	vec4 textTex = texture(texText, titleCoord);
	vec4 textbgTex = texture(texTextBG, titleCoord);
	vec4 textMaskTex = texture(texTextMask, titleCoord);
	vec4 textbgMaskTex = texture(texTextBGMask, titleCoord);
	
	float textGradX = clamp((textTex.r / 3.) + (1.0 - text_fadeAmount), 0.01, 0.99);
	float textBGGradX = clamp((textbgTex.r / 3.) + (1.0 - textbg_fadeAmount), 0.01, 0.99);
	
	vec4 gradTex = textureLod(texGradient, vec2(textGradX, 0.0), 0);
	vec4 gradBGTex = textureLod(texGradient, vec2(textBGGradX, 0.0), 0);
	
	vec4 logoTex = mix(screenTex, vec4(0.18, 0.69, 0.54, 1.0), (gradBGTex.r * textbgMaskTex.r));
	logoTex = mix(logoTex, vec4(0.96, 0.96, 0.96, 1.0), (gradTex.r * textMaskTex.r));
	
	FragColor = logoTex;
}