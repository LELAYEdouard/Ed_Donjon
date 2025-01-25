from const import *
from var import *
from graphic_func import *
from Room_class import Room
from random import randint
from msvcrt import getch
    
def isCollision(co:list[int]):
    if(co[0]==1 or co[0]==WIDTH or co[1]==1 or co[1]==HEIGHT):
        return True
    
    
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
