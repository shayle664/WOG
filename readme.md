#🎮 World of Games (WOG)

This project is a Python-based mini-games platform.
It currently includes several small games that can be played via the command line (CLI) and a basic Flask web app that displays scores.

##📂 Project Structure
"""
app/
│
├── games/                     # Individual game implementations
│   ├── currency_roulette_game.py   # Guess the ILS value of random USD
│   ├── guess_game.py               # Guess a number against the computer
│   └── memory_game.py              # Remember a random sequence
│
├── app.py                     # (Flask app entry point for web usage)
├── main.py                    # CLI entry point (game selection & difficulty)
├── main_score.py              # Runs Flask server to display current score
├── score.py                   # Score calculation & updating logic
├── scores.txt                 # Stores accumulated scores
├── utils.py                   # Utility functions
├── requirements.txt           # Python dependencies
└── e2e.py                     # End-to-End test (verifies web app is running)
