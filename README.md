Tic Tac Toe is a classic two-player game. It is a simple yet engaging game played on a 3x3 grid.The objective is straightforward: be the first to form a line of three of your symbols in a horizontal, vertical, or diagonal row.In Tic Tac Toe, each player takes a turn placing their designated symbol, usually "X" or "O," on an empty grid space. The strategic challenge lies within anticipating your opponent's moves while planning your own to create winning combinations.
In this report, we are going to explain how we implement it on pyhon.

The code of this game is written in separated modules, because it enhances the code organization, readability, and maintainability. Each module has a specific responsibility, making it easier to understand and modify individual components without affecting the entire program.
The code is organized into four modules: game_logic.py, ui_functions.py, game_setup.py, and main.py.
_main.py
The main.py module acts as the entry point to the program. It imports functions from the other modules and sets up the Tkinter window. It initializes the list of players, selects a starting player, creates the UI elements (label, restart button, and game buttons), and starts the Tkinter main loop.
_ui_functions.py
This module includes functions for creating and configuring the label (create_label), restart button (create_restart_button), and game buttons (create_game_buttons). These functions use the Tkinter library to create and configure UI elements. The create_game_buttons function also takes the next_turn function as a parameter to connect the button actions to the game logic.
_game_logic.py
This module contains functions related to the game's logic. These functions include determining the next turn (next_turn), checking for a winner (check_winner), and checking for empty spaces (check_empty_spaces). Each of these functions takes the game buttons (game_btns) as parameters to perform their logic. The next_turn function also takes additional parameters such as the current player, a list of players, the label, and the selected row and column.
_game_setup.py
The game_setup.py module is responsible for initializing or resetting the game. The start_new_game function takes parameters such as the list of players, the label, game buttons, and the next_turn function. It sets up a new game by randomly choosing a starting player, updating the label, and clearing the game buttons.
