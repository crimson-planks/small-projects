import json
from pathlib import Path
file_path = Path(input("\nfile path:"))
map_json: dict = {}
with open(file_path,'r') as fr:
    map_json = json.load(fr)
fin_EventObject_list = []
for EventObject in map_json["EventObject"]:
    if EventObject["Type"]!=6044:
        fin_EventObject_list.append(EventObject)
map_json["EventObject"] = fin_EventObject_list
with open(file_path,'w') as fw:
    json.dump(map_json,fw,indent=4)