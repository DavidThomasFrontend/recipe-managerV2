

# Receipe Manager

  
I have an keen interest in cooking and finding recipes and wanted to build something simple and clear so I could save my recipes and view them when I need them.

I also wanted a compact recipe experience to negate the need for a lot of scrolling to the next recipe as each recipe can be expanded to real the information.

  

## UX

  

The UX was extremely important in this project. I wanted to make a positive user experience so the user would keep coming back to add new recipes and could view them easily aswell as edit or remove them.

  i wanted navigation to be the same in every part of the website so as not to confuse and potentially irritate users. I want to achieve a smooth experience for visitors who wont be put off by confusing navigation and to a recipe in as few clicks as possible. 

  Each recipe has its own dropdown popout showing utensils, ingredients and meal procedure method. 

I added photos showing the finished recipe. These are placeholders to illustrate what it would look like if a user wanted to upload a photo alongside. The photos shown in the project were pulled from my database rather than hard coded into the template.

  In particular, as part of this section we recommend that you provide a list of User Stories, with the following general structure:

  
As someone who is interested in cooking and the  recipes on the website I want the ability to go straight to the recipe to get new ideas or expand my tastes. I also want the recipes to filter the good from the bad based on user review  **End user goal:**  the visitor gets a new idea and can store their recipes for future use  **End business goal:**  build out a complete and diverse library that caters for all diets

  

As a new visitor to the website, I want view the list of recipes in an intuitive way and find a recipe to try and perhaps share my knowledge with a recipe of my own.

  

As a visitor i want a clean and simple interface that clearly tells me where the recipes are.

  

Here is a folder with some mockups:

  

[https://github.com/Vileblood/recipe-managerV2/tree/master/Web%20Mockups](https://github.com/Vileblood/recipe-managerV2/tree/master/Web%20Mockups)

  

## Features

The features of my site are as follows:

  -  Home: This is the landing page for my site. It shows a food inspired backdrop with logo and search bar

-  Recipes: Here you will find a collection of user uploaded recipes with utensils used ingredients and method on how to compile everything to make the meal

-  Add a recipe : Here you can add recipes and save them to the database where they are shown on the recipes page

  

### Existing Features

  

-  Feature 1 - Simple navigation.

-  Feature 2 - Simple form to add recipes

- Feature 3- Recipe is then saved to Mongo DB cluster

- Feature 4 - Recipes then outputs saved recipe

- Feature 5 - User star rating 

  

### Features Left to Implement

  

-  A feature i would like to implement would be full search capability based on ingredient, utensil, method etc.

-  While investigating for this project , i had the idea of a function that, when you would view ingredients there would be a simple button next to it that would lead you to a supermarket (tesco, lidl marks and spencer etc) that would put the needed ingredients into your basket. Unfortunately when i looked into making an example with tesco they unlisted their developer support. I feel this would be interesting to add to offer more ease of use.

- Another feature id like to implement would be a file upload feature directly to the database

  

## Technologies Used

  

The technologies used in the creation of this website was HTML, CSS and Javascript. I also imported from Google Fonts and  jQuery.
I also used Python and MongoDB with Flask

  

-  [MongoDB](https://www.mongodb.com)
  The project uses  **MongoDB**  to add storage space

-  [Google Fonts](https://fonts.google.com/)  - The project uses  **Google Font**  to add font styling

- [Materialize](https://materializecss.com) - Used this for navbar and recipe dropdown styling aswell as search tool

  

## Testing

  

I have conducted a lot of testing since the start of this project. Usually this would mean i would add extra features then save and then test how it looks and how it responds.

  I would test after every piece of code. As per the user stories it shouldn't be too difficult to add more recipes.

  

The way the site was made would be easy to more recipes and more features

  I had some problems with understanding naming conventions such as url_for and some aspects of app routing. I was just a case of getting used to this way of working

  

i sent a link to friends and family and asked them to use the website and give feedback on what they thought needed to improve or any stumbling blocks they'd encountered.

  

Most of these problems were remedied by researching the issue and adding the relevant  fixes such as entering the correct path to my css file or keeping track of my mongo labels for each recipe

  

The devices i used to test the website was a macbook pro and ipad.

  

## Deployment

  

The deployment was straight forward enough. i set up a file system through git and made regular git commits as i made changes.

  

## Credits

  

### Media

  

-  The background i found was a generic search in google and thought it was appropriate of other cooking based websites

  

### Acknowledgements

  
Used https://materializecss.com for icons and nav bar

https://stackoverflow.com For some troubleshooting of issues

https://docs.mongodb.com/manual/core/document/ For getting a clear picture on how mongo works

https://flask.palletsprojects.com/en/1.1.x/

And i went through some older tutorials from code institute to fully understand the concepts