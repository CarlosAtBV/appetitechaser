void main()
{
	vec4 screenTex = texture(InputTexture, TexCoord);
	
	float gray = dot(screenTex.rgb, vec3(0.299, 0.587, 0.114));
	vec4 muted = texture(rampTex, vec2(clamp(gray,0.01,0.99), 0.5));
	
	FragColor = mix(screenTex, muted, fadeAmount);
}
