
"""
All coordinates assume a screen resolution of 1280x1024, and Chrome 
maximized with the Bookmarks Toolbar enabled.
Down key has been hit 4 times to center play area in browser.
x_pad = 156
y_pad = 345
Play area =  x_pad+1, y_pad+1, 796, 825
"""

from PIL import ImageGrab
from numpy import *
import os
import time
import win32api, win32con


#CONSTANTS
#--------------
x_pad = 187
y_pad = 157



def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    print("Click")

def leftDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    print('LeftDown')

def leftUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(.1)
    print('LeftRelease')

def mousePos(cord):
    win32api.SetCursorPos((x_pad + cord[0], y_pad + cord[1]))

def get_cords():
    x,y = win32api.GetCursorPos()
    x = x - x_pad
    y = y - y_pad
    print(x,y)
    
def screenGrab():
    box = (x_pad+1,y_pad+1,x_pad+640,y_pad+480)
    
    im = ImageGrab.grab(box) # args: 1. (top_x, top_y, bot_x, bot_y
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
    return im

def clear_tables():
    mousePos((100, 200))
    leftClick()

    mousePos((200, 200))
    leftClick()

    mousePos((300, 200))
    leftClick()

    mousePos((400, 200))
    leftClick()

    mousePos((500, 200))
    leftClick()

    mousePos((600, 200))
    leftClick()
 
    time.sleep(1)

def foldMat():
    mousePos((Cord.f_rice[0]+40,Cord.f_rice[1])) 
    leftClick()
    time.sleep(.1)

def makeFood(food):
    if food == 'caliroll':
        print('Making a caliroll')
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(.1)
        foldMat()
        time.sleep(1.5)
     
    elif food == 'onigiri':
        print('Making a onigiri')
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.1)
        foldMat()
        time.sleep(.05)
         
        time.sleep(1.5)
 
    elif food == 'gunkan':
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(.1)
        foldMat()
        time.sleep(1.5)

def buyFood(food):

    mousePos(Cord.phone)

    mousePos(Cord.menu_toppings)

    mousePos(Cord.t_shrimp)
    mousePos(Cord.t_nori)
    mousePos(Cord.t_roe)
    mousePos(Cord.t_salmon)
    mousePos(Cord.t_unagi)
    mousePos(Cord.t_exit)
     
    mousePos(Cord.menu_rice)
    mousePos(Cord.buy_rice)
     
    mousePos(Cord.delivery_norm)

def buyFood(food):
     
    if food == 'rice':
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()
        mousePos(Cord.menu_rice)
        time.sleep(.05)
        leftClick()
        s = screenGrab()
        if s.getpixel(Cord.buy_rice) != (183,222,255):
            print('rice is available')
            mousePos(Cord.buy_rice)
            time.sleep(.1)
            leftClick()
            mousePos(Cord.delivery_norm)
            time.sleep(.1)
            leftClick()
            time.sleep(2.5)
        else:
            print('rice is NOT available')
            mousePos(Cord.t_exit)
            leftClick()
            time.sleep(1)
            buyFood(food)
             
 
             
    if food == 'nori':
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()
        mousePos(Cord.menu_toppings)
        time.sleep(.05)
        leftClick()
        s = screenGrab()
        print('test')
        time.sleep(.1)
        if s.getpixel(Cord.t_nori) != (204,172,89):
            print('nori is available')
            mousePos(Cord.t_nori)
            time.sleep(.1)
            leftClick()
            mousePos(Cord.delivery_norm)
            time.sleep(.1)
            leftClick()
            time.sleep(2.5)
        else:
            print('nori is NOT available')
            mousePos(Cord.t_exit)
            leftClick()
            time.sleep(1)
            buyFood(food)
 
    if food == 'roe':
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()
        mousePos(Cord.menu_toppings)
        time.sleep(.05)
        leftClick()
        s = screenGrab()
         
        time.sleep(.1)
        if s.getpixel(Cord.t_roe) != (252,130,200):
            print('roe is available')
            mousePos(Cord.t_roe)
            time.sleep(.1)
            leftClick()
            mousePos(Cord.delivery_norm)
            time.sleep(.1)
            leftClick()
            time.sleep(2.5)
        else:
            print('roe is NOT available')
            mousePos(Cord.t_exit)
            leftClick()
            time.sleep(1)
            buyFood(food)

def startGame():
    mousePos((314, 185))
    leftClick()
    time.sleep(.1)

    mousePos((328, 386))
    leftClick()
    time.sleep(.1)
    
    mousePos((580, 457))
    leftClick()
    time.sleep(.1)

    mousePos((321, 372))
    leftClick()
    time.sleep(.1)

def main():
    pass

if __name__ == '__main__':
    main()


class Cord:

    f_Shrimp = (30, 330)
    f_Rice = (90, 330)
    f_Nori = (30, 380)
    f_Roe = (90, 380)
    f_Salmon = (30, 440)
    f_Unagi = (90, 440)

#------------------------------

    phone = (562, 389)
 
    menu_toppings = (538, 337)
     
    t_shrimp = (541, 354)
    t_nori = (496, 285)
    t_roe = (503, 337)
    t_salmon = (583, 337)
    t_unagi = (499, 397)
    t_exit = (590, 425)
 
    menu_rice = (541, 354)
    buy_rice = (545, 344)
     
    delivery_norm = (579, 376)
