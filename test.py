from const import *
from var import *
from graphic_func import *
from function import *
from obj_class import *
from Player_class import *
from Room_class import *
import os
import time
#from msvcrt import getch

map=create_map(5)
os.system('cls' if os.name == 'nt' else 'clear')
i,j=0,0
map[i][j].show()
enable_echo(False)
logs=Logs()
player=Player("TEST",PLAYER)
player.add_item("bb")
player.add_item("aa")
os.system('cls' if os.name == 'nt' else 'clear')

arme=Weapon(weapon[0][0],weapon[0][1])
ch=Chest(6,9)
ch.add_item(arme)
ch.add_item(arme)
ch.add_item(arme)
ch1=Chest(15,3)
ch1.add_item(arme)
ch1.add_item(arme)
ch1.add_item(arme)
ch2=Chest(12,9)
ch2.add_item(arme)
ch2.add_item(arme)
ch2.add_item(arme)
map[0][0].add_item(ch)
map[0][0].add_item(ch1)
map[0][0].add_item(ch2)
print_ui(map[i][j],player,logs)
while(key!=QUIT):
    gotoxy(0,0)
    
    key = getch()
    if(key==INTERACT and (isCollisionChest(player_co,DOWN,map[i][j]) or isCollisionChest(player_co,UP,map[i][j]) or isCollisionChest(player_co,LEFT,map[i][j]) or isCollisionChest(player_co,RIGHT,map[i][j]))):
        chest_interact(player_co,map[i][j])
        chest_print=True

    #take item from chest to put in player inventory
    if(chest_print and key!=INTERACT):
        for k in range(MAX_CHEST_INV):
            if(key == str(k+1)):
                logs.add_log(player.add_item(map[i][j].inv[0].take_item(k)))
                print_ui(map[i][j],player,logs)
                
    #move the player on the map
    player.move(player_co,key,map[i][j])  

    #erase display of the chest inventory if the player not in front of the chest anymore
    if(chest_print and key!=INTERACT and not(isCollisionChest(player_co,DOWN,map[i][j]) or isCollisionChest(player_co,UP,map[i][j]) or isCollisionChest(player_co,LEFT,map[i][j]) or isCollisionChest(player_co,RIGHT,map[i][j]))):
        chest_erase()
        chest_print=False

    if(player_co[0]==WIDTH and ((HEIGHT-2)//3)+1<player_co[1]<(((HEIGHT-2)//3)*2)+2 and map[i][j].right):
        j+=1
        os.system('cls' if os.name == 'nt' else 'clear')
        player_co[0]-=WIDTH-2
        collision=False
        player.add_xp(20)
        print_ui(map[i][j],player,logs)
        
    if(player_co[0]==1 and ((HEIGHT-2)//3)+1<player_co[1]<(((HEIGHT-2)//3)*2)+2 and map[i][j].left):
        j-=1
        os.system('cls' if os.name == 'nt' else 'clear')
        player_co[0]+=WIDTH-2
        collision=False
        player.add_xp(20)
        print_ui(map[i][j],player,logs)
        
    if(player_co[1]==1 and ((WIDTH-2)//3)+1<player_co[0]<(((WIDTH-2)//3)*2)+4 and map[i][j].up):
        i-=1
        os.system('cls' if os.name == 'nt' else 'clear')
        player_co[1]+=HEIGHT-2
        collision=False
        player.add_xp(20)
        print_ui(map[i][j],player,logs)

    if(player_co[1]==HEIGHT and ((WIDTH-2)//3)+1<player_co[0]<(((WIDTH-2)//3)*2)+4 and map[i][j].down):
        i+=1
        os.system('cls' if os.name == 'nt' else 'clear')
        player_co[1]-=HEIGHT-2
        collision=False
        player.add_xp(20)
        print_ui(map[i][j],player,logs)
    
    time.sleep(SPEED)
os.system('cls' if os.name == 'nt' else 'clear')
enable_echo(True)