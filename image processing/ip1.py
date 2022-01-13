import PIL
from PIL import Image, ImageFilter, ImageFont, ImageDraw
  
# Location of the image
img = Image.open("/home/marija/OpenCV/data/squirrel.jpg")
#img = img.rotate(90, PIL.Image.NEAREST, expand = 1)
#img = img.transpose(method=Image.FLIP_TOP_BOTTOM)
#img = img.transpose(method=Image.FLIP_LEFT_RIGHT)
#img = img.resize((300,300))
#r, g, b, = img.split()
#r.show()
#g.show()
#b.show()
#img = Image.merge('RGB', (g, b, r))
#width, height = img.size
#left = 120 
#top = 100 
#right = 360
#bottom = 360
#img = img.crop((120, 100, 360, 360))
#img = img.filter(ImageFilter.BLUR)
#img = img.filter(ImageFilter.GaussianBlur(8))

font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSansOblique.ttf", 35)
draw = ImageDraw.Draw(img)
draw.text((100, 70), "THIS IS SQUIRREL", font = font, fill=(0, 0, 255))


img.save("/home/marija/OpenCV/data/crop.jpg")
img.show()

print(img.size)
print(img.format)
print(img.mode)

