from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(.1)
    snake.move()
    # Detect collision with food
    if snake.head.distance(food) < 17:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.ycor() < -290 or snake.head.ycor() > 290 or snake.head.xcor() < -290:
        scoreboard.game_over()
        is_game_on = False

    # Detect collision with tail
    for segment in snake.snake[1:]:
        if snake.head.distance(segment) < 7:
            is_game_on = False
            scoreboard.game_over()


screen.exitonclick()


