import socket
import time
import random
import psutil  

SERVER_IP = "192.168.1.10"   
SERVER_PORT = 5000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_id = random.randint(1, 100)
sequence = 0

print(f"Telemetry Client {client_id} started...\n")

while True:

    sequence += 1

    # REAL system data
    cpu_usage = psutil.cpu_percent(interval=None)                # Since our system is designed for high-rate telemetry over UDP, we avoided blocking calls like interval=1. Using interval=None allows continuous, non-blocking data transmission, which better reflects real-world telemetry systems where timeliness is prioritized over perfect accuracy.
    memory_usage = psutil.virtual_memory().percent

    # timestamp
    timestamp = time.time()

    message = f"{client_id},{sequence},{timestamp},{cpu_usage},{memory_usage}"

    data = message.encode()
    client_socket.sendto(data, (SERVER_IP, SERVER_PORT))

    print("Sent:", message)


    time.sleep(0.1)
