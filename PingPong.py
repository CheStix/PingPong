import turtle
from gameobj import Rocket, GameField, Ball, Score

FONT = ('Arial', 44)
WIDTH = 1000
HEIGHT = 600

window = turtle.Screen()
window.title('Ping-Pong')
window.setup(width=0.8, height=0.8)
window.bgcolor('black')
window.tracer(2)

# game field
field = GameField(WIDTH, HEIGHT)
field.draw_field()

# first player
rocket_a = Rocket(WIDTH, HEIGHT)
rocket_a.goto(-WIDTH//2 + 50, 0)

# second player
rocket_b = Rocket(WIDTH, HEIGHT)
rocket_b.goto(WIDTH//2 - 50, 0)

# ball
ball = Ball()

# players score
score_a = Score(-WIDTH//4, HEIGHT//2, FONT)
score_b = Score(WIDTH//4, HEIGHT//2, FONT)

window.listen()
window.onkeypress(rocket_a.move_up, 'w')
window.onkeypress(rocket_a.move_down, 's')
window.onkeypress(rocket_b.move_up, 'Up')
window.onkeypress(rocket_b.move_down, 'Down')


while True:
    window.update()
    ball.move()

    if HEIGHT//2 - 10 <= ball.ycor() or ball.ycor() <= -HEIGHT//2 + 10:
        ball.dy = -ball.dy

    if ball.xcor() <= -WIDTH//2 + 10:
        score_b.goal()
        ball.restart()

    if ball.xcor() >= WIDTH//2 - 10:
        score_a.goal()
        ball.restart()

    if ball.check_hitting(rocket_a, rocket_b):
        ball.dx = -ball.dx

window.mainloop()
# TODO изменение скорости мяча
