from const import *
from var import *
from graphic_func import *
from Room_class import Room
from obj_class import Chest,Weapon
from random import randint
import sys, termios
#get char from keyboard (from : https://forums.raspberrypi.com/viewtopic.php?t=69046)
def getch():
  old_settings = termios.tcgetattr(0)
  new_settings = old_settings[:]
  new_settings[3] &= ~termios.ICANON
  try:
    termios.tcsetattr(0, termios.TCSANOW, new_settings)
    ch = sys.stdin.read(1)
  finally:
    termios.tcsetattr(0, termios.TCSANOW, old_settings)
  return ch
#enable or disable echo (from : https://gist.github.com/kgriffs/5726314)
def enable_echo(enable):
    fd = sys.stdin.fileno()
    new = termios.tcgetattr(fd)
    if enable:
        new[3] |= termios.ECHO
    else:
        new[3] &= ~termios.ECHO

    termios.tcsetattr(fd, termios.TCSANOW, new)
#check if the player is in collision with a wall or a chest
def isCollision(co:list[int],key:str,room:Room):
    lst=co.copy()
    if(key == UP):
        lst[1]-=1
    elif(key == DOWN):
        lst[1]+=1
    elif(key == LEFT):
        lst[0]-=1
    elif(key == RIGHT):
        lst[0]+=1   

    if((lst[1]==1 and room.up==False)or (lst[1]==HEIGHT and room.down==False) or (lst[0]==1 and room.left==False )or (lst[0]==WIDTH and room.right==False)):
        return True
    if((lst[1]==1 and room.up==True and (((WIDTH-2)//3)+3 >lst[0]>1 or (((WIDTH-2)//3)*2)+2<lst[0]<WIDTH))
        or (lst[1]==HEIGHT and room.down==True and (((WIDTH-2)//3)+3 >lst[0]>1 or (((WIDTH-2)//3)*2)+2<lst[0]<WIDTH))
          or (lst[0]==1 and room.left==True and (((HEIGHT-2)//3)+2>lst[1]>1 or (((HEIGHT-2)//3)*2)+1<lst[1]<HEIGHT))
          or (lst[0]==WIDTH and room.right==True and(((HEIGHT-2)//3)+2>lst[1]>1 or (((HEIGHT-2)//3)*2)+1<lst[1]<HEIGHT))):
        return True
    for i in range(len(room.inv)):
        if((lst[0]==room.inv[i].pos_x and lst[1]==room.inv[i].pos_y )
           or (lst[1]==room.inv[i].pos_y and lst[0]==room.inv[i].pos_x)):
            return True
    return False
'''create a map with random room and chest  
the two first room are already created and are always the same'''
def create_map(x):
    map=[[None for i in range(x)]for i in range(x)]

    start_room=Room(True,False,False,False)
    start_room2=Room(True,True,False,True)

    map[0][0]=start_room
    ch=Chest(WIDTH//2,HEIGHT//2)
    ch.add_item(rand_weapon())
    map[0][0].inv.append(ch)

    map[0][1]=start_room2
    room=None
    for i in range(len(map)): #coin haut droit dejai fait (Room d'entrée)
        for j in range(len(map)):
            if map[i][j] == None and 0<j<len(map)-1 and i==0 :  # arrete haut
                room=Room(rand_bool(),map[i][j-1].right,False,rand_bool())
                map[i][j]=room
            if map[i][j] == None and j==len(map)-1 and 0<i<len(map)-1 : #arrete droite
                room=Room(False,map[i][j-1].right,map[i-1][j].down,rand_bool())
                map[i][j]=room
            if map[i][j] == None and j==0 and 0<i<len(map)-1 : # arrete gauche
                room=Room(rand_bool(),False,map[i-1][j].down,rand_bool())
                map[i][j]=room
            if map[i][j] == None and 0<j<len(map)-1 and i==len(map)-1 : # arrete bas 
                room=Room(rand_bool(),map[i][j-1].right,map[i-1][j].down,False)
                map[i][j]=room
            if map[i][j] == None and j==len(map)-1 and i==0 : # coin haut droit
                room=Room(False,map[i][j-1].right,False,rand_bool())
                map[i][j]=room
            if map[i][j] == None and j==len(map)-1 and i==len(map)-1 : # coin bas droit
                room=Room(False,map[i][j-1].right,map[i-1][j].down,False)
                map[i][j]=room
            if map[i][j] == None and j==0 and i==len(map)-1 : #coin bas gauche
                room=Room(rand_bool(),False,map[i-1][j].down,False)
                map[i][j]=room
            if map[i][j] == None and 0<j<len(map)-1 and 0<i<len(map)-1: # milieu
                room=Room(rand_bool(),map[i][j-1].right,map[i-1][j].down,rand_bool())
                map[i][j]=room
                
            if(i!=0 and j!=0):
                lst=rand_chest()
                if(lst is not None):
                    for k in range(len(lst)):
                        map[i][j].inv.append(lst[k])
    return map    
#generate a random boolean
def rand_bool():
    a=randint(0,1)
    if a==0:
        return True
    return False
#generate a random chest
def rand_chest():
    chest=[]
    nb_chest=randint(0,MAX_CHEST)
    nb_items=randint(1,MAX_CHEST_INV)
    for i in range(nb_chest):
        x=randint(3,WIDTH-2)
        y=randint(3,HEIGHT-2)
        ch=Chest(x,y)
        for j in range(nb_items):
            weap=rand_weapon()
            ch.add_item(weap)
        chest.append(ch)
    return chest
#generate a random weapon
def rand_weapon():
    nb=randint(0,NB_WEAPON-1)
    weap=Weapon(weapon[nb][0],weapon[nb][1])
    return weap