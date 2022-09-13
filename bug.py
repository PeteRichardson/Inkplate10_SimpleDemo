# https://inkplate.readthedocs.io/en/stable/micropython.html

from inkplate10 import Inkplate
display = Inkplate(Inkplate.INKPLATE_2BIT)
display.begin()
display.clearDisplay()
display.setRotation(3)
display.setTextSize(8)
print("started drawing image file")
#display.printText(100,100,"Pete Rules!")
display.drawImageFile(0, 0, "sd/bug.bmp")
print("finished drawing image file")
display.display()