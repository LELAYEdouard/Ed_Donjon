from const import *
from var import *
from graphic_func import *
from function import *
from obj_class import *
import os
m=create_map(5)
os.system('cls' if os.name == 'nt' else 'clear')
i,j=0,0
m[i][j].show()


player=Player("TEST",PLAYER)
player.add_item("bb")
player.add_item("aa")
os.system('cls' if os.name == 'nt' else 'clear')
print_ui(m[i][j],player)
for k in range (200):
    player.add_xp(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    print_ui(m[i][j],player)
    print(player.xp,player.prog)
