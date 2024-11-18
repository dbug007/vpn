import socket
import ssl

def start_vpn_server(host='0.0.0.0', port=12345, certfile='cert.pem', keyfile='key.pem'):
    # Create a socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"VPN Server listening on {host}:{port}")
    
    # Wrap the socket with SSL
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile=certfile, keyfile=keyfile)
    secure_socket = context.wrap_socket(server_socket, server_side=True)
    
    while True:
        client_socket, addr = secure_socket.accept()
        print(f"Connection from {addr}")
        try:
            data = client_socket.recv(1024)
            print(f"Received: {data.decode('utf-8')}")
            client_socket.send(b"Secure connection established!")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            client_socket.close()

# Generate certificates using OpenSSL before running this server.
if __name__ == "__main__":
    start_vpn_server()