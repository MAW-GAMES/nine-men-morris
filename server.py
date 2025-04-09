import socket
import threading

# Configuration du serveur
HOST = '127.0.0.1'  # Adresse IP locale
PORT = 5555         # Port du serveur

# Gestion des connexions clients
clients = []

def handle_client(client_socket, address):
    print(f"Nouvelle connexion : {address}")
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"Message de {address} : {message}")
                # Envoyer le message à tous les autres clients
                for client in clients:
                    if client != client_socket:
                        client.sendall(message.encode('utf-8'))
            else:
                break
        except ConnectionResetError:
            break
    print(f"Connexion fermée : {address}")
    clients.remove(client_socket)
    client_socket.close()

# Démarrage du serveur
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(2)  # Limité à 2 connexions (Humain et IA)
    print(f"Serveur démarré sur {HOST}:{PORT}")
    while True:
        client_socket, addr = server.accept()
        clients.append(client_socket)
        thread = threading.Thread(target=handle_client, args=(client_socket, addr))
        thread.start()

if __name__ == "__main__":
    start_server()