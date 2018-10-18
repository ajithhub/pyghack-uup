from main import db, Event
import json



events = [
{ 'name': "Test event 1", 'lat': "40.123435", 'lng': "40.23432" },
{ 'name': "Test event 2", 'lat': "40.123435", 'lng': "40.23432" },
{ 'name': "Test event 3", 'lat': "40.123435", 'lng': "40.23432" },
{ 'name': "Test event 4", 'lat': "40.123435", 'lng': "40.23432" },
]

try:
    db.drop_all()
except:
    pass

db.create_all()
for event in events:
    db.session.add(Event(**event))

db.session.commit()

loaded_events = Event.query.all()
print (json.dumps([x.as_dict() for x in loaded_events]))

