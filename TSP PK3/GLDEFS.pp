HardwareShader PostProcess Screen
{
	Name "TSP_PSXFade"
	Shader "shaders/pp/psx.fp" 330
	Texture "loadingText" "LOADING"
	Uniform float fadeAmount
	Enabled
}

HardwareShader Texture "graphics/menu/common/header_top_green.png"
{
	Shader "shaders/glsl/menuscan.fp"
	Texture "texScanline" "graphics/menu/common/scanlines.png"
	Texture "texBorder" "graphics/menu/common/header_top.png"
}

HardwareShader Texture "graphics/menu/common/border/border_bg_green.png"
{
	Shader "shaders/glsl/menuscan.fp"
	Texture "texScanline" "graphics/menu/common/scanlines.png"
	Texture "texBorder" "graphics/menu/common/border/border.png"
}

HardwareShader Texture "graphics/menu/common/border/border_bg_green.png"
{
	Shader "shaders/glsl/menuscan.fp"
	Texture "texScanline" "graphics/menu/common/scanlines.png"
	Texture "texBorder" "graphics/menu/common/border/border.png"
}

HardwareShader Texture "textures/mirrortest.png"
{
	Shader "shaders/glsl/fakemirror.fp"
}

HardwareShader Sprite "131XA0"
{
	Shader "shaders/glsl/scopescan.fp"
}