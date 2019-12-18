from turtle import Turtle
from random import choice, randint


class GameField(Turtle):
    def __init__(self, width, height):
        super().__init__()
        self.speed(0)
        self.color('green')
        self.field_width = width
        self.field_height = height
        self.hideturtle()

    def draw_field(self):
        x = self.field_width // 2
        y = self.field_height // 2
        self.begin_fill()
        self.goto(-x, y)
        self.goto(x, y)
        self.goto(x, -y)
        self.goto(-x, -y)
        self.goto(-x, y)
        self.end_fill()
        self.draw_line()

    def draw_line(self):
        size = self.field_height // 25
        self.goto(0, self.field_height // 2)
        self.color('white')
        self.setheading(270)
        for i in range(25):
            if i % 2:
                self.forward(size)
            else:
                self.up()
                self.forward(size)
                self.down()


class Rocket(Turtle):
    def __init__(self, width, height):
        super().__init__()
        self.color('white')
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.field_width = width
        self.field_height = height
        self.score = 0
        self.penup()
        # self.goto()

    def move_up(self):
        if self.ycor() < self.field_height//2-50:
            self.sety(self.ycor() + 10)

    def move_down(self):
        if self.ycor() > - (self.field_height//2-50):
            self.sety(self.ycor() - 10)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.shape('circle')
        self.color('red')
        self.dx = -0.5
        self.dy = 0.5
        self.penup()

    def move(self):
        self.setx(self.xcor() + self.dx)
        self.sety(self.ycor() + self.dy)

    def restart(self):
        self.goto(0, randint(-100, 100))
        self.dx = choice([-0.5, -0.4, -0.3, 0.3, 0.4, 0.5])
        self.dy = choice([-0.5, -0.4, -0.3, 0.3, 0.4, 0.5])

    def check_hitting(self, rocket_a, rocket_b):
        if self.dx > 0:
            return (rocket_b.ycor()-50 <= self.ycor()+10 <= rocket_b.ycor()+50) and (self.xcor() >= rocket_b.xcor()-10)
        else:
            return (rocket_a.ycor()-50 <= self.ycor()+10 <= rocket_a.ycor()+50) and (self.xcor() <= rocket_a.xcor()+10)


class Score(Turtle):
    def __init__(self, pos_x, pos_y, font=('Arial', 44)):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.penup()
        self.setposition(pos_x, pos_y)
        self.point = 0
        self.font = font
        self.write(0, font=self.font)

    def goal(self):
        self.point += 1
        self.clear()
        self.write(self.point, font=self.font)


