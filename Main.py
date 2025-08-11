from RandomingCursor import RanSkinCursor
from RandomingHitSound import RanHitSounds
from RandomingMenuOverlay import RanMenuOverlay
import json
import os
import random
from time import sleep

# Цвета для терминала
BRIGHT_MAGENTA = '\033[95m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
RED = '\033[31m'
BRIGHT_MAGENTA = '\033[95m'
RESET = '\033[0m'
If_True = GREEN+"On"+RESET
If_False = RED+"Off"+RESET
# Важные настройки
with open('Settings.json', 'r') as JS:
    SETTINGS = json.load(JS)
    PathToSkin = SETTINGS['PathToSkin']
if SETTINGS['Delay']:
    sleep(0.5) 
print(BRIGHT_MAGENTA+"""                               ###                                       ###        ##
                                ##                                        ##
 ######    ####    #####        ##    ####    ##  ##             #####    ##  ##   ###     #####
  ##  ##      ##   ##  ##    #####   ##  ##   #######           ##        ## ##     ##     ##  ##
  ##       #####   ##  ##   ##  ##   ##  ##   ## # ##            #####    ####      ##     ##  ##
  ##      ##  ##   ##  ##   ##  ##   ##  ##   ##   ##                ##   ## ##     ##     ##  ##
 ####      #####   ##  ##    ######   ####    ##   ##           ######    ##  ##   ####    ##  ##
"""+RESET)
if SETTINGS['Delay']:
    sleep(0.5)
choice = -1
with open('Settings.json', 'r') as JS:
    SETTINGS = json.load(JS)
    PathToSkin = SETTINGS['PathToSkin']
if PathToSkin == None:
        print(GREEN+"Введите путь до скина"+RESET)
        print(GREEN+"Пример: C:/Users/dizzy/AppData/Local/osu!/Skins/-                    A_Random skin/"+RESET)
        PathToSkin = input("> ")
        SETTINGS['PathToSkin'] = PathToSkin
        with open('Settings.json', 'w') as JS:
            json.dump(SETTINGS, JS)
if SETTINGS["ShowName"]:
    SHOWNAME = If_True
else:
    SHOWNAME = If_False
if SETTINGS['Delay']:
    Delay = If_True
else:
    Delay = If_False
def UpdateSettings():
    global SETTINGS
    global SHOWNAME
    global Delay
    with open('Settings.json', 'r') as JS:
       SETTINGS = json.load(JS)
    if SETTINGS["ShowName"]:
        SHOWNAME = If_True
    else:
        SHOWNAME = If_False
    if not(SETTINGS['Delay']):
        Delay = If_True
    else:
        Delay = If_False
cur_list = os.listdir(PathToSkin+"/Cursors")
hit_list = os.listdir(PathToSkin+"/HitSounds")
menu_list = os.listdir(PathToSkin+"/MenuOverlays")
        

    
# Основная функция которая отвечает за самое первое разветвление
def MainChoice():
    print()
    print("Какую часть скина вы хотите изменить?")
    print("1: Скин целиком")
    print("2: Курсор")
    print("3: Хитсаунды")
    print("4: Меню оверлей")
    print('0: Настройки')
    choice = int(input("> "))
    match(choice):
        case 1:
            AllChoice()
        case 2:
            CursorChoice()
        case 3:
            HitSoundsChoice()
        case 4:
            MenuChoice()
        case 0:
            settings()
        case _:
            print(RED+'Неверный ввод'+RESET)
            if SETTINGS['Delay']:
                sleep(0.5)
            MainChoice()
#Настройки

def settings():
    UpdateSettings()
    print(f'[1] Выводить название : {SHOWNAME}')
    print(f'[2] Убрать задержку : {Delay}')
    print(f'[3] Изменить путь до скина')
    print("[0] Назад")
    settings_choice = int(input("> "))
    match (settings_choice):
        case 1 :
            SETTINGS['ShowName'] = not(SETTINGS['ShowName'])
            with open ("Settings.json", 'w') as JS:
                json.dump(SETTINGS, JS)
                JS.close()
            settings()
            
        case 2:
            SETTINGS['Delay'] = not(SETTINGS['Delay'])
            with open ("Settings.json", 'w') as JS:
                json.dump(SETTINGS, JS)
                JS.close()
            settings()
        case 3:
            print(YELLOW+'Вы уверены что хотите изменить путь до папки со скином?'+RESET)
            print("[1] ДА")
            print("[0] Назад")
            
            agreement = int(input("> "))
            match(agreement):
                case 1:
                    print(YELLOW+"Введите новый путь до скина"+RESET)
                    PathToSkin = input("> ")
                    if "\\" in PathToSkin:
                        PathToSkin = PathToSkin.replace("\\", "/")
                    SETTINGS['PathToSkin'] = PathToSkin
                    with open ('Settings.json', 'w') as JS:
                        json.dump(SETTINGS, JS)
                case 0:
                    settings()              
        case 0:
            MainChoice()
        case _:
            settings()
#БЛОК СО СКИНОМ В ЦЕЛОМ        
def AllChoice():
        print()
        print("Выберите один из вариантов:")
        print("1: Ручной выбор")
        print("2: Рандом цельный скин")
        print("3: Рандом каждая часть из разных скинов")
        print("0: Назад")
        cur_choice = int(input("> "))
        match(cur_choice):
            case 1:
                ManualAll()
            case 2:
                RandomAllSolid()
            case 3:
                RandomAllInParts()
            case 0:
                MainChoice()
                
#Ручной выбор скина           
def ManualAll():
    print()
    print("Выберите нужный скин:")
    for i in hit_list:
        print(f'[{hit_list.index(i)+1}] {i}')
    print("[0] Назад")
    choice = int(input("> "))
    if choice == 0:
        AllChoice()
    else:
        RanHitSounds(hit_list[choice-1], PathToSkin)
        RanSkinCursor(hit_list[choice-1], PathToSkin)
        RanMenuOverlay(hit_list[choice-1], PathToSkin)
        
        print(GREEN+"СКИН УСПЕШНО ОБНОВЛЕН"+RESET)
        if (SETTINGS['ShowName']):
            print(hit_list[choice-1])
        print()
        if SETTINGS['Delay']:
            sleep(0.5)
        ManualAll()
       
#Рандомизация цельного скина 
def RandomAllSolid():
    print()
    print("Выберите нужную опцию:")
    print("1: Цикличный рандом")
    print("2: Одноразовый рандом")
    print("0: Назад")
    all_random_choice = int(input("> "))
    match(all_random_choice):
        case 1:
            count = 0
            print("Выберите время интервала между итерациями:")
            print("[1] 10 секунд (рекомендованно)")
            print("[2] 30 секунд ")
            print("[3] 1 минута")
            print("[4] Своё значение")
            print("[0] Назад")
            time_choise = int(input("> "))
            match (time_choise):
                case 1:
                    seconds = 10
                case 2:
                    seconds = 30
                case 3:
                    seconds = 60
                case 4:
                    print("Укажите своё значение времени (в секундах):")
                    seconds = int(input('> '))
                case 0:
                    RandomAllSolid()
            
            print("Для остановки нажмите Ctrl + C")
            while True:
                try:
                    all_ran = random.choice(cur_list)
                    RanSkinCursor(all_ran, PathToSkin)
                    RanHitSounds(all_ran, PathToSkin)
                    RanMenuOverlay(all_ran, PathToSkin)
                    if (SETTINGS['ShowName']):
                        print(all_ran)
                    count+=1
                    if count == 5:
                        print("Для остановки нажмите Ctrl + C")
                    sleep(seconds)
                    
                except KeyboardInterrupt:
                    MainChoice()
                    break  
        case 2:
            all_ran = random.choice(cur_list)
            RanSkinCursor(all_ran, PathToSkin)
            RanHitSounds(all_ran, PathToSkin)
            RanMenuOverlay(all_ran, PathToSkin)
            print(GREEN+f"СКИН УСПЕШНО ОБНОВЛЕН"+RESET)
            if (SETTINGS['ShowName']):
                print(all_ran)
            print()
            if SETTINGS['Delay']:
                sleep(0.5)
            RandomAllSolid()
        case 0:
            AllChoice() 


#Рандомизация скина по частям
def RandomAllInParts():
    print()
    print("Выберите нужную опцию:")
    print("1: Цикличный рандом")
    print("2: Одноразовый рандом")
    print("0: Назад")
    all_random_choice = int(input("> "))
    match(all_random_choice):
        case 1:
            count = 0
            print("Выберите время интервала между итерациями:")
            print("[1] 10 секунд (рекомендованно)")
            print("[2] 30 секунд ")
            print("[3] 1 минута")
            print("[4] Своё значение")
            print('[0] Назад')
            time_choise = int(input("> "))
            if time_choise == 0:
                RandomAllInParts()
            else:
                match (time_choise):
                    case 1:
                        seconds = 10
                    case 2:
                        seconds = 30
                    case 3:
                        seconds = 60
                    case 4:
                        print("Укажите своё значение времени (в секундах):")
                        seconds = int(input('> '))
                    case 0: 
                        RandomAllInParts
                
                print("Для остановки нажмите Ctrl + C")
                while True:
                    try:
                        all_ran1 = random.choice(cur_list)
                        all_ran2 = random.choice(cur_list)
                        all_ran3 = random.choice(cur_list)
                        RanSkinCursor(all_ran1,PathToSkin)
                        RanHitSounds(all_ran2,PathToSkin)
                        RanMenuOverlay(all_ran3,PathToSkin)
                        if (SETTINGS['ShowName']):
                            print(f'Курсор - {all_ran1}')
                            print(f'Хитсаунды - {all_ran2}')
                            print(f'Меню - {all_ran3}')
                        count+=1
                        if count == 5:
                            print("Для остановки нажмите Ctrl + C")
                        sleep(seconds)
                        
                    except KeyboardInterrupt:
                        MainChoice()
                        break  
        case 2:
            all_ran1 = random.choice(cur_list)
            all_ran2 = random.choice(cur_list)
            all_ran3 = random.choice(cur_list)
            RanSkinCursor(all_ran1,PathToSkin)
            RanHitSounds(all_ran2,PathToSkin)
            RanMenuOverlay(all_ran3,PathToSkin)
            print(GREEN+f"СКИН УСПЕШНО ОБНОВЛЕН"+RESET)
            if (SETTINGS['ShowName']):
                print(f'Курсор - {all_ran1}')
                print(f'Хитсаунды - {all_ran2}')
                print(f'Меню - {all_ran3}')
            print()
            if SETTINGS['Delay']:
                sleep(0.5)
            RandomAllInParts()
        case 0:
            AllChoice() 
            
            
#БЛОК С КУРСОРАМИ
def CursorChoice():
        print()
        print("Выберите один из вариантов:")
        print("1: Ручной выбор")
        print("2: Рандом")
        print("0: Назад")
        cur_choice = int(input("> "))
        match(cur_choice):
            case 1:
                ManualCursor()
            case 2:
                RandomCursorChosen()
            case 0:
                MainChoice()
#Ручной выбор курсора
def ManualCursor():
    print()
    print("Выберите нужный вариант:")
    for i in cur_list:
        print(f'[{cur_list.index(i)+1}] {i}')
    print("[0] Назад")
    choice = int(input("> "))
    if choice == 0:
        CursorChoice()
    else:
                    
        RanSkinCursor(cur_list[choice-1],PathToSkin)
        print(GREEN+"КУРСОР УСПЕШНО ОБНОВЛЕН"+RESET)
        if (SETTINGS['ShowName']):
            print(cur_list[choice-1])
        print()
        if SETTINGS['Delay']:
            sleep(0.5)
        ManualCursor()
                
#Рандомизация курсора
def RandomCursorChosen():
    print()
    print("Выберите нужную опцию:")
    print("1: Цикличный рандом")
    print("2: Одноразовый рандом")
    print("0: Назад")
    skin_random_choice = int(input("> "))
    match(skin_random_choice):
        case 1:
            count = 0
            print("Выберите время интервала между итерациями:")
            print("[1] 10 секунд (рекомендованно)")
            print("[2] 30 секунд ")
            print("[3] 1 минута")
            print("[4] Своё значение")
            time_choise = int(input("> "))
            match (time_choise):
                case 1:
                    seconds = 10
                case 2:
                    seconds = 30
                case 3:
                    seconds = 60
                case 4:
                    print("Укажите своё значение времени (в секундах):")
                    seconds = int(input('> '))
            
            print("Для остановки нажмите Ctrl + C")
            while True:
                try:
                    cur_ran = random.choice(cur_list)
                    RanSkinCursor(cur_ran,PathToSkin)
                    if (SETTINGS['ShowName']):
                        print(cur_ran)
                    count+=1
                    if count == 5:
                        print("Для остановки нажмите Ctrl + C")
                    sleep(seconds)
                    
                except KeyboardInterrupt:
                    MainChoice()
                    break
                                
        case 2:
            cur_ran = random.choice(cur_list)
            RanSkinCursor(cur_ran,PathToSkin)
            print(GREEN+"КУРСОР УСПЕШНО ОБНОВЛЕН"+RESET)
            if (SETTINGS['ShowName']):
                print(cur_ran)
            print()
            if SETTINGS['Delay']:
                sleep(0.5)
            RandomCursorChosen()
        case 0:
            CursorChoice()
          
                 
#БЛОК С ХИТСАУНДАМИ   
def HitSoundsChoice():
        print()
        print("Выберите один из вариантов:")
        print("1: Ручной выбор")
        print("2: Рандом")
        print("0: Назад")
        hit_choice = int(input("> "))
        match(hit_choice):
            case 1:
                ManualHitSounds()
            case 2:      
                RandomHitSChosen()
                        
            case 0:
                MainChoice()
            case _:
                pass
#Ручной выбор хитсаундов
def ManualHitSounds():
    print()
    print("Выберите нужный вариант:")
    for i in hit_list:
        print(f'[{hit_list.index(i)+1}] {i}')
    print("[0] Назад")
    choice = int(input("> "))
    if choice == 0:
        HitSoundsChoice()
    else:
        RanHitSounds(hit_list[choice-1],PathToSkin)
        print(GREEN+"ХИТСАУНДЫ УСПЕШНО ОБНОВЛЕНЫ"+RESET)
        if (SETTINGS['ShowName']):
            print(hit_list[choice-1])
        print()
        if SETTINGS['Delay']:
            sleep(0.5)
        ManualHitSounds()
#Рандомизация хитсаундов   
def RandomHitSChosen():
    print()
    print("Выберите нужную опцию:")
    print("1: Цикличный рандом")
    print("2: Одноразовый рандом")
    print("0: Назад")
    hit_random_choice = int(input("> "))
    match(hit_random_choice):
        case 1:
            print("Выберите время интервала между итерациями:")
            print("[1] 10 секунд (рекомендованно)")
            print("[2] 30 секунд ")
            print("[3] 1 минута")
            print("[4] Своё значение")
            time_choise = int(input("> "))
            match (time_choise):
                case 1:
                    seconds = 10
                case 2:
                    seconds = 30
                case 3:
                    seconds = 60
                case 4:
                    print("Укажите своё значение времени (в секундах):")
                    seconds = int(input('> '))
            
            print("Для остановки нажмите Ctrl + C")
            while True:
                try:
                    hit_ran = random.choice(hit_list)
                    RanHitSounds(hit_ran,PathToSkin)
                    if (SETTINGS['ShowName']):
                        print(hit_ran)
                    sleep(seconds)
                    print("Для остановки нажмите Ctrl + C")
                except KeyboardInterrupt:
                    MainChoice()
                    break
        case 2:
            hit_ran = random.choice(hit_list)
            RanHitSounds(hit_ran,PathToSkin)
            print(GREEN+"ХИТСАУНДЫ УСПЕШНО ОБНОВЛЕНЫ"+RESET)
            if (SETTINGS['ShowName']):
                print(hit_ran)
            print()
            if SETTINGS['Delay']:
                sleep(0.5)
            RandomHitSChosen()
        case 0:
            HitSoundsChoice()
def MenuChoice():
        print()
        print("Выберите один из вариантов:")
        print("1: Ручной выбор")
        print("2: Рандом")
        print("0: Назад")
        menu_choice = int(input("> "))
        match(menu_choice):
            case 1:
                ManualMenu()
            case 2:      
                RandomMenuChosen()       
            case 0:
                MainChoice()
            case _:
                pass
def ManualMenu():
    print()
    print("Выберите нужный вариант:")
    for i in hit_list:
        print(f'[{menu_list.index(i)+1}] {i}')
    print("[0] Назад")
    choice = int(input("> "))
    if choice == 0:
        MenuChoice()
    else:
        RanMenuOverlay(menu_list[choice-1],PathToSkin)
        print(GREEN+"МЕНЮ УСПЕШНО ОБНОВЛЕНО"+RESET)
        if (SETTINGS['ShowName']):
            print(menu_list[choice-1])
        print()
        if SETTINGS['Delay']:
            sleep(0.5)
        ManualMenu()    
def RandomMenuChosen():
    print()
    print("Выберите нужную опцию:")
    print("1: Цикличный рандом")
    print("2: Одноразовый рандом")
    print("0: Назад")
    menu_random_choice = int(input("> "))
    match(menu_random_choice):
        case 1:
            print("Выберите время интервала между итерациями:")
            print("[1] 10 секунд (рекомендованно)")
            print("[2] 30 секунд ")
            print("[3] 1 минута")
            print("[4] Своё значение")
            time_choise = int(input("> "))
            match (time_choise):
                case 1:
                    seconds = 10
                case 2:
                    seconds = 30
                case 3:
                    seconds = 60
                case 4:
                    print("Укажите своё значение времени (в секундах):")
                    seconds = int(input('> '))
            
            print("Для остановки нажмите Ctrl + C")
            while True:
                try:
                    menu_ran = random.choice(menu_list)
                    RanMenuOverlay(menu_ran,PathToSkin)
                    if (SETTINGS['ShowName']):
                        print(menu_ran)
                    sleep(seconds)
                    print("Для остановки нажмите Ctrl + C")
                except KeyboardInterrupt:
                    MainChoice()
                    break
        case 2:
            menu_ran = random.choice(menu_list)
            RanMenuOverlay(menu_ran,PathToSkin)
            print(GREEN+"МЕНЮ УСПЕШНО ОБНОВЛЕНО"+RESET)
            if (SETTINGS['ShowName']):
                print(menu_ran)
            print()
            if SETTINGS['Delay']:
                sleep(0.5)
            RandomMenuChosen()
        case 0:
            MenuChoice()
  
 
MainChoice()

        
# RandomingHitSound.RanHitSounds("FlyingTuna_Selyu") тут забейте, это самые первые строчки кода, не хочу удалять, воспоминания как никак
# RandomingCursor.RanSkinCursor("whiteCat")