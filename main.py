#libriary
import os
import time
from msvcrt import getch

#files
from const import *
from var import *
from graphic_func import *
from function import *
from obj_class import *
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

os.system('cls' if os.name == 'nt' else 'clear')
print_ui(map[i][j],player)


while(key!=QUIT and not(collision)):
    gotoxy(0,0)
    key = getch().decode('utf-8')
    
    player.move(player_co,key)
    collision= isCollision(player_co)

    if(player_co[0]==WIDTH and ((HEIGHT-2)//3)<player_co[1]<(((HEIGHT-2)//3)*2)+2 and map[i][j].right):
        j+=1
        os.system('cls' if os.name == 'nt' else 'clear')
        player_co[0]-=WIDTH-2
        collision=False
        player.add_xp(20)
        print_ui(map[i][j],player)
        
    if(player_co[0]==1 and ((HEIGHT-2)//3)<player_co[1]<(((HEIGHT-2)//3)*2)+2 and map[i][j].left):
        j-=1
        os.system('cls' if os.name == 'nt' else 'clear')
        player_co[0]+=WIDTH-2
        collision=False
        player.add_xp(20)
        print_ui(map[i][j],player)
        
    if(player_co[1]==1 and ((WIDTH-2)//3)+1<player_co[0]<(((WIDTH-2)//3)*2)+4 and map[i][j].up):
        i-=1
        os.system('cls' if os.name == 'nt' else 'clear')
        player_co[1]+=HEIGHT-2
        collision=False
        player.add_xp(20)
        print_ui(map[i][j],player)

    if(player_co[1]==HEIGHT and ((WIDTH-2)//3)+1<player_co[0]<(((WIDTH-2)//3)*2)+4 and map[i][j].down):
        i+=1
        os.system('cls' if os.name == 'nt' else 'clear')
        player_co[1]-=HEIGHT-2
        collision=False
        player.add_xp(20)
        print_ui(map[i][j],player)
    
    time.sleep(SPEED)
os.system('cls' if os.name == 'nt' else 'clear')