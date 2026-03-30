import socket
import time
import threading
import psutil
import random

SERVER_IP = "127.0.0.1"
SERVER_PORT = 5000

def run_client(client_id):

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sequence = 0

    while True:
        sequence += 1

        if random.random() < 0.1:
            continue                                                        #simulate packet loss

        cpu = psutil.cpu_percent(interval=None)
        memory = psutil.virtual_memory().percent
        timestamp = time.time()

        message = f"{client_id},{sequence},{timestamp},{cpu},{memory}"
        client_socket.sendto(message.encode(), (SERVER_IP, SERVER_PORT))

        time.sleep(0.1)

NUM_CLIENTS = 10  # change to 20, 50 for testing

threads = []

for i in range(NUM_CLIENTS):
    t = threading.Thread(target=run_client, args=(i+1,))
    t.start()
    threads.append(t)

print(f"{NUM_CLIENTS} clients started...\n")