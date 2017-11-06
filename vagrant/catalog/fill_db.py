from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Category, Base, Item

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Create categories
category1 = Category(name="Books")
category2 = Category(name="Movies, Music & Games")
category3 = Category(name="Electronics, Computers & Office")
category4 = Category(name="Home, Garden & Tools")
category5 = Category(name="Food & Grocery")
category6 = Category(name="Beauty & Health")
category7 = Category(name="Toys, Kids & Baby")
category8 = Category(name="Clothing, Shoes & Jewelry")
category9 = Category(name="Handmade")
category10 = Category(name="Sports & Outdoors")
category11 = Category(name="Automotive & Industrials")

categories = [category1, category2, category3, category4, category5,
              category6, category7, category8, category9, category10,
              category11]

# Add categories to database
for category in categories:
    if session.query(Category).filter_by(name=category.name).first() is
    not None:
        print("Category already existing. Skipping...")
    else:
        session.add(category)
        session.commit()
print "Categories added!"

# Create items
item1 = Item(name="Origin", description="Robert Langdon, Harvard professor\
    of symbology and religious iconology, arrives at the ultramodern \
    Guggenheim Museum Bilbao to attend a major announcement—the unveiling of \
    a discovery that “will change the face of science forever.” The evening’s \
    host is Edmond Kirsch, a forty-year-old billionaire and futurist whose \
    dazzling high-tech inventions and audacious predictions have made him a \
    renowned global figure. Kirsch, who was one of Langdon’s first students \
    at Harvard two decades earlier, is about to reveal an astonishing \
    breakthrough . . . one that will answer two of the fundamental \
    questions of human existence.", category=category1)
item2 = Item(name="It", description="Stephen King’s terrifying, classic \
    #1 New York Times bestseller, “a landmark in American literature” \
    (Chicago Sun-Times)—about seven adults who return to their hometown to \
    confront a nightmare they had first stumbled on as teenagers…an evil \
    without a name: It.", category=category1)
item3 = Item(name="A Column of Fire", description="As Europe erupts, can \
    one young spy protect his queen? International bestselling author Ken \
    Follett takes us deep into the treacherous world of powerful monarchs, \
    intrigue, murder, and treason with his magnificent new epic, \
    A Column of Fire.", category=category1)
item4 = Item(name="The Rooster Bar", description="Mark, Todd, and Zola came \
    to law school to change the world, to make it a better place. But now, \
    as third-year students, these close friends realize they have been duped. \
    They all borrowed heavily to attend a third-tier, for-profit law school \
    so mediocre that its graduates rarely pass the bar exam, let alone get \
    good jobs. And when they learn that their school is one of a chain owned \
    by a shady New York hedge-fund operator who also happens to own a bank \
    specializing in student loans, the three know they have been caught up \
    in The Great Law School Scam.", category=category1)
item5 = Item(name="Harry Potter and the Sorcerer's Stone", description="\
    Harry Potter has never even heard of Hogwarts when the letters start \
    dropping on the doormat at number four, Privet Drive. Addressed in green \
    ink on yellowish parchment with a purple seal, they are swiftly \
    confiscated by his grisly aunt and uncle. Then, on Harry's eleventh \
    birthday, a great beetle-eyed giant of a man called Rubeus Hagrid bursts \
    in with some astonishing news: Harry Potter is a wizard, and he has a \
    place at Hogwarts School of Witchcraft and Wizardry. An incredible \
    adventure is about to begin!", category=category1)
item6 = Item(name="Before We Were Yours", description="Memphis, 1939. \
    Twelve-year-old Rill Foss and her four younger siblings live a magical \
    life aboard their family’s Mississippi River shantyboat. But when their \
    father must rush their mother to the hospital one stormy night, Rill is \
    left in charge—until strangers arrive in force. Wrenched from all that is \
    familiar and thrown into a Tennessee Children’s Home Society orphanage, \
    the Foss children are assured that they will soon be returned to their \
    parents—but they quickly realize the dark truth. At the mercy of the \
    facility’s cruel director, Rill fights to keep her sisters and brother \
    together in a world of danger and uncertainty.", category=category1)
item7 = Item(name="The Cuban Affair", description="Daniel Graham \
    MacCormick—Mac for short—seems to have a pretty good life. At age \
    thirty-five he’s living in Key West, owner of a forty-two-foot charter \
    fishing boat, The Maine. Mac served five years in the Army as an infantry \
    officer with two tours in Afghanistan. He returned with the Silver Star, \
    two Purple Hearts, scars that don’t tan, and a boat with a big bank \
    loan. Truth be told, Mac’s finances are more than a little \
    shaky.", category=category1)
item8 = Item(name="Harry Potter and the Order of the Phoenix", description="\
    Dark times have come to Hogwarts. After the Dementors' attack on his \
    cousin Dudley, Harry Potter knows that Voldemort will stop at nothing to \
    find him. There are many who deny the Dark Lord's return, but Harry is \
    not alone: a secret order gathers at Grimmauld Place to fight against the \
    Dark forces. Harry must allow Professor Snape to teach him how to protect \
    himself from Voldemort's savage assaults on his mind. But they are \
    growing stronger by the day and Harry is running out of \
    time ...", category=category1)
item9 = Item(name="Sleeping Beauties", description="In a future so real and \
    near it might be now, something happens when women go to sleep: they \
    become shrouded in a cocoon-like gauze. If they are awakened, if the \
    gauze wrapping their bodies is disturbed or violated, the women become \
    feral and spectacularly violent. And while they sleep they go to another \
    place, a better place, where harmony prevails and conflict is \
    rare.", category=category1)
item10 = Item(name="A Game of Thrones", description="From a master of \
    contemporary fantasy comes the first novel of a landmark series unlike \
    any you’ve ever read before. With A Game of Thrones, George R. R. Martin \
    has launched a genuine masterpiece, bringing together the best the genre \
    has to offer. Mystery, intrigue, romance, and adventure fill the pages \
    of this magnificent saga, the first volume in an epic series sure to \
    delight fantasy fans everywhere.", category=category1)

items = [item1, item2, item3, item4, item5, item6, item7, item8, item9, item10]
for item in items:
    if session.query(Item).filter_by(name=item.name).first() is
    not None:
        print("Item already existing. Skipping...")
    else:
        session.add(item)
        session.commit()
print "Items added!"

# item1 = Item(name="", description="", category=category1)
# item2 = Item(name="", description="", category=category1)
# item3 = Item(name="", description="", category=category1)
# item4 = Item(name="", description="", category=category1)
# item5 = Item(name="", description="", category=category1)
# item6 = Item(name="", description="", category=category1)
# item7 = Item(name="", description="", category=category1)
# item8 = Item(name="", description="", category=category1)
# item9 = Item(name="", description="", category=category1)
# item10 = Item(name="", description="", category=category1)

# items = [item1, item2, item3, item4, item5, item6, item7, item8, item9, item10]
# for item in items:
#     if session.query(Category).filter_by(name=category.name).first() is not None:
#         print("Item already existing. Skipping...")
#     else:
#         session.add(category)
#         session.commit()
# print "Categories added!"

print "Catalog items added!"