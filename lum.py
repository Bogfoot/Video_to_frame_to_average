import cv2
import numpy as np
import argparse
from PIL import Image
from matplotlib import pyplot as plt
import csv
import pandas as pd

def lum(In, Out):
    im = cv2.imread(In)
    dio = im[240:241,100:500]
    #print("Shape: ", im.shape, "Size: ", im.size)   
    #cv2.imshow('Dio slike', dio)  
    #cv2.imshow('Cila slika', im)
    #cv2.waitKey(0)
    cv2.imwrite('Dio_slike.jpg', dio)
    #cv2.destroyAllWindows() 
    im2 = Image.open('Dio_slike.jpg', 'r')
    width, height = im2.size
    #print("širina:", width, "Visina: ", height)   
    im2_pix = list(im2.getdata())
    
    #treba dobiti vrijednosti rgba i odrediti intenzitet. Pretpostavljam da je ukupni intenzitet iznos sqrt(r**2+g**2+b**2). Triba provjerit kako izvuč svaku zasebnu
    #r, g i b vrijednost i pohraniti iznost u drugi array. 
    
    #print(im2_pix[0])
    #print(im2_pix[0][0]) 
    #print(len(im2_pix))
    #print(len(im2_pix[0]))
    with open('text1.csv','a') as f:
        csv_reader = csv.writer(f, delimiter=',')
        for i in range(len(im2_pix)):
            dul = 0.0
            for j in range(len(im2_pix[i])):
                dul += im2_pix[i][j]**2    
            iznos = np.sqrt(dul)/255
            linecount = i+1
            csv_reader.writerow(linecount)
            csv_reader.writerow(iznos)
    #header =['Luminescencija']
    #df = pd.read_csv('text1.csv', names=header)
    #x = np.linspace(0,len(im2_pix),1)
    #y = df.Luminescencija
    #plt.scatter(x,y)
    #plt.show()

     
        
        
    
if __name__ == "__main__":
    a = argparse.ArgumentParser()
    a.add_argument("--In", help="path to image")
    a.add_argument("--Out", help="path to images")
    args = a.parse_args()
    print(args)
    lum(args.In, args.Out)
