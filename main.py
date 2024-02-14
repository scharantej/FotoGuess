
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/game')
def game():
    return render_template('game.html')

@app.route('/upload_photo', methods=['POST'])
def upload_photo():
    file = request.files['photo']
    filename = secure_filename(file.filename)
    file.save(os.path.join("static/photos", filename))
    return "", 200

@app.route('/get_photo', methods=['GET'])
def get_photo():
    photo_list = os.listdir("static/photos")
    return photo_list

@app.route('/submit_answer', methods=['POST'])
def submit_answer():
    answer = request.form['answer']
    return "", 200

@app.route('/check_winner', methods=['GET'])
def check_winner():
    return "", 200

if __name__ == '__main__':
    app.run(debug=True)
