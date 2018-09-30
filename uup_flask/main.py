from flask import Flask
from flask import Response, render_template
import json
app = Flask(__name__)

events = [
        {"name": "party", "date": "today" },
        {"name": "party", "date": "tomorrow" },
        {"name": "party", "date": "yesterday" }
        ]
@app.route("/api_hello")
def hello():

    return Response(json.dumps(events), mimetype="application/json")


@app.route('/')
@app.route('/hello')
@app.route('/hello/<user>')
def hello_world(user=None):
    user = user or 'get uup user'
    return render_template('index.html', user=user)


if __name__ == "__main__":

	ssl_path =  "/etc/letsencrypt/live/getuupnow.com"
	from os.path import join as pjoin
	app.run(
        port=443,
        host="0.0.0.0",
        ssl_context=(pjoin(ssl_path, 'fullchain.pem'), pjoin(ssl_path,'privkey.pem')))
