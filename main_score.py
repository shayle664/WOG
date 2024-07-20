from flask import Flask
import utils
import os

app = Flask(__name__)

bad_return = f"""<html>
                                    <head>
                                        <title>Score game</title>
                                    </head>
                                    <body>
                                        <h1>ERROR</h1>
                                        <div id="score" style="color:red">{utils.BAD_RETURN_CODE}</div>
                                    </body>
                                    </html>"""
@app.route("/")
def score_server():
    try:
        if os.path.exists(utils.SCORES_FILE_NAME):
            with open(utils.SCORES_FILE_NAME, 'r') as file:
                SCORE = int(file.readline())
                return f"""<html>
                                <head>
                                    <title>Score game</title>
                                </head>
                                <body>
                                    <h1>The score is:</h1>
                                    <div id="score">{SCORE}</div>
                                </body>
                                </html>"""
        else:
            return bad_return
    except (FileNotFoundError, ValueError):
        return bad_return



if __name__ == "__main__":
    app.run(debug=True)