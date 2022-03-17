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
        "createdAt": "Sun, 13 Mar 2022 16:31:26 GMT",
        "text": "# Title",
        "title": "test",
        "updatedAt": "Sun, 13 Mar 2022 16:31:26 GMT",
        "user": "admin",
        "markdown": "0d0e1224-7f9c-4e81-a254-61617b996da1"
    },
    {
        "_id": "4141506e-7c80-4f7b-8976-3ac739b4747f",
        "createdAt": "Sun, 13 Mar 2022 16:31:26 GMT",
        "text": "# efiuefifehi efhieuf eifuhe ifuhe fiuefh ",
        "title": "test 2",
        "updatedAt": "Sun, 13 Mar 2022 16:31:26 GMT",
        "user": "admin",
        "markdown": "0d0e1224-7f9c-4e81-a254-61617b996da1"
    }
]);
