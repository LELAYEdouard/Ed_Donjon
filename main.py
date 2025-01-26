#libriary
import os
import time
from msvcrt import getch

#files
from const import *
from var import *
from graphic_func import *
from function import create_map,isCollision
from obj_class import *
from Player_class import *
from Room_class import *

#game
os.system('cls' if os.name == 'nt' else 'clear')

map=create_map(LENGTH_MAP)
i,j=0,0

print("    ______    __                           __   _                  __                                 ")
print("   / ____/___/ /___  __  ______ __________/ /  ( )  _____     ____/ /___  ____  ____ ____  ____  ____ ")
print("  / __/ / __  / __ \/ / / / __ `/ ___/ __  /   |/  / ___/    / __  / __ \/ __ \/ __ `/ _ \/ __ \/ __ \ ")
print(" / /___/ /_/ / /_/ / /_/ / /_/ / /  / /_/ /       (__  )    / /_/ / /_/ / / / / /_/ /  __/ /_/ / / / /")
print("/_____/\__,_/\____/\__,_/\__,_/_/   \__,_/       /____/     \__,_/\____/_/ /_/\__, /\___/\____/_/ /_/ ")
print("                                                                             /____/                   ")

player=Player(input("Enter your name:\n"),PLAYER)
logs=Logs()
os.system('cls' if os.name == 'nt' else 'clear')
print_ui(map[i][j],player,logs)


while(key!=QUIT):
    
    gotoxy(0,0)
    key = getch().decode('utf-8')

    if(key==INTERACT and (isCollision(player_co,DOWN,map[i][j]) or isCollision(player_co,UP,map[i][j]) or isCollision(player_co,LEFT,map[i][j]) or isCollision(player_co,RIGHT,map[i][j]))):
        chest_interact(player_co,map[i][j])
        chest_print=True

    if(chest_print and key!=INTERACT):
        for k in range(MAX_CHEST_INV):
            if(key == str(k+1)):
                logs.add_log(player.add_item(map[i][j].inv[0].take_item(k)))
                print_ui(map[i][j],player,logs)
                

    player.move(player_co,key,map[i][j])    
    if(chest_print and key!=INTERACT and not(isCollision(player_co,DOWN,map[i][j]) or isCollision(player_co,UP,map[i][j]) or isCollision(player_co,LEFT,map[i][j]) or isCollision(player_co,RIGHT,map[i][j]))):
        chest_erase()
        chest_print=False
    
    
    

    if(player_co[0]==WIDTH and ((HEIGHT-2)//3)<player_co[1]<(((HEIGHT-2)//3)*2)+2 and map[i][j].right):
        j+=1
        os.system('cls' if os.name == 'nt' else 'clear')
        player_co[0]-=WIDTH-2
        collision=False
        logs.add_log(player.add_xp(10))
        print_ui(map[i][j],player,logs)
        
    if(player_co[0]==1 and ((HEIGHT-2)//3)<player_co[1]<(((HEIGHT-2)//3)*2)+2 and map[i][j].left):
        j-=1
        os.system('cls' if os.name == 'nt' else 'clear')
        player_co[0]+=WIDTH-2
        collision=False
        logs.add_log(player.add_xp(10))
        print_ui(map[i][j],player,logs)
        
    if(player_co[1]==1 and ((WIDTH-2)//3)<player_co[0]<(((WIDTH-2)//3)*2)+3 and map[i][j].up):
        i-=1
        os.system('cls' if os.name == 'nt' else 'clear')
        player_co[1]+=HEIGHT-2
        collision=False
        logs.add_log(player.add_xp(10))
        print_ui(map[i][j],player,logs)

    if(player_co[1]==HEIGHT and ((WIDTH-2)//3)<player_co[0]<(((WIDTH-2)//3)*2)+3 and map[i][j].down):
        i+=1
        os.system('cls' if os.name == 'nt' else 'clear')
        player_co[1]-=HEIGHT-2
        collision=False
        logs.add_log(player.add_xp(10))
        print_ui(map[i][j],player,logs)
    
    time.sleep(SPEED)
os.system('cls' if os.name == 'nt' else 'clear')