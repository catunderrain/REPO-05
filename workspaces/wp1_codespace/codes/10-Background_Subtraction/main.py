import cv2
cap = cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorMOG2()

while(1):
    ret, frame = cap.read()
    fgmask = cap.read()
    fgmask = fgbg.apply(frame)

    cv2.imshow('fgmask', cv2.flip(fgmask, 1))
    cv2.imshow('frame', cv2.flip(frame, 1))

    key = cv2.waitKey(1)
    if key == 27:
        break