from multiprocessing import Process
from streamReceiver import RovCam
import cv2

frontcam = 5500
armcam =5600
sidecam = 5700


def show(source,view):
    cap = RovCam(source)
    while 1:
        cv2.imshow(view,cap.read())


if __name__=='__main__':
    try:
        Process(target = show , args = (frontcam,'front'))
        Process(target = show , args = (armcam,'arm'))
        Process(target = show , args = (sidecam,'side'))

    except Exception as e:
            print(e)
