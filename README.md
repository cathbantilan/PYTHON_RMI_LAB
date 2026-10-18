# Python RMI Distributed System (Pyro5)

This repository contains a Python implementation of a Java Remote Method Invocation (RMI) architecture translated using **Pyro5 (Python Remote Objects)**.

## Project Structure

- `product.py`: Exposes the `Product` remote object class and attributes.
- `server.py`: Creates product instances, registers them with the Pyro Name Server, and runs the daemon loop.
- `client.py`: Looks up registered objects from the Name Server and calls remote methods.

## Prerequisites

- Python 3.8+
- Pyro5 (`pip install Pyro5`)

## How to Run

1. **Start the Pyro Name Server** (acts as the RMI Registry):
   ```bash
   python -m Pyro5.nameserver -n 127.0.0.1 -p 9090
   ```
2. **Start the RMI Server (Terminal 2)**
   ```bash
   python server.py
 Expected Output:
 Server is booting and products are registered in Name Server...
   ```
3. **Run the RMI Client (Terminal 3)**
   ```bash
  python client.py
Expected Output:
Name: Laptop
Description: Lenovo laptop
Price: 800000.0
   ```
