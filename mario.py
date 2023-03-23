import turtle , Gameobjects , time , Map , threading

screen_height = 800
screen_width = 800


wn = turtle.Screen()
wn.title("Game")
wn.bgcolor("black")
wn.setup(width=screen_width, height=screen_height)
wn.tracer(0)


text = turtle.Turtle()
text.hideturtle()
text.goto(screen_width/2 - 110,screen_height/2 - 23)
text.color('white')
style = ('Comic Sane', 15)
text.write('Score:', font=style, align='center')
text.penup()


floors = {}
X = 0
Y = -100
Check = abs(Y)

def Map_Create():

    Objects_Dict = {
        "#" : Gameobjects.Floor_Tile,
        "S" : Gameobjects.Spike_Tile,
        "E" : Gameobjects.Exit_Tile,
    }

    global X , Y , Player , Player_Obj
    Y = -100 * len(Map.Level1)

    for i in reversed(range(len(Map.Level1))):
        for j in range(len(Map.Level1[i])):

            if Map.Level1[i][j][0] in Objects_Dict:
                GameObject = Objects_Dict[Map.Level1[i][j][0]]
                try:
                    GameObject.Create(None,X,Y,5,5,floors,Map.Level1[i][j][1])
                except:  
                    GameObject.Create(None,X,Y,5,5,floors,"w")   
                    
            X += 100
        Y += 100
        X = 0

    Player = Gameobjects.Player
    Player_Obj = Player.Create()


Map_Create()



def Death():
    global floors
    for Object in floors:
        Object.ht() ; Object.clear()
        #floors.pop(Object)

        #Map_Create()
    
    Player_Obj.ht() ; Player_Obj.clear()
    floors = {}
    Map_Create()



def floor_col():
    global Down , Counter 

    Hit = False
    for floor in floors:
        if floor.color()[0] == "dark violet" or floor.color()[0] == "gold": continue
        
        Shape_size = floors[floor][0]
        #Shape_Width = floors[floor][1]
        Top =  floors[floor][2]
        Side = floors[floor][3]
        Bottom = floors[floor][4]

        if floor.pos()[1] + Top >= Player_Obj.pos()[1] and floor.pos()[1] + Top <= Player_Obj.pos()[1] + Check and floor.pos()[0] + Side > Player_Obj.pos()[0] and floor.pos()[0] - Side < Player_Obj.pos()[0]:
            
            #print("collide ",floor.pos()[1] + Top,"---",Player_Obj.pos()[1])
            
            #print(floor.pos()[0] + Side ,"--", Player_Obj.pos()[0])
            #print(floor.pos(),"--",Player_Obj.pos())
            Hit = True
            
            break
        elif floor.pos()[1] - Bottom > Player_Obj.pos()[1] and abs(floor.pos()[1] - Player_Obj.pos()[1]) < Shape_size + 1 and floor.pos()[0] + Side > Player_Obj.pos()[0] and floor.pos()[0] - Side < Player_Obj.pos()[0]:
            #print(floor.pos()[1] - Bottom,"--",Player_Obj.pos()[1] + Shape_size )
           # print("below")   
            Player_Obj.goto(Player_Obj.xcor(),Player_Obj.ycor() - 10)
            Hit = False
        else:
            Hit = False


    if Hit == True:
        if floor.pos()[1] + Top / 2 + floor.shapesize()[1] * 4> Player_Obj.pos()[1] and abs(floor.pos()[0] - Player_Obj.pos()[0]) < Side:
            if Output[0]:
                Player_Obj.goto(Player_Obj.xcor() - 10, Player_Obj.ycor())
                #Pos_Update(floor,-10)
            else:
                Player_Obj.goto(Player_Obj.xcor() + 10, Player_Obj.ycor())
                #Pos_Update(floor,10)
            Hit = False
        
    if Hit == True:
        Gameobjects.Can_Jump = True
        Counter = 0

    return Hit , floor

UpForce = 0.1
def Pos_Update(OB,offset = None):


        

    if Output[0]: 
        PosX = -Physics[3]
    elif Output[1]:
        PosX = Physics[3]
    else:
        PosX = 0


    if offset:
        PosX = offset
    PosY = 0
    if Output[2]:
        PosY = -Physics[2]
        for i in floors:
            i.goto(i.pos()[0] + PosX,i.pos()[1] + PosY)
    else:
       PosY = Physics[0]    

    if Player_Obj.ycor() < 1:
       PosY = UpForce * 20
    elif Player_Obj.ycor() > 1:
       PosY = -UpForce



    #print(PosY)
    #print(PosX,PosY,"--",Player_Obj.pos()[0],Player_Obj.pos()[1])
    if floor_col()[0] == True:
        for i in floors:
            i.goto(i.pos()[0] + PosX,i.ycor())
    else:
        for i in floors:
            i.goto(i.pos()[0] + PosX,i.pos()[1] + PosY)

    



wn.onkeypress(Player.Jump, "w")
wn.onkeypress(Player.Right, "d")
wn.onkeypress(Player.Left, "a")
wn.onkeypress(Player.Jump, "space")

wn.onkey(Player.Jump_release,"w")
wn.onkey(Player.Right_release,"d")
wn.onkey(Player.Left_release,"a") 
wn.onkey(Player.Jump_release,"space")


wn.listen()


print("play")
#print(floor.shapesize()[0])

Jump_start = False
last_Jump = time.time()
countedFrames = 0
Counter = 0
start_time = time.time()
frames = []


while 1:
    wn.update()
    Down = Gameobjects.Can_Jump
    Output = Player.Get_Values()
    Physics = Player.Physics()




    fpsTimer = time.time()
    avgFPS = countedFrames / ( fpsTimer - start_time)


    text.clear()
    score_text = 'FPS '+str(avgFPS)[:5]
    text.write(score_text, font=style, align='center')

    #if Output[0] == True:
    #    Player_Obj.goto(Player_Obj.xcor()+Physics[3],Player_Obj.ycor())
    #if Output[1] == True:
    #    Player_Obj.goto(Player_Obj.xcor()-Physics[3],Player_Obj.ycor())
    if Gameobjects.Can_Jump == False:
        Counter += 1
        if Counter > 25:
            Player.Jump_release()
    '''
    if Player_Obj.ycor() < 15:
        Player_Obj.goto(Player_Obj.xcor(),Player_Obj.ycor() + UpForce * 10)
    elif Player_Obj.ycor() > 15:
        Player_Obj.goto(Player_Obj.xcor(),Player_Obj.ycor() - UpForce * 10)
    '''
    if Player_Obj.xcor() < 1:
        Player_Obj.goto(Player_Obj.xcor() + UpForce * 10,Player_Obj.ycor())
    elif Player_Obj.xcor() > 1:
        Player_Obj.goto(Player_Obj.xcor() - UpForce * 10,Player_Obj.ycor())    

    if Output[2] == True:
        Player_Obj.goto(Player_Obj.xcor(),Player_Obj.ycor()+Player.Physics()[2])
        Gameobjects.Can_Jump = False
        last_Jump = time.time()



    #Gravity
    if floor_col()[0] == False and abs(last_Jump -time.time()) > 0.1:
        Gameobjects.Can_Jump = False
        Player_Obj.goto(Player_Obj.xcor(),Player_Obj.ycor()-Physics[0])


    Pos_Update(list(floors)[0])

    if (floor_col()[1].shape() == "triangle"):
        Death()

    
    countedFrames += 1
    #time.sleep(0.01)


#def While_Loop():
#    while True:
#        print("he")

#Position_Update_Thread = threading.Thread(target=Pos_Update, args=(floors[0],),daemon=True)
#Position_Update_Thread = threading.Thread(target=While_Loop)
#Position_Update_Thread.start()
    

wn.mainloop()

