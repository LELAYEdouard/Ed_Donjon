from var import *
from const import *
from function import gotoxy

class Weapon():
    def __init__(self,name,damage,lvl):
        self.name=name
        self.lvl=lvl
        self.damage=damage*self.lvl
        self.prog=0
        self.xp_ratio=XP_RATIO
        self.xp=0

    def attack(self):
        return self.damage
    
    def add_xp(self,nb):
        nb*=self.xp_ratio
        self.xp+=nb
        self.prog=round(self.xp)
        if(self.prog>=MAX_XP_WEAPON):
            self.lvl+=1
            self.xp=0
            self.prog=0
            self.xp_ratio-=0.01
            self.damage*=self.lvl

    def __repr__(self) :
        return f"{self.name} (LVL {self.lvl})"

class Mob():
    def __init__(self,name,hp,posX,posY,xp):
        self.name=name
        self.hp=hp
        self.weapon=None
        self.pos=[posX,posY]
        self.xp=xp

    def add_item(self,item):
        self.weapon=item

    def take_damage(self,nb):
        self.hp-=nb
        if self.hp<0:
            self.hp=0

    def print_mob(self):
        gotoxy(self.pos[0],self.pos[1])
        print(MOB)
    
    def attack(self):
        return self.weapon.damage

    def __repr__(self):
        return self.name
    
class Obj():
    def __init__(self,name,hp):  
        self.name=name
        self.hp=hp
    
    def use(self):
        return self.hp
    
    def __repr__(self):
        return self.name
       
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
            print(f"{i+1}: {self.inv[i]}                                              ")
        gotoxy(TEXT_CHEST_COX,TEXT_CHEST_COY+len(self.inv))
        print("----------------------------------------") 


    def print_chest(self):
        gotoxy(self.pos_x,self.pos_y)
        print(CHEST)

class Logs():
    def __init__(self,name):
        self.inv=[]
        self.name=name

    def print_logs(self):
        gotoxy(TEXT_COX,TEXT_COY-1)
        print(f"--------------------{self.name}--------------------")
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
                self.inv[-1]="● "+log+VOID*30
            else:    
                self.inv.append("● "+log+VOID*30)

    def erase(self):
        gotoxy(TEXT_COX,TEXT_COY-1)                                 
        print(VOID*45)
        for i in range(len(self.inv)):
            gotoxy(TEXT_COX,TEXT_COY+i)
            print(VOID*45)
        gotoxy(TEXT_COX,TEXT_COY+len(self.inv))
        print(VOID*45)
                                                        