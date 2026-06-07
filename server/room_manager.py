class RoomManager:
    def __init__(self):
        self.rooms = {}  # dictionary to store room information

    def create_room(self, room_name):
        if room_name in self.rooms:
            raise ValueError(f"room '{room_name}' already exists.")
        self.rooms[room_name] = []  # initialize an empty list to store users in the room

    def join_room(self, room_name, username):
        if room_name not in self.rooms:
            raise ValueError(f"room '{room_name}' does not exist.")
        if username in self.rooms[room_name]:
            raise ValueError(f"username '{username}' already in room '{room_name}'.")
        self.rooms[room_name].append(username)  # add user to the room

    def leave_room(self, room_name, username):
        if room_name not in self.rooms:
            raise ValueError(f"room '{room_name}' does not exist.")
        if username not in self.rooms[room_name]:
            raise ValueError(f"username '{username}' not in room '{room_name}'.")
        self.rooms[room_name].remove(username)  # remove user from the room

    def track_user_in_room(self, room_name):
        if room_name not in self.rooms:
            raise ValueError(f"room '{room_name}' does not exist.")
        return list(self.rooms[room_name])  # return a copy of the list of users in the room

    def get_all_rooms(self):
        return list(self.rooms.keys())  # return a list of all room names
     
