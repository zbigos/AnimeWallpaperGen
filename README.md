# AnimeWallpaperGen
Python script for automatic generation of anime-themed wallpapers

Converts a image with simple background to a wallpaper with specified resolution.  
It uses opencv's border feature, so make sure that every edge of your input image is the background.  

# Usage  
  python3 generator.py if=source.jpg of=destination -vhfF  
*  if - Specify what image you want to convert  
*  of - Specify where the image will be saved  
*  V - Instead placing the source image on the bottom, it will be placed on top  
*  H - Instead placing the source image on the right, it will be placed on the left  
*  f - Flip the image by a vertical axis  
*  F - Flip the image by a horizontal axis

# Examples
  
Input image:  
<img src="https://github.com/zbigos/AnimeWallpaperGen/blob/master/example/test.jpg" width="200" height="200">

| x | Image snapped to left (-H) | Image snapped to right |
| ------------- | ------------- | ------------- |
| **No horizontal flip** | <img src="https://github.com/zbigos/AnimeWallpaperGen/blob/master/example/Harg.jpg" width="288" height="162"> | <img src="https://github.com/zbigos/AnimeWallpaperGen/blob/master/example/default.jpg" width="288" height="162"> |
| **horizontal flip**  (-F) | <img src="https://github.com/zbigos/AnimeWallpaperGen/blob/master/example/Harg_flipped.jpg" width="288" height="162"> | <img src="https://github.com/zbigos/AnimeWallpaperGen/blob/master/example/flipped.jpg" width="288" height="162"> |


TODO:  
  -Ability to rescale the input image in relation to the wallpaper size  
  -Ability to run filters (such as constraining the color space of image)  
  -Better interface than changing code in .py files  
More sensible interface is on the way

Image used in the examples has been stolen from
https://safebooru.org/index.php?page=post&s=view&id=2961643




Please remember that we live in a society.
