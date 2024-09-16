from ZippedBase64 import encode,pad_bytes_to_str
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
    encoded_data = encode(data)
    MM_Texture(encoded_data, "ZippedBase64", rgba_image.height, id, rgba_image.width)