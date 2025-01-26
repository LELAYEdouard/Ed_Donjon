from const import *
from var import *
from Room_class import Room

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

def print_ui(room,player,logs):
    room.show()
    if(len(room.inv)!=0):
        for i in range(len(room.inv)):
            room.inv[i].print_chest()
    gotoxy(X_UI-31-len(player.name)//2,Y_UI-1)
    print(player)
    print_controls()
    logs.print_logs()
    player.show_inventory()
    gotoxy(player_co[0],player_co[1])
    draw(PLAYER)

def chest_erase():
    gotoxy(TEXT_CHEST_COX,TEXT_CHEST_COY-1)
    print("                                        ")
    for i in range(MAX_INV):
        gotoxy(TEXT_CHEST_COX,TEXT_CHEST_COY+i)
        print("                                        ")
    gotoxy(TEXT_CHEST_COX,TEXT_CHEST_COY+MAX_INV)
    print("                                        ")

def chest_interact(co:list[int],room:Room):
    for i in range(len(room.inv)):  
        if((co[0]==room.inv[i].pos_x and co[1]+1==room.inv[i].pos_y )
            or (co[1]==room.inv[i].pos_y and co[0]-1==room.inv[i].pos_x)
            or (co[1]==room.inv[i].pos_y and co[0]+1==room.inv[i].pos_x)
            or (co[0]==room.inv[i].pos_x and co[1]-1==room.inv[i].pos_y)):
            room.inv[i].print_content()    