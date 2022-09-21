from itertools import product
from unittest import result
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
import requests
import re

my_app = Flask(__name__)


@my_app.route("/")
def homepage():

    url_title = request.args.get('url_title')
    try:
        if url_title != None and re.search("^https://", url_title):

            print(url_title)
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
            response = requests.get(url_title)
            if response.status_code == 200:
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
            return render_template("home.html", pagetitle="HomePage", url_title=url_title)
        else:
            return render_template("home.html", pagetitle="HomePage", error="Please enter valid link")
    except:
        return render_template("home.html", pagetitle="HomePage", error="Please enter valid link")


@my_app.route("/getdata")
def getdata():
    try:
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
        price_from = request.args.get('price_from')
        to = request.args.get('to')
        prod = products.select()
        conn = engine.connect()
        result = conn.execute(prod)
        data = []
        x = price_from
        y = to
        for i in result:
            if x != None and y != None:
                if int(i[4]) >= int(x) and int(i[4]) <= int(y):
                    data.append(i)
            else:
                x = 0
                y = 0

        return render_template("getdata.html", pagetitle="DataPage", price_from=price_from, to=to, data=data)
    except:
        return render_template("getdata.html", pagetitle="DataPage",error="Please enter valid price range" )

if __name__ == "__main__":
    my_app.run(debug=True, port=8000)
