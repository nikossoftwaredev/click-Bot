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
        sleep(0.80) #time to stop the formula
        pyautogui.mouseUp()        
        phase = 3
    elif phase == 3:    
        sleep(0.60)  #time to wait for six clicks
        pyautogui.click(x=mouseX, y=mouseY,clicks=6, interval=0.001)
        phase = 4
    elif phase == 4:  
        sleep(0.5)   #time to wait for the 1st slide up           
        pyautogui.dragTo(mouseX, mouseY - 101, button='left')                  
        pyautogui.mouseDown()           
        phase = 5
    elif phase == 5: 
        sleep(0.75)    
        pyautogui.mouseUp()  
        pyautogui.dragTo(mouseX, mouseY, button='left')   
        phase = 7
    elif phase == 7:           
            pyautogui.dragTo(mouseX, mouseY - 101, button='left')  
            pyautogui.dragTo(mouseX, mouseY, button='left') 
            pyautogui.dragTo(mouseX, mouseY - 101, button='left') 
            pyautogui.dragTo(mouseX, mouseY, button='left') 
            pyautogui.dragTo(mouseX, mouseY - 101, button='left')         
            pyautogui.dragTo(mouseX, mouseY, button='left') 
            pyautogui.dragTo(mouseX, mouseY - 101, button='left')    
            pyautogui.dragTo(mouseX, mouseY, button='left') 
            pyautogui.dragTo(mouseX, mouseY - 101, button='left')                    
            pyautogui.mouseDown()   
            phase = 8             
    elif phase == 8:
        sleep(0.70) #time to release when green
        pyautogui.mouseUp()     
        pyautogui.dragTo(mouseX, mouseY, button='left')                 
        pyautogui.click(x=mouseX, y=mouseY,clicks=6, interval=0.001)       
        pyautogui.dragTo(mouseX + 101, mouseY, button='left')  
        pyautogui.moveTo(mouseX,mouseY)  
        pyautogui.dragTo(mouseX + 101, mouseY, button='left')  
        pyautogui.moveTo(mouseX,mouseY)   
        pyautogui.dragTo(mouseX + 101, mouseY, button='left')  
        pyautogui.moveTo(mouseX,mouseY) 
        pyautogui.dragTo(mouseX + 101, mouseY, button='left')  
        pyautogui.moveTo(mouseX,mouseY)                
        phase = 11
    elif phase == 11:
        break             
            

        
  
