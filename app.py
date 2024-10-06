from flask import Flask, render_template, jsonify
import os
import json
from markov import get_data

app = Flask(__name__)

# Home route - simple homepage with a link to the second endpoint
@app.route('/')
def home():
    return '''
        <h1>Welcome to the Home Page</h1>
        <p><a href="/view-data">View JSON Data</a></p>
    '''

@app.route('/markov')
def markov():
    initial_sentence = "The cat sat on the mat. It looked up at the sun. Birds chirped in the trees. The cat looked at the birds. The birds chirped at the cat. The cat sat in the trees. The sun looked down at the cat."
    data = json.dumps(get_data(initial_sentence), indent=4)
    return render_template('display_markov.html',initial_sentence=initial_sentence, data=data)


# Second route - displays a page with JSON data (use a placeholder for now)
@app.route('/view-data')
def view_data():
    # Placeholder JSON structure
    # json_data = {
    #     "conversation_name": "Example Conversation",
    #     "questions_and_answers": [
    #         {"question": "What is Python?", "answer": "Python is a programming language."},
    #         {"question": "What is Flask?", "answer": "Flask is a micro web framework for Python."}
    #     ]
    # }

    json_data = read_articles()
    conversation_name = ""
    questions_and_answers = []

    # for now, this will only have one conversation
    for key, value in json_data.items():
        conversation_name = key
        print(key)
        questions_and_answers = value
        print(questions_and_answers)

    return render_template('display_data.html', questions_and_answers=questions_and_answers, conversation_name=conversation_name)

def read_articles():
    # Get the current directory (same as where the Flask app is located)
    # Path to your JSON file (assuming it is in the same directory as this Python file)
    # Read and load the JSON file

    current_directory = os.path.dirname(os.path.abspath(__file__))
    json_file_path = os.path.join(current_directory, 'articles(2).json')

    with open(json_file_path, 'r') as json_file:
        json_data = json.load(json_file)

    #print(json.dumps(json_data, indent=4))  
    return json_data;

if __name__ == '__main__':
    app.run(debug=True)
