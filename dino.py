import cv2          
from cvzone.HandTrackingModule import HandDetector
from pynput.keyboard import Key, Controller

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1, detectionCon=0.8)
keyboard = Controller()

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)

    if hands:
        hand = hands[0]
        fingers = detector.fingersUp(hand)

        if fingers[1] == 1:
            keyboard.press(Key.up)
            keyboard.release(Key.up)
        if fingers[0]==1:
            keyboard.press(Key.down)
            keyboard.release(Key.down)

            cv2.putText(img, "Index Finger opened - dinosaur UP", (10, 110), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        else:
            pass


    cv2.imshow("Hand Tracking", img)

    if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
        break

cap.release()
cv2.destroyAllWindows()
