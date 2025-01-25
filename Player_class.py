from var import *
from const import *
from function import gotoxy,draw,isCollision

class Player():
    def __init__(self,name:str,char:str):
        self.hp=MAX_HEALTH
        self.name=name
        self.inventory=[]
        self.char=char
        self.lvl=BASE_LVL
        self.xp=BASE_XP
        self.xp_ratio=XP_RATIO
        self.prog=0

    def take_damage(self,nb):
        self.hp-=nb
        if self.hp<=0:
            self.hp=0

    def add_item(self,item):
        if(len(self.inventory)==MAX_INV):
            print("Not enough space in inventory\n")
        self.inventory.append(item)
    
    def drop_item(self):
        if self.inventory is not None:
            choice=int(input())-1
            return self.inventory.pop(choice)
        return None
    
    def show_inentory(self):
        gotoxy(X_UI-50,Y_UI)
        print(f"---------------Inventory----------HP:{self.hp}")
        for i in range(len(self.inventory)):
            gotoxy(X_UI-50,Y_UI+i+1)
            print(f"{i+1}: {self.inventory[i]}")
        gotoxy(X_UI-50,Y_UI+len(self.inventory)+1)
        print("----------------------------------------") 
        self.show_level()
              
    def show_level(self):
        gotoxy(X_UI-50,Y_UI+len(self.inventory)+3)
        print(f"-----------------LEVEL-{self.lvl}----------------") 
        gotoxy(X_UI-50,Y_UI+len(self.inventory)+4)
        print("█"*self.prog)
        gotoxy(X_UI-50,Y_UI+len(self.inventory)+5)
        print("----------------------------------------") 
    
    def add_xp(self,nb:int):
        nb*=self.xp_ratio
        self.xp+=nb
        self.prog=round(self.xp)
        if(self.prog>=MAX_XP):
            self.lvl+=1
            self.xp=0
            self.prog=0
            self.xp_ratio-=0.01
            

    def move(self,co:list[int],key:str,room):
        #progression
        oldX,oldY=co[0],co[1]
        if(key==UP and not(isCollision(co,key,room))):
            player_co[1]-=1
        elif(key==DOWN and not(isCollision(co,key,room))):
            player_co[1]+=1
        elif(key==LEFT and not(isCollision(co,key,room))):
            player_co[0]-=1
        elif(key==RIGHT and not(isCollision(co,key,room))):
            player_co[0]+=1
        
        gotoxy(oldX,oldY)
        draw(VOID)
        gotoxy(co[0],co[1])
        draw(PLAYER)

    def __repr__(self):
        return self.name