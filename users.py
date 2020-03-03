import pickle
import config
import os.path

if not os.path.isfile(config.STORAGE_FILE):
    with open(config.STORAGE_FILE, 'wb') as new_file:
        pickle.dump(list(), new_file)


def get_users():
    with open(config.STORAGE_FILE, 'rb') as f:
        users = pickle.load(f)
        return users


def add_user(user):
    users = get_users()
    users.append(user)
    with open(config.STORAGE_FILE, 'wb') as f:
        pickle.dump(users, f)


def get_user(user_id):
    for user in get_users():
        if user['user_id'] == user_id:
            return user
    return None


def update_user(user):
    users = get_users()
    for db_user in users:
        if db_user['user_id'] == user['user_id']:
            db_user.update(user)
            with open(config.STORAGE_FILE, 'wb') as f:
                pickle.dump(users, f)
                return


