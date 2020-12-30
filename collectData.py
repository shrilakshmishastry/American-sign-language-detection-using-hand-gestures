import cv2
import numpy as np
import os

# create the directory
if not os.path.exists("data"):
    os.mkdir("data")
    os.mkdir("data/test")
    os.mkdir("data/train")
    os.mkdir("data/train/n")
    os.mkdir("data/train/o")
    os.mkdir("data/train/p")
    os.mkdir("data/train/q")
    os.mkdir("data/train/r")
    os.mkdir("data/train/s")
    os.mkdir("data/test/n")
    os.mkdir("data/test/o")
    os.mkdir("data/test/p")
    os.mkdir("data/test/q")
    os.mkdir("data/test/r")
    os.mkdir("data/test/s")

# set the mode
mode = "train"
directory = "data/" + mode + "/"

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    count = {
        'n': len(os.listdir(directory + "/n")),
        'o': len(os.listdir(directory + "/o")),
        'p': len(os.listdir(directory + "/p")),
        'q': len(os.listdir(directory + "/q")),
        'r': len(os.listdir(directory + "/r")),
        's': len(os.listdir(directory + "/s"))
    }
    # printing the count of each char image
    cv2.putText(frame, "MODE :" + mode, (10, 50), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "IMAGE COUNT", (10, 100), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "N :"+str(count['n']), (10, 120), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "O :"+str(count['o']), (10, 140), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "P :"+str(count['p']), (10, 160), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "Q :"+str(count['q']), (10, 180), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "R :"+str(count['r']), (10, 200), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "S :"+str(count['s']), (10, 220), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)

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

    if key & 0xff == ord('n'):
        cv2.imwrite(directory + 'n/' + str(count['n']) + '.jpg', roi)

    if key & 0xff == ord('o'):
        cv2.imwrite(directory + 'o/' + str(count['o']) + '.jpg', roi)

    if key & 0xff == ord('p'):
        cv2.imwrite(directory + 'p/' + str(count['p']) + '.jpg', roi)

    if key & 0xff == ord('q'):
        cv2.imwrite(directory + 'q/' + str(count['q']) + '.jpg', roi)

    if key & 0xff == ord('r'):
        cv2.imwrite(directory + 'r/' + str(count['r']) + '.jpg', roi)

    if key & 0xff == ord('s'):
        cv2.imwrite(directory + 's/' + str(count['s']) + '.jpg', roi)

# print(frame.shape)
cap.release()
cv2.destroyAllWindows()
