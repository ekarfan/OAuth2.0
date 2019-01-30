from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, drop_database, create_database
from database_setup import Category, CategoryItem, User, Base


def database_init():

    engine = create_engine('sqlite:///itemcatalog.db?check_same_thread=False')
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    Base.metadata.bind = engine

    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    user1 = User(name="Karen Fan", email="fancp@yahoo.com")
    session.add(user1)
    session.commit()

    category1 = Category(name="Meat", user_id=1)

    session.add(category1)
    session.commit()

    item1 = CategoryItem(name="pork", user_id=1, description="\
        Pork is an excellent source of protein", category=category1)
    session.add(item1)
    session.commit()

    item2 = CategoryItem(name="beef", user_id=1, description="\
        Beef is a great source of 10 essential nutrients \
        including protein", category=category1)

    session.add(item2)
    session.commit()

    item3 = CategoryItem(name="chicken", user_id=1, description="\
        Skinless white meat chicken breast is the \
        lowest in fat and calories.", category=category1)

    session.add(item3)
    session.commit()

    category2 = Category(name="Grain", user_id=1)

    session.add(category2)
    session.commit()

    item1 = CategoryItem(name="bread", user_id=1, description="\
        Bread made with sprouted grains \
        is a good option", category=category2)

    session.add(item1)
    session.commit()

    item2 = CategoryItem(name="pasta", user_id=1,  description="\
        Pasta is a fat-free, low sodium food that can fit right in with \
        a weight loss or management plan.", category=category2)

    session.add(item2)
    session.commit()

    item3 = CategoryItem(name="rice", user_id=1, description="\
        Brown rice contains a fair amount of fiber (1.8%), \
        while white rice is very low in fiber (0.3%)", category=category2)

    session.add(item3)
    session.commit()

# Items for Percussion
    category3 = Category(name="Dairyfood", user_id=1)

    session.add(category3)
    session.commit()

    item1 = CategoryItem(name="milk", user_id=1, description="\
        Milk Is the Top-Source of Calcium in Americans' \
        Diets", category=category3)

    session.add(item1)
    session.commit()

    item2 = CategoryItem(name="cheese", user_id=1, description="\
        Cheese contains a host of nutrients like calcium, protein, \
        phosphorus, zinc, vitamin A and \
        vitamin B12.", category=category3)

    session.add(item2)
    session.commit()

    item3 = CategoryItem(
        name="yogurt", user_id=1,
        description="Yogurt(also spelled yoghurt),is one of the most popular \
        fermented dairy products in the world,made by adding \
        live bacteria to milk",
        category=category3
        )

    session.add(item3)
    session.commit()

# Items for Brass
    category4 = Category(name="Vegetables", user_id=1)

    session.add(category4)
    session.commit()
    categories = session.query(Category).all()
    for category in categories:
        print("Category: " + category.name)


if __name__ == '__main__':
    database_init()
