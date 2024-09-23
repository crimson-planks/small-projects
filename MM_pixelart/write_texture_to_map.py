from create_texture import encode_texture
from texture import MM_PixelArt, MM_Texture, NamedTuple_to_dict
from pathlib import Path
from PIL import Image
import json
import base64
basepath = Path(__file__).resolve(True).parent

texture_list: list[dict] = [None]*256
with open(basepath/"most_common_textures.json","r") as mct_file:
    for index, (b64_texture, occurance) in enumerate(json.load(mct_file)):
        decoded_texture = base64.b64decode(b64_texture)
        texture_image = Image.frombytes("1",(8,8),decoded_texture)
        texture_list[index] = NamedTuple_to_dict(encode_texture(texture_image, hex(index)[2:]))
        pass

with open(basepath/"used_textures.json","w") as texture_file:
    json.dump(texture_list,texture_file,indent=4)
filepath = Path(input("file path: "))
mapjson={}
with filepath.open("r") as fr:
    mapjson = json.load(fr)
    mapjson["Texture"]=texture_list
with filepath.open("w") as fw:
    json.dump(mapjson,fw,indent=4)