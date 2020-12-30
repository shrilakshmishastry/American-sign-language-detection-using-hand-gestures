import cv2
import numpy as np
import os

# Create the directory structure
if not os.path.exists("data"):
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

# Train or test
mode = 'train'
directory = 'data/' + mode + '/'

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    # Simulating mirror image
    frame = cv2.flip(frame, 1)

    # Getting count of existing images
    count = {'t': len(os.listdir(directory + "/t")),
             'u': len(os.listdir(directory + "/u")),
             'v': len(os.listdir(directory + "/v")),
             'w': len(os.listdir(directory + "/w")),
             'x': len(os.listdir(directory + "/x")),
             'y': len(os.listdir(directory + "/y")),
             'z': len(os.listdir(directory + "/z"))}


    # Printing the count in each set to the screen
    cv2.putText(frame, "MODE : " + mode, (10, 50), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "IMAGE COUNT", (10, 100), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "T : " + str(count['t']), (10, 120), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "U : " + str(count['u']), (10, 140), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "V : " + str(count['v']), (10, 160), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "W : " + str(count['w']), (10, 180), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "X : " + str(count['x']), (10, 200), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "Y : " + str(count['y']), (10, 220), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "Z : " + str(count['z']), (10, 240), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)

    # Coordinates of the ROI
    x1 = int(0.5 * frame.shape[1])
    y1 = 10
    x2 = frame.shape[1] - 10
    y2 = int(0.5 * frame.shape[1])
    # Drawing the ROI
    # The increment/decrement by 1 is to compensate for the bounding box
    cv2.rectangle(frame, (x1 - 1, y1 - 1), (x2 + 1, y2 + 1), (255, 0, 0), 1)
    # Extracting the ROI
    roi = frame[y1:y2, x1:x2]
    roi = cv2.resize(roi, (64, 64))

    cv2.imshow("Frame", frame)

    # _, mask = cv2.threshold(mask, 200, 255, cv2.THRESH_BINARY)
    # kernel = np.ones((1, 1), np.uint8)
    # img = cv2.dilate(mask, kernel, iterations=1)
    # img = cv2.erode(mask, kernel, iterations=1)
    # do the processing after capturing the image!
    roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    _, roi = cv2.threshold(roi, 120, 255, cv2.THRESH_BINARY)
    cv2.imshow("ROI", roi)

    interrupt = cv2.waitKey(10)
    if interrupt & 0xFF == 27:  # esc key
        break
    if interrupt & 0xFF == ord('t'):
        cv2.imwrite(directory + 't/' + str(count['t']) + '.jpg', roi)
    if interrupt & 0xFF == ord('u'):
        cv2.imwrite(directory + 'u/' + str(count['u']) + '.jpg', roi)
    if interrupt & 0xFF == ord('v'):
        cv2.imwrite(directory + 'v/' + str(count['v']) + '.jpg', roi)
    if interrupt & 0xFF == ord('w'):
        cv2.imwrite(directory + 'w/' + str(count['w']) + '.jpg', roi)
    if interrupt & 0xFF == ord('x'):
        cv2.imwrite(directory + 'x/' + str(count['x']) + '.jpg', roi)
    if interrupt & 0xFF == ord('y'):
        cv2.imwrite(directory + 'y/' + str(count['y']) + '.jpg', roi)
    if interrupt & 0xFF == ord('z'):
            cv2.imwrite(directory + 'z/' + str(count['z']) + '.jpg', roi)

cap.release()
cv2.destroyAllWindows()
