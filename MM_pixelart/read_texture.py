from ZippedBase64 import decode,pad_bytes_to_str
from PIL import Image
from texture import MM_Texture


def decode_texture(texture: MM_Texture) -> Image.Image:
    decoded_data = decode(texture.Data)
    image: Image.Image = Image.frombytes("RGBA",(texture.Width,texture.Height),decoded_data)
    image = image.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
    # MM uses RGBA flipped top_bottom, keep in mind when encoding texture
    return image

if __name__=="__main__":
    import json
    from pathlib import Path
    filepath = Path(input("file dir: "))
    with filepath.open() as f:
        jf = json.load(f)
        for texture in jf["Texture"]:
            image = decode_texture(MM_Texture(**texture))
            if texture["ID"]=="num":
                image.show(texture["ID"])