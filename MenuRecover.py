import json
import os
import shutil
Menu = "Gura_"
PathToSkin = "C:/Users/dizzy/AppData/Local/osu!/Skins/-                    A_Random skin/"
with open (PathToSkin+"CurrentMenuOverlayDetails.json", "w+", encoding="utf-8") as file:
    json.dump(os.listdir(PathToSkin+"MenuOverlays/"+Menu), file)

for add_detail in os.listdir(PathToSkin+"MenuOverlays/"+Menu):
    
    if not(".txt" in add_detail):
        shutil.move(PathToSkin+"MenuOverlays/"+Menu+"/"+add_detail, PathToSkin)
    elif (".txt" in add_detail):
        CurrentHitName = add_detail[:-4]
print(CurrentHitName)