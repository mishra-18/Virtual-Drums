import cv2 
from pygame import mixer
from playsound import playsound
import numpy as np 
import time
from threading import Thread
cap = cv2.VideoCapture(0)
drum= cv2.imread("drum.jpg")
drum = cv2.cvtColor( drum , cv2.COLOR_RGB2BGR)
drum = cv2.resize(drum , ( 128 , 128))


mixer.init()
cap.set(3 , 400 )
cap.set(4 , 512 )
cap.set(10, 100 ) 
colours = np.array([ 32 , 78 , 90 ,  79  ,   255 , 255 ])
lower = np.array(colours[ 0:3]) 
higher = np.array(colours[3:6])
def play_sounds():     
    mixer.music.load("vinyl-snare-02.mp3")
    mixer.music.set_volume(0.1)
    mixer.music.play() 
    time.sleep(0)
def play_soundk():
    mixer.music.load("vinyl-kick-01.mp3") 
    mixer.music.set_volume(1)
    mixer.music.play() 
    time.sleep(0)

def color_detection( img ):
    hsv_img = cv2.cvtColor(img , cv2.COLOR_BGR2HSV)   
    mask = cv2.inRange(hsv_img , lower , higher)
    detect = np.sum(mask)
    
    return detect

a = 0      
b = 0
n = 0 
t = Thread(target=play_sounds)
t1 = Thread(target=play_soundk)
ct = [[0 , 0] , [0 , 0]]
i = 0 
while True: 
   
    _ , im = cap.read()
    im = cv2.resize(im , ( 800 , 512 ))
    s2 = im.copy()
    s2 = s2[320:448 , 608:736]
    
    k = im.copy()
    k = k[320:448 , 64:192 ]
    cv2.rectangle(im , (736,320) , (608,448) , ( 255 , 0 , 0 , 0.5) , 2 )
    cv2.rectangle(im , (192,320) , (64,448) , (255 , 0 , 0  , 0.5 ) , 2 )
    contour_img = im.copy()
    num_pix=[0 , 0]
    num_pix[0] = color_detection( s2 )
    num_pix[1] = color_detection( k )
    
    if num_pix[0] < 100:
        a = 1
    if not t.is_alive() and num_pix[0] > 10000 :
        if a == 1 :
            t = Thread(target=play_sounds)
            t.start() 
        a = 0
    if num_pix[1] < 100:
        b = 1
    if not t1.is_alive() and num_pix[1] > 10000 :
        if b == 1 :
            t1 = Thread(target=play_soundk)
            t1.start() 
        b = 0    
   
    added = cv2.addWeighted(contour_img[320:448 , 608:736, :], 0.5 , drum[0:128 , 0:128 , :] , 1 - 0.5 ,0)
    contour_img[320:448 , 608:736] = added
    added = cv2.addWeighted(contour_img[320:448 , 64:192 , :], 0.5 , drum[0:128 , 0:128 , :] , 1 - 0.5   ,0 )
    contour_img[320:448 , 64:192] = added  
    cv2.imshow("win" , contour_img )
    if cv2.waitKey(1) & 0xff == ord('q') :
          break
        
