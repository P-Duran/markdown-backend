db = db.getSiblingDB("markdown_db");
db.animal_tb.drop();
db.createUser({user: 'markdown_backend', pwd: 'Cep%mc7X4msE6mBU', roles: [{role: 'readWrite', db: 'markdown_db'}]})

db.markdown.insertMany([
    {
        "_id": "4141506e-7c80-4f7b-8976-3ac739b4747f",
        "createdAt": {"$date": "2022-03-13T16:31:26.681Z"},
        "markdown": "# Title",
        "title": "test",
        "updatedAt": {"$date": "2022-03-13T16:31:26.681Z"},
        "user": "pablopoi",
        "workspace": "0d0e1224-7f9c-4e81-a254-61617b996da1"
    }
]);

db.workspace.insertMany([
    {
        "_id": "0d0e1224-7f9c-4e81-a254-61617b996da1",
        "createdAt": {"$date": "2022-03-13T16:30:03.190Z"},
        "name": "test",
        "updatedAt": {"$date": "2022-03-13T16:30:03.190Z"},
        "user": "pablopoi"
    }
]);