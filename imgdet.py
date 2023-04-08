import cv2
import matplotlib.pyplot as plt
import cvlib as cv
import urllib.request
import numpy as np
from cvlib.object_detection import draw_bbox
import concurrent.futures
import pandas as pd
from datetime import date
import time

url='Enter the url from the code in ESP32-Loader for high resolution image'
im=None
def run1():
    cv2.namedWindow("live transmission", cv2.WINDOW_AUTOSIZE)
    while True:
        img_resp=urllib.request.urlopen(url)
        imgnp=np.array(bytearray(img_resp.read()),dtype=np.uint8)
        im = cv2.imdecode(imgnp,-1)
        cv2.imshow('live transmission',im)
        key=cv2.waitKey(5)
        if key==ord('q'):
            break 
    cv2.destroyAllWindows()        
def run2():
    cv2.namedWindow("detection", cv2.WINDOW_AUTOSIZE)
    while True:
        img_resp=urllib.request.urlopen(url)
        imgnp=np.array(bytearray(img_resp.read()),dtype=np.uint8)
        im = cv2.imdecode(imgnp,-1)
 
        bbox, label, conf = cv.detect_common_objects(im,confidence=0.25, model='yolov4-tiny')
        im = draw_bbox(im, bbox, label, conf)
        cv2.imshow('detection',im)
        if 'person' in str(label):
            p = 0
            for lb in label:
                if str(lb) == 'person':
                    p = p + 1
            df = pd.read_csv('data.csv')
            ldf = pd.DataFrame([[p,date.today()]],columns=['people','date'])
            df = pd.concat([df,ldf],axis=0)
            df.to_csv('data.csv',index=False)
            print(df)
            time.sleep(1)
        key=cv2.waitKey(5)
        if key==ord('q'):
            break   
    cv2.destroyAllWindows() 
if __name__ == '__main__':
    print("started")
    with concurrent.futures.ProcessPoolExecutor() as executer:
            f1= executer.submit(run1)
            f2= executer.submit(run2)
