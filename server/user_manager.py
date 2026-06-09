from multiprocessing import connection


class UserManager:
    def __init__(self):
        self.users = {}  # Dictionary to store user information
        self.sockets = {}  # Dictionary to store user connections
    def add_user(self, username, connection):
        if username in self.users:
            raise ValueError(f"username '{username}' already exists.")
        else:
            self.users[username] = connection
            self.sockets[connection] = username
        
    def remove_user(self, username):
        if username in self.users:

            connection = self.users[username]

            del self.users[username]
            del self.sockets[connection]
        else:
            raise ValueError(f"username '{username}' does not exist.")
        
    def get_user_connection(self, username):
        if username in self.users:
            return self.users[username]
        else:
            raise ValueError(f"username '{username}' does not exist.")
        
    def get_username(self, connection):
        if connection in self.sockets:
            return self.sockets[connection]
        else:
            raise ValueError(f"connection '{connection}' does not exist.")

    def username_exists(self, username):
        return username in self.users
        
    def get_all_users(self):
        return list(self.users.keys())