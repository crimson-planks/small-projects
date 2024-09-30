from fractions import Fraction
from pathlib import Path
import json
import zlib
import numpy as np
from PIL import Image
from texture import MM_CustomEnemy, NamedTuple_to_dict
from tqdm import tqdm
basepath = Path(__file__).resolve(True).parent
framespath = basepath/"frames"

def main(file_path):
    with Image.open(framespath/"0.png") as init_image:
        block_amount = (init_image.size[0]//8,init_image.size[1]//8)
    with open(basepath/"pixelart_data.bin","br") as compressed_data_file:
        decompressed_data = zlib.decompress(compressed_data_file.read())
        data_array = np.reshape(np.frombuffer(decompressed_data,np.uint8),(6507+1,block_amount[1],block_amount[0]))

    CustomEnemy_list : list[dict] = [None]*(block_amount[0]*block_amount[1])
    with tqdm(desc="converting pixelart data to CustomEnemy format",total=block_amount[0]*block_amount[1]) as pbar:
        for y in range(block_amount[1]):
            for x in range(block_amount[0]):
                PixelArtID_csv = ','.join(hex(n)[2:] for n in data_array[0:150,y,x])
                CustomEnemy_list[y*block_amount[0]+x] = NamedTuple_to_dict(MM_CustomEnemy(PixelArtID_csv, "VB", 8.0 + 8*x, 8.0 + 8*y))
                pbar.update()

    map_json: dict = {}
    with open(file_path,'r') as fr:
        map_json = json.load(fr)
    fin_Enemy_list = []
    for Enemy in map_json["Enemy"]:
        if Enemy["Type"]==3068 and Enemy["TemplateID"]=="VB": continue
        fin_Enemy_list.append(Enemy)
    fin_Enemy_list.extend(CustomEnemy_list)
    map_json["Enemy"] = fin_Enemy_list
    with open(file_path,'w') as fw:
        json.dump(map_json,fw,indent=4)
if __name__=="__main__":
    main(Path(input("file path: ")))


CE_template = {
    "AbleToFlip" : False,
    "Behavior" : 3,
    "BehaviorPreset" : 0,
    "FlyAngle" : 180.0,
    "FlySpeed" : 1.0,
    "FlyStyle" : 1,
    "ID" : "VB",
    "WingPosition" : 2
} #VB stands for Video Block





#1: 0.100
#2: 0.366
#3: 0.633
#4: 0.900
#speed 1: block / 0.266s
#speed 1: 3.75 blocks / s
#0.66
#0.200
#internal speed * (15/4) = speed in blocks/second