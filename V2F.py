import sys
import argparse
import cv2
import average as Average


def extractImages(pathIn, pathOut):
    count = 0
    vidcap = cv2.VideoCapture(pathIn)
    success,image = vidcap.read()
    success = True
    while success:
        vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*500))    
        success,image = vidcap.read()
        print ('Read a new frame: ', success)
        if success:
            cv2.imwrite( pathOut + "slika%d.jpg" % count, image)    
            count = count + 1
        else:
            break;
   

if __name__=="__main__":
    a = argparse.ArgumentParser()
    a.add_argument("--pathIn", help="path to video")
    a.add_argument("--pathOut", help="path to images")
    args = a.parse_args()
    print(args)
    extractImages(args.pathIn, args.pathOut)
