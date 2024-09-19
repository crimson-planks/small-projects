from texture import MM_Texture
from create_texture import encode_texture
from read_texture import decode_texture
from PIL import Image, ImageDraw
def yield_binary(size: int):
    rslt=[0]*size
    yield rslt.copy()
    while True:
        rslt[0]+=1
        i=0
        while rslt[i]==2:
            if i>=size-1:
                return
            rslt[i]=0
            rslt[i+1]+=1
            i+=1
        yield rslt.copy()
print(list(yield_binary(4)))
def imgify_bin(points) -> Image.Image:
    pointdata=[]
    for p in points:
        pointdata.extend([p*255,p*255,p*255,0xff])
    img = Image.frombytes("RGBA",(2,2),bytes(pointdata))
    img=img.resize((8,8),Image.Resampling.NEAREST)
    return img
for i, b in enumerate(yield_binary(4)):
    texture = encode_texture(imgify_bin(b),hex(i)[2:])
    print()
MM_Texture()._fields