from PIL import Image
img1 = Image.open("crimson_planks.png")
img2 = Image.open("acacia_planks.png")
img2 = img2.convert("RGBA")
print(img1.mode,img2.mode)
new_image = Image.new("RGBA",(16,16))
for y in range(0,16):
    for x in range(0,16):
        print(img2.getpixel((x,y)))
        if ((x+y)%2)==0:
            new_image.putpixel((x,y), img1.getpixel((x,y)))
        else:
            new_image.putpixel((x,y), img2.getpixel((x,y)))
new_image.save("checkerplanks.png")