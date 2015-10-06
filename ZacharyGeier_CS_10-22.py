import random

def pickCard():
    suit = random.randint(1,4)
    
    if suit == 1:   suit = "Spades"
    elif suit == 2: suit = "Clubs"
    elif suit == 3: suit = "Hearts"
    elif suit == 4: suit = "Diamonds"

    value = random.randint(1,13)

    if value == 13: value = "Ace"
    if value == 12: value = "King"
    if value == 11: value = "Queen"
    if value == 10: value = "Jack"   
    
    return value, suit

def findCards():
    numCardsDrawn = 0
    cardsFound = []
    suitsFound = []
    
    while len(cardsFound) < 4:
        isUnique = True
        card = pickCard()
        
        for s in suitsFound:
            if s == card[1]:
                isUnique = False

        if isUnique == True:
            suitsFound.append(card[1])
            cardsFound.append(card)
        
        numCardsDrawn += 1

    return cardsFound, numCardsDrawn

def main():
    foundCards = findCards()[0]
    numDrawn = findCards()[1]
    
    for i in range(4):
        print(str(foundCards[i][0]), 'of', foundCards[i][1])

    print('\n', numDrawn, "cards were drawn")

main()


