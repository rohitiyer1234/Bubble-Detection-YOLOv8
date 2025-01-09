from ultralytics import YOLO
import cv2

# Load the YOLOv8 model pre-trained on COCO dataset
model = YOLO("yolov8n.pt")  # yolov8n.pt is trained on the COCO dataset

# Open the default camera
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Cannot access the camera.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Cannot read frame.")
        break

    # Run YOLOv8 object detection
    results = model.predict(frame, conf=0.5)  # Adjust confidence threshold as needed

    # Extract detections
    for result in results[0].boxes:
        x1, y1, x2, y2 = map(int, result.xyxy[0])  # Bounding box coordinates
        confidence = result.conf[0]  # Confidence score
        class_id = int(result.cls[0])  # Class ID
        label = f"{model.names[class_id]}: {confidence:.2f}"  # Label with confidence

        # Draw the bounding box and label
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Display the frame with detections
    cv2.imshow("YOLOv8 COCO Detection", frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
