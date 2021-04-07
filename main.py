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

# movevements direction setting function
def go_up():
    head.direction = 'up'
def go_down():
    head.direction = 'down'
def go_left():
    head.direction = 'left'
def go_right():
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
    time.sleep(delay)
    move()
    if head.xcor() > 240:
        head.goto(-head.xcor(),head.ycor())
    elif head.xcor() < -240:
        head.goto(-head.xcor(),head.ycor())
    if head.ycor() > 240:
        head.goto(head.xcor(),-head.ycor())
    elif head.ycor() < -240:
        head.goto(head.xcor(),-head.ycor())

    if head.distance(food) < 20:
        food.goto(random.randint(-240,+240),random.randint(-240,+240))
wn.mainloop()