from const import *
from var import *
from graphic_func import *
from function import *
from obj_class import *
from Player_class import *
from Room_class import *
import os
import time
from msvcrt import getch


m=create_map(5)
os.system('cls' if os.name == 'nt' else 'clear')
i,j=0,0
m[i][j].show()


player=Player("TEST",PLAYER)
player.add_item("bb")
player.add_item("aa")
os.system('cls' if os.name == 'nt' else 'clear')

arme=Weapon(weapon[0][0],weapon[0][1])
ch=Chest(6,9)
ch.add_item(arme)
ch.add_item(arme)
ch.add_item(arme)

m[0][0].add_item(ch)


print_ui(m[i][j],player)
m[0][0].inv[0].print_content()
while(key!=QUIT and not(collision)):
    gotoxy(0,0)
    
    key = getch().decode('utf-8')
    
    player.move(player_co,key)
    collision= isCollision(player_co)

    if(player_co[0]==WIDTH and ((HEIGHT-2)//3)+1<player_co[1]<(((HEIGHT-2)//3)*2)+2 and m[i][j].right):
        j+=1
        os.system('cls' if os.name == 'nt' else 'clear')
        player_co[0]-=WIDTH-2
        collision=False
        player.add_xp(20)
        print_ui(m[i][j],player)
        
    if(player_co[0]==1 and ((HEIGHT-2)//3)+1<player_co[1]<(((HEIGHT-2)//3)*2)+2 and m[i][j].left):
        j-=1
        os.system('cls' if os.name == 'nt' else 'clear')
        player_co[0]+=WIDTH-2
        collision=False
        player.add_xp(20)
        print_ui(m[i][j],player)
        
    if(player_co[1]==1 and ((WIDTH-2)//3)+1<player_co[0]<(((WIDTH-2)//3)*2)+4 and m[i][j].up):
        i-=1
        os.system('cls' if os.name == 'nt' else 'clear')
        player_co[1]+=HEIGHT-2
        collision=False
        player.add_xp(20)
        print_ui(m[i][j],player)

    if(player_co[1]==HEIGHT and ((WIDTH-2)//3)+1<player_co[0]<(((WIDTH-2)//3)*2)+4 and m[i][j].down):
        i+=1
        os.system('cls' if os.name == 'nt' else 'clear')
        player_co[1]-=HEIGHT-2
        collision=False
        player.add_xp(20)
        print_ui(m[i][j],player)
    
    time.sleep(SPEED)
os.system('cls' if os.name == 'nt' else 'clear')