from bus import *


def play_perfectly1():
    deck = Deck()
    playing = True
    rounds = 0
    while(playing):
        rounds += 1
        if deck.size() <= 4:
            deck = Deck()

        # Smoke or Fire, guess red or black, 50-50 chance
        guess = deck.guessColor()
        card1 = deck.draw_card()
        print(f'card1:', card1.toString())
        print('guess:', guess, 'actual:', card1.color)
        if guess != card1.color:
            continue

        # High or lower, if the last card is equal to 8, guess higher, otherwise guess lower
        guess = deck.guessHighLow(card1.value)
        print('highlow guess:', guess)
        card2 = deck.draw_card()
        print('card2', card2.toString())
        if guess == 1:  # high
            # If guesses higher, continue loop if lower
            if card1.value >= card2.value:
                continue
        else:  # low
            # If guesses lower, continue loop if new card is higher
            if card1.value <= card2.value:
                continue
        print('guessed correct, card2:', card2.value)
        # Attempt 3, inside or outside, guesses inside if gap is greater than 6)
        card3 = deck.draw_card()
        print('card3', card3.toString())
        actual = inside_or_out(card1.value, card2.value, card3.value)
        print('actual:', actual)
        if actual == 2:
            # If cards match continute
            continue

        # Counts the options
        guess = deck.guessInOut(card1.value, card2.value)
        print('In-Out guess:', guess)
        # Compare the actual to the reality
        if actual != guess:
            continue
        print('guessed correct, card3:', card3.value)

        card4 = deck.draw_card()
        guess = deck.guessType()
        print('Type guess', guess)
        print('card4', card4.toString())
        if(guess == card4.type):
            print("Congrats, you are off the bus")
            playing = False
    return rounds


print('drank', play_memory_less(), 'times')
print('drank', play_perfectly1(), 'times')
