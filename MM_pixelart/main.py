from texture import MM_Texture
from create_texture import encode_texture
from read_texture import decode_texture
from PIL import Image, ImageDraw
img = Image.new("RGBA",(8,8),(0,0,0,0xff))
d = ImageDraw.Draw(img)
d.rectangle((0,0,3,3),(0xff,0xff,0xff,0xff))
img.show()