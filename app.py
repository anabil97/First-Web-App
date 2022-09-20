from itertools import product
from unittest import result
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
import requests


my_app = Flask(__name__)


@my_app.route("/")
def homepage():
    return render_template("home.html", pagetitle="HomePage")


@my_app.route("/getdata")
def getdata():
    return render_template("getdata.html", pagetitle="DataPage")

# def app(url):

#     engine = create_engine("sqlite:///web.db")

#     meta_data = MetaData()

#     products = Table(
#         "products", meta_data,
#         Column("id", Integer, primary_key=True),
#         Column("title", String),
#         Column("category", String),
#         Column("rating", String),
#         Column("price", String)
#     )
#     meta_data.create_all(engine)

#     response = requests.get(url)
#     file = response.json()

#     file1 = file["products"]

#     for i in file1:
#         x1 = i["title"]
#         x2 = i["category"]
#         x3 = i["rating"]
#         x4 = i["price"]
#         ins = products.insert().values(title=x1, category=x2, rating=x3, price=x4)
#         conn = engine.connect()
#         result = conn.execute(ins)
#     return 

# def getdata(x, y):
#     engine = create_engine("sqlite:///web.db")
#     meta_data = MetaData()

#     products = Table(
#         "products", meta_data,
#         Column("id", Integer, primary_key=True),
#         Column("title", String),
#         Column("category", String),
#         Column("rating", String),
#         Column("price", String)
#     )

#     prod = products.select()
#     conn = engine.connect()
#     result = conn.execute(prod)
#     data = []
#     for i in result:
#         if int(i[4]) >= x and int(i[4]) <= y:
#             data.append(i)
#     return data




if __name__ == "__main__":
    my_app.run(debug=True, port=8000)
