# -*- coding: Utf-8 -*

from flask import Flask, render_template, request, jsonify
from app.grandpy import question_for_app_grandpy

app = Flask(__name__)

@app.route('/')
def grandpy_question():
    return render_template('base.html')

@app.route('/question')
def question():
    user_question = request.args.get("question", "")
    return jsonify(question_for_app_grandpy(user_question))

if __name__ == '__main__':
    app.run(debug=True, port=3000)