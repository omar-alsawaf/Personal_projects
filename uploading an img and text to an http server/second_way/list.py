import requests
from status import status
from status import read_img
import cv2

status_=status()
info = {
    "lat" :str(status_[0]),
    "long" :str(status_[1]),
    "mission" :str(status_[2])
}
url = 'http://httpbin.org/post'
img_encode = cv2.imencode('.jpg',read_img())
files= {'image': str(img_encode)}
r=requests.post(url=url ,files=files,data=info)
print(r.status_code)
print(r.text)