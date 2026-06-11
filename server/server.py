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

