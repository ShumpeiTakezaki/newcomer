from cProfile import label
import os
import tarfile 
import cv2

pwd = os.getcwd()

def load_image(info):
    if "png" in info.name:
        print(info.name)
        info.name
        file = tar.extractfile(info)
        with open("check.png", "wb") as c:
            c.write(file.read()) 
    else:
        pass

def a(file_name):
    with tarfile.open(pwd+file_name, mode='r') as tar:
        for info in tar.getmembers():
            if "png" in info.name:
                print(info.name)
                file = tar.extractfile(info)
                with open("img_"+ {info.name[-5:]}, "wb") as c:
                    c.write(file.read()) 

def save_image():
    with tarfile.open(name=f'{pwd}/Dataset/{}.tar.gz', mode='r') as tar:
        for info in tar.getmembers():
            


def unpack_image():

with tarfile.open(name="Dataset/test.tar.gz", mode='r') as tar:
    for info in tar.getmembers():
        if "png" in info.name:
            print(info.name)
            file = tar.extractfile(info)
            with open("check.png", "wb") as c:
                c.write(file.read())
            break

if __name__ == "__main__":
    unpack_image()