# Simple image display on Inkplate 10


1. Pick a greyscale image with lots of detail.  I find that line drawings of insects look impressive on eink displays.   For example, see https://collections.nmnh.si.edu/search/ento/
1. (optional?) resize the image to 1200x825 

1. Use imagemagick to convert your image to a 4 shades of gray bmp file.

> ```brew install imagemagick```
> ```convert bug.jpg -dither FloydSteinberg -define dither:diffusion-amount=85% -remap eink-4gray.png BMP3:bug.bmp```

Note the -remap option, which remaps colors from the original to the colors in eink-4gray.png (courtesy of adafruit.com)

3. Save the bmp file onto a microSD card and load it into the Inkplate 10.
1. Open  and execute the bug.py file in your favorite micropython IDE (I use Thonny [https://thonny.org]

Note that this image takes minutes(!) to load.

#### Relevant Links
* Purchase Inkplate: https://inkplate.io
* Inkplate docs including API reference: https://inkplate.readthedocs.io/en/latest/index.html 
* Preparing graphics for eink displays: https://learn.adafruit.com/preparing-graphics-for-e-ink-displays
