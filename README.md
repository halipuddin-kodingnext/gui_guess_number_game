# GUI Guess Number Game

A simple graphical number-guessing game written in Python. The application selects a random number within a defined range and challenges the player to guess it, providing feedback after each attempt.

## Features

- Graphical user interface for easy interaction
- Randomly generated target number
- Feedback indicating whether a guess is too high or too low
- Attempt tracking
- Clear game-reset workflow
- Input validation for invalid or empty guesses

## Requirements

- Python 3.8 or later
- Tkinter, included with most standard Python installations

If Tkinter is missing on Linux, install it using your distribution's package manager. For example:

```bash
sudo apt install python3-tk
```

## Running the Game

1. Open a terminal in the project directory.
2. Run the Python entry-point file:

```bash
python <script-name>.py
```

On Windows, you may need to use:

```bash
py <script-name>.py
```

Replace `<script-name>.py` with the Python file that starts the application.

## How to Play

1. Start the application.
2. Enter a whole-number guess in the input field.
3. Submit the guess.
4. Read the feedback and adjust your next guess.
5. Continue until you find the target number.
6. Start a new round when prompted or by using the reset control.

## Typical Project Structure

```text
gui_guess_number_game/
├── README.md
└── <game-script>.py
```

The exact Python filename may vary depending on the project version.

## Input Validation

The game expects numeric, whole-number input. Empty values, non-numeric text, and guesses outside the supported range should be rejected with an explanatory message rather than causing the application to close.

## Customization

The game can be extended by changing the number range, adding a maximum-attempt limit, displaying a score, adding difficulty levels, or improving the visual theme.

## License

No license is currently specified for this project. Add a license file and update this section if the project is distributed publicly.
