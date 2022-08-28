import cv2
import random

def read_img():
    img = cv2.imread('batman.jpg')
    return img;

def status():
    status = [str(random.randint(0,10)),str(random.randint(10,20)),str(random.randint(20,30))]
    return status;

