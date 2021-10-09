#py
from PIL import Image

f = Image.open("Sir.png")

# temp = f.read()
# for i in f:
    # print(i)
temp = f
# Get the size of the image
width, height = f.size

# Process every pixel
for x in range(width):
   for y in range(height):
       current_color = f.getpixel( (x,y) )
       # print(current_color,end = " | ")
       
       if (sum(current_color)//3)>180:
           f.putpixel( (x,y),(255,255,255) )
       else:
           f.putpixel( (x,y),(0,0,0) )
           
       # if (sum(current_color)//3) in range(100,200):
           # f.putpixel( (x,y),(255,0,70) )
           
   # print()
f.save("ola.png")

"""
Next step creating a NxN Grid of images with different shading and Color combo's!
"""