from flask import Flask, render_template, request, redirect, url_for, \
                    g, abort, flash, jsonify
from flask import session as login_session
from sqlalchemy import create_engine, asc, desc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, Category, Item
from flask_httpauth import HTTPBasicAuth
import random
import string
import json
import httplib2
import requests

from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
from flask import make_response

app = Flask(__name__)
auth = HTTPBasicAuth()

CLIENT_ID = json.loads(open('client_secrets.json',
                            'r').read())['web']['client_id']
APPLICATION_NAME = "Catalog App"

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Global variable to store the categories as they are
# use used in near every template
categories = session.query(Category)


# Function to authenticate an user with local authentication and
# token authentication
@auth.verify_password
def verify_password(email_or_token, password):
    user_id = User.verify_auth_token(email_or_token)
    if user_id:
        user = session.query(User).filter_by(id=user_id).one()
    else:
        user = session.query(User).filter_by(email=email_or_token).first()
        if not user or not user.verify_password(password):
            return False
    g.user = user
    return True


# Get token for API use without username and password
@app.route('/api/v1/token/')
@auth.login_required
def get_auth_token():
    token = g.user.generate_auth_token()
    return jsonify({'token': token.decode('ascii')})


# Route for new user registration
@app.route('/signup/', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if not email or not password:
            flash('The required fields are empty')
            return redirect(url_for('signup'))
        if session.query(User).filter_by(
             email=email).first():
            flash('User already existing, please try to login')
            return redirect(url_for('login'))
        user = User(email=email)
        user.hash_password(password)
        session.add(user)
        session.commit()
        return redirect(url_for('login'))
    else:
        return render_template('signup.html')


# Load the login page for both local and external authentication
@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if (verify_password(email, password) and
                login_session['state'] == request.form['csrf']):
            login_session['email'] = email
            login_session['logged_in'] = True
            login_session['auth_method'] = 'local'
            flash('Logged in succesfully')
            return redirect(url_for('home'))
        else:
            state = ''.join(random.choice(string.ascii_uppercase +
                            string.digits) for x in xrange(32))
            login_session['state'] = state
            flash('Something went wrong, incorrect email or username')
            return render_template('login.html', STATE=state)
    else:
        state = ''.join(random.choice(string.ascii_uppercase +
                        string.digits) for x in xrange(32))
        login_session['state'] = state
        return render_template('login.html', STATE=state)

# Authenticate an user with Google OAuth and create a new user based on
# the information received
# @app.route('/oauth2/')
# def oauth2():
#     if request.args.get('state') != login_session['state']:
#         abort(401)
#     flow = client.flow_from_clientsecrets(
#         'client_secrets.json',
#         scope='openid email profile',
#         redirect_uri=url_for('categories', _external=True))
#     credentials = flow.step2_exchange(auth_code)
#     if 'code' not in request.args:
#         auth_uri = flow.step1_get_authorize_url()
#         return redirect(auth_uri)
#     auth_code = request.args.get('code')
#     login_session['access_token'] = credentials.access_token
#     url = ('https://www.googleapis.com/oauth2/v1/userinfo?'
#             'alt=json&access_token=%s' % login_session['access_token'])
#     h = httplib2.Http()
#     result = json.loads(h.request(url, 'GET')[1])
#     if session.query(User).filter_by(
#         email=result['email']).first() is not None:
#         login_session['email'] = result['email']
#         login_session['auth_method'] = 'google'
#         login_session['logged_in'] = True
#     else:
#         user = User(email=email)
#         login_session['auth_method'] = 'google'
#         session.add(user)
#         session.commit()
#     flash('Logged in succesfully')
#     return redirect(url_for('home'))

# Authenticate an user with Google OAuth and create a new user based on
# the information received


@app.route('/oauth2callback/', methods=['POST'])
def oauth2callback():
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print "Token's client ID does not match app's."
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps("Current user is already \
            connected."), 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['access_token'] = credentials.access_token

    # Add an OAuth authenticated user information to the database and
    # update the session information
    if session.query(User).filter_by(
            email=result['email']).first() is not None:
        login_session['email'] = result['email']
        login_session['auth_method'] = 'google'
        login_session['logged_in'] = True
    else:
        user = User(email=result['email'])
        login_session['email'] = result['email']
        login_session['auth_method'] = 'google'
        login_session['logged_in'] = True
        session.add(user)
        session.commit()
    flash('Logged in succesfully')
    return redirect(url_for('home'))

# Perform logout and clear session for of an authenticated user.


@app.route('/logout/')
def logout():
    if not login_session:
        flash('Already logged out')
        return redirect(url_for('home'))
    if login_session['auth_method'] == 'google':
        url = ("https://accounts.google.com/o/oauth2/revoke?token=%s"
               % login_session['access_token'])
        h = httplib2.Http()
        result = h.request(url, 'GET')[0]
        if result == '200':
            login_session.pop('access_token', None)
    login_session.pop('email', None)
    login_session.pop('logged_in', None)
    login_session.pop('state', None)
    return redirect(url_for('home'))


# Load the root page listing the last 10 added items
@app.route('/')
@app.route('/categories/')
def home():
    items = session.query(Item).order_by(desc(Item.id)).limit(10)
    return render_template('categories.html', categories=categories,
                           items=items)


# Render the template for a given category listing all the items
# belonging to it
@app.route('/categories/<int:category_id>/')
@app.route('/categories/<int:category_id>/items/')
def showCategory(category_id):
    category = session.query(Category).filter_by(
               id=category_id).one()
    items = session.query(Item).filter_by(category_id=category.id)
    return render_template('showCategory.html', categories=categories,
                           category=category, items=items)


# Render a template to create a new category
@app.route('/categories/new', methods=['GET', 'POST'])
def newCategory():
    if 'email' not in login_session:
        flash('You need to be logged in to perform this action.')
        return redirect(url_for('login'))
    if request.method == 'POST':
        if login_session['state'] == request.form['csrf']:
            newCategory = Category(name=request.form['name'])
            session.add(newCategory)
            session.commit()
            return redirect(url_for('showCategory',
                                    category_id=newCategory.id))
        else:
            abort(403)
    else:
        return render_template('newCategory.html', categories=categories)


# Render a template to edit an existing category
@app.route('/categories/<int:category_id>/edit/', methods=['GET', 'POST'])
def editCategory(category_id):
    if 'email' not in login_session:
        flash('You need to be logged in to perform this action.')
        return redirect(url_for('login'))
    category = session.query(Category).filter_by(id=category_id).one()
    if request.method == 'POST':
        if login_session['state'] == request.form['csrf']:
            category.name = request.form['name']
            session.add(category)
            session.commit()
            return redirect(url_for('showCategory', category_id=category.id))
        else:
            abort(403)
    else:
        return render_template('editCategory.html',
                               categories=categories, category=category)


# Render a page to confirm the delete operation for the given category
@app.route('/categories/<int:category_id>/delete/', methods=['GET', 'POST'])
def deleteCategory(category_id):
    if 'email' not in login_session:
        flash('You need to be logged in to perform this action.')
        return redirect(url_for('login'))
    category = session.query(Category).filter_by(id=category_id).one()
    items = session.query(Item).filter_by(category_id=category_id).all()
    if request.method == 'POST':
        if login_session['state'] == request.form['csrf']:
            session.delete(category)
            session.commit()
            for item in items:
                session.delete(item)
                session.commit()
            return redirect(url_for('home'))
        else:
            abort(403)
    else:
        return render_template('deleteCategory.html',
                               categories=categories, category=category)


# Render a page that will show the item detailed information
# (name and description)
@app.route('/categories/<int:category_id>/items/<int:item_id>/')
def showItem(category_id, item_id):
    category = session.query(Category).filter_by(id=category_id).one()
    item = session.query(Item).filter_by(id=item_id).one()
    return render_template('showItem.html', categories=categories,
                           category=category, item=item)


# Render the form to create a new item
@app.route('/categories/<int:category_id>/items/new/',
           methods=['GET', 'POST'])
def newItem(category_id):
    if 'email' not in login_session:
        flash('You need to be logged in to perform this action.')
        return redirect(url_for('login'))
    category = session.query(Category).filter_by(id=category_id).one()
    if request.method == 'POST':
        if login_session['state'] == request.form['csrf']:
            newItem = Item(name=request.form['name'],
                           category_id=request.form['category'],
                           description=request.form['description'])
            session.add(newItem)
            session.commit()
            return redirect(url_for('showItem', category_id=category.id,
                                    item_id=newItem.id))
        else:
            abort(403)
    else:
        return render_template('newItem.html', categories=categories,
                               category=category)


# Render the form to edit an existing item
@app.route('/categories/<int:category_id>/items/<int:item_id>/edit/',
           methods=['GET', 'POST'])
def editItem(category_id, item_id):
    if 'email' not in login_session:
        flash('You need to be logged in to perform this action.')
        return redirect(url_for('login'))
    category = session.query(Category).filter_by(id=category_id).one()
    item = session.query(Item).filter_by(id=item_id).one()
    if request.method == 'POST':
        if login_session['state'] == request.form['csrf']:
            item.name = request.form['name']
            item.category_id = request.form['category']
            item.description = request.form['description']
            session.add(item)
            session.commit()
            return redirect(url_for('showItem', category_id=category.id,
                                    item_id=item.id))
        else:
            abort(403)
    else:
        return render_template('editItem.html', categories=categories,
                               category=category, item=item)


# Render a page to confirm the delete operation for the given item
@app.route('/categories/<int:category_id>/items/<int:item_id>/delete/',
           methods=['GET', 'POST'])
def deleteItem(category_id, item_id):
    if 'email' not in login_session:
        flash('You need to be logged in to perform this action.')
        return redirect(url_for('login'))
    category = session.query(Category).filter_by(id=category_id).one()
    item = session.query(Item).filter_by(id=item_id).one()
    if request.method == 'POST':
        if login_session['state'] == request.form['csrf']:
            session.delete(item)
            session.commit()
            items = session.query(Item).filter_by(category_id=category.id)
            return redirect(url_for('showCategory', category_id=category.id))
        else:
            abort(403)
    else:
        return render_template('deleteItem.html', categories=categories,
                               category=category, item=item)


# Below are the routes for API
# API route to get a list of all categories
@app.route('/api/v1/categories/')
@auth.login_required
def showCategoriesAPI():
    return jsonify(Category=[i.serialize for i in categories])


# API route to get a list of all the items belonging to a given category
@app.route('/api/v1/categories/<int:category_id>/')
@app.route('/api/v1/categories/<int:category_id>/items/')
@auth.login_required
def showCategoryAPI(category_id):
    category = session.query(Category).filter_by(id=category_id).one()
    items = session.query(Item).filter_by(category_id=category.id)
    return jsonify(Category=[category.serialize, [i.serialize for i in items]])


# API route to create a new category
@app.route('/api/v1/categories/new/', methods=['POST'])
@auth.login_required
def newCategoryAPI():
    name = request.json.get('name')
    if name is None:
        abort(400)
    if session.query(Category).filter_by(name=name).first() is not None:
        return jsonify({'message': 'category already exists'})
    category = Category(name=name)
    session.add(category)
    session.commit()
    return jsonify(Category=[category.serialize],
                   message='category succesfully created'), 201


# API route to edit an existing category
@app.route('/api/v1/categories/<int:category_id>/edit/', methods=['POST'])
@auth.login_required
def editCategoryAPI(category_id):
    name = request.json.get('name')
    if name is None:
        abort(400)
    category = session.query(Category).filter_by(id=category_id).first()
    category.name = name
    session.add(category)
    session.commit()
    return jsonify(Category=[category.serialize],
                   message='category succesfully edited'), 200


# API route to delete a given category
@app.route('/api/v1/categories/<int:category_id>/delete/', methods=['POST'])
@auth.login_required
def deleteCategoryAPI(category_id):
    category = session.query(Category).filter_by(id=category_id).first()
    items = session.query(Item).filter_by(category_id=category_id).all()
    for item in items:
        session.delete(item)
        session.commit()
    session.delete(category)
    session.commit()
    return jsonify(message='category succesfully deleted'), 200


# API route to get the detailed information for a given item
@app.route('/api/v1/items/<int:item_id>/')
@app.route('/api/v1/categories/<int:category_id>/items/<int:item_id>/')
@auth.login_required
def showItemAPI(item_id, *args, **kwargs):
    try:
        item = session.query(Item).filter_by(id=item_id).first()
    except:
        return jsonify(message='item not found')
    category = session.query(Category).filter_by(id=item.category_id).one()
    return jsonify(Category=[category.serialize], Item=[item.serialize])


# API route to add a new item inside a given category
@app.route('/api/v1/categories/<int:category_id>/items/new/', methods=['POST'])
@auth.login_required
def newItemAPI(category_id):
    name = request.json.get('name')
    description = request.json.get('description')
    if name is None:
        abort(400)
    item = Item(name=name, description=description, category_id=category_id)
    session.add(item)
    session.commit()
    return jsonify(Item=[item.serialize],
                   message='item succesfully created'), 201


# API route to edit an existing item
@app.route('/api/v1/categories/<int:category_id>/items/<int:item_id>/edit/',
           methods=['POST'])
@auth.login_required
def editItemAPI(category_id, item_id):
    try:
        item = session.query(Item).filter_by(id=item_id).first()
        name = request.json.get('name')
        description = request.json.get('description')
        newCategory_id = request.json.get('category_id')
        if name is None:
            name = item.name
        if description is None:
            description = item.description
        if newCategory_id is None:
            newCategory_id = category_id
        item.name = name
        item.description = description
        category = session.query(Category).filter_by(id=newCategory_id).one()
        item.category_id = newCategory_id
        session.add(item)
        session.commit()
    except:
        return jsonify(message='item not found')
    return jsonify(Category=[category.serialize], Item=[item.serialize],
                   message='item succesfully edited'), 200


# API route to delete a given item
@app.route('/api/v1/categories/<int:category_id>/items/<int:item_id>/delete/',
           methods=['POST'])
@auth.login_required
def deleteItemAPI(category_id, item_id):
    try:
        item = session.query(Item).filter_by(id=item_id).first()
        category = session.query(Category).filter_by(id=category_id).one()
        session.delete(item)
        session.commit()
    except:
        return jsonify(message='item not found')
    return jsonify(Category=[category.serialize],
                   message='item succesfully deleted'), 200

if __name__ == '__main__':
    app.config['SECRET_KEY'] = ''.join(random.choice(
        string.ascii_uppercase + string.digits) for x in xrange(32))
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
