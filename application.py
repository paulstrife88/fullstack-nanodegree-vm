from flask import Flask, render_template, request, redirect, url_for, g, abort, flash
from flask import session as login_session
from sqlalchemy import create_engine, asc, desc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, Category, Item
from flask_httpauth import HTTPBasicAuth
import random, string

app = Flask(__name__)
auth = HTTPBasicAuth()
engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()
categories = session.query(Category)

@auth.verify_password
def verify_password(email, password):
	user = session.query(User).filter_by(email=email).first()
	if not user or not user.verify_password(password):
		return False
		#g.user = user
	return True

@app.route('/signup/', methods=['GET', 'POST'])
def signup():
	if request.method == 'POST':
		email = request.form['email']
		password = request.form['password']
		if email is None or password is None:
			abort(400)
		if session.query(User).filter_by(email=email).first() is not None:
			abort(400)
		user = User(email = email)
		user.auth_method = 'local'
		user.hash_password(password)
		session.add(user)
		session.commit()
		return redirect(url_for('login'))
	else:
		return render_template('signup.html')

@app.route('/login/', methods=['GET','POST'])
def login():
	if request.method == 'POST':
		email = request.form['email']
		password = request.form['password']
		if verify_password(email, password):
			login_session['email'] = email
			login_session['logged_in'] = True
			flash('Logged in succesfully')
			return redirect(url_for('home'))
		else:
			flash('Something went wrong, incorrect email or username')
			return render_template('login.html')
	else:
		return render_template('login.html')

@app.route('/logout/')
def logout():
	login_session.pop('email', None)
	login_session.pop('logged_in', None)
	return redirect(url_for('home'))

#Routes for the web application
@app.route('/')
@app.route('/categories/')
def home():
	items = session.query(Item).order_by(desc(Item.id)).limit(10)
	return render_template('categories.html', categories=categories, items=items)

@app.route('/categories/new', methods=['GET', 'POST'])
def newCategory():
	if request.method == 'POST':
		newCategory = Category(name = request.form['name'])
		session.add(newCategory)
		session.commit()
		return redirect(url_for('showCategory', category_id=newCategory.id))
	else:
		return render_template('newCategory.html', categories=categories)

@app.route('/categories/<int:category_id>/')
@app.route('/categories/<int:category_id>/items/')
def showCategory(category_id):
	category = session.query(Category).filter_by(id = category_id).one()
	items = session.query(Item).filter_by(category_id = category.id)
	return render_template('showCategory.html', categories=categories, category=category, items=items)

@app.route('/categories/<int:category_id>/edit/', methods=['GET', 'POST'])
@auth.login_required
def editCategory(category_id):
	category = session.query(Category).filter_by(id = category_id).one()
	if request.method == 'POST':
		category.name = request.form['name']
		session.add(category)
		session.commit()
		return redirect(url_for('showCategory', category_id=category.id))
	else:
		return render_template('editCategory.html', categories=categories, category=category)

@app.route('/categories/<int:category_id>/delete/', methods=['GET', 'POST'])
def deleteCategory(category_id):
	category = session.query(Category).filter_by(id = category_id).one()
	if request.method == 'POST':
		session.delete(category)
		session.commit()
		return redirect(url_for('home'))
	else:
		return render_template('deleteCategory.html', categories=categories, category=category)

@app.route('/categories/<int:category_id>/items/new/', methods=['GET', 'POST'])
def newItem(category_id):
	category = session.query(Category).filter_by(id = category_id).one()
	if request.method == 'POST':
		newItem = Item(name = request.form['name'],
					   category_id = request.form['category'],
					   description = request.form['description'])
		session.add(newItem)
		session.commit()
		return redirect(url_for('showItem', category_id=category.id, item_id=newItem.id))
	else:
		return render_template('newItem.html', categories=categories, category=category)

@app.route('/categories/<int:category_id>/items/<int:item_id>/')
def showItem(category_id, item_id):
	category = session.query(Category).filter_by(id = category_id).one()
	item = session.query(Item).filter_by(id = item_id).one()
	return render_template('showItem.html', categories=categories, category=category, item=item)

@app.route('/categories/<int:category_id>/items/<int:item_id>/edit/', methods=['GET', 'POST'])
def editItem(category_id, item_id):
	category = session.query(Category).filter_by(id = category_id).one()
	item = session.query(Item).filter_by(id = item_id).one()
	if request.method == 'POST':
		item.name = request.form['name']
		item.category_id = request.form['category']
		item.description = request.form['description']
		session.add(item)
		session.commit()
		return redirect(url_for('showItem', category_id=category.id, item_id=item.id))
	else:
		return render_template('editItem.html', categories=categories, category=category, item=item)

@app.route('/categories/<int:category_id>/items/<int:item_id>/delete/', methods=['GET', 'POST'])
def deleteItem(category_id, item_id):
	category = session.query(Category).filter_by(id = category_id).one()
	item = session.query(Item).filter_by(id = item_id).one()
	if request.method == 'POST':
		session.delete(item)
		session.commit()
		items = session.query(Item).filter_by(category_id = category.id)
		return redirect(url_for('showCategory', category_id=category.id))
	else:
		return render_template('deleteItem.html', categories=categories, category=category, item=item)

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
def newItemAPI(category_id):
	return "Create a new item"

@app.route('/api/v1/categories/<int:category_id>/items/<int:item_id>/')
def showItemAPI(category_id, item_id):
	return "Show the items within a given item"

@app.route('/api/v1/categories/<int:category_id>/items/<int:item_id>/edit/', methods=['GET', 'POST'])
def editItemAPI(category_id, item_id):
	return "Edit a given item"

@app.route('/api/v1/categories/<int:category_id>/items/<int:item_id>/delete/', methods=['GET', 'POST'])
def deleteItemAPI(category_id, item_id):
	return "Delete a item"

if __name__ == '__main__':
	app.config['SECRET_KEY'] = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in xrange(32))
	app.debug = True
	app.run(host = '0.0.0.0', port = 8000)