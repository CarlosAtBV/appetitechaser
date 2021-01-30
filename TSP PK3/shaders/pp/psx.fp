vec3 tsp_saturation(vec3 color, float amount)
{
    // Algorithm from Chapter 16 of OpenGL Shading Language
    const vec3 W = vec3(0.2125, 0.7154, 0.0721);
    vec3 intensity = vec3(dot(color, W));
    return mix(intensity, color, amount);
}

void main()
{
	vec2 coord = TexCoord;
	vec4 screenTex = texture(InputTexture, coord);
	
	vec4 blacken = vec4(0.0,0.0,0.0,1.0);
	vec4 saturated = screenTex;
	saturated.r *= 1.0 + fadeAmount * 1.25;
	saturated.g *= 1.0 + fadeAmount * 2;
	
	vec4 fadeMoment = mix(saturated, blacken, fadeAmount);

	FragColor = mix(screenTex, fadeMoment, fadeAmount);
}
