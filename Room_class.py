from var import *
from const import *
class Room():
    def __init__(self,right,left,up,down):
        self.right=right
        self.left=left
        self.up=up
        self.down=down
        self.inv=[]
        self.mobs=[]

    def show(self):
        #top
        if(self.up ==True):
            print((((WIDTH-2)//3)+2)*WALL + ((WIDTH-2)//3)*VOID + (((WIDTH-2)//3)+2)*WALL)
            for i in range((((HEIGHT-2)+1)//3)):
                print(WALL + (WIDTH-2)*VOID + WALL)
        else:
            print(WIDTH*WALL)
            for i in range((((HEIGHT-2)+1)//3)):
                print(WALL + (WIDTH-2)*VOID + WALL)
        
        #mid
        if self.left==True and self.right==True:
            for i in range((HEIGHT-2)//3):
                print(VOID + (WIDTH-2)*VOID + VOID)
        elif self.left==True and self.right==False:
            for i in range((HEIGHT-2)//3):
                print(VOID + (WIDTH-2)*VOID + WALL)
        elif self.left==False and self.right==True:
            for i in range((HEIGHT-2)//3):
                print(WALL + (WIDTH-2)*VOID + VOID)
        elif self.left==False and self.right==False:
            for i in range((HEIGHT-2)//3):
                print(WALL + (WIDTH-2)*VOID + WALL)
        
        #bottom
        if(self.down ==True):
            for i in range((((HEIGHT-2)+1)//3)):
                print(WALL + (WIDTH-2)*VOID + WALL)
            print((((WIDTH-2)//3)+2)*WALL + ((WIDTH-2)//3)*VOID + (((WIDTH-2)//3)+2)*WALL)
            
        else:
            for i in range((((HEIGHT-2)+1)//3)):
                print(WALL + (WIDTH-2)*VOID + WALL)
            print(WIDTH*WALL)

        
    def add_mob(self,mob):
        self.mobs.append(mob)    

    def add_item(self,item):
        self.inv.append(item)