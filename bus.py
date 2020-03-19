from deck import *
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# If they are inside it is wrong
def inside_or_out(val1, val2, val3):
    if val1 == val2 or val2 == val3:
        return 2
    # Inside
    if val3 < val1 and val3 > val2:
        return 0
    if val3 < val2 and val3 > val1:
        return 0
    # outside
    return 1


def scatterPlot(result):
    xvalues = np.arange(len(result))
    df = pd.DataFrame({'Number of drinks': xvalues, 'probability': result})
    df.replace(0, np.nan).plot('Number of drinks', 'probability',
                               kind='scatter', title='The Perfect Game')
    plt.show()


def graphline(result, label):
    xvalues = np.arange(len(result))
    plt.figure(num='bus - pefect playing')
    plt.xlabel('Number of drinks consumed')
    plt.ylabel('Probability of Recieiving')
    line = pd.Series(data=result, index=xvalues)
    plt.xlim(0, 50)
    line.plot(label=label, legend=True, linewidth=5.0)


def play_memory_less():
    deck = Deck()
    playing = True
    rounds = 0
    while(playing):
        rounds += 1
        if deck.size() <= 4:
            deck = Deck()

            # Smoke or Fire, guess red or black, 50-50 chance
        guess = random.randint(0, 1)
        if guess == 0:
            color = 'black'
        else:
            color = 'red'
        card1 = deck.draw_card()
        if color != card1.color:
            continue

        # High or lower, if the last card is equal to 8, guess higher, otherwise guess lower
        if card1.value <= 8:
            guess = 1
        else:
            guess = 0

        card2 = deck.draw_card()
        if guess == 1:
            # If guesses higher, continue loop if lower
            if card1.value >= card2.value:
                continue
        else:
            # If guesses lower, continue loop if new card is higher
            if card1.value <= card2.value:
                continue

        # Attempt 3, inside or outside, guesses inside if gap is greater than 6
        gap = abs(card1.value - card2.value)
        card3 = deck.draw_card()
        actual = inside_or_out(card1.value, card2.value, card3.value)
        if actual == 2:
            # If cards match continute
            continue

        if gap <= 6:
            # 1 is outside
            guess = 1
        else:
            # 0 is inside
            guess = 0

        # Compare the actual to the reality
        if actual != guess:
            continue

        card4 = deck.draw_card()
        guess = random.randint(0, 3)
        if(guess == card4.type):
            # print("Congrats, you are off the bus")
            playing = False
    return rounds

# If you could count every card and play a perfect game


def play_perfectly():
    deck = Deck()
    playing = True
    rounds = 0
    while(playing):
        rounds += 1
        if deck.size() <= 4:
            deck = Deck()

        # Smoke or Fire, guess red or black, 50-50 chance
        guess = deck.guessColor()
        # print('color guess:', guess)
        card1 = deck.draw_card()
        #print('guess:', color, 'actual:', card1.color)
        if guess != card1.color:
            continue

        # High or lower, if the last card is equal to 8, guess higher, otherwise guess lower
        guess = deck.guessHighLow(card1.value)
        # print('highlow guess:', guess)
        card2 = deck.draw_card()
        if guess == 1:
            # If guesses higher, continue loop if lower
            if card1.value >= card2.value:
                continue
        else:
            # If guesses lower, continue loop if new card is higher
            if card1.value <= card2.value:
                continue
        #print('guessed correct, card2:', card2.value)
        # Attempt 3, inside or outside, guesses inside if gap is greater than 6)
        card3 = deck.draw_card()
        #print('card3:', card3.value)
        actual = inside_or_out(card1.value, card2.value, card3.value)
        #print('actual:', actual)
        if actual == 2:
            # If cards match continute
            continue

        # Counts the options
        guess = deck.guessInOut(card1.value, card2.value)
        # print('In-Out guess:', guess)
        # Compare the actual to the reality
        if actual != guess:
            continue
        #print('guessed correct, card3:', card3.value)

        card4 = deck.draw_card()
        guess = deck.guessType()
        #print('Type guess', guess)
        #print('card4.type:', card4.type)
        if(guess == card4.type):
            #print("Congrats, you are off the bus")
            playing = False
    return rounds
