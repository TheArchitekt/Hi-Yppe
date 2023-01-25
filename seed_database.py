"""This file seeds the database."""

import os
import json
from datetime import datetime

import crud
import model
import server

os.system("dropdb sneakers")
os.system("createdb sneakers")

model.connect_to_db(server.app)
model.db.create_all()

with open("data/apidata.json") as f:
    sneaker_data = json.loads(f.read())

sneakers_in_db = []

for sneaker in sneaker_data:
    sneaker_name = sneaker["shoeName"]
    sneaker_brand = sneaker["brand"]
    sneaker_description = sneaker["description"]
    sneaker_price = sneaker["retailPrice"]
    release_date = datetime.strptime(sneaker["releaseDate"], "%Y-%m-%d")
    sneaker_img_path = sneaker["thumbnail"]



    db_sneakers = crud.new_sneaker(sneaker_name, sneaker_brand, sneaker_price, sneaker_description, release_date, sneaker_img_path)

    sneakers_in_db.append(db_sneakers)

model.db.session.add_all(sneakers_in_db)
model.db.session.commit()

for i in range(10):
    user_email = f"test{i}@gmail.com"
    user_password = "1234"
    user_name = f"test{i}"

    user = crud.new_user(user_email, user_password, user_name)

    model.db.session.add(user)

model.db.session.commit()
