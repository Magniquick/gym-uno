# gym-uno
Uno environment compatible with OpenAI gym

This takes the output from uno.jar and changes it into a OpenAI gym type format.

The step() function takes the action the algorithm gives and returns a set of observations, in this case
the points, amount of cards and the color last played of all three players, the card on top of the deck,
its color and the direction of play, and 10 of the player's own cards.

The action function then pipes the input to uno.jar and the feedback loop is ready.
