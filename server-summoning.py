from Flask import flask, flash, jsonify, render
import requests
import json

app = Flask(__name__)
app.secret_key = 'GIMMECATTOS'

def call_out_to_the_void(mood):
    """call to the server with the given mood to get the goods"""

    response = requests.get(MARKOVIAN_URL + "?mood=" + mood)
    response_json = json.loads(response.text)
    quote = response_json['quote']
    img_url = response_json['url']

    return render_template("catto_page.html",
                            quote=quote,
                            img_url=img_url)


if __name__ == '__main__':

    connect_to_db(app)
    app.run(port=5000, host='0.0.0.0', debug=True)
