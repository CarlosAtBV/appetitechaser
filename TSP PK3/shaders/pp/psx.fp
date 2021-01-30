vec3 tsp_saturation(vec3 color, float amount)
{
    // Algorithm from Chapter 16 of OpenGL Shading Language
    const vec3 W = vec3(0.2125, 0.7154, 0.0721);
    vec3 intensity = vec3(dot(color, W));
    return mix(intensity, color, amount);
}

void main()
{
	/*vec2 coord = TexCoord;
	vec4 screenTex = texture(InputTexture, coord);
	
	vec4 blacken = vec4(0.0,0.0,0.0,1.0);
	vec4 saturated = screenTex;
	saturated.r *= 1.0 + fadeAmount * 1.25;
	saturated.g *= 1.0 + fadeAmount * 2;
	
	vec4 fadeMoment = mix((screenTex-0.5)*2, blacken, max(0.0, (fadeAmount-0.5)*2));*/

	vec2 baseSize = textureSize(InputTexture,0);
	vec2 coord = TexCoord;
	vec2 scan = coord * baseSize;
	
	vec4 screenTex = texture(InputTexture, coord);
	vec4 blacken = vec4(0.0,0.0,0.0,1.0);
	
	FragColor = mix(blacken, screenTex, mod(scan.y, 4));//vec4(1, 1, mod(scan.y, 4), 1);
}
