from const import *
from var import *
from graphic_func import *
from obj_class import Salle
from random import randint
    
def isCollision(co:list[int]):
    if(co[0]==1 or co[0]==WIDTH or co[1]==1 or co[1]==HEIGHT):
        return True
    
def create_map(x):
    map=[[None for i in range(x)]for i in range(x)]
    start_room=Salle(True,False,False,False,None)
    start_room2=Salle(True,True,False,True,None)

    map[0][0]=start_room
    map[0][1]=start_room2
    room=None
    for i in range(len(map)): #coin haut droit dejai fait (salle d'entrée)
        for j in range(len(map)):
            if map[i][j] == None and 0<j<len(map)-1 and i==0 :  # arrete haut
                room=Salle(rand_bool(),map[i][j-1].right,False,rand_bool(),None)
                map[i][j]=room
            if map[i][j] == None and j==len(map)-1 and 0<i<len(map)-1 : #arrete droite
                room=Salle(False,map[i][j-1].right,map[i-1][j].down,rand_bool(),None)
                map[i][j]=room
            if map[i][j] == None and j==0 and 0<i<len(map)-1 : # arrete gauche
                room=Salle(rand_bool(),False,map[i-1][j].down,rand_bool(),None)
                map[i][j]=room
            if map[i][j] == None and 0<j<len(map)-1 and i==len(map)-1 : # arrete bas 
                room=Salle(rand_bool(),map[i][j-1].right,map[i-1][j].down,False,None)
                map[i][j]=room
            if map[i][j] == None and j==len(map)-1 and i==0 : # coin haut droit
                room=Salle(False,map[i][j-1].right,False,rand_bool(),None)
                map[i][j]=room
            if map[i][j] == None and j==len(map)-1 and i==len(map)-1 : # coin bas droit
                room=Salle(False,map[i][j-1].right,map[i-1][j].down,False,None)
                map[i][j]=room
            if map[i][j] == None and j==0 and i==len(map)-1 : #coin bas gauche
                room=Salle(rand_bool(),False,map[i-1][j].down,False,None)
                map[i][j]=room
            if map[i][j] == None and 0<j<len(map)-1 and 0<i<len(map)-1: # milieu
                room=Salle(rand_bool(),map[i][j-1].right,map[i-1][j].down,rand_bool(),None)
                map[i][j]=room
    return map    

def rand_bool():
    a=randint(0,1)
    if a==0:
        return True
    return False
