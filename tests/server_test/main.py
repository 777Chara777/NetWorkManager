import socket


def server_program():
    # get the hostname
    host = "127.0.0.1"
    port = 5000  

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # get instance
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(1)

    conn, address = server_socket.accept()  # accept new connection

    print("Connection from: " + str(address))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        print("from connected user: " + str(data))
        conn.send(data.encode())

    conn.close()  # close the connection

if __name__ == '__main__':
    server_program()