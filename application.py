from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, Category, Item

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

#Routes for the web application
@app.route('/')
@app.route('/categories/')
def home():
	categories = session.query(Category)
	return render_template('categories.html', categories=categories)

@app.route('/categories/new', methods=['GET', 'POST'])
def newCategory():
	categories = session.query(Category)
	return render_template('newCategory.html', categories=categories)

@app.route('/categories/<int:category_id>/')
@app.route('/categories/<int:category_id>/items/')
def showCategory(category_id):
	categories = session.query(Category)
	category = session.query(Category).filter_by(id = category_id).one()
	return render_template('showCategory.html', categories=categories, category=category)

@app.route('/categories/<int:category_id>/edit/', methods=['GET', 'POST'])
def editCategory(category_id):
	categories = session.query(Category)
	category = session.query(Category).filter_by(id = category_id).one()
	return render_template('editCategory.html', categories=categories, category=category)

@app.route('/categories/<int:category_id>/delete/', methods=['GET', 'POST'])
def deleteCategory(category_id):
	categories = session.query(Category)
	category = session.query(Category).filter_by(id = category_id).one()
	return render_template('deleteCategory.html', categories=categories, category=category)

@app.route('/categories/<int:category_id>/items/new/', methods=['GET', 'POST'])
def newCategoryItem(category_id):
	categories = session.query(Category)
	category = session.query(Category).filter_by(id = category_id).one()
	return "Create a new item"

@app.route('/categories/<int:category_id>/items/<int:item_id>/')
def showCategoryItem(category_id, item_id):
	category = session.query(Category).filter_by(id = category_id).one()
	item = session.query(Item).filter_by(id = item_id).one()
	return "Show the items within a given item"

@app.route('/categories/<int:category_id>/items/<int:item_id>/edit/', methods=['GET', 'POST'])
def editCategoryItem(category_id, item_id):
	category = session.query(Category).filter_by(id = category_id).one()
	item = session.query(Item).filter_by(id = item_id).one()
	return "Edit a given item"

@app.route('/categories/<int:category_id>/items/<int:item_id>/delete/', methods=['GET', 'POST'])
def deleteCategoryItem(category_id, item_id):
	category = session.query(Category).filter_by(id = category_id).one()
	item = session.query(Item).filter_by(id = item_id).one()
	return "Delete a item"

#Below are the routes for API
@app.route('/api/v1/categories/new', methods=['GET', 'POST'])
def newCategoryAPI():
	return "Create a new category"

@app.route('/api/v1/categories/<int:category_id>/')
@app.route('/api/v1/categories/<int:category_id>/items/')
def showCategoryAPI(category_id):
	return "Show the items within a given category"

@app.route('/api/v1/categories/<int:category_id>/edit/', methods=['GET', 'POST'])
def editCategoryAPI(category_id):
	return "Edit a given category"

@app.route('/api/v1/categories/<int:category_id>/delete/', methods=['GET', 'POST'])
def deleteCategoryAPI(category_id):
	return "Delete a category"

@app.route('/api/v1/categories/<int:category_id>/items/new/', methods=['GET', 'POST'])
def newCategoryItemAPI(category_id):
	return "Create a new item"

@app.route('/api/v1/categories/<int:category_id>/items/<int:item_id>/')
def showCategoryItemAPI(category_id, item_id):
	return "Show the items within a given item"

@app.route('/api/v1/categories/<int:category_id>/items/<int:item_id>/edit/', methods=['GET', 'POST'])
def editCategoryItemAPI(category_id, item_id):
	return "Edit a given item"

@app.route('/api/v1/categories/<int:category_id>/items/<int:item_id>/delete/', methods=['GET', 'POST'])
def deleteCategoryItemAPI(category_id, item_id):
	return "Delete a item"

if __name__ == '__main__':
	app.secret_key = ''
	app.debug = True
	app.run(host = '0.0.0.0', port = 8000)