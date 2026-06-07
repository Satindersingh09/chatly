class UserManager:
    def __init__(self):
        self.users = {}  # Dictionary to store user information

    def add_user(self, username, connection):
        if username in self.users:
            raise ValueError(f"username '{username}' already exists.")
        else:
            self.users[username] = connection
        
    def remove_user(self, username):
        if username in self.users:
            del self.users[username]
        else:
            raise ValueError(f"username '{username}' does not exist.")
        
    def get_user_connection(self, username):
        if username in self.users:
            return self.users[username]
        else:
            raise ValueError(f"username '{username}' does not exist.")
    
    def get_all_users(self):
        return list(self.users.keys())