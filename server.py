import socket


class GenericServer:
    """
        Server class accept as attributes:
            host: str the name of the local host ('localhost' by default)
            port: int the port number
            backlog: int the queue, i.e. max number of clients in queue
    """
    def __init__(self, host: str, port: int, backlog: int):
        self.socket = socket.socket()
        self.socket.bind((host, port))
        self.socket.listen(backlog)

        print("Server is listening...")

        self.connect_and_receive()

    # Attempt to establish a connection and receive the client request
    def connect_and_receive(self):
        while True:
            connection, address = self.socket.accept()

            # Until connection is open...
            with connection:
                print(f"Connected by {address}")
                
                # ... read the data
                while True:
                    data = connection.recv(4096)
                    
                    # Break is message i void
                    if not data:
                        break
                    
                    connection.sendall(data)
                    print(f"Response sent.")

    # Function to override to elaborate the Client request
    @staticmethod
    def elaborate_request(req):
        pass


if __name__ == "__main__":
    srv = GenericServer(host='localhost', port=50000, backlog=5)
