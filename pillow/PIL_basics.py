## This example shows-
# - Useful funcs
# - resize image
# - control brightness of image
# - draw rectangle on an image
# - How write text and change its font size on an image
# - creating a new work sheet where other images can be composed
# - diff Image filters

import PIL
import inspect

from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance
from PIL import ImageDraw, ImageFont

img_ob = Image.open("msi_recruitment.gif")

## Useful funcs
## Methods supported by the class object
# print ("------------> Dir:", dir(img_ob))

# ## what type of data it holds 
# print ("------------> Type", type(img_ob))

# ## help func
# print ("------------> HELP:", help(img_ob.rotate))

# ## getmro() returns a tuple of base classes inherited from 
# print ("------------> inspect:", inspect.getmro(type(img_ob)))

img_rgb = img_ob.convert("RGB").resize(size=(900,450))

# Image enhancements types from ImageEnhance.py 
enh_ob = ImageEnhance.Brightness(img_rgb)
# enh_ob = ImageEnhance.Contrast(img_rgb)
# enh_ob = ImageEnhance.Color(img_rgb)
# enh_ob = ImageEnhance.Sharpness(img_rgb)

enh_images = []

for i in range(1,10):
    enh_images.append(enh_ob.enhance(i/10))

sheet = PIL.Image.new("RGB", (img_rgb.width, img_rgb.height))

draw_ob = ImageDraw.Draw(sheet)
# the Draw() in ln332 in ImageDraw.py returns an instance of ImageDraw class.
# This instance has access to all methods in this class eg: rectangle(), line() etc

myfont = ImageFont.truetype("arial.ttf",size=15)

x,y=0,0
i=1
for img in enh_images:
    box_w = int(img.width/3) 
    box_h = int(img.height/3)
    resized = img.resize(size=(box_w, box_h))
    sheet.paste(resized, box=(x,y))

    draw_ob.rectangle((x,y, x+box_w, y+box_h), fill=None, outline="red")

    brightness = "Brightness Level is:{}%".format(i*10)
    draw_ob.text((x+100,y+100),brightness, font=myfont )
    i+=1
    x+=box_w
    if x == int(img.width):
        x=0
        y+=box_h
sheet.show()


##Image Filters

# img_rgb.filter(ImageFilter.BLUR).show()
# img_rgb.filter(ImageFilter.CONTOUR).show()
# img_rgb.filter(ImageFilter.DETAIL).show()
# img_rgb.filter(ImageFilter.EMBOSS).show()


## Croping ROI
img_rgb.crop((50,0,190,150)).show() 




