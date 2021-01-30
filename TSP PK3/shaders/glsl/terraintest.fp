uniform float timer;

vec4 Process(vec4 color)
{
	ivec2 texSize = textureSize(mixTex1, 0);
	vec2 texCoord1 = gl_TexCoord[0].st;
	vec2 texCoord2 = pixelpos.xz / texSize;
	
	vec4 maskColor = (getTexel(texCoord1) * color);
	//vec4 tex1Color = texture(color, texCoord);
	vec4 tex1Color = texture(mixTex1, texCoord2);
	vec4 tex2Color = texture(mixTex2, texCoord2);
	
	return mix(tex1Color, tex2Color, maskColor.r);//mix(tex1, tex2, maskColor.r);
	//return vec4(pixelpos.xyz, 1.0);//mix(tex1, tex2, .r);// mask);
}