import socket
import os

def handle_command(command, client_socket):
    try:
        if command.startswith('ls'):
            files = os.listdir('.')
            result = '\n'.join(files) if files else 'Directory is empty'
        elif command.startswith('cd '):
            directory = command[3:]
            os.chdir(directory)
            result = f"Changed directory to {directory}"
        elif command.startswith('mkdir '):
            folder_name = command[6:]
            os.mkdir(folder_name)
            result = f"Folder {folder_name} created"
        elif command.startswith('del '):
            filename = command[4:]
            os.remove(filename)
            result = f"File {filename} deleted"
        elif command.startswith('rmdir '):
            folder_name = command[6:]
            os.rmdir(folder_name)
            result = f"Folder {folder_name} removed"
        elif command.startswith('touch '):
            filename = command[6:]
            open(filename, 'a').close()
            result = f"File {filename} created"
        elif command.startswith('tree'):
            tree_result = []
            for root, dirs, files in os.walk('.'):
                level = root.replace(os.path.sep, '/').count('/')
                indent = ' ' * 4 * (level)
                tree_result.append(f"{indent}{os.path.basename(root)}/")
                subindent = ' ' * 4 * (level + 1)
                for f in files:
                    tree_result.append(f"{subindent}{f}")
            result = '\n'.join(tree_result)
        elif command.startswith('upload '):
            filename = command[7:]
            client_socket.send("Ready to receive".encode())
            with open(filename, 'wb') as f:
                while True:
                    data = client_socket.recv(4096)
                    if data == b'EOF':
                        break
                    f.write(data)
            result = f"File {filename} uploaded successfully"
        else:
            result = 'Unknown command'
    except Exception as e:
        result = str(e)
    
    client_socket.send(result.encode())

def handle_client(client_socket):
    while True:
        command = client_socket.recv(1024).decode()
        if not command:
            break
        if command.startswith('upload '):
            handle_command(command, client_socket)
        else:
            handle_command(command, client_socket)
    
    client_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 3000))
    server_socket.listen(5)
    print("Server is listening on port 3000..")
    
    while True:
        client_socket, address = server_socket.accept()
        print(f"Connection from {address} has been established!")
        handle_client(client_socket)

if __name__ == "__main__":
    start_server()

