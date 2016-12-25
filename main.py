import os
from flask import (
    Flask,
    request,
)

app = Flask(__name__)

def get_acronyms():
    with open('acronyms.txt') as acronyms:
        return {a.split('=')[0].strip(): a.split('=')[1].strip()
                for a in acronyms.readlines()}

acronyms = get_acronyms()

def expand_acronym(word):
    return acronyms.get(word, word)

@app.route('/')
def respond():
    with open('slack_token') as slack_token:
        token = slack_token.read().strip()
    if request.args['token'] == token:
        return ' '.join(
            expand_acronym(word) for word in request.args['text'].split(' ')
        )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
