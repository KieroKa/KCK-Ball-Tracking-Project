import numpy as np
import cv2 as cv
import sys

if __name__ == '__main__':

    # Checking if there is given argument for clip
    if len(sys.argv) <= 1:
        exit("Too less arguments calling script")

    # Saving giving argument and changing its type to int
    choose_clip = int(sys.argv[1])

    # Opening right clip depending on given argument,
    # setting window for tracking,
    # commented lines are for saving clip with window (works really slow to save)
    if choose_clip == 1:
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

    elif choose_clip == 2:
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

    elif choose_clip == 3:
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

    elif choose_clip == 4:
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

    elif choose_clip == 5:
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

    elif choose_clip == 6:
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

    elif choose_clip == 7:
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

    elif choose_clip == 8:
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

    # Saving frame of the window
    ret, frame = cap.read()

    # Setting up the window of tracking on frame
    roi = frame[r:r + h, c:c + w]

    # Changing colors from gbr to hsv
    hsv_roi = cv.cvtColor(roi, cv.COLOR_BGR2HSV)

    # Using mask to leave only ball on frame
    mask = cv.inRange(hsv_roi, np.array((43, 0, 0)), np.array((63, 110, 255)))

    # Setting up criteria
    term_crit = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 5, 1)

    while 1:

        # Loading next frame
        ret, frame = cap.read()

        # If clip hasn't ended
        if ret:

            # Changing colors from gbr to hsv
            hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

            # Using mask to leave only ball on frame
            lower_blue = np.array([43, 0, 210])
            upper_blue = np.array([63, 110, 255])
            mask = cv.inRange(hsv, lower_blue, upper_blue)

            # Using meanshift using mask, window and criteria
            ret, track_window = cv.meanShift(mask, track_window, term_crit)

            # Drawing new window on current frame
            x, y, w, h = track_window
            result = cv.rectangle(frame, (x, y), (x + w, y + h), 255, 2)

            # Showing result
            cv.imshow('Wynik', result)

            # Saving result
            '''
            out.write(result)
            '''
            k = cv.waitKey(60) & 0xff
            if k == 27:
                break
        else:
            print("Could not read video or video has ended")
            break

    # Closing windows and release clips
    cv.destroyAllWindows()
    cap.release()
    '''
    out.release()
    '''
