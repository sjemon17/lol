import turtle
import random
import tkinter as tk

# Ustawienia ekranu
szerokosc = 800
wysokosc = 600

# Inicjalizacja ekranu
ekran = turtle.Screen()
ekran.title("Żółw na drodze")
ekran.setup(szerokosc, wysokosc)
ekran.bgcolor("green")

# Tworzenie żółwia
zolw = turtle.Turtle()
zolw.shape("turtle")
zolw.color("white")
zolw.penup()
zolw.goto(0, -wysokosc/2 + 30)
zolw.setheading(90)

# Tworzenie samochodów
samochody = []
kolory_samochodow = ["red", "blue", "orange", "yellow", "purple", "green"]
predkosc_samochodu = 5

for _ in range(10):
    samochod = turtle.Turtle()
    samochod.shape("square")
    kolor = random.choice(kolory_samochodow)
    samochod.color(kolor)
    samochod.penup()
    samochod.goto(random.randint(-szerokosc/2 + 20, szerokosc/2 - 20), random.randint(-wysokosc/2 + 50, wysokosc/2 - 50))
    samochody.append(samochod)

# Wyświetlanie wyniku
wynik = 0
wynik_pen = turtle.Turtle(
wynik_pen.color("white")
wynik_pen.penup()
wynik_pen.goto(-szerokosc/2 + 10, wysokosc/2 - 40)
wynik_pen.hideturtle()

# Komunikat przegranej
komunikat = turtle.Turtle()
komunikat.color("white")
komunikat.penup()
komunikat.goto(0, 0)
komunikat.hideturtle()

# Funkcja do poruszania żółwiem
def idz_do_gory():
    y = zolw.ycor()
    y += 20
    zolw.sety(y)

# Poruszanie żółwiem za pomocą klawiszy
ekran.listen()
ekran.onkeypress(idz_do_gory, "Up")

# Efekt kolizji
def efekt_kolizji():
    zolw.color("red")
    ekran.update()
    tk.messagebox.showinfo("PRZEGRAŁEŚ", "Koniec gry")
    zolw.color("white")

# Główna pętla gry
while True:
    ekran.update()

    # Poruszanie samochodami
    for samochod in samochody:
        x = samochod.xcor()
        x -= predkosc_samochodu
        samochod.setx(x)

        # Sprawdzenie kolizji
        if zolw.distance(samochod) < 20:
            efekt_kolizji()
            komunikat.write("PRZEGRAŁEŚ", align="center", font=("Arial", 24, "bold"))
            ekran.update()
            time.sleep(2)
            komunikat.clear()
            zolw.goto(0, -wysokosc/2 + 30)
            predkosc_samochodu = 5
            wynik = 0
            wynik_pen.clear()
            wynik_pen.write("Wynik: {}".format(wynik), align="left", font=("Arial", 16, "normal"))

    # Sprawdzenie, czy żółw przeszedł przez drogę
    if zolw.ycor() > wysokosc/2 - 20:
        zolw.goto(0, -wysokosc/2 + 30)
        wynik += 1
        wynik_pen.clear()
        wynik_pen.write("Wynik: {}".format(wynik), align="left", font=("Arial", 16, "normal"))

    # Sprawdzenie, czy samochody dotarły do lewej krawędzi ekranu
    for samochod in samochody:
        if samochod.xcor() < -szerokosc/2:
            samochod.goto(random.randint(szerokosc/2 - 20, szerokosc/2 - 20), random.randint(-wysokosc/2 + 50, wysokosc/2 - 50))
            predkosc_samochodu += 1

    # Tworzenie przycisku "Koniec"
    przycisk_koniec = tk.Button(text="Koniec", command=ekran.bye)
    przycisk_koniec_window = ekran.getcanvas().create_window(szerokosc/2 - 50, wysokosc/2 - 50, window=przycisk_koniec)
