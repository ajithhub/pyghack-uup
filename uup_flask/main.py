from flask import Flask
from flask import Response, render_template
import json
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(150), unique=True, nullable=False)
    lat = db.Column(db.String(10), nullable=False)
    lng = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return '<Event %r (%s, %s)>' % (self.name, self.lat, self.lng)
    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}


@app.route("/api_hello")
def hello():

    loaded_events = Event.query.all()
    return Response(json.dumps([x.as_dict() for x in loaded_events]),
		    mimetype="application/json")


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
