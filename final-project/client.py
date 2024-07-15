import socket

def send_command(command):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 3000))
    if command.startswith('upload '):
        filename = command[7:]
        client_socket.send(command.encode())
        response = client_socket.recv(1024).decode()
        if response == "Ready to receive":
            with open(filename, 'rb') as f:
                while (chunk := f.read(4096)):
                    client_socket.send(chunk)
            client_socket.send(b'EOF')
    else:
        client_socket.send(command.encode())
    
    response = client_socket.recv(4096).decode()
    print(f"Server response: {response}")
    client_socket.close()

def main():
    print("Welcome to the file management client. Available commands:")
    print("ls, cd <directory>, mkdir <folderName>, del <filename>, rmdir <folderName>, touch <filename>, tree, upload <filename>, exit")
    while True:
        command = input("Enter command (type 'exit' to quit): ")
        if command == 'exit':
            break
        send_command(command)

if __name__ == "__main__":
    main()
