db = db.getSiblingDB("animal_db");
db.animal_tb.drop();
db.createUser({user: 'flaskuser', pwd: 'your_password', roles: [{role: 'readWrite', db: 'animal_db'}]})

db.animal_tb.insertMany([
    {
        "id": 1,
        "name": "Lion",
        "type": "wild"
    },
    {
        "id": 2,
        "name": "Cow",
        "type": "domestic"
    },
    {
        "id": 3,
        "name": "Tiger",
        "type": "wild"
    },
]);