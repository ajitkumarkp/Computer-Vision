import PIL
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import numpy as np

fp= "painting.jpg"

myImage = Image.open(fp).convert("RGB").resize((600,600))

myImage_array = np.array(myImage)

print (myImage_array.shape)

intensity=0.1

##################### Method 1 ##################### 

myImage_list = []

def myText_func(myImage, channel, intensity):
    draw = ImageDraw.Draw(myImage)
    Text = "channel {} intensity {}".format(channel, intensity)
    font = ImageFont.truetype("arial.ttf",size=50)
    #font = ImageFont.truetype("readonly/fanwood-webfont.ttf",size=50)
    draw.text((10,400), Text, font= font)

# channel = 1
# intensity = 0.9
# myImage_array[:,:,channel] = myImage_array[:,:,channel] * intensity
# myImage_mod = Image.fromarray(myImage_array)
# myText_func (myImage_mod, channel, intensity)
# myImage_mod.show()


for channel in range(3):
    for intensity in [0.1, 0.5, 0.9]:
        myImage_array = np.array(myImage)
        myImage_array[:,:,channel] = myImage_array[:,:,channel]*intensity
        myImage_mod = Image.fromarray(myImage_array)
        myText_func(myImage_mod, channel, intensity)
        myImage_list.append(myImage_mod)

Image_1 = myImage_list[0]
sheet =  Image.new(Image_1.mode, (Image_1.width*3, Image_1.height*3+(60*3)))

x,y = 0,0
for img in myImage_list:
    sheet.paste(img,(x,y))
    x+=img.width
    if x==sheet.width:
        x=0
        y+=img.height+60
sheet.show()

##################### Method 2 ##################### 
# x, y = 0, 0
# offset = 60

# sheet =  Image.new(myImage.mode, (myImage.width*3, myImage.height*3+(offset*3)))

# def putText(sheet, channel, intensity, x, y):
#     draw = ImageDraw.Draw(sheet)
#     Text = "channel {} intensity {}".format(channel, intensity)
#     font = ImageFont.truetype("arial.ttf",size=50)
#     #font = ImageFont.truetype("readonly/fanwood-webfont.ttf",size=50)
#     draw.text((x+10,y+460), Text, font= font)

# for channel in range(3):
#     intensity = 0.1
#     for i in range(3):
#         myImage_array = np.array(myImage)
#         myImage_array[:,:,channel] = myImage_array[:,:,channel]*intensity
#         myImage_mod = Image.fromarray(myImage_array)

#         sheet.paste(myImage_mod,(x,y))
#         putText(sheet, channel, intensity, x, y)

#         x+=myImage.width
#         if x==sheet.width:
#             x=0
#             y+=myImage.height+offset
#         intensity += 0.4

# sheet.show()

##################### Submitted below ##################### 
# import PIL
# from PIL import Image
# from PIL import ImageDraw
# from PIL import ImageFont
# import numpy as np
# from IPython.display import display

# fp= "readonly/msi_recruitment.gif"

# myImage = Image.open(fp).convert("RGB")
# myImage_array = np.array(myImage)
# intensity=0.1

# x, y = 0, 0
# offset = 60

# sheet =  Image.new(myImage.mode, (myImage.width*3, myImage.height*3+(offset*3)))

# def putText(sheet, channel, intensity, x, y):
#     draw = ImageDraw.Draw(sheet)
#     Text = "channel {} intensity {}".format(channel, intensity)
#     font = ImageFont.truetype("readonly/fanwood-webfont.ttf",size=50)
#     draw.text((x+10,y+460), Text, font= font)

# for channel in range(3):
#     intensity = 0.1
#     for i in range(3):
#         myImage_array = np.array(myImage)
#         myImage_array[:,:,channel] = myImage_array[:,:,channel]*intensity
#         myImage_mod = Image.fromarray(myImage_array)

#         sheet.paste(myImage_mod,(x,y))
#         putText(sheet, channel, intensity, x, y)

#         x+=myImage.width
#         if x==sheet.width:
#             x=0
#             y+=myImage.height+offset
#         intensity += 0.4
        
# display(sheet)









