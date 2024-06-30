from flask import Flask
import utils
import os

app = Flask(__name__)


@app.route("/")
def score_server():
    try:
        if os.path.exists(utils.SCORES_FILE_NAME):
            with open(utils.SCORES_FILE_NAME, 'r') as file:
                SCORE = int(file.readline())
        else:
            SCORE = 0
    except (FileNotFoundError, ValueError):
        SCORE = 0
    return f"""<html>
                <head>
                    <title>Score game</title>
                </head>
                <body>
                    <h1>The score is:</h1>
                    <div id="score">{SCORE}</div>
                </body>
                </html>"""


if __name__ == "__main__":
    app.run(debug=True)