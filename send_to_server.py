import json
import socket
# from typing import List

HOST = "127.0.0.1"
PORT = 42069

class ServerCommunicator:
    shape_to_letter = {
        "square": "S",
        "plus": "P",
        "circle": "O",
        "arrow": "A"
    }

    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((HOST, PORT))

    def send(self, shapes):
        shapeString = "".join((self.shape_to_letter.get(shape) for shape in shapes))
        data = json.dumps({"sequence": shapeString})
        self.socket.sendall(bytes(data, encoding="utf-8"))
