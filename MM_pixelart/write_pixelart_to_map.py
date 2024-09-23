from pathlib import Path
import json
import base64
import zlib
import numpy as np
from PIL import Image
basepath = Path(__file__).resolve(True).parent
framespath = basepath/"frames"
with Image.open(framespath/"0.png") as init_image:
    block_amount = (init_image.size[0]//8,init_image.size[1]//8)
with open(basepath/"pixelart_data.bin","br") as compressed_data_file:
    decompressed_data = zlib.decompress(compressed_data_file.read())
    data_array = np.reshape(np.frombuffer(decompressed_data,np.uint8),(6507,block_amount[1],block_amount[0]))
for frame in data_array:
    for y in block_amount[1]:
        for x in block_amount[0]:
            pass
    pass