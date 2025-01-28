from random import randint
from var import *
from const import *
from function import gotoxy

class Weapon():
    def __init__(self,name,damage):
        self.name=name
        self.damage=damage

    def attack(self):
        return self.damage
    
    def __repr__(self) :
        return self.name

class Mob():
    def __init__(self,name,hp):
        self.name=name
        self.hp=hp
        self.weapon=None

    def add_item(self,item):
        self.weapon=item

    def take_damage(self,nb):
        self.hp-=nb
        if self.hp<0:
            self.hp=0
       
class Chest():
    def __init__(self,x:int,y:int):
        self.inv=[]
        self.pos_x=x
        self.pos_y=y

    def add_item(self,item):
        self.inv.append(item)

    def take_item(self,i):            
        elt=self.inv.pop(i)
        return elt

    def print_content(self):
        gotoxy(TEXT_CHEST_COX,TEXT_CHEST_COY-1)
        print("-----------------CHEST------------------")
        for i in range(len(self.inv)):
            gotoxy(TEXT_CHEST_COX,TEXT_CHEST_COY+i)
            print(f"{i+1}: {self.inv[i]}")
        gotoxy(TEXT_CHEST_COX,TEXT_CHEST_COY+len(self.inv))
        print("----------------------------------------") 


    def print_chest(self):
        gotoxy(self.pos_x,self.pos_y)
        print(CHEST)

class Logs():
    def __init__(self):
        self.inv=[]

    def print_logs(self):
        gotoxy(TEXT_COX,TEXT_COY-1)
        print("--------------------LOGS--------------------")
        for i in range(len(self.inv)):
            gotoxy(TEXT_COX,TEXT_COY+i)
            print(self.inv[i])
        gotoxy(TEXT_COX,TEXT_COY+len(self.inv))
        print("--------------------------------------------")

    def add_log(self,log:str):
        if(log!=VOID_MESS):
            if(len(self.inv)==MAX_LOG):
                for i in range(1,len(self.inv)):
                    self.inv[i-1]=self.inv[i]
                self.inv[-1]="● "+log+VOID*20
            else:    
                self.inv.append("● "+log+VOID*20)
        
        
        
