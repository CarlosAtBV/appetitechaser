uniform float timer;

vec4 Process(vec4 color)
{
	ivec2 texSize = textureSize(tex, 0);
	vec2 texCoord = gl_TexCoord[0].st;
	
	float lineAmount = floor(texCoord.t * texSize.t) + timer * 16;
	float alsoLineAmount = floor(texCoord.t * texSize.t) + timer * 63;
	
	float bigAlpha = max(0.0, (mod(-alsoLineAmount, 64) / 32.) - 1.0);
	
	float getAlpha = 0.5 + (mod(lineAmount, 2) / 2);
	
	vec4 tex1Color = texture(tex, texCoord);
	
	return vec4(tex1Color.rgb, tex1Color.a * min(bigAlpha + getAlpha, 1.0));
}