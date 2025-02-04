from var import *
from const import *
from function import gotoxy,draw,isCollisionBorder,isCollisionChest,getch,isCollisionMob

class Player():
    def __init__(self,name:str,char:str):
        self.hp=MAX_HEALTH
        if(name==""):
            name=BASE_NAME
        self.name=name
        self.inventory=[]
        self.char=char
        self.lvl=BASE_LVL
        self.xp=BASE_XP
        self.xp_ratio=XP_RATIO
        self.prog=0

    def take_damage(self,nb):
        self.hp-=nb
        if self.hp<=MIN_HP:
            self.hp=MIN_HP

    def add_item(self,item):
        if(len(self.inventory)==MAX_INV):
            return "Not enough space in inventory"
        else:
            self.inventory.append(item)
        return VOID_MESS
    
    def drop_item(self,room):
        gotoxy(TEXT_CHEST_COX,TEXT_CHEST_COY-1)
        print(f"-----------------DROP----STOP : {DROP_ITEM} ------")
        for i in range(len(self.inventory)):
            gotoxy(TEXT_CHEST_COX,TEXT_CHEST_COY+i)
            print(f"{i+1}: {self.inventory[i]}                                              ")
        gotoxy(TEXT_CHEST_COX,TEXT_CHEST_COY+len(self.inventory))
        print("----------------------------------------") 
        if (len(self.inventory)!=0):
            if(len(room.inv)!=0):
                key=getch()
                if(key==DROP_ITEM): 
                    return "Drop stopped"
                elif(key.isdigit() and int(key)<=len(self.inventory)):
                    elt=self.inventory.pop(int(key)-1)
                    for k in range(len(room.inv)):
                        if(len(room.inv[k].inv)!=MAX_CHEST_INV):
                            room.inv[0].add_item(elt)
                            return f"{elt} has been dropped" 
                        else:
                            self.inventory.insert(int(key),elt)
                            return "No space in chest to drop item"
                else:
                    return "Drop stopped"
            else:
                return "No chest to drop item"
        return "No item to drop"
                
    
    def show_inventory(self):
        for k in range(10):
            gotoxy(X_UI-50,Y_UI+k)
            print(VOID*WIDTH_INV)
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
        print(LVL_CHAR*self.prog)
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
            return f"Level UP {self.lvl-1}->{self.lvl}                               "
        return VOID_MESS

    def move(self,co:list[int],key:str,room):
        #progression
        oldX,oldY=co[0],co[1]
        if(key==UP and (not(isCollisionBorder(co,key,room)) and not(isCollisionChest(co,key,room)) and not(isCollisionMob(co,key,room)[0]))):
            player_co[1]-=1
        elif(key==DOWN and (not(isCollisionBorder(co,key,room)) and not(isCollisionChest(co,key,room)) and not(isCollisionMob(co,key,room)[0]))):
            player_co[1]+=1
        elif(key==LEFT and (not(isCollisionBorder(co,key,room)) and not(isCollisionChest(co,key,room)) and not(isCollisionMob(co,key,room)[0]))):
            player_co[0]-=1
        elif(key==RIGHT and (not(isCollisionBorder(co,key,room)) and not(isCollisionChest(co,key,room)) and not(isCollisionMob(co,key,room)[0]))):
            player_co[0]+=1
        
        gotoxy(oldX,oldY)
        draw(VOID)
        gotoxy(co[0],co[1])
        draw(PLAYER)

    def __repr__(self):
        return self.name
    
    def use_item(self,hp):
        self.hp+=hp
        if self.hp>MAX_HEALTH:
            self.hp=MAX_HEALTH