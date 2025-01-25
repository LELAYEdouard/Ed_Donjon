from const import *
from var import *
from graphic_func import *
from Room_class import Room
from random import randint

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
    
def chest_interact(co:list[int],room:Room):
    for i in range(len(room.inv)):  
        if((co[0]==room.inv[i].pos_x and co[1]+1==room.inv[i].pos_y )
            or (co[1]==room.inv[i].pos_y and co[0]-1==room.inv[i].pos_x)
            or (co[1]==room.inv[i].pos_y and co[0]+1==room.inv[i].pos_x)
            or (co[0]==room.inv[i].pos_x and co[1]-1==room.inv[i].pos_y)):
            room.inv[i].print_content()
    
def chest_erase():
    gotoxy(TEXT_COX,TEXT_COY-1)
    print("                                        ")
    for i in range(MAX_INV):
        gotoxy(TEXT_COX,TEXT_COY+i)
        print("                                        ")
    gotoxy(TEXT_COX,TEXT_COY+MAX_INV)
    print("                                        ")

def create_map(x):
    map=[[None for i in range(x)]for i in range(x)]
    start_room=Room(True,False,False,False)
    start_room2=Room(True,True,False,True)

    map[0][0]=start_room
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
    return map    

def rand_bool():
    a=randint(0,1)
    if a==0:
        return True
    return False
