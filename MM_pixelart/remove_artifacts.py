import json
from pathlib import Path
file_path = Path(input("\nfile path:"))
map_json: dict = {}
with open(file_path,'r') as fr:
    map_json = json.load(fr)
fin_EventObject_list = []
fin_Enemy_list = []
for EventObject in map_json["EventObject"]:
    if EventObject["Type"]==6044: continue
    fin_EventObject_list.append(EventObject)
for Enemy in map_json["Enemy"]:
    if Enemy["Type"]==3068 and Enemy["TemplateID"]=="VB": continue
    fin_Enemy_list.append(Enemy)
map_json["EventObject"] = fin_EventObject_list
map_json["Enemy"] = fin_Enemy_list
with open(file_path,'w') as fw:
    json.dump(map_json,fw,indent=4)