import cv2
import socket
from ultralytics import YOLO

# ESP32 IP and port (replace with your ESP32's IP address)
ESP32_IP = "your ip address"  # Replace with the IP printed on Serial Monitor
ESP32_PORT = 8080             # Port defined in the ESP32 code

# Data to send to the ESP32
data_to_send = "Bubble\n"

# YOLO model path (replace with the path to your trained model)
model = YOLO("best.pt   ")  # Update with your best.pt path

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

# Initialize the camera (0 for laptop camera)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not access the camera.")
    exit()

print("Starting bubble detection...")
while True:
    ret, frame = cap.read()  # Read a frame
    
    if not ret:
        print("Failed to capture frame. Exiting...")
        break

    # Run YOLO object detection
    results = model(frame)

    # Annotate the frame with detections
    annotated_frame = results[0].plot()  # Draw bounding boxes and labels

    # Check if a bubble is detected with a confidence score > 0.5
    for detection in results[0].boxes:  # Iterate over detections
        if detection.cls == 0 and detection.conf.item() > 0.5:  # cls == 0 for "bubble" class
            print(f"Bubble found with confidence {detection.conf.item():.2f}")
            send_data_to_esp32(ESP32_IP, ESP32_PORT, data_to_send)
            cap.release()
            cv2.destroyAllWindows()
            exit()  # Exit the program after detection

    # Display the annotated frame
    cv2.imshow("Bubble Detection", annotated_frame)

    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()



