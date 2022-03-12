db = db.getSiblingDB("markdown_db");
db.animal_tb.drop();
db.createUser({user: 'markdown_backend', pwd: 'Cep%mc7X4msE6mBU', roles: [{role: 'readWrite', db: 'markdown_db'}]})

db.markdown.insertMany([
    {
        "markdown": "# Title\n## Subtitle\n**bold**",
        "user": "paco",
    }
]);