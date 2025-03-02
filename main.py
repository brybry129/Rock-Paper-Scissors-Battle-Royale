from turtle import Screen
from Objects import Objects
import time

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)

num_objects = screen.textinput("Battle Royale", "Enter number of participants: ")
objects = Objects(int(num_objects))
print(objects)
game_over = False
while not game_over:
    screen.update()
    time.sleep(0.1)
    objects.move_objects()
    objects.check_bounce()
    objects.check_collision()

screen.exitonclick()
