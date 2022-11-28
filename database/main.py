from database.db_tools import inserts
from database.db_tools.base import Session
from database.db_tools.db_workers import DBWorker


session = Session()

worker = DBWorker(session)
# get all users
users = worker.get_all_users()
print(users)

#get user by id
user = worker.get_user(user_id=1)
print(user)

# get user and his address
user, address = worker.get_user_address(user_id=1)
print(user)
print(address)

# get user and contacts
user, contacts = worker.get_user_contacts(user_id=1)
print(user)

for cont in contacts:
    print(cont)
