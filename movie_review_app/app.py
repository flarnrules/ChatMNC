import os
from utils.chat_mnc import generate_review
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route('/generate_review', methods=['POST'])
def generate_review_route():
    reviewer_name = request.form['reviewer_name']
    movie_prompt = request.form['movie_prompt']
    
    model_path = os.path.join('models', reviewer_name)
    generated_review = generate_review(model_path, movie_prompt)
    
    return jsonify({'review': generated_review})

if __name__ == '__main__':
    app.run(debug=True)
