import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config['MONGO_DBNAME'] = "recipe_manager"
app.config['MONGO_URI'] = 'mongodb+srv://dthomas86:r00tuser@myfirstcluster-pf6q6.mongodb.net/recipe_manager?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_recipes')
def get_recipes():
   return render_template('recipes.html', recipes=mongo.db.recipes.find())


@app.route('/add_recipe')
def add_recipe():
    recipes=mongo.db.recipes.find()
    categories = mongo.db.categories.find()
    return render_template(
    'add_recipe.html', recipes=recipes, categories=categories)


@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes= mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipes'))


@app.route('/edit_recipe/<recipes_id>')
def edit_recipe(recipes_id):
    recipes = mongo.db.recipes.find_one({"_id": ObjectId(recipes_id)})
    all_diet_categories = mongo.db.categories.find()
    return render_template('edit_recipe.html',
     recipes = recipes, categories = all_diet_categories)


@app.route('/update_recipe/<recipes_id>', methods=['POST'])    
def update_recipe(recipes_id):
    recipes=mongo.db.recipes
    recipes.update( {'_id': ObjectId(recipes_id)},
    {
        'recipe_name':request.form.get('recipe_name'),
        'ingredients':request.form.get('ingredients'),
        'utensil_name': request.form.get('utensil_name'),
        'meal_procedure': request.form.get('meal_procedure'),
        'diet_category':request.form.get('diet_category')
    })
    return redirect(url_for('get_recipes'))


@app.route('/delete_recipe/<recipes_id>')
def delete_recipe(recipes_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipes_id)})
    return redirect(url_for('get_recipes'))


@app.route('/home')
def home():
    return render_template('home.html')    


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)