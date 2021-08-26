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

HardwareShader Texture "CYBAB"
{
	Shader "shaders/glsl/fakemirror.fp"
	Texture "toReflect" "textures/mirrortest_2.png"
	Texture "refMask" "textures/dex/CYBG.png"
}

HardwareShader Texture "CYBF00"
{
	Shader "shaders/glsl/fakefog.fp"
}
HardwareShader Texture "CYBF01"
{
	Shader "shaders/glsl/fakefog.fp"
}
HardwareShader Texture "CYBF02"
{
	Shader "shaders/glsl/fakefog.fp"
}
HardwareShader Texture "CYBF03"
{
	Shader "shaders/glsl/fakefog.fp"
}
HardwareShader Texture "CYBF04"
{
	Shader "shaders/glsl/fakefog.fp"
}
HardwareShader Texture "CYBF05"
{
	Shader "shaders/glsl/fakefog.fp"
}
HardwareShader Texture "CYBF06"
{
	Shader "shaders/glsl/fakefog.fp"
}
HardwareShader Texture "CYBF07"
{
	Shader "shaders/glsl/fakefog.fp"
}

HardwareShader Sprite "131XA0"
{
	Shader "shaders/glsl/scopescan.fp"
}