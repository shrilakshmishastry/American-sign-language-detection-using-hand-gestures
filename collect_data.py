import cv2
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
    os.makedirs("data")
    os.makedirs("data/train")
    os.makedirs("data/test")
    os.makedirs("data/train/t")
    os.makedirs("data/train/u")
    os.makedirs("data/train/v")
    os.makedirs("data/train/w")
    os.makedirs("data/train/x")
    os.makedirs("data/train/y")
    os.makedirs("data/train/z")
    os.makedirs("data/test/t")
    os.makedirs("data/test/u")
    os.makedirs("data/test/v")
    os.makedirs("data/test/w")
    os.makedirs("data/test/x")
    os.makedirs("data/test/y")
    os.makedirs("data/test/z")

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
        'f': len(os.listdir(directory + "/f")),
        't': len(os.listdir(directory + "/t")),
        'u': len(os.listdir(directory + "/u")),
        'v': len(os.listdir(directory + "/v")),
        'w': len(os.listdir(directory + "/w")),
        'x': len(os.listdir(directory + "/x")),
        'y': len(os.listdir(directory + "/y")),
        'z': len(os.listdir(directory + "/z"))
    }
    # printing the count of each char image
    cv2.putText(frame, "MODE :" + mode, (10, 50), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "IMAGE COUNT", (10, 100), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "A :" + str(count['a']), (10, 120), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "B :" + str(count['b']), (10, 140), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "C :" + str(count['c']), (10, 160), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "D :" + str(count['d']), (10, 180), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "E :" + str(count['e']), (10, 200), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "F :" + str(count['f']), (10, 220), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "T : " + str(count['t']), (10, 120), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "U : " + str(count['u']), (10, 140), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "V : " + str(count['v']), (10, 160), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "W : " + str(count['w']), (10, 180), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "X : " + str(count['x']), (10, 200), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "Y : " + str(count['y']), (10, 220), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "Z : " + str(count['z']), (10, 240), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)

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

    if key & 0xFF == ord('t'):
        cv2.imwrite(directory + 't/' + str(count['t']) + '.jpg', roi)

    if key & 0xFF == ord('u'):
        cv2.imwrite(directory + 'u/' + str(count['u']) + '.jpg', roi)

    if key & 0xFF == ord('v'):
        cv2.imwrite(directory + 'v/' + str(count['v']) + '.jpg', roi)

    if key & 0xFF == ord('w'):
        cv2.imwrite(directory + 'w/' + str(count['w']) + '.jpg', roi)

    if key & 0xFF == ord('x'):
        cv2.imwrite(directory + 'x/' + str(count['x']) + '.jpg', roi)

    if key & 0xFF == ord('y'):
        cv2.imwrite(directory + 'y/' + str(count['y']) + '.jpg', roi)

    if key & 0xFF == ord('z'):
        cv2.imwrite(directory + 'z/' + str(count['z']) + '.jpg', roi)

    # print(frame.shape)
cap.release()
cv2.destroyAllWindows()
