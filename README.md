# rock-paper-scissor-game
# Rock · Paper · Scissors

A simple and interactive **Rock, Paper, Scissors** game built with **Python** and **Tkinter**.

The project uses the original Rock, Paper, Scissors game logic and adds a graphical user interface (GUI) with score tracking, emojis, and a reset button.

## Features

* Rock, Paper, and Scissors choices
* Computer makes a random choice
* Displays both player's and computer's choices
* Win, lose, and draw detection
* Score tracking
* Reset Score button
* Interactive graphical interface
* Clean and modern Tkinter design
* Emoji-based game interface

## Technologies Used

* **Python**
* **Tkinter**
* **Random module**

## How the Game Works

The player chooses one of three options:

* 🪨 Rock
* 📄 Paper
* ✂️ Scissors

The computer randomly selects one of the same three choices.

The winner is determined using these rules:

| Player      | Computer    | Result        |
| ----------- | ----------- | ------------- |
| Rock        | Scissors    | You Win       |
| Paper       | Rock        | You Win       |
| Scissors    | Paper       | You Win       |
| Same choice | Same choice | Draw          |
| Otherwise   | —           | Computer Wins |

## Project Structure

```text
Rock-Paper-Scissors/
│
├── rock_paper_scissors.py
└── README.md
```

## How to Run

### 1. Install Python

Make sure Python is installed on your computer.

You can check it using:

```bash
python --version
```

### 2. Download or Clone the Repository

Clone the repository using:

```bash
git clone YOUR_REPOSITORY_URL
```

Then open the project folder.

### 3. Run the Game

Run:

```bash
python rock_paper_scissors.py
```

The game window will open.

## Game Interface

The GUI contains:

* Your current choice
* Computer's choice
* Current score
* Game result
* Rock, Paper, and Scissors buttons
* Reset Score button

## Learning Goals

This project helped me practice:

* Python functions
* Lambda functions
* Conditional expressions
* `random.choice()`
* Dictionaries
* Classes and objects
* Tkinter GUI development
* Event handling
* Updating GUI elements dynamically
* Basic project organization
* GitHub project publishing

## Future Improvements

Possible future improvements include:

* Add sound effects
* Add animations
* Add multiple game modes
* Add a winning score target
* Add game statistics
* Add difficulty levels
* Improve the GUI further

## Author

Created as a Python GUI project for learning and practicing programming.

## License

This project is open for learning and educational purposes.

```

For your GitHub repository, I recommend naming the Python file **`rock_paper_scissors.py`** and the repository something like **`rock-paper-scissors`**.
```
