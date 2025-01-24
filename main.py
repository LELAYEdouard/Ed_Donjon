import os
import time
from msvcrt import getch

WALL="#"
VOID=" "
HEIGHT=20
WIDTH=40
SPEED=0.00002
QUIT="a"
PLAYER="X"
UP="z"
DOWN ="s"
LEFT="q"
RIGHT="d"
BASE_PLAYER_CO_X=5
BASE_PLAYER_CO_Y=5


def aff_salle(long:int,larg:int):
    print(larg*WALL)
    for i in range(long-2):
        print(WALL + (larg-2)*VOID + WALL)
    print(larg*WALL)

def gotoxy(x:int ,y:int ):
    print("%c[%d;%df" % (0x1B, y, x), end='')

def draw(char:str):
    print(char)

def move(co:list[int],key:str):
    
    #progression
    oldX,oldY=co[0],co[1]
    if(key==UP):
        player_co[1]-=1
    elif(key==DOWN):
        player_co[1]+=1
    elif(key==LEFT):
        player_co[0]-=1
    elif(key==RIGHT):
        player_co[0]+=1
    
    gotoxy(oldX,oldY)
    draw(VOID)
    gotoxy(co[0],co[1])
    draw(PLAYER)
    
def isCollision(co:list[int]):
    if(co[0]==1 or co[0]==WIDTH or co[1]==1 or co[1]==HEIGHT):
        return True

def print_controls():
    print("------controls------\n") 
    print("up: z\ndown: s\nright: d\nleft: q\n")
    print("--------------------")


#game
collision=False
key=""
player_co=[BASE_PLAYER_CO_X,BASE_PLAYER_CO_Y]
os.system('cls' if os.name == 'nt' else 'clear')
aff_salle(HEIGHT,WIDTH)
gotoxy(player_co[0],player_co[1])
draw(PLAYER)
while(key!=QUIT and not(collision)):
    gotoxy(0,0)
    key = getch().decode('utf-8')
    
    move(player_co,key)
    collision= isCollision(player_co)
    time.sleep(SPEED)
os.system('cls' if os.name == 'nt' else 'clear')