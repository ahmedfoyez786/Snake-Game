from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 15
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]
        self.head.shape("turtle")

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_snake_segment(position)

    def add_snake_segment(self, position):
        snake_segment = Turtle("square")
        snake_segment.shapesize(stretch_wid=.7, stretch_len=.7)
        snake_segment.penup()
        snake_segment.color("white")
        snake_segment.goto(position)
        self.snake.append(snake_segment)

    def extend(self):
        self.add_snake_segment(self.snake[-1].position())

    def move(self):
        for segment in range(len(self.snake)-1, 0, -1):
            x = self.snake[segment - 1].xcor()
            y = self.snake[segment - 1].ycor()
            self.snake[segment].goto(x, y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
