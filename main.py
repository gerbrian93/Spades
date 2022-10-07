# imports
from tkinter import *
from card import card
from client import player
import random


root = Tk()
score1 = 0
score2 = 0


def exit():
    root.destroy()


def deal(a, b, c, d, e):
    x = 1
    for element in e:
        if x > 4:
            x = 1

        if x == 1:
            a.append(element)
        elif x == 2:
            b.append(element)
        elif x == 3:
            c.append(element)
        else:
            d.append(element)
        x = x + 1
    a.sort()
    b.sort()
    c.sort()
    d.sort()


def make_bids():
    return


def play_game():
    game = Toplevel(root)
    game.configure(bg="green")
    game.geometry("1020x720")
    game.title("♠ Spades ♠")
    game.resizable(False, False)

    i = 1
    j = 1
    k = 1
    l = 1
    deck = []
    while i < 14:
        deck.append("S"+str(i))
        i = i+1
    while j < 14:
        deck.append("C"+str(j))
        j = j+1
    while k < 14:
        deck.append("H"+str(k))
        k = k+1
    while l < 14:
        deck.append("D"+str(l))
        l = l+1
    # shuffles deck
    random.shuffle(deck)
    # print(deck)
    p1 = player("Danyelle", [], 0, "A")
    p2 = player("Brian", [], 0, "A")
    p3 = player("Lindsay", [], 0, "B")
    p4 = player("Grant", [], 0, "B")

    deal(p1.hand, p2.hand, p3.hand, p4.hand, deck)
    # players look at hands and make their bids

    while p1.hand != None and p2.hand != None and p3.hand != None and p4.hand != None:

        return


root.title("Card Game")
root.configure(bg="green")
root.geometry('850x600')
root.resizable(False, False)
Font_tuple = ("Algerian", 50, "bold")
Font_tuple2 = ("Cosmic Sans MS", 20, "bold")
Font_tuple3 = ("Cosmic Sans MS", 80, "bold")
# Created Labels
mainTitle = Label(root, text="Spades", font=Font_tuple,
                  background="green", pady=80)
leftSymbol = Label(root, text="♠", font=Font_tuple3,
                   background="green", padx=60, pady=80)
rightSymbol = Label(root, text="♠", font=Font_tuple3,
                    background="green", padx=60, pady=80)
space = Label(text=" ", background="green", padx=60)

playButton = Button(text="PLAY", padx=35, pady=5,
                    font=Font_tuple2, background="lightgreen", command=play_game)
exitButton = Button(text="EXIT", padx=35, pady=5,
                    font=Font_tuple2, background="lightgreen", command=exit)

space.grid(row=0, column=0)
mainTitle.grid(row=0, column=2)
leftSymbol.grid(row=0, column=1)
rightSymbol.grid(row=0, column=3)
playButton.grid(row=1, column=2)
exitButton.grid(row=2, column=2)
root.mainloop()
