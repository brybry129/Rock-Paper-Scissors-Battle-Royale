from turtle import Turtle, Screen
import random


PAPER_IMAGE = "paper.gif"
ROCK_IMAGE = "rock.gif"
SCISSOR_IMAGE = "scissors.gif"

PAPER_XRANGE = [50, 150]
ROCK_XRANGE = [-50, 50]
SCISSOR_XRANGE = [-50, -150]

PAPER_YRANGE = [50, 150]
ROCK_YRANGE = [-50, -150]
SCISSOR_YRANGE = [50, 150]

DIRECTION = (-5, 5)


class Objects:
    def __init__(self, num_objects):
        self.scissors = []
        self.papers = []
        self.rocks = []
        self.players = []
        screen = Screen()
        screen.addshape(SCISSOR_IMAGE)
        screen.addshape(ROCK_IMAGE)
        screen.addshape(PAPER_IMAGE)
        for _ in range(0, num_objects):
            self.create_scissors()
            self.create_rocks()
            self.create_papers()

    def create_scissors(self):
        scissor = Turtle()
        scissor.penup()
        scissor.shape(SCISSOR_IMAGE)
        new_x = random.randint(SCISSOR_XRANGE[1], SCISSOR_XRANGE[0])
        new_y = random.randint(SCISSOR_YRANGE[0], SCISSOR_YRANGE[1])
        scissor.goto(new_x, new_y)
        new_scissor = {
            "Type": "scissor",
            "Object": scissor,
            "X_move": random.uniform(-5, 5),
            "Y_move": random.uniform(-5, 5)
        }
        self.players.append(new_scissor)

    def create_rocks(self):
        rock = Turtle()
        rock.penup()
        rock.shape(ROCK_IMAGE)
        new_x = random.randint(ROCK_XRANGE[0], ROCK_XRANGE[1])
        new_y = random.randint(ROCK_YRANGE[1], ROCK_YRANGE[0])
        rock.goto(new_x, new_y)
        new_rock = {
            "Type": "rock",
            "Object": rock,
            "X_move": random.uniform(-5, 5),
            "Y_move": random.uniform(-5, 5)
        }
        self.players.append(new_rock)

    def create_papers(self):
        paper = Turtle()
        paper.penup()
        paper.shape(PAPER_IMAGE)
        new_x = random.randint(PAPER_XRANGE[0], PAPER_XRANGE[1])
        new_y = random.randint(PAPER_YRANGE[0], PAPER_YRANGE[1])
        paper.goto(new_x, new_y)
        new_paper = {
            "Type": "paper",
            "Object": paper,
            "X_move": random.uniform(-5, 5),
            "Y_move": random.uniform(-5, 5)
        }
        self.players.append(new_paper)

    def move_objects(self):
        for player in self.players:
            new_x = player["Object"].xcor() + player["X_move"]
            new_y = player["Object"].ycor() + player["Y_move"]
            player["Object"].goto(new_x, new_y)

    def check_bounce(self):
        for player in self.players:
            if player["Object"].ycor() > 280 or player["Object"].ycor() < -280:
                player["Y_move"] *= -1
            if player["Object"].xcor() > 280 or player["Object"].xcor() < -280:
                player["X_move"] *= -1

    def check_collision(self):
        for player in self.players:
            for i in range(1, len(self.players), 1):
                if player["Object"].distance(self.players[i]["Object"]) < 15:

                    player["X_move"] *= -1
                    player["Y_move"] *= -1
                    self.players[i]["X_move"] *= -1
                    self.players[i]["Y_move"] *= -1

                    # Check for rock and scissor collision
                    if player["Type"] == "rock" and self.players[i]["Type"] == "scissor":
                        self.players[i]["Object"].shape(ROCK_IMAGE)
                        self.players[i]["Type"] = "rock"

                    # Check rock and paper collision
                    elif player["Type"] == "rock" and self.players[i]["Type"] == "paper":
                        player["Object"].shape(PAPER_IMAGE)
                        player["Type"] = "paper"

                    # Check paper and scissor collision
                    elif player["Type"] == "paper" and self.players[i]["Type"] == "scissor":
                        player["Object"].shape(SCISSOR_IMAGE)
                        player["Type"] = "scissor"
