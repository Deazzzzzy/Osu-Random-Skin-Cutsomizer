import json
import os
import shutil
PathToSkin = "C:/Users/dizzy/AppData/Local/osu!/Skins/-                    A_Random skin/"
Curs="WhiteCat"
with open (PathToSkin+"CurrentSkinDetailsCursors.json", "w+", encoding="utf-8") as file:
    json.dump(os.listdir(PathToSkin+"Cursors/"+Curs), file)

for add_detail in os.listdir("C:/Users/dizzy/AppData/Local/osu!/Skins/-                    A_Random skin/Cursors/"+Curs):
    if not(".txt" in add_detail):
        shutil.move(PathToSkin+"Cursors/"+Curs+"/"+add_detail, PathToSkin)
    elif (".txt" in add_detail):
        CurrentName = add_detail[:-4]
        print(CurrentName)