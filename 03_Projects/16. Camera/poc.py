# poc = proof of concept
# computer vision - cv

import cv2

cap = cv2.VideoCapture(0) # 0 --> 1st camera

while True:
    _, frame = cap.read()

    cv2.imshow("Nayeem's Camera", frame)

    if cv2.waitKey(10) == ord('q'): # 10 miliseconds time gap 
        break

cap.release()
cv2.destroyAllWindows()