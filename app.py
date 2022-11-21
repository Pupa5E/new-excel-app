from flask import Flask, render_template

app = Flask(__name__)

@app.route('/video')
def video():
    return render_template('video.html')

@app.route('/')
def index():
    return render_template('video.html')