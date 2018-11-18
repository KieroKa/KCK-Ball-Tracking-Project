import numpy as np
import cv2 as cv
import sys

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        exit("Too less arguments calling script")

    wybierz_film = int(sys.argv[1])

    if wybierz_film == 1:
        cap = cv.VideoCapture('Good_clips/1.mp4')
        r, h, c, w = 380, 50, 650, 50

        if not cap.isOpened():
            print("Could not open video")
            sys.exit()
        '''
        width = cap.get(3)
        height = cap.get(4)
        out = cv.VideoWriter('Result/1.avi', -1, 20.0, (int(width), int(height)))
        '''

    elif wybierz_film == 2:
        cap = cv.VideoCapture('Good_clips/2.mp4')
        r, h, c, w = 430, 50, 630, 50

        if not cap.isOpened():
            print("Could not open video")
            sys.exit()
        '''
        width = cap.get(3)
        height = cap.get(4)
        out = cv.VideoWriter('Result/2.avi', -1, 20.0, (int(width), int(height)))
        '''

    elif wybierz_film == 3:
        cap = cv.VideoCapture('Good_clips/3.mp4')
        r, h, c, w = 450, 50, 550, 50

        if not cap.isOpened():
            print("Could not open video")
            sys.exit()
        '''
        width = cap.get(3)
        height = cap.get(4)
        out = cv.VideoWriter('Result/3.avi', -1, 20.0, (int(width), int(height)))
        '''

    elif wybierz_film == 4:
        cap = cv.VideoCapture('Good_clips/4.mp4')
        ret, frame = cap.read()
        r, h, c, w = 330, 25, 710, 25

        if not cap.isOpened():
            print("Could not open video")
            sys.exit()
        '''
        width = cap.get(3)
        height = cap.get(4)
        out = cv.VideoWriter('Result/4.avi', -1, 20.0, (int(width), int(height)))
        '''

    elif wybierz_film == 5:
        cap = cv.VideoCapture('Good_clips/5.mp4')
        r, h, c, w = 425, 50, 575, 50

        if not cap.isOpened():
            print("Could not open video")
            sys.exit()
        '''
        width = cap.get(3)
        height = cap.get(4)
        out = cv.VideoWriter('Result/5.avi', -1, 20.0, (int(width), int(height)))
        '''

    elif wybierz_film == 6:
        cap = cv.VideoCapture('Bad_clips/6.mp4')
        ret, frame = cap.read()
        r, h, c, w = 480, 50, 525, 50

        if not cap.isOpened():
            print("Could not open video")
            sys.exit()
        '''
        width = cap.get(3)
        height = cap.get(4)
        out = cv.VideoWriter('Result/6.avi', -1, 20.0, (int(width), int(height)))
        '''

    elif wybierz_film == 7:
        cap = cv.VideoCapture('Bad_clips/7.mp4')
        ret, frame = cap.read()
        r, h, c, w = 500, 50, 750, 50

        if not cap.isOpened():
            print("Could not open video")
            sys.exit()
        '''
        width = cap.get(3)
        height = cap.get(4)
        out = cv.VideoWriter('Result/7.avi', -1, 20.0, (int(width), int(height)))
        '''

    elif wybierz_film == 8:
        cap = cv.VideoCapture('Bad_clips/8.mp4')
        ret, frame = cap.read()
        r, h, c, w = 300, 50, 665, 50

        if not cap.isOpened():
            print("Could not open video")
            sys.exit()
        '''
        width = cap.get(3)
        height = cap.get(4)
        out = cv.VideoWriter('Result/8.avi', -1, 20.0, (int(width), int(height)))
        '''

    else:
        print("You didn't choose right clip")
        sys.exit()

    track_window = (c, r, w, h)
    ret, frame = cap.read()

    roi = frame[r:r + h, c:c + w]
    hsv_roi = cv.cvtColor(roi, cv.COLOR_BGR2HSV)

    mask = cv.inRange(hsv_roi, np.array((43, 0, 0)), np.array((63, 110, 255)))

    term_crit = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 5, 1)

    while 1:

        ret, frame = cap.read()
        if ret:

            hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

            lower_blue = np.array([43, 0, 210])
            upper_blue = np.array([63, 110, 255])
            mask = cv.inRange(hsv, lower_blue, upper_blue)

            ret, track_window = cv.meanShift(mask, track_window, term_crit)

            x, y, w, h = track_window
            result = cv.rectangle(frame, (x, y), (x + w, y + h), 255, 2)

            cv.imshow('Wynik', result)
            '''
            out.write(result)
            '''
            k = cv.waitKey(60) & 0xff
            if k == 27:
                break
        else:
            print("Could not read video or video has ended")
            break
    cv.destroyAllWindows()
    cap.release()
    '''
    out.release()
    '''
