from const import *


controls={"up": UP,"down": DOWN,"right": RIGHT,"left": LEFT,"interact": INTERACT,"drop item":DROP_ITEM,"use item":OPEN_INV,"QUIT": QUIT}
collision=False
key=""
chest_print=False
use_inv=False
player_co=[BASE_PLAYER_CO_X,BASE_PLAYER_CO_Y] 
weapon={0:["Sword",10],1:["Hand Axe",15],2:["Lance",12]} # dont forget to increase NB_WEAPON if we add weapon
mob={0:["Skeleton",60,20],1:["Zombie",50,15],2:["Ghoul",80,40]} # dont forget to increase NB_MOB if we add mob (name,PV,XP given)
fight_choice={0:[ATTACK,"Attack"],1:[RUN,"Run"]}
objects={0:["Potion",20],1:["Meat",30]}# dont forget to increase NB_OBJECT if we add object