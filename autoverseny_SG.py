import turtle
import random

class Auto_SG:
    def __init__(self, y_pos=-200):
        self.t = turtle.Turtle()
        self.t.shape("square")
        self.t.shapesize(stretch_len=1.5, stretch_wid=1)
        self.t.color("blue")
        self.t.penup()
        self.x_poziciok = [-150, -50, 50, 150]
        self.sav = 1
        self.t.goto(self.x_poziciok[self.sav], y_pos)

    def balra_SG(self):
        if self.sav > 0:
            self.sav -= 1
            self.t.goto(self.x_poziciok[self.sav], self.t.ycor())

    def jobbra_SG(self):
        if self.sav < len(self.x_poziciok) - 1:
            self.sav += 1
            self.t.goto(self.x_poziciok[self.sav], self.t.ycor())


class Akadaly_SG:
    def __init__(self, y_start=600):
        self.t = turtle.Turtle()
        self.t.shape("square")
        self.t.penup()
        self.x_poziciok = [-150, -50, 50, 150]
        self.y_start = y_start
        self.sebesseg = 5
        self.delay = random.randint(0, 10)
        self.ujra_SG()

    def ujra_SG(self):
        self.sav = random.choice([0, 1, 2, 3])
        szinek = ["red", "yellow", "green"]
        self.t.color(random.choice(szinek))
        self.t.goto(self.x_poziciok[self.sav], self.y_start)
        self.delay = random.randint(0, 10)

    def lefele_SG(self):
        if self.delay > 0:
            self.delay -= 1
            return
        self.t.sety(self.t.ycor() - self.sebesseg)


def utkozes_SG(auto: Auto_SG, akadaly: Akadaly_SG) -> bool:
    return auto.t.distance(akadaly.t) < 30
