import turtle ,time
R = False ; L = False ; Jump_bt = False
Last_Jump = time.time()
Can_Jump = True
class Player:
    

    def Get_Values(self=None):
        return R,L,Jump_bt

    def Right(self=None):
        global R , L
        R = True
        L = False

    def Left(self=None):
        global L , R
        L = True
        R = False

    def Jump_release(self=None):
        global Jump_bt
        Jump_bt = False

    def Jump(self=None):
        global Jump_bt , Last_Jump
        if abs(Last_Jump - time.time()) > 1:
            Jump_bt = True
            Last_Jump = time.time()
        


    def Left_release(self=None):
        global L
        L = False

    def Right_release(self=None):
        global R
        R = False


    def Create(self=None):
        Player = turtle.Turtle()
        Player.color("red")
        Player.shape("square")
        Player.penup()
        Player.speed(0)  
        Player.penup()
        Player.goto(0,0)
        Player.direction = "stop"
        return Player

    
    def Physics(self=None):
        Gravity = 3
        Mass = 1
        Jump_Height = 5
        Speed= 2
        return Gravity , Mass , Jump_Height , Speed


def Get_Colour(self=None,Colour=None):
    Colour_dict = {
        "r" : "red",
        "w" : "white",
        "b" : "black",
        "B" : "blue",
        "R" : "royal blue",
        "o" : "orange red",
        "i" : "indigo",
        "g" : "gold",
        "v" : "dark violet"
    }
    return Colour_dict[Colour]

class Floor_Tile:
    def Create(self=None,X=None,Y=None,SX=None,SY=None,floors=None,Col=None):
        floor = turtle.Turtle()  
        Col = Get_Colour(None,Col)
        floor.color(Col)
        floor.shape("square")
        floor.penup()
        floor.speed(0)  
        floor.penup()
        floor.goto(X,Y)
        floor.shapesize(SX,SY,None) # 1 ~ 20
        floor.direction = "stop"


        floors[floor] = [floor.shapesize()[0] * 10 , floor.shapesize()[1] * 10 , (floor.shapesize()[0] * 10) + 10 , (floor.shapesize()[1] * 10) + 10 , (floor.shapesize()[0] * 10) - 10]
        #floors.insert(0,floor)

class Spike_Tile:
    def Create(self=None,X=None,Y=None,SX=None,SY=None,floors=None,Col=None):
        Spike = turtle.Turtle()  
        Col = Get_Colour(None,Col)
        Spike.color(Col)
        Spike.shape("triangle")
        Spike.penup()
        Spike.speed(0)  
        Spike.penup()
        Spike.goto(X,Y-20)
        Spike.right(-90)
        Spike.shapesize(SX,SY,None) # 1 ~ 20
        Spike.direction = "stop"
        floors[Spike] = [Spike.shapesize()[0] * 10 , Spike.shapesize()[1] * 10 , (Spike.shapesize()[0] * 10) + 10 , (Spike.shapesize()[1] * 10) + 10 , (Spike.shapesize()[0] * 10) - 10]
        #floors.insert(0,Spike)
   
class Exit_Tile:
    def Create(self=None,X=None,Y=None,SX=None,SY=None,floors=None,Col=None):
        Exit = turtle.Turtle()  
        Col = Get_Colour(None,Col)
        Exit.color(Col)
        Exit.shape("circle")
        Exit.penup()
        Exit.speed(0)  
        Exit.penup()
        Exit.goto(X,Y)
        Exit.shapesize(SX,SY,None) # 1 ~ 20
        Exit.direction = "stop"
        floors[Exit] = [Exit.shapesize()[0] * 10 , Exit.shapesize()[1] * 10 , (Exit.shapesize()[0] * 10) + 10 , (Exit.shapesize()[1] * 10) + 10 , (Exit.shapesize()[0] * 10) - 10]
        #floors.insert(0,Exit)