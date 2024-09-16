from pathlib import Path
import json
import base64
import decode_ZippedBase64
if __name__=="__main__":
    filepath = Path(input("file dir: "))
    with filepath.open() as f:
        jf = json.load(f)
        for texture in jf["Texture"]:
            print(base64.b64decode(texture["Data"]))