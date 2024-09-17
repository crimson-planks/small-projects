from PIL import Image
from pathlib import Path
import json
from texture import MM_Texture
test_image = Image.open(Path(__file__).resolve(True).parent / "num.png")
test_MM_Texture = MM_Texture(**json.load((Path(__file__).resolve(True).parent / "num.json").open()))

def test_same_image(img1: Image.Image, img2: Image.Image)->bool:
    return img1.convert("RGBA").tobytes()==img2.convert("RGBA").tobytes()
def test_read_texture():
    import read_texture
    from texture import MM_Texture
    assert test_same_image(read_texture.decode_texture(test_MM_Texture),test_image)
    print("read_texture pass!")

def test_create_texture():
    import create_texture
    from texture import MM_Texture
    created_MM_Texture = create_texture.encode_texture(test_image,"num")
    for index, key in enumerate(test_MM_Texture._fields):
        try:
            assert test_MM_Texture[index] == created_MM_Texture[index]
        except AssertionError:
            print(test_MM_Texture[index])
            print(created_MM_Texture[index])
            assert False
    print("create_texture pass!")
def main_test():
    test_read_texture()
    test_create_texture()
    print("all unit tests pass!")
if __name__=='__main__':
    main_test()