import pgzrun
WIDTH=800
r2=Rect(0,0, 800,80)
qbox=Rect(10,100, 600,125)
timebox=Rect(630,100, 125,125)
box1=Rect(20,250, 280,100)
box2=Rect(20,370, 280,100)
box3=Rect(330,250, 280,100)
box4=Rect(330,370, 280,100)
skipbox=Rect(630,250, 125, 225)
allquestions=[]
currentquestion=0
numofquestion=0
Score=0
boxes=[box1,box2,box3,box4]
Time=60
question=[]
HEIGHT=500
gamefin=False
def draw():
    screen.fill("black")
    screen.draw.filled_rect(r2, "black")
    screen.draw.filled_rect(qbox, "dark blue")
    screen.draw.filled_rect(timebox, "dark blue")
    screen.draw.filled_rect(box1, "dark orange")
    screen.draw.filled_rect(box2, "dark orange")
    screen.draw.filled_rect(box3, "dark orange")
    screen.draw.filled_rect(box4, "dark orange")
    screen.draw.filled_rect(skipbox, "dark green")
    
    screen.draw.textbox(question[0], qbox, color="white")
    screen.draw.textbox(str(Time), timebox, color="white")
    screen.draw.textbox(question[1], box1, color="black")
    screen.draw.textbox(question[2], box2, color="black")
    screen.draw.textbox(question[3], box3, color="black")
    screen.draw.textbox(question[4], box4, color="black")
    screen.draw.textbox("Answer the question to win the game", r2, color="white")
    screen.draw.textbox("Skip", skipbox, color="black", angle=90)
def readquestions():
    global allquestions
    global numofquestion
    file=open("questions.txt", "r")
    allquestions=file.readlines()
    numofquestion=len(allquestions)
def ifansweredcorrectly():
    global currentquestion
    global question
    if currentquestion<numofquestion:
        question=allquestions[currentquestion].split(",")
    else:
        gameover()
def on_mouse_down(pos):
    global currentquestion
    global Score
    if gamefin==False:
        if boxes[int(question[5])-1].collidepoint(pos):
            currentquestion+=1
            Score+=1
            ifansweredcorrectly()
        elif skipbox.collidepoint(pos):
            currentquestion+=1
            ifansweredcorrectly()
        else:
            gameover()
    else:
        gameover()
def gameover():
    global question
    global gamefin
    question=["Game over", "-", "-", "-", "-", "5"]
    gamefin=True
def timer():
    global Time
    global gamefin
    if gamefin==False:
        if Time>0:
            Time-=1
        else:
            gameover()
clock.schedule_interval(timer, 1)
def update():
    r2.x-=2
    if r2.x==-800:
        r2.x=1000
readquestions()
ifansweredcorrectly()
pgzrun.go()