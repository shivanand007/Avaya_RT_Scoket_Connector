import socket
import threading


def start_listener(port):
    # Start listener on the specified port
    try:
        listener_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener_socket.bind(('localhost', port))
        listener_socket.listen(1)
        print(f"Listener is running on port {port}")

        while True:
            # Accept incoming connections
            client_socket, client_address = listener_socket.accept()
            print(f"Received connection from {client_address}")

            # Start a new thread to handle the client
            client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
            client_thread.start()
    except Exception as e:
        print(f"Error starting listener on port {port}: {e}")
    finally:
        # Close the listener socket (won't be reached in this example as the listener is designed to run indefinitely)
        listener_socket.close()


def handle_client(client_socket, client_address):
    # Handle client connection
    try:
        # Receive and process client data
        data = client_socket.recv(1024)
        # Process data as needed
        print(f"Received data from {client_address}: {data.decode()}")

        # Send a response back to the client
        response = "Hello from the server!"
        client_socket.send(response.encode())
    except Exception as e:
        print(f"Error handling client connection: {e}")
    finally:
        # Close the client socket
        client_socket.close()

