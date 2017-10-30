from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from database_setup import Category, Base, Item
 
engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Create categories
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

# Add categories to database
for category in categories:
	if session.query(Category).filter_by(name = category.name).first() is not None:
		print("Category already existing. Skipping...")
	else:
		session.add(category)
		session.commit()
print "Categories added!"

# Create items
# item1 = Item(name = "", description = "", category = category1)
# item2 = Item(name = "", description = "", category = category1)
# item3 = Item(name = "", description = "", category = category1)
# item4 = Item(name = "", description = "", category = category1)
# item5 = Item(name = "", description = "", category = category1)
# item6 = Item(name = "", description = "", category = category1)
# item7 = Item(name = "", description = "", category = category1)
# item8 = Item(name = "", description = "", category = category1)
# item9 = Item(name = "", description = "", category = category1)
# item10 = Item(name = "", description = "", category = category1)

# items = [item1, item2, item3, item4, item5, item6, item7, item8, item9, item10]
# for item in items:
#     if session.query(Category).filter_by(name = category.name).first() is not None:
#         print("Item already existing. Skipping...")
#     else:
#         session.add(category)
#         session.commit()
# print "Categories added!"

# item1 = Item(name = "", description = "", category = category1)
# item2 = Item(name = "", description = "", category = category1)
# item3 = Item(name = "", description = "", category = category1)
# item4 = Item(name = "", description = "", category = category1)
# item5 = Item(name = "", description = "", category = category1)
# item6 = Item(name = "", description = "", category = category1)
# item7 = Item(name = "", description = "", category = category1)
# item8 = Item(name = "", description = "", category = category1)
# item9 = Item(name = "", description = "", category = category1)
# item10 = Item(name = "", description = "", category = category1)

# items = [item1, item2, item3, item4, item5, item6, item7, item8, item9, item10]
# for item in items:
#     if session.query(Category).filter_by(name = category.name).first() is not None:
#         print("Item already existing. Skipping...")
#     else:
#         session.add(category)
#         session.commit()
# print "Categories added!"

print "Catalog items added!"