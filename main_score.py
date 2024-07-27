from flask import Flask, render_template_string
from utils import SCORES_FILE_NAME

app = Flask(__name__)

@app.route('/')
def score_server():
    try:
        with open(SCORES_FILE_NAME, 'r') as file:
            score = int(file.read().strip())
        html_content = """
        <html>
        <head>
            <title>Scores Game</title>
        </head>
        <body>
            <h1>The score is:</h1>
            <div id="score">{{score}}</div>
        </body>
        </html>
        """
        return render_template_string(html_content, score=score)
    except Exception as e:
        error_html_content = """
        <html>
        <head>
            <title>Scores Game</title>
        </head>
        <body>
            <h1>ERROR:</h1>
            <div id="score" style="color:red">{{error}}</div>
        </body>
        </html>
        """
        return render_template_string(error_html_content, error=str(e))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
