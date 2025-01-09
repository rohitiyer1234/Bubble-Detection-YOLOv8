import socket

# ESP32 IP and port (replace with your ESP32's IP address)
ESP32_IP = "192.168.224.185"  # Replace with the IP printed on Serial Monitor
ESP32_PORT = 8080         # Port defined in the ESP32 code

# Data to send to the ESP32
data_to_send = "Bubble\n"

def send_data_to_esp32(ip, port, data):
    try:
        # Create a socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Connect to the ESP32 server
        client_socket.connect((ip, port))
        print(f"Connected to ESP32 at {ip}:{port}")
        
        # Send data
        client_socket.sendall(data.encode())
        print(f"Data sent: {data}")
        
        # Close the connection
        client_socket.close()
        print("Connection closed.")
    except Exception as e:
        print(f"Error: {e}")

# Call the function to send data
send_data_to_esp32(ESP32_IP, ESP32_PORT, data_to_send)
