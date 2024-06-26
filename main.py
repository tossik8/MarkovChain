"""
NumPy: Numerical Python.

NumPy provides support for multidimensional arrays, mathematical functions,
random number generation,linear algebra, Fourier transforms, and more.
See the documentation: https://numpy.org/doc/stable/
"""
import numpy as np
import numpy.typing as npt


def play_game() -> None:
    """
    Simulate a game of Rock-Paper-Scissors against an adaptive computer opponent.

    The game continues until either 30 rounds are completed or the computer's score reaches 10.

    Returns:
    -------
    None
    """
    transition_matrix = {
        'VR': np.array([1 / 6] * 6),
        'VP': np.array([1 / 6] * 6),
        'VS': np.array([1 / 6] * 6),
        'LR': np.array([1 / 6] * 6),
        'LP': np.array([1 / 6] * 6),
        'LS': np.array([1 / 6] * 6)
    }
    state = 'VR'
    i = 0
    score = 0
    while i < 30 and score < 10:
        i += 1
        opponent_move = ask_move()
        computer_move = predict_counter_move(transition_matrix[state])
        print('Opponent:', opponent_move, 'vs Computer:', computer_move)
        res = fight(opponent_move, computer_move)
        score += res
        new_state = determine_state(res, opponent_move)
        if new_state is not None:
            transitions = adjust_transitions(new_state, transition_matrix[state])
            transition_matrix[state] = transitions
            state = new_state
        print_round_results(res, score)


def determine_state(res: int, opponent_move: str) -> str | None:
    """
    Determines the state based on the result of the round and the opponent's move.

    Parameters:
    ----------
    res : int
        Result of the round: 1 for victory, 0 for tie, -1 for loss.
    opponent_move : str
        Opponent's move ('R', 'P', or 'S').

    Returns:
    -------
    str or None
        The determined state (V or L + the opponent's move).
        Returns None if the result is a tie.
    """
    if res == 1:
        return 'L' + opponent_move
    if res == -1:
        return 'V' + opponent_move
    return None


def ask_move() -> str:
    """
    Prompt the user to input a move (R for Rock, P for Paper, S for Scissors)
    and validate the input.

    Returns:
    -------
    str
        The valid move input by the user.
    """
    opponent_move = input('Make a move (R for Rock, P for Paper, S for Scissors): ')
    if opponent_move not in ('R', 'P', 'S'):
        print(opponent_move, 'is not a valid move')
        return ask_move()
    return opponent_move


def print_round_results(res: int, score: int) -> None:
    """
    Print the result of the current round and the computer's score.

    Parameters:
    ----------
    res : int
        Result of the round: 1 for victory, 0 for tie, -1 for loss.
    score : int
        Current score of the computer.

    Returns:
    -------
    None
    """
    if res == 1:
        print("Victory")
    elif res == 0:
        print("Tie")
    else:
        print("Loss")
    print('Computer\'s score:', score)
    print()


def predict_counter_move(transitions: npt.NDArray[np.float32]) -> str:
    """
    Predicts the counter move based on transition probabilities.

    Parameters:
    ----------
    transitions : npt.NDArray[np.float32]
        Transition probabilities for moves 'R', 'P', and 'S',
        and their corresponding victory/defeat transitions.

    Returns:
    -------
    str
        The predicted counter move ('R', 'P', or 'S').
    """
    move_probabilities = (transitions[0] + transitions[3],
                          transitions[1] + transitions[4],
                          transitions[2] + transitions[5])
    predicted_move = np.random.choice(['R', 'P', 'S'], p=move_probabilities)
    counter_move = get_counter_move(predicted_move)
    return counter_move


def adjust_transitions(new_state: str,
                       transitions: npt.NDArray[np.float32]) -> npt.NDArray[np.float32]:
    """
    Adjust transition probabilities based on the new state.

    Parameters:
    ----------
    new_state : str
        The new state.
    transitions : npt.NDArray[np.float32]
        Array containing transition probabilities.

    Returns:
    -------
    npt.NDArray[np.float32]
        Updated transition probabilities.
    """
    states = ('VR', 'VP', 'VS', 'LR', 'LP', 'LS')
    for i, state in enumerate(states):
        if state == new_state:
            transitions[i] += transitions[i] * 0.05
        else:
            transitions[i] -= transitions[i] * 0.01
    transitions /= transitions.sum()
    return transitions


def fight(opponent_move: str, computer_move: str) -> int:
    """
    Determine the outcome of a rock-paper-scissors fight.

    Parameters:
    ----------
    opponent_move : str
        The opponent's move ('R', 'P', or 'S').
    computer_move : str
        The computer's move ('R', 'P', or 'S').

    Returns:
    -------
    int
        1 if the computer wins, 0 if it's a tie, -1 if the opponent wins.
    """
    if opponent_move == 'R' and computer_move == 'P':
        return 1
    if opponent_move == 'P' and computer_move == 'S':
        return 1
    if opponent_move == 'S' and computer_move == 'R':
        return 1
    if computer_move == opponent_move:
        return 0
    return -1


def get_counter_move(predicted_move: str) -> str:
    """
    Get the counter move for a given predicted move.

    Parameters:
    ----------
    predicted_move : str
        The predicted move ('R', 'P', or 'S').

    Returns:
    -------
    str
        The counter move ('R', 'P', or 'S').
    """
    if predicted_move == 'R':
        return 'P'
    if predicted_move == 'P':
        return 'S'
    return 'R'


if __name__ == '__main__':
    play_game()
