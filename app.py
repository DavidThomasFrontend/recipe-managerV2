import os
from flask import Flask

app = Flask(__name__)

app.config('MONGO_DBNAME') = recipe_manager
app.config('MONGO_URI') = mongodb+srv://dthomas86:r00tuser@myfirstcluster-pf6q6.mongodb.net/recipe_manager?retryWrites=true&w=majority

@app.route('/')
def hello():
    return "Hello World"

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)    