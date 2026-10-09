import re
from database import db

user = db.UsersTable()
user.connect_to_store_database()
user.create_users_table()