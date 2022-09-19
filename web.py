from dbm import dumb
from itertools import product
from tokenize import Ignore
from unittest import result
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
import requests
import json
import yaml
from sqlalchemy.dialects.postgresql import insert

url = input("please enter url")


def app(url):

    engine = create_engine("sqlite:///web.db")

    meta_data = MetaData()

    products = Table(
        "products", meta_data,
        Column("id", Integer, primary_key=True),
        Column("title", String),
        Column("category", String),
        Column("rating", String),
        Column("price", Integer)
    )
    meta_data.create_all(engine)

    response = requests.get(url)
    file = response.json()

    file1 = file["products"]

    for i in file1:
        x1 = i["title"]
        x2 = i["category"]
        x3 = i["rating"]
        x4 = i["price"]
        ins = products.insert().values(title=x1, category=x2, rating=x3, price=x4)
        conn = engine.connect()
        result = conn.execute(ins)
    return


app(url)
x = int(input("please enter price range from"))
y = int(input("please enter price range to"))

def getdata(x, y):
    engine = create_engine("sqlite:///web.db")
    meta_data = MetaData()

    products = Table(
        "products", meta_data,
        Column("id", Integer, primary_key=True),
        Column("title", String),
        Column("category", String),
        Column("rating", String),
        Column("price", Integer)
    )

    prod = products.select()
    conn = engine.connect()
    result = conn.execute(prod)
    data = []
    for i in result:
        if int(i[4]) >= x and int(i[4]) <= y:
            data.append(i)
    return data

print(getdata(int(x),int(y)))