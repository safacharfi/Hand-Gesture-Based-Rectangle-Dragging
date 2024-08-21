import cv2
from cvzone.HandTrackingModule import HandDetector

# Initialize the camera
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

class DragRec:
    def __init__(self, posCenter, size=[200, 200]):
        self.posCenter = tuple(posCenter)
        self.size = size
        self.colorR = (255, 0, 255)

    def update(self, cursor):
        cursor = tuple(cursor[:2])
        cx, cy = self.posCenter
        w, h = self.size
        # Check if the index finger is in the box
        if cx - w // 2 < cursor[0] < cx + w // 2 and cy - h // 2 < cursor[1] < cy + h // 2:
            self.colorR = (0, 255, 0)  # Change color if inside the rectangle
            self.posCenter = cursor  # Update the position of the rectangle
        else:
            self.colorR = (255, 0, 255)

rectList = [DragRec([x * 250 + 150, 150]) for x in range(5)]

detector = HandDetector(detectionCon=0.8)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    if not success:
        break

    hands, img = detector.findHands(img)  # 'hands' contains the list of detected hands

    # If hands are detected, find landmarks
    if hands:
        # lmList contains landmark points for the first hand detected
        lmList = hands[0]['lmList']  # 'lmList' contains the list of 21 hand landmarks

        # Check the distance between the index finger (8) and middle finger (12)
        length, info, img = detector.findDistance(lmList[8][0:2], lmList[12][0:2], img, color=(255, 0, 255), scale=10)
        print("Distance between fingers:", length)

        # If the distance is less than 50, check for dragging
        if length < 50:
            cursor = lmList[8]
            print("Cursor position:", cursor)
            for rect in rectList:
                rect.update(cursor)
        else:
            for rect in rectList:
                rect.colorR = (255, 0, 255)

    for rect in rectList:
        cx, cy = rect.posCenter
        w, h = rect.size
        cv2.rectangle(img, (cx - w // 2, cy - h // 2), (cx + w // 2, cy + h // 2), rect.colorR, cv2.FILLED)

    cv2.imshow("Image", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
