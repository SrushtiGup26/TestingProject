from flask import Flask, render_template, request
from Model import detect_spam

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        message_text = request.form['message_text']
        result = detect_spam(message_text)
    return render_template('index.html', result=result)

@app.route('/check', methods=['POST'])
def check():
    message_text = request.form['message_text']
    result = detect_spam(message_text)
    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
