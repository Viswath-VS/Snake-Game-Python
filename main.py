import turtle
import time
import random
# screen settings
wn = turtle.Screen()
wn.bgcolor('green')
wn.title('Snake game by Viswath')
wn.setup(width=500, height=500)
wn.tracer(0)
delay = 0.1
bodys = []
score = 0
high_score = 0
# snake head settings
head = turtle.Turtle()
head.speed(0)
head.color('black')
head.shape('square')
head.penup()
head.goto(0,0)
head.direction = 'stop'

# snake food settings
food = turtle.Turtle()
food.speed(0)
food.color('red')
food.shape('circle')
food.penup()
food.goto(random.randint(-240,240),random.randint(-240,240))

# score settings
pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.color('white')
pen.hideturtle()
pen.goto(0,200)
pen.write("Score: 0  Highscore: 0",align='center',font=('Courier',24,'normal'))

# movevements direction setting function
def go_up():
    if head.direction != 'down':
        head.direction = 'up'
def go_down():
     if head.direction != 'up':
        head.direction = 'down'
def go_left():
    if head.direction != 'right':
        head.direction = 'left'
def go_right():
    if head.direction != 'left':
        head.direction = 'right'

# keyboard bindings
wn.listen()
wn.onkeypress(go_up,'Up')
wn.onkeypress(go_down,'Down')
wn.onkeypress(go_left,'Left')
wn.onkeypress(go_right,'Right')

# move function
def move():
    if head.direction == 'up':
        head.sety(head.ycor()+20)
    if head.direction == 'down':
        head.sety(head.ycor()-20)
    if head.direction == 'left':
        head.setx(head.xcor()-20)
    if head.direction == 'right':
        head.setx(head.xcor()+20)

# game main loop
while True:
    wn.update()
  
    # snake boder movements
    if head.xcor() > 240:
        head.goto(-head.xcor(),head.ycor())
    elif head.xcor() < -240:
        head.goto(-head.xcor(),head.ycor())
    if head.ycor() > 240:
        head.goto(head.xcor(),-head.ycor())
    elif head.ycor() < -240:
        head.goto(head.xcor(),-head.ycor())
# snake and food collision
    if head.distance(food) < 20:
        food.goto(random.randint(-240,+240),random.randint(-240,+240))
        body_part = turtle.Turtle()
        body_part.speed(0)
        body_part.color('grey')
        body_part.shape('square')
        body_part.penup()
        bodys.append(body_part)
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {}  Highscore: {}".format(score,high_score),align='center',font=('Courier',24,'normal'))
# moving body parts along head
    for index in range(len(bodys)-1,0,-1):
         x = bodys[index-1].xcor()
         y = bodys[index-1].ycor()
         bodys[index].goto(x,y)

    if len(bodys) > 0:
         x = head.xcor()
         y = head.ycor()
         bodys[0].goto(x,y)
    
    time.sleep(delay)
    move()
# checking for head and body collision
    for body in bodys:
        if body.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            score=0
            pen.clear()
            pen.write("Score: {}  Highscore: {}".format(score,high_score),align='center',font=('Courier',24,'normal'))
# clearing the body parts after collision
            for body in bodys:
                body.goto(2000,2000)
            bodys.clear()



wn.mainloop()