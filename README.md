# Ride The Bus

Drinking game where players get 4 trials, any failure results in a restart of the game and a single drink.

## Game
First Trial:
Smoke or Fire:
Player guesses a red or black card, and then is assigned one
If they are correct they move onto the next round

Second Trial:
Higher or Lower:
Player guesses if next card in shuffled deck is higher or lower than previous

Third Trial:
Inbetween or Outside:
Player guesses if the next card will be inbetween or outside the first pair

Fourth and Final Trial:
Guess the suit of the last card

## Program
card.py
- Contains a Card class that can be assigned a value, and face. Can return a copy, print and return a string clone

deck.py
- Contains a Deck class with 52 cards. Removes one at a time, randomly fro the array of cards to simulate a shuffuled deck. Functions: guessColor, guessHighlow, guessInOut, guessType, simply count the number of cards in the deck to come out with the optimal guess. (more in bus.py about this)

bus.py
- Contains functions for playing and graphing the simulation. play_memory_less() make 'logical' guesses based on the current round, not the deck of cards. play_perfectly() makes the 'optimal' guess using card counting basics. ScatterPlot() and graphLine() can show these functions and how they play out after thousands of trials.

main.py
- Runs the program and graphs 1000 iterations of play_memory_less and play_perfectly to calculate the drinking distribution for each strategy. To run write into your terminal ! python3 main.py


Problem:
- The play_memory_less() strategy works better than play_perfectly(). I do not understand exactly why this happens, but its very interesting. On average p_m_l() takes 13 drinks and p_p() is 16 drinks. I have checked everyline and I believe it is correct, just that in this situation the perfect solution of counting cards isn't the optimal one.
