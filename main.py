import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models import Book, Publisher, Sale, Shop, create_tables

DSN = 'postgresql://postgres:LSamovar69@localhost:5432/HW_db'

engine = sqlalchemy.create_engine(DSN)
Session = sessionmaker(bind=engine)
session = Session()

create_tables(engine)

name = input("Введите имя издателя:")

sales = session.query(Book.title, Shop.name, Sale.price, Sale.date_sale).filter(Publisher.name == name).all()


if sales:
    for sale in sales:
        print(f"{sale.title}, {sale.name}, {sale.price}, {sale.date_sale}")
else:
    print(f"Издатель с именем {name} не найден")

session.close()
