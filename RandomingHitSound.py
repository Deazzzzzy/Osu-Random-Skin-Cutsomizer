import os
import json
import shutil
#Перенос старых значений хитсаундов обратно в директорию с названием скина откуда были взяты
def RanHitSounds(Hit, Path):
    Name = ""
    with open (Path+'/'+"CurrentSkinDetailsHitSounds.json", "r+", encoding="utf-8") as file:
        data = json.load(file)
        for i in data:
            if ".txt" in i:
                data.remove(i)
                Name = i[:-4]
        

    for detail in data:
        shutil.move(Path+'/'+detail, Path +"/HitSounds/"+Name)

    with open (Path+'/'+ "CurrentSkinDetailsHitSounds.json", "w+", encoding="utf-8") as file:
        json.dump(os.listdir(Path+"/HitSounds/"+Hit), file)

    for add_detail in os.listdir(Path+"/HitSounds/"+Hit):
        
        if not(".txt" in add_detail):
            shutil.move(Path+"/HitSounds/"+Hit+"/"+add_detail, Path)
        else:
            pass
    
    

    
            
    

    
    
    
    
    
    
