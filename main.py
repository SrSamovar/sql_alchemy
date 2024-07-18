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
    if name is isdigit():
        pub = sales.filter(Publisher.id == int(name)).all()
    else:
        pub = sales.filter(Publisher.name == name).all()

    for title, shop_name, sale_price, data_sale in pub:
        print(f'Издание: {title},название магазина: {shop_name},цена: {sale_price},дата продажи: {data_sale}')


if __name__ == "__main__":
    name = input('Введите имя или айди публициста:')
    get_shops(name)

session.close()
