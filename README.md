# Telemetry-Collection-and-Aggregation-System
This project implements a distributed telemetry system where multiple clients continuously send system metrics (CPU and memory usage) to a central server using UDP socket programming.

The server collects, processes, and analyzes incoming data to compute:

* Packet loss
* Throughput
* Average system metrics

---

## 🎯 Objectives

* Implement low-level **UDP socket communication**
* Handle **multiple concurrent clients**
* Track **packet sequence and detect loss**
* Perform **data aggregation and performance evaluation**
* Simulate **real-world telemetry systems**

---

## 🧠 System Architecture

```
Multiple Clients  --->  UDP Network  --->  Telemetry Server
       |                                      |
   CPU & Memory Data                  Processing & Analysis
```

---

## ⚙️ Technologies Used

* **Python 3**
* **Socket Programming (UDP)**
* **Multithreading**
* **psutil (system monitoring library)**

---

## 📂 Project Structure

```
TELEMETRY/
│
├── server.py        # Central telemetry server
├── client.py        # Single telemetry client
├── load_test.py     # Multi-client simulation (load testing)
├── stats.py         # Helper functions (optional)
├── README.md        # Project documentation
```

---

## 🚀 Features

### ✅ Core Features

* UDP-based communication
* Multiple client support
* Real-time telemetry transmission
* Sequence number tracking

### 📊 Analytical Features

* Packet loss detection
* Packet loss percentage calculation
* Throughput measurement (packets/sec)
* Average CPU & memory usage

### ⚡ Performance Features

* High-rate packet ingestion
* Load testing using multithreading
* Scalability evaluation

---

## 📦 Telemetry Packet Format

Each client sends data in the following format:

```
client_id,sequence,timestamp,cpu_usage,memory_usage
```

### Example:

```
12,5,17123000,45.5,60.2
```

---

## 🧪 How to Run

### 1️⃣ Install Dependencies

```
pip install psutil
```

---

### 2️⃣ Start the Server

```
python server.py
```

Output:

```
Smart Telemetry Server Started...
```

---

### 3️⃣ Run a Single Client

```
python client.py
```

---

### 4️⃣ Run Load Test (Multiple Clients)

```
python load_test.py
```

Modify number of clients in:

```python
NUM_CLIENTS = 10
```

---

## 📊 Performance Metrics

### 1. Packet Loss

```
Loss = Expected Packets - Received Packets
```

### 2. Packet Loss Percentage

```
Loss % = (Lost / Total Packets) × 100
```

### 3. Throughput

```
Throughput = Packets Received / Time (packets/sec)
```

### 4. Average Metrics

```
Average CPU = Total CPU / Packets
Average Memory = Total Memory / Packets
```

---

## 🔍 Sample Output

```
[DATA] Client 1 | Seq 10 | CPU 45.2% | MEM 60.3%

--- SUMMARY ---
Client 1
Packets Received: 10
Packets Lost: 1
Packet Loss %: 9.09%
Average CPU: 47.12%
Average Memory: 58.33%
Throughput: 95.21 packets/sec
----------------
```

---

## 🧠 Key Concepts Used

* UDP vs TCP communication
* Connectionless data transfer
* Sequence tracking
* Distributed systems simulation
* Multithreading for concurrency

---

## ⚠️ Challenges Faced

* Handling packet loss in UDP
* Managing multiple clients simultaneously
* Maintaining per-client state
* Measuring performance metrics accurately

---

## 🎯 Learning Outcomes

* Deep understanding of **socket programming**
* Practical knowledge of **UDP communication**
* Experience with **real-time data systems**
* Understanding of **network performance metrics**
* Implementation of **distributed architecture**

---

## 🚀 Future Enhancements

* 📊 Real-time dashboard (Streamlit / Web UI)
* 📈 Graph visualization (Matplotlib)
* 🔐 Secure communication (SSL/TLS)
* 🌐 Deployment on multiple machines
* 📡 IoT integration

---


## 📌 Conclusion

This project successfully demonstrates a **real-world telemetry system** capable of handling multiple clients, detecting packet loss, and evaluating performance using UDP communication.

It reflects key principles of **distributed systems, networking, and real-time data processing**.
