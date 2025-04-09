import socket

HOST = '127.0.0.1'
PORT = 5555

def start_human_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    print("Connecté au serveur. Tapez vos messages :")

    while True:
        message = input("> ")
        client.sendall(message.encode('utf-8'))
        response = client.recv(1024).decode('utf-8')
        print(f"Serveur : {response}")

if __name__ == "__main__":
    start_human_client()