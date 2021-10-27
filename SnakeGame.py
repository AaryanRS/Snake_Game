import turtle
import time
import random

#Screen
screen = turtle.Screen()
screen.title("! Snake Game !")
screen.setup(width=700, height=700)
screen.tracer(0)
turtle.bgcolor("turquoise")

t = turtle.Turtle()

#Border   
t.speed(5)
t.pensize(7)
t.penup()
t.goto(-310,250)
t.pendown()
t.pencolor("red")
t.forward(600)
t.right(90)
t.forward(500)
t.right(90)
t.forward(600)
t.right(90)
t.forward(500)
t.penup()
t.hideturtle()

#Snake
snake = turtle.Turtle()
snake.speed(0)
snake.penup()
snake.color("black")
snake.goto(0,0)
snake.shape("square")
snake.direction = "stop"

#Food
food = turtle.Turtle()
food.shape("circle")
food.speed(0)
food.penup()
food.goto(30,30)
food.color("dark blue")

#Variables
score = 0
old_fruit = []
delay = 0.1

##scoring
scoring = turtle.Turtle()
scoring.hideturtle()
scoring.speed(0)
scoring.penup()
scoring.goto(0,300)
scoring.color("black")
scoring.write("Score: 0", align="center", font=("times",24, "italic"))

def snake_up ():
    if snake.direction != "down":
        snake.direction ="up"

def snake_down ():
    if snake.direction != "up":
        snake.direction = "down"

def snake_right ():
    if snake.direction != "left":
        snake.direction = "right"

def snake_left ():
    if snake.direction != "right":
        snake.direction = "left"

def snake_move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y +20)

    elif snake.direction == "down":
        y = snake.ycor()
        snake.sety(y -20)

    elif snake.direction == "right":
        x = snake.xcor()
        snake.setx(x +20)

    elif snake.direction == "left":
        x = snake.xcor()
        snake.setx(x -20)

#key binding
screen.listen()
screen.onkeypress(snake_up, "Up")
screen.onkeypress(snake_down,"Down")
screen.onkeypress(snake_right,"Right")
screen.onkeypress(snake_left, "Left")

while True :
    screen.update()
    
    #snake and fruitcollision
    if snake.distance(food) < 20 :
        x = random.randint(-290, 270)
        y = random.randint(-240, 240)

        food.goto(x,y)

        scoring.clear()
        score += 1
        scoring.write(f"Score: {score}", align = "center", font=("times",24,"italic"))
        delay -= 0.001

        #create turtle to put at the end of snake
        new_turtle=turtle.Turtle()
        new_turtle.speed(0)
        new_turtle.shape("square")
        new_turtle.color("black")
        new_turtle.penup()

        old_fruit.append(new_turtle)

        #adding height to snake

    for i in range(len(old_fruit)-1,0,-1) :
            x = old_fruit[i - 1].xcor()
            y = old_fruit[i - 1].ycor()

        
            old_fruit[i].goto(x,y)

    if len(old_fruit) > 0:
            x =snake.xcor()
            y =snake.ycor()

            old_fruit[0].goto(x,y)

    snake_move()

        #snake and border collision

    if snake.xcor() > 280 or snake.xcor() < -300 or snake.ycor() > 240 or snake.ycor() < -240 :
            time.sleep(1)
            screen.clear()
            screen.bgcolor('blue')
            scoring.goto(0,0)
            scoring.write(f"    Game Over \n Your Score is {score}",align="center", font=("times",24,"italic"))

    for fruit in old_fruit :
        if fruit.distance(snake) < 20 :
                time.sleep(1)
                screen.clear()
                screen.bgcolor("turquoise")
                scoring.goto(0,0)
                scoring.write(f"    Game Over \n Your Score is {score}",align="center", font=("times",24,"italic"))
                

    time.sleep(delay)

turtle.Terminator()
