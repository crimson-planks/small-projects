import ZippedBase64
from PIL import Image
from texture import MM_Texture


def encode_texture(image: Image.Image, id: str) -> MM_Texture:
    if image.width % 8 !=0:
        raise RuntimeError("width must be multiple of 8")
    if image.height % 8 !=0:
        raise RuntimeError("height must be multiple of 8")
    rgba_image = image.convert("RGBA")
    rgba_image = rgba_image.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
    data = rgba_image.tobytes()
    encoded_data = ZippedBase64.encode(data).decode("ascii") #base64 is a subset of ascii
    return MM_Texture(encoded_data, "ZippedBase64", rgba_image.height, id, rgba_image.width)

def main():
    from pathlib import Path
    imgpath = Path(input("image path: "))
    with Image.open(imgpath) as image:
        print(encode_texture(image,"cheese"))
if __name__=="__main__":
    main()