from PIL import Image, ImageGrab 
import time
import threading
import pyautogui
import keyboard
from time import sleep


#for mouse clicks
mouseX = 1049
mouseY = 887
sixClick  = False

phase = 0
while True:
    if keyboard.is_pressed('s'):  # start
        phase = 1
    elif keyboard.is_pressed('a'):
        phase = 11


    if phase == 1:
        pyautogui.click(x=mouseX, y=mouseY)        
        pyautogui.mouseDown()
        phase = 2            
    elif phase == 2 :
        im2 = ImageGrab.grab(bbox=(999,802,1001,803)) #formula
        rgb1 = im2.convert('RGB')
        r2, g2, b2 = rgb1.getpixel((0, 0))
        if  r2 <= 10 and g2 < 10 and b2 <10 :
            pyautogui.mouseUp()        
            phase = 3
    elif phase == 3:
        p3 = ImageGrab.grab(bbox=(964,968,965,969)) #formula
        rgb3 =p3.convert('RGB')
        r3, g3, b3 = rgb3.getpixel((0, 0))
        if  r2 != 255 and g2 != 255 and b3 != 255:
            pyautogui.click(x=mouseX, y=mouseY,clicks=6, interval=0.1)
            phase = 4
    elif phase == 4:  
        im5 = ImageGrab.grab(bbox=(740,968,741,969)) #led down 1
        rgb5 = im5.convert('RGB')
        r5, g5, b5 = rgb5.getpixel((0, 0))
        if  r5 == 255 and g5 == 255 and b5 == 255: 
            sleep(0.5)    
            pyautogui.dragTo(mouseX, mouseY - 300, button='left')            
            pyautogui.mouseDown()            
            phase = 5
    elif phase == 5:
        im1 = ImageGrab.grab(bbox=(1012,799,1025,814)) #led up 1
        rgb1 = im1.convert('RGB')
        r1, g1, b1 = rgb1.getpixel((5, 5))
        if  r1 == 84 and g1 == 216 and b1 == 90:
            pyautogui.mouseUp()                           
            phase = 6
    elif phase == 6:            
        exp = ImageGrab.grab(bbox=(798,968,799,969)) #e3airetikos
        rgb1 = exp.convert('RGB')
        r1, g1, b1 = rgb1.getpixel((0, 0))
        if r1 != 255 and g1 != 255 and b1 != 255:                 
            pyautogui.dragTo(mouseX, mouseY, button='left')                                     
            phase = 7
    elif phase == 7:         
        im5 = ImageGrab.grab(bbox=(745,970,746,971)) #led down 2
        rgb5 = im5.convert('RGB')
        r5, g5, b5 = rgb5.getpixel((0, 0))
        if  r5 == 255 and g5 == 255 and b5 == 255: 
            sleep(0.75)    
            pyautogui.dragTo(mouseX, mouseY - 300, button='left')            
            pyautogui.mouseDown()   
            phase = 8               
    elif phase == 8:
        im1 = ImageGrab.grab(bbox=(1012,799,1025,814)) #led up 1
        rgb1 = im1.convert('RGB')
        r1, g1, b1 = rgb1.getpixel((5, 5))
        if  r1 == 84 and g1 == 216 and b1 == 90:
            pyautogui.mouseUp()       
            pyautogui.dragTo(mouseX, mouseY, button='left')     
            phase = 9
    elif phase == 9:
        pyautogui.click(x=mouseX, y=mouseY,clicks=6, interval=0.1)
        phase = 10
    elif phase == 10:
        pyautogui.dragTo(mouseX + 300, mouseY, button='left')  
        pyautogui.moveTo(mouseX,mouseY)  
        pyautogui.dragTo(mouseX + 300, mouseY, button='left')  
        pyautogui.moveTo(mouseX,mouseY) 
        pyautogui.dragTo(mouseX + 300, mouseY, button='left')  
        pyautogui.moveTo(mouseX,mouseY) 
        phase = 11
    elif phase == 11:
        break             
            

        
  
