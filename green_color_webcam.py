import cv2
import numpy as np

cap = cv2.VideoCapture(0)

print("🎥 Webcam started")
print("🟢 Show a green object to the camera")
print("❌ Press 'q' to exit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define green color range in HSV
    lower_green = np.array([40, 40, 40])
    upper_green = np.array([80, 255, 255])

    # Create mask for green color
    mask = cv2.inRange(hsv, lower_green, upper_green)

    # Apply mask
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Display windows
    cv2.imshow("Original Frame", frame)
    cv2.imshow("Green Mask", mask)
    cv2.imshow("Green Detection", result)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
