# Catalog Application project for Udacity
This is a simple catalog application project for an Udacity course.
The application allows you to create categories and store items in each category.
It implements a simple local authentication system and also use the Google OAuth API for external authentication.

## Prerequisites

To use this application you will need to download and install the following softwares:

1. [Git](https://git-scm.com/downloads)
2. [VirtualBox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1) (version 5.1)
3. [Vagrant](https://www.vagrantup.com/downloads.html)

## Usage

After you installed the softwares required as per in the prerequisites please follow the steps below:

1. Clone this repository to your local machine `git@github.com:paulstrife88/fullstack-nanodegree-vm.git`
2. Move to the `vagrant` directory inside the repository.
3. Type `vagrant up`. (This will download and prepare the virtual machine environment)
4. Once the the virtual machine is ready, use the `vagrant ssh` command to log into it.
5. Change directory to `/vagrant/catalog`.
6. Run `python fill_db.py` to fill the database with mock data.
7. Run `python application.py` to start the application.
8. Open your favorite browser to [http://localhost:8000](http://localhost:8000)

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
|Delete an item|/api/v1/categories/<int:category_id>/items/<int:item_id>/delete/<br>eg. curl -u auth_token: -X POST http://localhost:8000/api/v1/categories/1/items/1/delete/|POST|