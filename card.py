class card():

    number = ""
    suit = ""
    faceup = False

    def __init__(self, number, suit, faceup):
        self.number = number
        self.suit = suit
        self.faceup = faceup

    def flip(self):
        if self.faceup == False:
            self.faceup = True
        else:
            self.faceup == False

    def show(self):
        print(self.number+" of "+self.suit)

 # Spades
S01 = card("A", "Spades", False)
S02 = card("2", "Spades", False)
S03 = card("3", "Spades", False)
S04 = card("4", "Spades", False)
S05 = card("5", "Spades", False)
S06 = card("6", "Spades", False)
S07 = card("7", "Spades", False)
S08 = card("8", "Spades", False)
S09 = card("9", "Spades", False)
S10 = card("10", "Spades", False)
S11 = card("J", "Spades", False)
S12 = card("Q", "Spades", False)
S13 = card("K", "Spades", False)
# Clubs
C01 = card("A", "Clubs", False)
C02 = card("2", "Clubs", False)
C03 = card("3", "Clubs", False)
C04 = card("4", "Clubs", False)
C05 = card("5", "Clubs", False)
C06 = card("6", "Clubs", False)
C07 = card("7", "Clubs", False)
C08 = card("8", "Clubs", False)
C09 = card("9", "Clubs", False)
C10 = card("10", "Clubs", False)
C11 = card("J", "Clubs", False)
C12 = card("Q", "Clubs", False)
C13 = card("K", "Clubs", False)
# Hearts
H01 = card("A", "Hearts", False)
# H02 = card("2", "Hearts", False)
H03 = card("3", "Hearts", False)
H04 = card("4", "Hearts", False)
H05 = card("5", "Hearts", False)
H06 = card("6", "Hearts", False)
H07 = card("7", "Hearts", False)
H08 = card("8", "Hearts", False)
H09 = card("9", "Hearts", False)
H10 = card("10", "Hearts", False)
H11 = card("J", "Hearts", False)
H12 = card("Q", "Hearts", False)
H13 = card("K", "Hearts", False)
# Diamonds
D01 = card("A", "Diamonds", False)
# D02 = card("2", "Diamonds", False)
D03 = card("3", "Diamonds", False)
D04 = card("4", "Diamonds", False)
D05 = card("5", "Diamonds", False)
D06 = card("6", "Diamonds", False)
D07 = card("7", "Diamonds", False)
D08 = card("8", "Diamonds", False)
D09 = card("9", "Diamonds", False)
D10 = card("10", "Diamonds", False)
D11 = card("J", "Diamonds", False)
D12 = card("Q", "Diamonds", False)
D13 = card("K", "Diamonds", False)
bJoker = card("Big", "Joker", False)
lJoker = card("Little", "Joker", False)
