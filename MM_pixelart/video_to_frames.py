import cv2, pathlib
from tqdm import tqdm
import numpy as np
from PIL import Image
import PIL._imaging
from collections import Counter
import json
import base64
print()
def dict_base64ify(d: dict):
    rslt = {}
    for key in d:
        rslt[base64.b64encode(key).decode("ascii")]=d[key]
    return rslt
def tuple_to_dict(l: list[list[str|int]]) -> dict[str, int]:
    rslt = {}
    for s, i in l:
        rslt[s]=i
    return rslt
def tuple_base64ify(l: list[tuple[bytes, int]])-> list[list[str|int]]:
    return [(base64.b64encode(key).decode("ascii"),count) for key,count in l]
pixelart_dimensions = (26*2-1,16*2) #the pixelarts are aligned weirdly
pixel_dimensions = (pixelart_dimensions[0]*8,pixelart_dimensions[1]*8)
#print(pixel_dimensions[0]/pixel_dimensions[1])
basepath = pathlib.Path(__file__).resolve(True).parent
videopath = basepath / "Bad Apple!!.webm"
outpath = basepath / "frames"
#print(str(videopath))
video_capture = cv2.VideoCapture(str(videopath))
#print(video_capture.getBackendName())
index=-1
video_dimensions = None
resized_video_dimensions = None
aligned_pixelart_dimensions = None
aligned_video_dimensions = None
perfect = None
texture_counter = Counter()
with tqdm(total=6507, desc="Processing frames... ") as pbar:
    while True:
        index+=1
        ret, frame = video_capture.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        #print(frame.shape)
        #frame = cv2.cvtColor(frame,cv.COLOR_)
        #cv2.imshow('frame',frame)
        
        img: Image.Image = Image.fromarray(frame, "RGB")
        img = img.crop((1,2,img.size[0]-1, img.size[1]-2)) #Bad Apple has a very thin border around the rectangle
        if index==150: img.show()
        if video_dimensions==None: video_dimensions = img.size
        if resized_video_dimensions==None:
            if pixel_dimensions[0]/pixel_dimensions[1] > video_dimensions[0]/video_dimensions[1]:
                resized_video_dimensions = (int(video_dimensions[0]*pixel_dimensions[1]/video_dimensions[1]),
                                            pixel_dimensions[1])
            else:
                resized_video_dimensions = (pixel_dimensions[0],
                                            int(video_dimensions[1]*pixel_dimensions[0]/video_dimensions[0]))
            if resized_video_dimensions[0]%8==0 and resized_video_dimensions[1]%8==0:
                perfect = True
            else: perfect = False
            aligned_pixelart_dimensions = (int(np.ceil(resized_video_dimensions[0]/8)),
                                           int(np.ceil(resized_video_dimensions[1]/8)))
            aligned_video_dimensions = (int(np.ceil(resized_video_dimensions[0]/8))*8,
                                        int(np.ceil(resized_video_dimensions[1]/8))*8)
        img = img.resize(resized_video_dimensions)
        img = img.convert("1")
        finimg: Image.Image
        if not perfect:
            finimg = Image.new('1',aligned_video_dimensions)
            finimg.paste(img)
        else:
            finimg = img.copy()
        for x in range(aligned_pixelart_dimensions[0]):
            for y in range(aligned_pixelart_dimensions[1]):
                imgblock = finimg.crop((x*8, y*8, x*8+8, y*8 +8))
                #print(imgblock.size)
                texture_counter.update((imgblock.tobytes(),))
                #print(imgblock.tobytes())
        finimg.save(outpath/(str(index)+".png"))
        pbar.update(1)
        #if index>=150: break
        if index>=6507: break
json.dump(tuple_base64ify(texture_counter.most_common(256)),(basepath/"most_common_textures.json").open("w"))
#json.dump(dict_base64ify(texture_counter),(basepath/"textures.json").open("w"))
video_capture.release()
cv2.destroyAllWindows()
print("Done!")