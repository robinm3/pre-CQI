import time
from send_to_server import ServerCommunicator

def main():
    serverCommunicator = ServerCommunicator();
    while 1:
        time.sleep(1)
        serverCommunicator.send(["circle", "circle", "arrow", "square", "plus"])


if __name__ == "__main__":
    main()
