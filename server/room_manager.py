class Room_Manager:
    def __init__(self):
        self.rooms = {}     # dictinary to store room information

    def create_room(self, room_name):
        if room_name in self.rooms:
            raise ValueError{f"room '{room_name}' already exists."}
        else:
            self.rooms[room_name] = []   # initialize an empty list to store users in the room

    def join_room(self, room_name, username):
        if room_name in self.rooms:
            if username not in self.rooms[room_name]:
                self.rooms[room_name].append(username)  # add user to the room
            else:
                raise ValueError{f"uername '{username}' already in room '{room_name}'."}
        else:
            raise ValueError{f"room '{room_name}' does not exist."}

    def leave_room(self, room_name, username):
        if room_name in self.rooms:
            if username in self.rooms[room_name]:
                self.rooms[room_name].remove(username)  # remove user from the room
            else:
                raise ValueError{f"uername '{username}' not in room '{room_name}'."}
        else:
            raise ValueError{f"room '{room_name}' does not exist."}

    def track_user_in_room(self, room_name):
        if room_name in self.rooms:
            return self.rooms[room_name]  # return the list of users in the room
        else:
            raise ValueError{f"room '{room_name}' does not exist."}
    
    def get_all_rooms(self):
        return list(self.rooms.keys())  # return a list of all room names
     
