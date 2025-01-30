'''
Edouard's Dongeon is a text-based game where the player can move in a map and interact with the environment.
'''
#libriary
import os
import time

#files
from const import *
from var import *
from graphic_func import *
from function import create_map,getch,enable_echo,isCollisionChest
from obj_class import *
from Player_class import *
from Room_class import *

#game
#clear screen
os.system('cls' if os.name == 'nt' else 'clear')

#create map
map=create_map(LENGTH_MAP)
i,j=0,0

#display Title
print("    ______    __                           __   _                  __                                 ")
print("   / ____/___/ /___  __  ______ __________/ /  ( )  _____     ____/ /___  ____  ____ ____  ____  ____ ")
print("  / __/ / __  / __ \/ / / / __ `/ ___/ __  /   |/  / ___/    / __  / __ \/ __ \/ __ `/ _ \/ __ \/ __ \ ")
print(" / /___/ /_/ / /_/ / /_/ / /_/ / /  / /_/ /       (__  )    / /_/ / /_/ / / / / /_/ /  __/ /_/ / / / /")
print("/_____/\__,_/\____/\__,_/\__,_/_/   \__,_/       /____/     \__,_/\____/_/ /_/\__, /\___/\____/_/ /_/ ")
print("                                                                             /____/                   ")

#init player
player=Player(input("Enter your name:\n"),PLAYER)
#init logs
logs=Logs()
#clear screen
os.system('cls' if os.name == 'nt' else 'clear')

#disable echo
enable_echo(False)
#display the UI
print_ui(map[i][j],player,logs,chest_print)

while(key!=QUIT):
    
    gotoxy(0,0)
    #get the input
    key = getch()
    
    #condition for dropping item
    if(key == DROP_ITEM):
        logs.add_log(player.drop_item(map[i][j]))
        print_ui(map[i][j],player,logs,chest_print)
    #codition for interaction with the chest if so displaying the chest inventory on screen
    if(key==INTERACT and (isCollisionChest(player_co,DOWN,map[i][j]) or isCollisionChest(player_co,UP,map[i][j]) or isCollisionChest(player_co,LEFT,map[i][j]) or isCollisionChest(player_co,RIGHT,map[i][j]))):
        chest_id=chest_interact(player_co,map[i][j])
        chest_print=True

    #take item from chest to put in player inventory
    if(chest_print and key!=INTERACT):
        for k in range(MAX_CHEST_INV):
            if(key == str(k+1) and int(key)<=len(map[i][j].inv[chest_id].inv)):
                full_inv=len(player.inventory)==MAX_INV
                elt=map[i][j].inv[chest_id].take_item(k)
                logs.add_log(player.add_item(elt))
                if(full_inv):
                    map[i][j].inv[chest_id].inv.insert(k,elt)
                chest_erase()
                print_ui(map[i][j],player,logs,chest_print,chest_id)
                
    #move the player on the map
    player.move(player_co,key,map[i][j])  

    #erase display of the chest inventory if the player not in front of the chest anymore
    if(chest_print and key!=INTERACT and not(isCollisionChest(player_co,DOWN,map[i][j]) or isCollisionChest(player_co,UP,map[i][j]) or isCollisionChest(player_co,LEFT,map[i][j]) or isCollisionChest(player_co,RIGHT,map[i][j]))):
        chest_print=False
        print_ui(map[i][j],player,logs,chest_print)

    #condition for changing room
    if(player_co[0]==WIDTH and ((HEIGHT-2)//3)<player_co[1]<(((HEIGHT-2)//3)*2)+2 and map[i][j].right):
        j+=1
        os.system('cls' if os.name == 'nt' else 'clear')
        player_co[0]-=WIDTH-2
        collision=False
        logs.add_log(player.add_xp(10))
        print_ui(map[i][j],player,logs,chest_print)
        
    if(player_co[0]==1 and ((HEIGHT-2)//3)<player_co[1]<(((HEIGHT-2)//3)*2)+2 and map[i][j].left):
        j-=1
        os.system('cls' if os.name == 'nt' else 'clear')
        player_co[0]+=WIDTH-2
        collision=False
        logs.add_log(player.add_xp(10))
        print_ui(map[i][j],player,logs,chest_print)
        
    if(player_co[1]==1 and ((WIDTH-2)//3)<player_co[0]<(((WIDTH-2)//3)*2)+3 and map[i][j].up):
        i-=1
        os.system('cls' if os.name == 'nt' else 'clear')
        player_co[1]+=HEIGHT-2
        collision=False
        logs.add_log(player.add_xp(10))
        print_ui(map[i][j],player,logs,chest_print)

    if(player_co[1]==HEIGHT and ((WIDTH-2)//3)<player_co[0]<(((WIDTH-2)//3)*2)+3 and map[i][j].down):
        i+=1
        os.system('cls' if os.name == 'nt' else 'clear')
        player_co[1]-=HEIGHT-2
        collision=False
        logs.add_log(player.add_xp(10))
        print_ui(map[i][j],player,logs,chest_print)
    
    time.sleep(SPEED)
#clear screen when the game is over    
os.system('cls' if os.name == 'nt' else 'clear')
#enable echo when the game is over
enable_echo(True)