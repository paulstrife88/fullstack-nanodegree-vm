from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from database_setup import Category, Base, Item
 
engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


category1 = Category(name = "Books")
category2 = Category(name = "Movies, Music & Games")
category3 = Category(name = "Electronics, Computers & Office")
category4 = Category(name = "Home, Garden & Tools")
category5 = Category(name = "Food & Grocery")
category6 = Category(name = "Beauty & Health")
category7 = Category(name = "Toys, Kids & Baby")
category8 = Category(name = "Clothing, Shoes & Jewelry")
category9 = Category(name = "Handmade")
category10 = Category(name = "Sports & Outdoors")
category11 = Category(name = "Automotive & Industrials")

categories = [category1, category2, category3, category4, category5,
			  category6, category7, category8, category9, category10,
			  category11]
for category in categories:
	session.add(category)
	session.commit()


# item1 = Item(name = "French Fries", description = "with garlic and parmesan", price = "$2.99", course = "Appetizer", category = category1)

# session.add(item1)
# session.commit()

# item2 = Item(name = "Chicken Burger", description = "Juicy grilled chicken patty with tomato mayo and lettuce", price = "$5.50", course = "Entree", category = category1)

# session.add(item2)
# session.commit()

# item3 = Item(name = "Chocolate Cake", description = "fresh baked and served with ice cream", price = "$3.99", course = "Dessert", category = category1)

# session.add(item3)
# session.commit()

# item4 = Item(name = "Sirloin Burger", description = "Made with grade A beef", price = "$7.99", course = "Entree", category = category1)

# session.add(item4)
# session.commit()

# item5 = Item(name = "Root Beer", description = "16oz of refreshing goodness", price = "$1.99", course = "Beverage", category = category1)

# session.add(item5)
# session.commit()

# item6 = Item(name = "Iced Tea", description = "with Lemon", price = "$.99", course = "Beverage", category = category1)

# session.add(item6)
# session.commit()

# item7 = Item(name = "Grilled Cheese Sandwich", description = "On texas toast with American Cheese", price = "$3.49", course = "Entree", category = category1)

# session.add(item7)
# session.commit()

# item8 = Item(name = "Veggie Burger", description = "Made with freshest of ingredients and home grown spices", price = "$5.99", course = "Entree", category = category1)

# session.add(item8)
# session.commit()

print "added menu items!"