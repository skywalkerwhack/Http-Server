import socket
import threading
from log import log_message
from response import (
    RESPONSES,
    NOT_FOUND_RESPONSE,
    FORBIDDEN_RESPONSE,
    BAD_REQUEST_RESPONSE,
    METHOD_NOT_ALLOWED_RESPONSE,
)

# Define the server host and port
HOST = "127.0.0.1"
PORT = 1212


# Function to handle client requests
def handle_client(connection, address):
    log_message("info", f"Connection established with {address}")
    try:
        request = connection.recv(1024).decode("utf-8")
        log_message("info", f"Received request:\n{request}")

        # Basic request validation
        lines = request.splitlines()
        if len(lines) == 0 or len(lines[0].split(" ")) < 2:
            connection.sendall(BAD_REQUEST_RESPONSE)
            return

        # Extract the method and path from the request
        first_line = lines[0]
        parts = first_line.split(" ")
        if len(parts) >= 2:
            method = parts[0]
            path = parts[1]
            log_message("info", f"Requested method: {method}, path: {path}")

            # Check if the path is forbidden
            if path == "/forbidden":
                response = FORBIDDEN_RESPONSE
            else:
                # Check if the method is allowed for the path
                if method in RESPONSES and path in RESPONSES[method]:
                    response = RESPONSES[method][path]
                elif path in {
                    path for methods in RESPONSES.values() for path in methods
                }:
                    response = METHOD_NOT_ALLOWED_RESPONSE
                else:
                    response = NOT_FOUND_RESPONSE

            connection.sendall(response)
            log_message("info", f"Response sent to {address}")
        else:
            connection.sendall(BAD_REQUEST_RESPONSE)
            log_message("error", "Bad request: unable to parse method and path")
    except Exception as e:
        log_message("error", f"Error handling request from {address}: {e}")
        connection.sendall(BAD_REQUEST_RESPONSE)
    finally:
        connection.close()
        log_message("info", f"Connection closed with {address}")


# Main function to set up the server
def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)  # Listen for up to 5 connections

    log_message("info", f"Server is listening on {HOST}:{PORT}")

    while True:
        try:
            client_connection, client_address = server_socket.accept()
            client_thread = threading.Thread(
                target=handle_client, args=(client_connection, client_address)
            )
            client_thread.start()
        except KeyboardInterrupt:
            log_message("info", "Shutting down the server.")
            server_socket.close()
            break


if __name__ == "__main__":
    run_server()
    print()
