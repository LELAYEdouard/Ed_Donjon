from const import *
from var import *

def gotoxy(x:int ,y:int ):
    print("%c[%d;%df" % (0x1B, y, x), end='')

def draw(char:str):
    print(char)

def print_controls():
    i=2
    gotoxy(X_UI,i-1)
    print("------controls------\n") 
    for key,values in controls.items():
        gotoxy(X_UI,i)
        print(f"| -{key}: {values}")
        gotoxy(X_UI+19,i)
        print("|")
        i+=1
    gotoxy(X_UI,i)
    print("--------------------")

def print_ui(room,player):
    room.show()
    gotoxy(X_UI-31-len(player.name)//2,Y_UI-1)
    print(player)
    print_controls()
    player.show_inentory()
    gotoxy(player_co[0],player_co[1])
    draw(PLAYER)