# Catalog Application project for Udacity
This is a simple catalog application project for an Udacity course.
The application allows you to create categories and store items in each category.
It implements a simple local authentication system and also use the Google OAuth API for external authentication.

## Usage
To be done...

1. Install Vagrant
2. Spin up the virtual machine
3. Run fill_db.py to fill the database with mock data
4. Run application.py
5. Open your favorite browser to [http://localhost:8000](http://localhost:8000)

## API Usage
| Title | URL | Method |
|-------|-----|--------|
|Get a token to use for authentication with API requests|/api/v1/token/<br>eg. curl -u user:pass http://localhost:8000/api/v1/token/|GET|
|List all the categories|/api/v1/categories/<br>eg. curl -u auth_token: http://localhost:8000/api/v1/categories/|GET|
|List all the items for a given category|/api/v1/categories/<int:category_id>/<br>eg. curl -u auth_token: http://localhost:8000/api/v1/categories/1/|GET|
|List all the items for a given category|/api/v1/categories/<int:category_id>/items/<br>eg. curl -u auth_token: http://localhost:8000/api/v1/categories/1/items/|GET|
|Create a new category|/api/v1/categories/new/<br>eg. curl -u auth_token: -d '{"name":"Test"}' -H "Content-Type: application/json" -X POST http://localhost:8000/api/v1/categories/new/|POST|
|Edit a category|/api/v1/categories/<int:category_id>/edit/<br>eg. curl -u auth_token: -d '{"name":"Test"}' -H "Content-Type: application/json" -X POST http://localhost:8000/api/v1/categories/1/edit/|POST|
|Delete a category|/api/v1/categories/<int:category_id>/delete/<br>eg. curl -u auth_token: -X POST http://localhost:8000/api/v1/categories/1/delete/|POST|
|List the details of a given item|/api/v1/items/<int:item_id>/<br>eg. curl -u auth_token: http://localhost:8000/api/v1/items/1/|GET|
|List the details of a given item|/api/v1/categories/<int:category_id>/items/<int:item_id>/<br>eg. curl -u auth_token: http://localhost:8000/api/v1/categories/1/items/1/|GET|
|Create a new item|/api/v1/categories/<int:category_id>/items/new/<br>eg. curl -u auth_token: -d '{"name":"Test", "description":"A new item"}' -H "Content-Type: application/json" -X POST http://localhost:8000/api/v1/categories/1/items/new/|POST|
|Edit an item|/api/v1/categories/<int:category_id>/items/<int:item_id>/edit/<br>eg. curl -u auth_token: -d '{"name":"Test", "description":"A new item", "category_id":1}' -H "Content-Type: application/json" -X POST http://localhost:8000/api/v1/categories/1/items/1/edit/|POST|
|Delete an item|/api/v1/categories/<int:category_id>/items/<int:item_id>/delete/<br>eg. curl -u auth_token: -X POST http://localhost:8000/api/v1/categories/1/items/1/dalete/|POST|
