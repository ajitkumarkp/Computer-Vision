import PIL

from PIL import Image, ImageDraw, ImageFont

# img_rgb = Image.open("painting.jpg").convert("RGB")
# img_rgb.show()
img_rgb = Image.open("painting.jpg").convert("RGB").resize((200, 200))

img_rgb_list=[]

intensity=0.1 
   
def myText_func(myImage, channel, intensity):
    draw = ImageDraw.Draw(myImage)
    Text = "channel {} intensity {}".format(channel, intensity)
    font = ImageFont.truetype("arial.ttf",size=15)
    #font = ImageFont.truetype("readonly/fanwood-webfont.ttf",size=50)
    draw.text((10,150), Text, font= font)

def small_img (channel, intensity):
    # global img_rgb, img_rgb_list
    img_rgb_copy= img_rgb.copy()
    for x in range (img_rgb.width):
        for y in range (img_rgb.height):
            r,g,b = img_rgb.getpixel((x,y))
            if channel == "red":
                img_rgb_copy.putpixel((x,y), (int(r*intensity), g, b))
            if channel == "green":
                img_rgb_copy.putpixel((x,y), (r, int(g*intensity), b))
            if channel == "blue":
                img_rgb_copy.putpixel((x,y), (r, g, int(b*intensity)))
    
    myText_func(img_rgb_copy, channel, intensity)
    img_rgb_list.append(img_rgb_copy)
    
for channel in ["red", "green", "blue"]:
    for intensity in [0.1,0.5,0.9]:
        small_img(channel, intensity)

sheet = Image.new("RGB", (600,600))

x,y=0,0
for img in img_rgb_list:
    sheet.paste(img,box=(x,y))
    x+=200
    if x==600:
        x=0
        y+=200

sheet.show()


