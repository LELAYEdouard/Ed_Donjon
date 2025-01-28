from const import *
from var import *
from graphic_func import *
from function import *
from obj_class import *
from Player_class import *
from Room_class import *
import os
import time
import sys, tty, termios
#from msvcrt import getch

m=create_map(5)
os.system('cls' if os.name == 'nt' else 'clear')
i,j=0,0
m[i][j].show()
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
m[0][0].add_item(ch)
m[0][0].add_item(ch1)
m[0][0].add_item(ch2)
print_ui(m[i][j],player,logs)
while(key!=QUIT):
    gotoxy(0,0)
    
    key = getch()
    if(key==INTERACT and (isCollision(player_co,DOWN,m[i][j]) or isCollision(player_co,UP,m[i][j]) or isCollision(player_co,LEFT,m[i][j]) or isCollision(player_co,RIGHT,m[i][j]))):
        chest_interact(player_co,m[i][j])
        chest_print=True
    if(chest_print and key!=INTERACT and not(isCollision(player_co,DOWN,m[i][j]) and isCollision(player_co,UP,m[i][j]) and isCollision(player_co,LEFT,m[i][j]) and isCollision(player_co,RIGHT,m[i][j]))):
        chest_erase()
            

    player.move(player_co,key,m[i][j])

    if(player_co[0]==WIDTH and ((HEIGHT-2)//3)+1<player_co[1]<(((HEIGHT-2)//3)*2)+2 and m[i][j].right):
        j+=1
        os.system('cls' if os.name == 'nt' else 'clear')
        player_co[0]-=WIDTH-2
        collision=False
        player.add_xp(20)
        print_ui(m[i][j],player,logs)
        
    if(player_co[0]==1 and ((HEIGHT-2)//3)+1<player_co[1]<(((HEIGHT-2)//3)*2)+2 and m[i][j].left):
        j-=1
        os.system('cls' if os.name == 'nt' else 'clear')
        player_co[0]+=WIDTH-2
        collision=False
        player.add_xp(20)
        print_ui(m[i][j],player,logs)
        
    if(player_co[1]==1 and ((WIDTH-2)//3)+1<player_co[0]<(((WIDTH-2)//3)*2)+4 and m[i][j].up):
        i-=1
        os.system('cls' if os.name == 'nt' else 'clear')
        player_co[1]+=HEIGHT-2
        collision=False
        player.add_xp(20)
        print_ui(m[i][j],player,logs)

    if(player_co[1]==HEIGHT and ((WIDTH-2)//3)+1<player_co[0]<(((WIDTH-2)//3)*2)+4 and m[i][j].down):
        i+=1
        os.system('cls' if os.name == 'nt' else 'clear')
        player_co[1]-=HEIGHT-2
        collision=False
        player.add_xp(20)
        print_ui(m[i][j],player,logs)
    
    time.sleep(SPEED)
os.system('cls' if os.name == 'nt' else 'clear')
enable_echo(True)