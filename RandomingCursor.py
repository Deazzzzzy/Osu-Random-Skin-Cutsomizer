import os
import json
import shutil
def RanSkinCursor(Curs, Path):
    Name = ""
    #Перенос старых значений курсора обратно в директорию с названием скина откуда взят
    with open (Path+"/CurrentSkinDetailsCursors.json", "r+", encoding="utf-8") as file:
        data = json.load(file)
        for i in data:
            if ".txt" in i:
                data.remove(i)
                Name = i[:-4]
        

    for detail in data:
        shutil.move(Path+'/'+detail, Path+"/Cursors/"+Name)

    with open (Path+"/CurrentSkinDetailsCursors.json", "w+", encoding="utf-8") as file:
        json.dump(os.listdir(Path+"/Cursors/"+Curs), file)

    for add_detail in os.listdir(Path+"/Cursors/"+Curs):
        if not(".txt" in add_detail):
            shutil.move(Path+"/Cursors/"+Curs+"/"+add_detail, Path)
        elif (".txt" in add_detail):
            pass


        

    
            
    

    
    
    
    
    
    
