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
The game begins with an initial transition matrix that represents the probabilities of transitioning between states.
These states are determined by the outcome of the previous round and the opponent's move, encompassing combinations such as "Victory with Rock (VR)", "Victory with Paper (VP)", and "Victory with Scissors (VS)", as well as their corresponding losing states.
In each round, the player inputs their move, and the computer predicts its move based on the current transition matrix.
Once both moves are made, the round's outcome is determined, and the transition matrix is adjusted based on the player's move.
This iterative process continues until the game meets its end conditions.
## Contributors
- Nikita Toropov
## License
This project is licensed under the <a href="https://opensource.org/licenses/MIT">MIT License</a>.