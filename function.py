from const import *
from var import *
from graphic_func import *
from Room_class import Room
from obj_class import Chest,Weapon,Mob,Obj
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
#check if the player is in collision with a wall 
def isCollisionBorder(co:list[int],key:str,room:Room):
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
    return False
#check if the player is in collision with a chest
def isCollisionChest(co:list[int],key:str,room:Room):
    lst=co.copy()
    if(key == UP):
        lst[1]-=1
    elif(key == DOWN):
        lst[1]+=1
    elif(key == LEFT):
        lst[0]-=1
    elif(key == RIGHT):
        lst[0]+=1   

    for i in range(len(room.inv)):
        if((lst[0]==room.inv[i].pos_x and lst[1]==room.inv[i].pos_y )
           or (lst[1]==room.inv[i].pos_y and lst[0]==room.inv[i].pos_x)):
            return True
#check if the player is in collision with a mob
def isCollisionMob(co:list[int],key:str,room:Room):
    lst=co.copy()
    if(key == UP):
        lst[1]-=1
    elif(key == DOWN):
        lst[1]+=1
    elif(key == LEFT):
        lst[0]-=1
    elif(key == RIGHT):
        lst[0]+=1   

    for i in range(len(room.mobs)):
        if((lst[0]==room.mobs[i].pos[0] and lst[1]==room.mobs[i].pos[1] )
           or (lst[1]==room.mobs[i].pos[1] and lst[0]==room.mobs[i].pos[0])):
            return True,room.mobs[i],i
    return False,None,None
'''create a map with random room and chest  
the two first room are already created and are always the same'''
def create_map(x):
    map=[[None for i in range(x)]for i in range(x)]

    start_room=Room(True,False,False,False)
    start_room2=Room(True,True,False,True)
    #init the first room
    map[0][0]=start_room
    ch=Chest(WIDTH//2,HEIGHT//2)
    ch.add_item(rand_weapon())
    map[0][0].inv.append(ch)

    #init the 2nd room
    weap=Weapon(weapon[0][0],weapon[0][1])
    map[0][1]=start_room2
    mob1=Mob(mob[0][0],mob[0][1],WIDTH//2,HEIGHT//2,mob[0][2])
    mob1.add_item(weap)
    map[0][1].add_mob(mob1)

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
                        map[i][j].add_item(lst[k])

                lst_mob=rand_mob()
                if(lst_mob is not None):
                    for l in range(len(lst_mob)):
                        map[i][j].add_mob(lst_mob[l])
                
    return map    
#generate a random boolean
def rand_bool():
    a=randint(0,3)
    return a==0
#generate a random chest
def rand_chest():
    a=randint(0,3)
    chest=[]
    if a>0:
        nb_chest=randint(0,MAX_CHEST)
        nb_items=randint(1,MAX_CHEST_INV-1)
        for i in range(nb_chest):
            x=randint(3,WIDTH-2)
            y=randint(3,HEIGHT-2)
            ch=Chest(x,y)
            for j in range(nb_items):
                weap=rand_weapon()
                obj=rand_obj()
                ch.add_item(weap)
                ch.add_item(obj)
            chest.append(ch)
        return chest
#generate a random weapon
def rand_weapon():
    nb=randint(0,NB_WEAPON-1)
    weap=Weapon(weapon[nb][0],weapon[nb][1])
    return weap
#generate a random mob
def rand_mob():
    a=randint(0,3)
    lstmob=[]
    if a>0:
        nb_mob=randint(0,NB_MAX_MOB)
        for i in range(nb_mob):
            x=randint(3,WIDTH-2)
            y=randint(3,HEIGHT-2)
            type=randint(0,NB_MOB-1)
            weap=rand_weapon()
            mb=Mob(mob[type][0],mob[type][1],x,y,mob[type][2])
            mb.add_item(weap)
            lstmob.append(mb)
        return lstmob
#generate a random object
def rand_obj():
    nb=randint(0,NB_OBJECT-1)
    o=Obj(objects[nb][0],objects[nb][1])
    return o
#fight function 
def fight(p1:object,mob:object,logs:object):
    arme=False
    for elt in p1.inventory:
        if type(elt)!=Obj:
            arme=True
    if(p1.hp==MIN_HP):
        return "Not enough HP to fight"
    if not(arme):
        return "No weapon to fight"
    logs.add_log("Fight")
    logs.print_logs()
    while p1.hp!=MIN_HP:
        gotoxy(TEXT_FIGHT_COX,TEXT_FIGHT_COY-1)
        print("-----------------CHOICE------------------")
        for i in fight_choice.keys():
            gotoxy(TEXT_FIGHT_COX,TEXT_FIGHT_COY+i)
            print(f"{i+1}: {fight_choice[i][1]}")
        gotoxy(TEXT_FIGHT_COX,TEXT_FIGHT_COY+len(fight_choice))
        print("-----------------------------------------") 
        choice=getch()
        if p1.inventory ==[]:
            logs.add_log("You don't have anything to fight")
            logs.print_logs()
        elif(choice.isdigit() and 0<int(choice)<=len(fight_choice)):
            choice=fight_choice[int(choice)-1][0]
        
            if choice == ATTACK:
                interaction_erase()
                gotoxy(TEXT_FIGHT_COX,TEXT_FIGHT_COY-1)
                print("-----------------CHOICE------------------")
                for i in range(len(p1.inventory)):
                    gotoxy(TEXT_FIGHT_COX,TEXT_FIGHT_COY+i)
                    print(f"{i+1}: {p1.inventory[i]}")
                gotoxy(TEXT_FIGHT_COX,TEXT_FIGHT_COY+len(p1.inventory))
                print("-----------------------------------------") 
                choice=getch()
                while not(choice.isdigit() and 0<int(choice)<=len(p1.inventory) and not(type(p1.inventory[int(choice)-1])==Obj)):
                    choice=getch()

                mob.take_damage(p1.inventory[int(choice)-1].attack())

                if mob.hp==0:
                    interaction_erase()
                    p1.add_xp(mob.xp)
                    return f"You defeated a {mob.name}"
                logs.add_log(f"{mob.name} lost {p1.inventory[int(choice)-1].damage} HP ({mob.hp} HP left)")
                logs.print_logs()
                interaction_erase()
            elif choice == RUN:
                interaction_erase()
                return "You ran"
            
            mob_damage=mob.attack()
            p1.take_damage(mob_damage)
            logs.add_log(f"{mob.name} attacks, you've lost {mob_damage} HP")
            p1.show_inventory()
            logs.print_logs()
        else:
            logs.add_log("Please choose a valid action")
            logs.print_logs()
    interaction_erase()
    return "You've lost"
#function to use item in your inventory
def use_item(player,logs):
    ob=False
    for elt in player.inventory:
        if type(elt)!=Weapon:
            ob=True
    if player.inventory ==[]:
            logs.add_log("You don't have anything")
            logs.print_logs()
            return VOID_MESS
    if not(ob):
        return "No object to consume"
    gotoxy(TEXT_CHEST_COX,TEXT_CHEST_COY-1)
    print(f"------------------INV---QUIT :{QUIT}----------")
    for i in range(len(player.inventory)):
        gotoxy(TEXT_CHEST_COX,TEXT_CHEST_COY+i)
        print(f"{i+1}: {player.inventory[i]}                                              ")
    gotoxy(TEXT_CHEST_COX,TEXT_CHEST_COY+len(player.inventory))
    print("----------------------------------------")
    choice=""
    while not(choice.isdigit()) or not(0<int(choice)<=len(fight_choice)):
        choice=getch()
        if choice ==QUIT:
            return VOID_MESS
        elif(choice.isdigit() and 0<int(choice)<=len(fight_choice) ):
            if type(player.inventory[int(choice)-1])==Obj:
                elt=player.inventory[int(choice)-1].use()
                player.inventory.pop(int(choice)-1)
                player.use_item(elt)
                return f"You've gained {elt} HP"
        else:
            logs.add_log("Please choose a valid action")
            logs.print_logs()
    return VOID_MESS
    