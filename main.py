from turtle import Screen
from Objects import Objects
import time

PAPER_IMAGE = "paper.gif"
ROCK_IMAGE = "rock.gif"
SCISSOR_IMAGE = "scissors.gif"

screen = Screen()
screen.setup(600, 600)
screen.addshape(SCISSOR_IMAGE)
screen.addshape(ROCK_IMAGE)
screen.addshape(PAPER_IMAGE)
screen.title("Rock Paper Scissors Battle Royale")
screen.tracer(0)

num_objects = screen.textinput("Battle Royale", "Enter number of participants: ")
objects = Objects(int(num_objects))
print(objects)
game_over = False
while not game_over:
    screen.update()
    time.sleep(0.01)
    objects.move_objects()
    objects.check_bounce()
    objects.check_collision()
    game_over, winner = objects.check_end_game()
    if game_over:
        num_objects = screen.textinput(f"WINNER: {winner}", "To play again enter number of participants")
        screen.clearscreen()
        objects.reset_game(int(num_objects))
        game_over = False

screen.exitonclick()
