"""
 
All coordinates assume a screen resolution of 1280x1024, and Chrome 
maximized with the Bookmarks Toolbar enabled.
Down key has been hit 4 times to center play area in browser.
x_pad = 156
y_pad = 345
Play area =  x_pad+1, y_pad+1, 796, 825
"""

from PIL import ImageGrab
import os
import time

#CONSTANTS
#--------------

x_pad = 187
y_pad = 157

def screenGrab():
    box = (x_pad+1,y_pad+1,x_pad+640,y_pad+479)
    
    im = ImageGrab.grab(box) # args: 1. (top_x, top_y, bot_x, bot_y
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time()))
            + '.png', 'PNG')

def main():
    screenGrab()

if __name__ == '__main__':
    main()
    
