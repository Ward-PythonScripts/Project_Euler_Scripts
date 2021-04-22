import math as m
import time

#TODO: the program doesn't work yet my dude, strangely enough it says in the solution a deck would only take 8 perfect shuffles to be perfectly ordened again and this is clearly not the case
#There are 13 cards of each suit in a deck of cards making a deck 52 cards long
def genDeck():
    deck = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    allDecks = []
    for x in ["A","B","C","D"]:
        row = []
        for i in range(len(deck)):
            #row.append(x+str(deck[i]))
            allDecks.append(x+str(deck[i]))
        #allDecks.append(row)
        #row = []
    #print(allDecks)
    return allDecks

def genSimpleDeck():
    deck = [0,1,2,3]
    allDecks = []
    for x in ["A","B"]:
        for i in range(len(deck)):
            allDecks.append(x + str(deck[i]))
    return allDecks

def genDeckeroonie():
    deck = []
    for x in range(52):
        deck.append(str(x))
    return deck
def shuffle(lst):
    a = lst[0:m.ceil(len(lst)/2)]
    b = lst[m.ceil(len(lst)/2):len(lst)]

    deck = []
    for i in range(len(a)):
        deck.append(a[i])
        deck.append(b[i])
    return deck



#main

deck = genDeckeroonie()
print(deck)
originalDeck = deck.copy()
counter = 1
deck = shuffle(deck)
print(deck)
while deck != originalDeck and counter < 100:
    deck = shuffle(deck)
    print(deck)
    counter += 1
print(counter)



