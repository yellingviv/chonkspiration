from flask import Flask, flash, jsonify, render_template, request
import requests
import json

app = Flask(__name__)
app.secret_key = 'GIMMECATTOS'

MARKOVIAN_URL = 'http://0.0.0.0:5002/mr_sandman'

@app.route('/')
def serve_homepage():
    """render the homepage so folks can request cats"""

    return render_template("index.html")


@app.route('/request_cats')
def call_out_to_the_void():
    """call to the server with the given mood to get the goods"""

    mood = request.args.get('mood')
    response = requests.get(MARKOVIAN_URL + '?mood=' + mood)
    response_json = json.loads(response.text)
    quote = response_json[1]
    img_url = response_json[0]

    return render_template("catto_page.html",
                            quote=quote,
                            img_url=img_url)


if __name__ == '__main__':

    app.run(port=5005, host='0.0.0.0', debug=True)
