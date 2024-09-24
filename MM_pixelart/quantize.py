6507
from PIL import Image
from pathlib import Path
from tqdm import tqdm
import json, base64
import numpy as np
import zlib
def find_closest_texture(input_texture: bytes) -> int:
    min_diff_index = -1
    min_diff = 256
    for i, compared_texture in enumerate(most_common_textures_list):
        for input_byte, compared_byte in zip(input_texture,compared_texture):
            difference = (input_byte^compared_byte).bit_count()
            if min_diff>difference:
                min_diff_index = i
                min_diff = difference
    return min_diff_index

basepath = Path(__file__).resolve(True).parent
most_common_textures_list: list[bytes] = [None]*256
most_common_textures_dict = {}
with open(basepath/"most_common_textures.json") as jsonfile:
    tmp = json.load(jsonfile)
    for index, (texture, occurance) in enumerate(tmp):
        most_common_textures_list[index] = base64.b64decode(texture)
        most_common_textures_dict[base64.b64decode(texture)] = index
        pass
def main():
    framespath = basepath/"frames"
    with Image.open(framespath/"0.png") as init_image:
        block_amount = (init_image.size[0]//8,init_image.size[1]//8)
    print(block_amount)
    data_array = np.zeros((6507+1,block_amount[1],block_amount[0]),dtype=np.uint8)
    with tqdm(total=6507, desc="Quantizing frames... ") as pbar:
        img_index = -1
        while True:
            img_index+=1
            with Image.open(framespath/f"{img_index}.png") as img:
                img = img.convert("1")
                for x in range(block_amount[0]):
                    for y in range(block_amount[1]):
                        imgblock = img.crop((x*8, y*8, x*8+8, y*8+8))
                        block_bytes = imgblock.tobytes()
                        if block_bytes in most_common_textures_dict:
                            data_array[img_index, y, x] = most_common_textures_dict[block_bytes]
                        else:
                            data_array[img_index, y, x] = find_closest_texture(block_bytes)
            pbar.update()
            if img_index>=6507: break
    compressed_data = zlib.compress(data_array.tobytes())
    with open(basepath/"pixelart_data.bin",mode="wb") as data_file:
        data_file.write(compressed_data)
    print("Done!")
if __name__=="__main__":
    main()