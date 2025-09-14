# 🎮 World of Games (WOG)

This project is a Python-based mini-games platform.
It currently includes several small games that can be played via the command line (CLI) and a basic Flask web app that displays scores.

### 📂 Project Structure
```
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
```


## 🎲 Games Included
1. **Memory Game**:
  - Shows a random sequence of numbers for a short time.
  - The player must re-enter the sequence correctly.
2. **Guess Game**:
  - Computer picks a number between 0 and difficulty.
  - Player must guess the number.
3. **Currency Roulette**:
  - Computer picks a random USD value.
  - Player must guess its value in ILS within a margin (depending on difficulty).


## 🏆 Score System
- All games award points based on difficulty level.

- Scores are saved into scores.txt.

- The Flask app (main_score.py) reads this file and displays: The score is:


## Testing 
- curl to verify that the Flask app is up and that the score is displayed correctly.

- This is integrated into Jenkins as part of the E2E test stage.


## 🚀 Pipeline (CI/CD)

The project is built and tested in a Jenkins pipeline with the following steps:

1. Clean up → remove old workspace.

2. Clone Repo → pull source code.

3. Docker Build & Run → build image and run with docker-compose.

4. E2E Test → check if the app is running and returning the expected output.

5. Finalize → bring down containers.

6. Docker Login & Push → push the built image to Docker Hub.
