import socket
import time

HOST = '127.0.0.1'
PORT = 5555

def start_ai_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    print("Client IA connecté au serveur.")

    while True:
        # Simulation d'un message généré par l'IA
        message = "Message de l'IA"
        client.sendall(message.encode('utf-8'))
        time.sleep(5)  # Pause entre les messages
        response = client.recv(1024).decode('utf-8')
        print(f"Serveur : {response}")

if __name__ == "__main__":
    start_ai_client()