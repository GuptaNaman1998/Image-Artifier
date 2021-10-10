#py
from PIL import Image

def create(black,white,color,name):
    # f = Image.open("img.jpg")
    f = Image.open("iv.png")
    width, height = f.size
    # Process every pixel
    for x in range(width):
       for y in range(height):
           current_color = f.getpixel( (x,y) )
           if (sum(current_color)//3)>128:
               f.putpixel( (x,y),black )
           else:
               f.putpixel( (x,y),white )
           if (sum(current_color)//3) in range(100,220):
               f.putpixel( (x,y),color )
    f.save(name)

# f = Image.open("img.jpg")
# temp = f

black = (0,0,0)
white = (225,255,255)

color = (255,195,105)
name = input()
create(black,white,color,name)

color = (238,83,55)
name = input()
create(black,white,color,name)

color = (191,245,48)
name = input()
create(black,white,color,name)

color = (58,255,255)
name = input()
create(black,white,color,name)

"""
Next step creating a NxN Grid of images with different shading and Color combo's!
"""