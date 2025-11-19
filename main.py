import turtle
import random
from autoverseny_SG import Auto_SG, Akadaly_SG, utkozes_SG

screen = turtle.Screen()
screen.setup(width=450, height=500)
screen.title("Autóverseny SG")
screen.bgcolor("gray")
screen.tracer(0, 0)

jatek_megy = True
pont = 0
akadalyok = None
jatekos = None

def uj_jatek():
    global jatek_megy, pont, akadalyok, jatekos
    jatek_megy = True
    pont = 0

    jatekos = Auto_SG()
    akadaly1 = Akadaly_SG()
    akadaly2 = Akadaly_SG()
    akadalyok = [akadaly1, akadaly2]

    akadaly1.sebesseg = 5
    akadaly2.sebesseg = 6

    akadaly1.delay = 0
    akadaly2.delay = 5

    print("Új játék indult. Sebesség:", akadalyok[0].sebesseg)
    frissites()

jatekos = Auto_SG()
akadaly1 = Akadaly_SG()
akadaly2 = Akadaly_SG()
akadalyok = [akadaly1, akadaly2]

akadaly1.sebesseg = 5
akadaly2.sebesseg = 6

akadaly1.delay = 0
akadaly2.delay = 5

def balra():
    if jatek_megy:
        jatekos.balra_SG()

def jobbra():
    if jatek_megy:
        jatekos.jobbra_SG()

def kilep():
    screen.bye()

def frissites():
    global jatek_megy, pont, akadalyok

    if not jatek_megy:
        return

    for i, akadaly in enumerate(akadalyok):
        akadaly.lefele_SG()

        if akadaly.t.ycor() < -250:
            akadaly.ujra_SG()
            pont += 1
            print("Pont:", pont)

            if pont > 0 and pont % 5 == 0:
                for a in akadalyok:
                    a.sebesseg += 1
                print("Gyorsulás!")

            for j, masik in enumerate(akadalyok):
                if j == i:
                    continue
                if masik.t.ycor() > 0 and akadaly.sav == masik.sav:
                    lehetseges = [0, 1, 2, 3]
                    lehetseges.remove(masik.sav)
                    uj_sav = random.choice(lehetseges)
                    akadaly.sav = uj_sav
                    akadaly.t.goto(akadaly.x_poziciok[uj_sav], akadaly.y_start)

        if utkozes_SG(jatekos, akadaly):
            print("Ütközés! Játék vége. Végeredmény:", pont, "pont")
            jatek_megy = False
            break

    screen.update()
    screen.ontimer(frissites, 30)

screen.listen()
screen.onkey(balra, "Left")
screen.onkey(jobbra, "Right")
screen.onkey(kilep, "q")
screen.onkey(uj_jatek, "r")

frissites()
screen.mainloop()
