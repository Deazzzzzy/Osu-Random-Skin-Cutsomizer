import os
import json
import shutil
import random
def RanMenuOverlay(Menu, Path):
    Name = ""
    



    #Перенос старых значений обратно в директорию с названием скина откуда взят
    with open (Path+'/'+"CurrentMenuOverlayDetails.json", "r+", encoding="utf-8") as file:
        data = json.load(file)
        for i in data:
            if ".txt" in i:
                data.remove(i)
                Name = i[:-4]
        

    for detail in data:
        shutil.move(Path+'/'+detail, Path+"/MenuOverlays/"+Name)
    # занесение новых значений в скин
    with open (Path+"/CurrentMenuOverlayDetails.json", "w+", encoding="utf-8") as file:
        json.dump(os.listdir(Path+"/MenuOverlays/"+Menu), file)

    for add_detail in os.listdir("C:/Users/dizzy/AppData/Local/osu!/Skins/-                    A_Random skin/MenuOverlays/"+Menu):
        if not(".txt" in add_detail):
            shutil.move(Path+"/MenuOverlays/"+Menu+"/"+add_detail, Path)
        elif (".txt" in add_detail):
            pass

        

    
            
    

    
    
    
    
    
    
