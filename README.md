# Rock-Paper-Scissors with Adaptive Computer Opponent
## Overview
This project simulates a game of Rock-Paper-Scissors against an adaptive computer opponent. The computer learns and adapts its strategy based on the player's moves using a transition matrix.

## Features
- Adaptive computer opponent: The computer adjusts its strategy based on the player's moves.
- Limited rounds: The game continues until either 30 rounds are completed or the computer's score reaches 10.
- User-friendly interface: The player is prompted to input their move, and the game displays the result of each round.
## Dependencies
- NumPy: The project utilizes NumPy for numerical operations and array handling.
## Usage
1. Clone the repository to your local machine.
2. Ensure you have Python and NumPy installed.
3. Run the `play_game()` function from the `main.py` file.
4. Follow the on-screen instructions to play the game.
## How It Works
The game starts with a transition matrix representing the probabilities of the computer's moves (Rock, Paper, Scissors).
In each round, the player inputs their move, and the computer predicts its move based on the current transition matrix.
After both moves are made, the outcome of the round is determined, and the computer's score is updated.
The transition matrix is adjusted based on the player's move, and the game continues until the end conditions are met.
## Contributors
- Nikita Toropov
## License
This project is licensed under the <a href="https://opensource.org/licenses/MIT">MIT License</a>.