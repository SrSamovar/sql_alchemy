from curses.ascii import isdigit
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models import Book, Publisher, Sale, Shop, Stock, create_tables

DSN = 'postgresql://postgres:LSamovar69@localhost:5432/HW_db'

engine = sqlalchemy.create_engine(DSN)
Session = sessionmaker(bind=engine)
session = Session()

create_tables(engine)

def get_shops(name):
    sales = session.query(Book.title, Shop.name, Sale.price, Sale.date_sale).select_from(Shop).\
    join(Stock).\
    join(Book).\
    join(Publisher).\
    join(Sale)
    if name is isdigit:
        pub = sales.filter(Publisher.id == name).all()
    else:
        pub = sales.filter(Publisher.name == name).all()

    for Book.title, Shop.name, Sale.price, Sale.date_sale in pub:
        print(f"Издание: {Book.title}, Магазин: {Shop.name}, Цена: {Sale.price}, Дата продажи: {Sale.date_sale}")


if __name__ == "__main__":
    name = input('Введите имя или айди публициста:')
    get_shops(name)

session.close()
