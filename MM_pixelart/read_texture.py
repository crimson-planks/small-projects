import ZippedBase64
from PIL import Image
from texture import MM_Texture


def decode_texture(texture: MM_Texture) -> Image.Image:
    decoded_data = ZippedBase64.decode(texture.Data)
    image: Image.Image = Image.frombytes("RGBA",(texture.Width,texture.Height),decoded_data)
    image = image.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
    # MM uses RGBA flipped top_bottom, keep in mind when encoding texture
    return image

def main():
    import json
    from pathlib import Path
    filepath = Path(input("file path: "))
    with filepath.open() as f:
        jf = json.load(f)
        for texture in jf["Texture"]:
            image = decode_texture(MM_Texture(**texture))
            if texture["ID"]=="windowslogo":
                image.save(r"MM_pixelart/windowslogo.png")

if __name__=="__main__":
    main()