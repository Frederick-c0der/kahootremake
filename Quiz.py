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
question=[]
HEIGHT=500
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
    screen.draw.textbox("Question", timebox, color="white")
    screen.draw.textbox(question[1], box1, color="black")
    screen.draw.textbox(question[2], box2, color="black")
    screen.draw.textbox(question[3], box3, color="black")
    screen.draw.textbox(question[4], box4, color="black")
    screen.draw.textbox("Question", r2, color="white")
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
    question=allquestions[currentquestion].split(",")
    print(question)
readquestions()
ifansweredcorrectly()
pgzrun.go()