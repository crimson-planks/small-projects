from pathlib import Path
import json
import base64
import zlib
import numpy as np
from PIL import Image
from texture import MM_AnimatedPixelArt, NamedTuple_to_dict
from tqdm import tqdm
basepath = Path(__file__).resolve(True).parent
framespath = basepath/"frames"

def main(file_path):
    with Image.open(framespath/"0.png") as init_image:
        block_amount = (init_image.size[0]//8,init_image.size[1]//8)
    with open(basepath/"pixelart_data.bin","br") as compressed_data_file:
        decompressed_data = zlib.decompress(compressed_data_file.read())
        data_array = np.reshape(np.frombuffer(decompressed_data,np.uint8),(6507+1,block_amount[1],block_amount[0]))

    EventObject_list: list[dict]=[None]*(block_amount[0]*block_amount[1])
    with tqdm(desc="converting pixelart data to AnimatedPixelArt format",total=block_amount[0]*block_amount[1]) as pbar:
        for y in range(block_amount[1]):
            for x in range(block_amount[0]):
                PixelArtID_csv = ','.join(hex(n)[2:] for n in data_array[:,y,x])
                EventObject_list[y*block_amount[0]+x] = NamedTuple_to_dict(MM_AnimatedPixelArt(0, 4, 2, True, PixelArtID_csv, 1, 8.0 + 8*x, 8.0 + 8*y))
                pbar.update()


    map_json: dict = {}
    with open(file_path,'r') as fr:
        map_json = json.load(fr)
    fin_EventObject_list = []
    for EventObject in map_json["EventObject"]:
        if EventObject["Type"]!=6044:
            fin_EventObject_list.append(EventObject) #remove all AnimatedPixelArt

    fin_EventObject_list.extend(EventObject_list)
    map_json["EventObject"] = fin_EventObject_list

    with open(file_path,'w') as fw:
        json.dump(map_json,fw,indent=4)
if __name__=="__main__":
    main(Path(input("file path: ")))