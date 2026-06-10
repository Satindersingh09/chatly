class RoomManager:
    def __init__(self):
        self.rooms = {}  # dictionary to store room information

    def create_room(self, room_name):
        if room_name in self.rooms:
            raise ValueError(f"room '{room_name}' already exists.")
        else:
            self.rooms[room_name] = []  # initialize an empty list to store users in the room

    def join_room(self, room_name, socket, username):
        if room_name not in self.rooms:
            raise ValueError(f"room '{room_name}' does not exist.")
        if socket in self.rooms[room_name]:
            raise ValueError(f"socket '{username}' already in room '{room_name}'.")
        self.rooms[room_name].append(socket)  # add user to the room

    def leave_room(self, room_name, socket, username):
        if room_name not in self.rooms:
            raise ValueError(f"room '{room_name}' does not exist.")
        if socket not in self.rooms[room_name]:
            raise ValueError(f"socket '{username}' not in room '{room_name}'.")
        self.rooms[room_name].remove(socket)  # remove user from the room

    def remove_user_from_all_rooms(self, socket, username):
        for room_name, sockets in self.rooms.items():
            if socket in sockets:
                sockets.remove(socket)  # remove user from all rooms they are in

    def delete_room(self, room_name):
        if room_name not in self.rooms:
            raise ValueError(f"room '{room_name}' does not exist.")
        if len(self.rooms[room_name]) == 0:
            del self.rooms[room_name]  # delete the room if its empty

    def track_members(self, room_name):
        if room_name not in self.rooms:
            raise ValueError(f"room '{room_name}' does not exist.")
        return list(self.rooms[room_name])  # return a copy of the list of users in the room
    
    def get_user_rooms(self, socket, username):
        user_rooms = []
        for room_name, sockets in self.rooms.items():
            if socket in sockets:
                user_rooms.append(room_name)
                print(f"{username} is in room #{room_name}")  # print which room user is in
        return user_rooms
    
    def broadcast_message(self, room_name, message, sender_socket):
        if room_name not in self.rooms:
            raise ValueError(f"room '{room_name}' does not exist.")
        for socket in self.rooms[room_name]:
            if socket != sender_socket:  # send message to all users except the sender
                socket.send(message.encode('utf-8'))  # send message to the user

    def get_all_rooms(self):
        return list(self.rooms.keys())  # return all available room names
     
