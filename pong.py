import turtle

win = turtle.Screen()
win.title("Pong by Iulian Stratan")
win.bgcolor("black")
win.setup(height=700, width=1100)
win.tracer(0)# ce se intampla daca scot

#Score and pause var
score_a = 0
score_b = 0
is_paused = False

#Paddle A
pad_a=turtle.Turtle()
pad_a.speed(0)
pad_a.shape("square")
pad_a.color("darkorange")
pad_a.shapesize(stretch_wid=7, stretch_len=1)
pad_a.penup()
pad_a.goto(-500, 0)


#Paddle B
pad_b=turtle.Turtle()
pad_b.speed(0)
pad_b.shape("square")
pad_b.color("darkorange")
pad_b.shapesize(stretch_wid=7, stretch_len=1)
pad_b.penup()
pad_b.goto(500, 0)

#Ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("orange")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = 0.1

#Score
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 310)
pen.write("Player A: 0   Player B: 0", align="center", font=("Courier", 24, "normal"))


# Functions
def pad_a_up():
    y = pad_a.ycor()
    y += 20
    pad_a.sety(y)

def pad_a_down():
    y = pad_a.ycor()
    y -= 20
    pad_a.sety(y)

def pad_b_up():
    y = pad_b.ycor()
    y += 20
    pad_b.sety(y)

def pad_b_down():
    y = pad_b.ycor()
    y -= 20
    pad_b.sety(y)

def pause():
    global is_paused
    if is_paused ==True:
        is_paused= False
    else:
        is_paused = True

# Keyboard binding
win.listen()
win.onkeypress(pad_a_up, "w")
win.onkeypress(pad_a_down, "s")
win.onkeypress(pad_b_up, "Up")
win.onkeypress(pad_b_down, "Down")
win.onkeypress(pause, " ")

# Main game loop
while True:
    if not is_paused:
        win.update()

        # Ball movment
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        #Border check
        if ball.ycor() > 340:
            ball.sety(340)
            ball.dy *=-1
        
        if ball.ycor() < -340:
            ball.sety(-340)
            ball.dy *=-1
        
        if ball.xcor() > 540:
            ball.goto(0, 0)
            ball.dx = 0.1
            ball.dx *= -1
            score_a += 1
            pen.clear()
            pen.write("Payer A: {}   Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        
        if ball.xcor() < -540:
            ball.goto(0, 0)
            ball.dx = 0.1
            ball.dx *= -1
            score_b += 1
            pen.clear()
            pen.write("Payer A: {}   Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        
        # Paddle and ball collisions
        if (ball.xcor() > 480 and ball.xcor() < 500) and (ball.ycor() < pad_b.ycor() + 80 and ball.ycor() > pad_b.ycor() - 80):
            ball.setx(480)
            ball.dx +=0.03
            ball.dx *= -1

        if (ball.xcor() < -480 and ball.xcor() > -500) and (ball.ycor() < pad_a.ycor() + 80 and ball.ycor() > pad_a.ycor() - 80):
            ball.setx(-480)
            ball.dx -=0.03
            ball.dx *= -1
    else:
        win.update()