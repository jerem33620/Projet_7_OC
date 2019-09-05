# -*- coding: Utf-8 -*
import os

from flask import Flask, render_template, request, jsonify
from .grandpy import question_for_app_grandpy

app = Flask(__name__)

@app.route('/')
def grandpy_question():
    return render_template('base.html', api_key=os.environ.get('GOOGLE_API_KEY_2'))

@app.route('/question', methods = ['POST'])
def question():
    if request.method == 'POST':
        question = request.form
        return jsonify(question_for_app_grandpy(question))

if __name__ == '__main__':
    app.run(debug=True, port=3000)