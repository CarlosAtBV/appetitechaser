uniform float timer;

vec4 Process(vec4 color)
{
	vec2 moveUV = (vTexCoord.st*4) + vec2(0, -timer*6);
	vec4 realTex = getTexel(vTexCoord.st);
	vec4 maskTex = texture(tex_mask, moveUV);
	
	return vec4(realTex.rgb, maskTex.r);
}