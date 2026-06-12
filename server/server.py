import socket
import threading
import json
import logging

from user_manager import UserManager
from room_manager import RoomManager


# Load configuration file
with open("config.json", "r") as file:
    config = json.load(file)

HOST = config["host"]
PORT = config["port"]
BUFFER_SIZE = config["buffer_size"]


# Logging setup
logging.basicConfig(
    filename="../logs/server.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)
user_manager = UserManager()
room_manager = RoomManager()

# Function to send messages to clients
def send(client_socket, message):
    try:
        client_socket.send(message.encode("utf-8"))
    except:
        pass
def handle_client(client_socket):
    username = None

    try:
        username = client_socket.recv(BUFFER_SIZE).decode("utf-8").strip()

        # Check if username already exists
        if user_manager.username_exists(username):
            send(client_socket, "ERROR: Username already exists")
            client_socket.close()
            return

        # Add user to user manager and join the default "Lobby" room
        user_manager.add_user(username, client_socket)
        room_manager.join_room("Lobby", client_socket, username)

        logging.info(f"{username} connected")

        send(client_socket, "Connected to server")
        while True:

            message = client_socket.recv(BUFFER_SIZE).decode("utf-8").strip()

            if not message:
                break

            # CREATE ROOM
            if message.startswith("/create "):

                room_name = message.split(" ", 1)[1]

                try:
                    room_manager.create_room(room_name)

                    room_manager.remove_user_from_all_rooms(
                        client_socket,
                        username
                    )

                    room_manager.join_room(
                        room_name,
                        client_socket,
                        username
                    )

                    send(client_socket, f"Room '{room_name}' created and joined")

                except Exception as e:
                    send(client_socket, str(e))

            # JOIN ROOM
            elif message.startswith("/join "):

                room_name = message.split(" ", 1)[1]

                try:
                    room_manager.remove_user_from_all_rooms(
                        client_socket,
                        username
                    )

                    room_manager.join_room(
                        room_name,
                        client_socket,
                        username
                    )

                    send(client_socket, f"Joined room '{room_name}'")

                except Exception as e:
                    send(client_socket, str(e))

            # LIST ROOMS
            elif message == "/rooms":

                rooms = room_manager.get_all_rooms()
                send(client_socket, "Rooms: " + ", ".join(rooms))

            # LIST USERS
            elif message == "/users":

                users = user_manager.get_all_users()
                send(client_socket, "Users: " + ", ".join(users))       