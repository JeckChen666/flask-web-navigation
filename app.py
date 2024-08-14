import os
import json
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Path to the JSON file for storing card data
CARDS_FILE = os.path.join(os.path.dirname(__file__), 'cards.json')


# Function to create an empty JSON file if it doesn't exist
def ensure_cards_file_exists():
    if not os.path.exists(CARDS_FILE):
        with open(CARDS_FILE, 'w') as f:
            json.dump([], f)  # Initialize the file with an empty list


# Function to load cards from JSON file
def load_cards():
    ensure_cards_file_exists()
    with open(CARDS_FILE, 'r') as f:
        return json.load(f)


# Function to save cards to JSON file
def save_cards(cards):
    with open(CARDS_FILE, 'w') as f:
        json.dump(cards, f, indent=4)


# Load cards initially
cards = load_cards()


@app.route('/')
def index():
    return render_template('index.html', cards=cards)


@app.route('/manage', methods=['GET', 'POST'])
def manage():
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'add':
            url = request.form.get('url')
            note = request.form.get('note')
            cards.append({'url': url, 'note': note})
        elif action == 'edit':
            index = int(request.form.get('index'))
            cards[index]['url'] = request.form.get('url')
            cards[index]['note'] = request.form.get('note')
        elif action == 'delete':
            index = int(request.form.get('index'))
            cards.pop(index)

        # Save cards after each operation
        save_cards(cards)

        return redirect(url_for('manage'))

    return render_template('manage.html', cards=cards, enumerate=enumerate)


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5000,use_reloader = False)
