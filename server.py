# parse incoming data
# track sequence numbers per client
# detect packet loss
# store statistics
# compute basic aggregation
# Each telemetry packet includes a sequence number. The server tracks the last received sequence per client. If the incoming sequence is greater than expected, the difference indicates the number of lost packets.


import socket
import time

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# FIX: avoid port reuse error
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind(("127.0.0.1", 5000))

print("Smart Telemetry Server Started...\n")

clients = {}

while True:
    data, addr = server_socket.recvfrom(1024)
    message = data.decode()

    try:
        client_id, sequence, timestamp, cpu, memory = message.split(",")

        client_id = int(client_id)
        sequence = int(sequence)
        cpu = float(cpu)
        memory = float(memory)

        current_time = time.time()

        if client_id not in clients:
            clients[client_id] = {
                "last_seq": sequence,
                "received": 0,
                "lost": 0,
                "cpu_sum": 0,
                "mem_sum": 0,
                "start_time": current_time
            }

        client = clients[client_id]

        # Packet loss detection
        expected = client["last_seq"] + 1
        if sequence > expected:
            lost_packets = sequence - expected
            client["lost"] += lost_packets
            print(f"[LOSS] Client {client_id} lost {lost_packets} packets")

        # Update stats
        client["last_seq"] = sequence
        client["received"] += 1
        client["cpu_sum"] += cpu
        client["mem_sum"] += memory

        print(f"[DATA] Client {client_id} | Seq {sequence} | CPU {cpu:.2f}% | MEM {memory:.2f}%")

        # Summary
        if client["received"] % 50 == 0:

            total = client["received"] + client["lost"]
            loss_percent = (client["lost"] / total) * 100 if total > 0 else 0

            avg_cpu = client["cpu_sum"] / client["received"]
            avg_mem = client["mem_sum"] / client["received"]

            elapsed = current_time - client["start_time"]
            throughput = client["received"] / elapsed if elapsed > 0 else 0

            print("\n--- SUMMARY ---")
            print(f"Client {client_id}")
            print(f"Packets Received: {client['received']}")
            print(f"Packets Lost: {client['lost']}")
            print(f"Packet Loss %: {loss_percent:.2f}%")
            print(f"Average CPU: {avg_cpu:.2f}%")
            print(f"Average Memory: {avg_mem:.2f}%")
            print(f"Throughput: {throughput:.2f} packets/sec")
            print("----------------\n")

    except Exception as e:
        print("Error:", e)