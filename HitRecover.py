import json
import os
import shutil
Hit = "FlyingTuna_Selyu"
PathToSkin = "C:/Users/dizzy/AppData/Local/osu!/Skins/-                    A_Random skin/"
with open (PathToSkin+ "CurrentSkinDetailsHitSounds.json", "w+", encoding="utf-8") as file:
    json.dump(os.listdir(PathToSkin+"HitSounds/"+Hit), file)

for add_detail in os.listdir(PathToSkin+"HitSounds/"+Hit):
        
    if not(".txt" in add_detail):
        shutil.move(PathToSkin+"HitSounds/"+Hit+"/"+add_detail, PathToSkin)
    elif ('.txt' in add_detail):
        CurrentHitName = add_detail[:-4]
print(CurrentHitName)
