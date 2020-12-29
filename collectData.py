import cv2
import numpy as np
import os

# create the directory
if not os.path.exists("data"):
    os.mkdir("data")
    os.mkdir("data/test")
    os.mkdir("data/train")
    os.mkdir("data/train/a")
    os.mkdir("data/train/b")
    os.mkdir("data/train/c")
    os.mkdir("data/train/d")
    os.mkdir("data/train/e")
    os.mkdir("data/train/f")
    os.mkdir("data/test/a")
    os.mkdir("data/test/b")
    os.mkdir("data/test/c")
    os.mkdir("data/test/d")
    os.mkdir("data/test/e")
    os.mkdir("data/test/f")

# set the mode
mode = "test"
directory = "data/" + mode + "/"

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    count = {
        'a': len(os.listdir(directory + "/a")),
        'b': len(os.listdir(directory + "/b")),
        'c': len(os.listdir(directory + "/c")),
        'd': len(os.listdir(directory + "/d")),
        'e': len(os.listdir(directory + "/e")),
        'f': len(os.listdir(directory + "/f"))
    }
    # printing the count of each char image
    cv2.putText(frame, "MODE :" + mode, (10, 50), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "IMAGE COUNT", (10, 100), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "A :", (10, 120), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "B :", (10, 140), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "C :", (10, 160), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "D :", (10, 180), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "E :", (10, 200), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "F :", (10, 220), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)

    # coordinates of roi
    x1 = int(0.5 * frame.shape[1])
    y1 = 10
    x2 = frame.shape[1] - 10
    y2 = int(0.5 * frame.shape[1])

    # drawing the ori
    cv2.rectangle(frame, (x1 - 1, y1 - 1), (x2 + 1, y2 + 1), (255, 0, 0), 1)

    # extracting the image from roi
    roi = frame[y1:y2, x1:x2]
    roi = cv2.resize(roi, (64, 64))

    # print(count['a'])
    cv2.imshow('Frame', frame)
    roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    _, roi = cv2.threshold(roi, 120, 255, cv2.THRESH_BINARY)
    cv2.imshow("ROI", roi)

    key = cv2.waitKey(30)
    # esc key to exit
    if key & 0xff == 27:
        break

    if key & 0xff == ord('a'):
        cv2.imwrite(directory + 'a/' + str(count['a']) + '.jpg', roi)

    if key & 0xff == ord('b'):
        cv2.imwrite(directory + 'b/' + str(count['b']) + '.jpg', roi)

    if key & 0xff == ord('c'):
        cv2.imwrite(directory + 'c/' + str(count['c']) + '.jpg', roi)

    if key & 0xff == ord('d'):
        cv2.imwrite(directory + 'd/' + str(count['d']) + '.jpg', roi)

    if key & 0xff == ord('e'):
        cv2.imwrite(directory + 'e/' + str(count['e']) + '.jpg', roi)

    if key & 0xff == ord('f'):
        cv2.imwrite(directory + 'f/' + str(count['f']) + '.jpg', roi)

# print(frame.shape)
cap.release()
cv2.destroyAllWindows()
