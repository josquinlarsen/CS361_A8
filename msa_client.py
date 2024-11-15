# Josquin Larsen
# 8/nov/2024
# A8 - Microservice A - Wikipedia Search

# ZMQ layout based on Luis Flores' Introduction to ZeroMQ (CS361 OSU)

import zmq


def main():
    """
    Runs the client logic for the ZeroMQ
    Client socket connection
    """

    context = zmq.Context()
    print("Connecting to server...")
    # request socket
    socket = context.socket(zmq.REQ)

    #  '*' may need to be updated to localhost or 127.0.0.1
    #  Port number may be altered to avoid collisions
    socket.connect("tcp://127.0.0.1:5555")
    print('Sending request...')

    
    while True:
        artist_name = ""
        if len(artist_name) < 1:
            artist_name = input("Please enter an artist's name to search: ")

        socket.send_string(artist_name)

        message = socket.recv()

        print(f"Here's what I've found: {message.decode()}")


if __name__ == "__main__":
    main()

