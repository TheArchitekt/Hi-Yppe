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
