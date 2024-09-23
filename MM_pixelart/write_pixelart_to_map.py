from pathlib import Path
import json
import base64
import zlib
import numpy as np
from PIL import Image
from texture import MM_AnimatedPixelArt
basepath = Path(__file__).resolve(True).parent
framespath = basepath/"frames"
with Image.open(framespath/"0.png") as init_image:
    block_amount = (init_image.size[0]//8,init_image.size[1]//8)
with open(basepath/"pixelart_data.bin","br") as compressed_data_file:
    decompressed_data = zlib.decompress(compressed_data_file.read())
    data_array = np.reshape(np.frombuffer(decompressed_data,np.uint8),(6507,block_amount[1],block_amount[0]))
data_array.shape
for y in range(block_amount[1]):
    for x in range(block_amount[0]):
        PixelArtID_csv = ','.join(hex(n)[2:] for n in data_array[0:100,y,x])
        print()
        MM_AnimatedPixelArt(4, 2, PixelArtID_csv, 1)