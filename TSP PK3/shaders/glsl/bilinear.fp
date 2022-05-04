vec4 doBilinear(sampler2D getTex, vec2 uv)
{
    vec2 getSize = textureSize(getTex, 0);
	
	vec2 getPos = uv * getSize - 0.5;
    vec2 getFract = fract(getPos);
    
    vec2 startPos = floor(getPos);
    
    vec4 topLeft = texture(getTex, (startPos + vec2(0.5, 0.5)) / getSize, -100.0);
    vec4 topRight = texture(getTex, (startPos + vec2(1.5, 0.5)) / getSize, -100.0);
	
    vec4 bottomLeft = texture(getTex, (startPos + vec2(0.5, 1.5)) / getSize, -100.0);
    vec4 bottomRight = texture(getTex, (startPos + vec2(1.5, 1.5)) / getSize, -100.0);
    
    vec4 color = mix(mix(topLeft,topRight,getFract.x), mix(bottomLeft,bottomRight,getFract.x), getFract.y);
    return color;
}

vec4 Process(vec4 color)
{
	return doBilinear(tex, vTexCoord.st);
}