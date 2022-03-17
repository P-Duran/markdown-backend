db = db.getSiblingDB("markdown_db");
db.animal_tb.drop();
db.createUser({user: 'markdown_backend', pwd: 'Cep%mc7X4msE6mBU', roles: [{role: 'readWrite', db: 'markdown_db'}]})

db.markdown.insertMany([
    {
        "_id": "0d0e1224-7f9c-4e81-a254-61617b996da1",
        "name": "md 1",
        "createdAt": "Sun, 13 Mar 2022 16:31:26 GMT",
        "updatedAt": "Sun, 13 Mar 2022 16:31:26 GMT",
        "user": "admin"
    },
    {
        "_id": "40ae34ec-d8fa-4eb0-b37c-8574814de04d",
        "name": "md 2",
        "createdAt": "Sun, 13 Mar 2022 16:31:26 GMT",
        "updatedAt": "Sun, 13 Mar 2022 16:31:26 GMT",
        "user": "admin"
    }
]);

db.page.insertMany([
    {
        "_id": "bd1df5df-d7ef-45de-8f6c-7482354bccc3",
        "createdAt": {"$date": "2022-03-13T16:31:26.681Z"},
        "text": "# Title",
        "title": "test",
        "updatedAt": {"$date": "2022-03-13T16:31:26.681Z"},
        "user": "admin",
        "markdown": "0d0e1224-7f9c-4e81-a254-61617b996da1"
    },
    {
        "_id": "4141506e-7c80-4f7b-8976-3ac739b4747f",
        "createdAt": {"$date": "2022-03-13T16:31:26.681Z"},
        "text": "# efiuefifehi efhieuf eifuhe ifuhe fiuefh ",
        "title": "test 2",
        "updatedAt": {"$date": "2022-03-13T16:31:26.681Z"},
        "user": "admin",
        "markdown": "0d0e1224-7f9c-4e81-a254-61617b996da1"
    }
]);

db.user.insertMany([
    {
        "_id": "30bbccfc-b81c-4420-9fcb-b9eaf671b1c8",
        "createdAt": {"$date": "2022-03-13T13:13:00.919Z"},
        "email": "admin@admin.com",
        "name": "admin",
        "password": {
            "$binary": "JDJiJDEyJFNKenhjcGltdU1FSkNON0dIVUQzai44dXQ4LmRBemRZdjY5RnhlV1JlcnY0Znh1SldGZEJL",
            "$type": "0"
        },
        "updatedAt": {"$date": "2022-03-13T13:13:00.919Z"},
        "role": "ADMIN"
    },
    {
        "_id": "f06f9d89-c49b-4e96-9b3e-6c7172a4211a",
        "createdAt": {"$date": "2022-03-13T13:13:00.919Z"},
        "email": "random@random.com",
        "name": "random",
        "password": {
            "$binary": "JDJiJDEyJFNKenhjcGltdU1FSkNON0dIVUQzai44dXQ4LmRBemRZdjY5RnhlV1JlcnY0Znh1SldGZEJL",
            "$type": "0"
        },
        "updatedAt": {"$date": "2022-03-13T13:13:00.919Z"}
    }
]);
