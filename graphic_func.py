from const import *
from var import *
from Room_class import Room
#go to the coordinate x,y on the terminal (from : https://stackoverflow.com/questions/21330632/pythonic-alternative-of-gotoxy-c-code)
def gotoxy(x:int ,y:int ):
    print("%c[%d;%df" % (0x1B, y, x), end='')
#print a char on the terminal
def draw(char:str):
    print(char)
#display the controls on screen
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
#dislay the UI on screen
def print_ui(room,player,logs,chest_print,chest_id):
    gotoxy(0,0)
    room.show()
    if(len(room.inv)!=0):
        for i in range(len(room.inv)):
            room.inv[i].print_chest()
    gotoxy(X_UI-31-len(player.name)//2,Y_UI-1)
    print(player)
    print_controls()
    logs.print_logs()
    player.show_inventory()
    if(chest_print):
        room.inv[chest_id].print_content()
    else:
        chest_erase()
    
    gotoxy(player_co[0],player_co[1])
    draw(PLAYER)
#erase the chest inventory on screen
def chest_erase():
    gotoxy(TEXT_CHEST_COX,TEXT_CHEST_COY-1)
    print("                                        ")
    for i in range(MAX_INV):
        gotoxy(TEXT_CHEST_COX,TEXT_CHEST_COY+i)
        print("                                        ")
    gotoxy(TEXT_CHEST_COX,TEXT_CHEST_COY+MAX_INV)
    print("                                        ")
#display the chest inventory on screen
def chest_interact(co:list[int],room:Room):
    for i in range(len(room.inv)):  
        if((co[0]==room.inv[i].pos_x and co[1]+1==room.inv[i].pos_y )
            or (co[1]==room.inv[i].pos_y and co[0]-1==room.inv[i].pos_x)
            or (co[1]==room.inv[i].pos_y and co[0]+1==room.inv[i].pos_x)
            or (co[0]==room.inv[i].pos_x and co[1]-1==room.inv[i].pos_y)):
            room.inv[i].print_content()
            return i    