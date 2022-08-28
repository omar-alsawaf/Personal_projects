import os
import requests
url = 'http://httpbin.org/post'
def post(path1,path2):
    def file():
        with open(f"{path1}", "r+") as file1:
            # Reading form a file
            status=file1.read()
            print(status)
            return status

    with open(f'{path2}', 'rb') as img:
        name_img= os.path.basename('oma/A.jpg')
        files= {'image': (name_img,img,'multipart/form-data',{'Expires': '0'}),"info":file() }
        with requests.Session() as s:
            r = s.post(url,files=files)
            print(r.status_code)
            print(r.text)

post("data\status.txt",'oma/A.jpg')