from const import *


controls={"up": UP,"down": DOWN,"right": RIGHT,"left": LEFT,"interact": INTERACT,"drop item":DROP_ITEM,"QUIT": QUIT}
collision=False
key=""
chest_print=False
player_co=[BASE_PLAYER_CO_X,BASE_PLAYER_CO_Y] 
weapon={0:["Sword",10],1:["Hand Axe",15],2:["Lance",12]} # dont forget to increase NB_WEAPON if we add weapon