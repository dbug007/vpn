import socket
import ssl

cafile = "server.crt"

def start_vpn_client(server_host='127.0.0.1', server_port=12345, cafile=cafile):
    # Create a socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Wrap the socket with SSL
    context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    context.load_verify_locations(cafile=cafile)
    
    # Disable certificate verification for self-signed certificates
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE
    
    secure_socket = context.wrap_socket(client_socket, server_hostname=server_host)
    
    try:
        secure_socket.connect((server_host, server_port))
        secure_socket.send(b"Hello from the client!")
        data = secure_socket.recv(1024)
        print(f"Server says: {data.decode('utf-8')}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        secure_socket.close()

if __name__ == "__main__":
    start_vpn_client()
