r"""
    ###     ####         ######
          ###  ###      #    ###
    ###         ###       ######
    ###      ####       ###   ##
    ###    ####        ###    ##
    ###   ##########    ##### ###

i2a creates ASCII representation of images right on your terminal.

Usage:
  i2a [options] [FILE | URL]
  i2a (-h | --help)
  i2a --version
Options:
  -h --help            Show this screen.
  --version            Show version.
  --colors             Show colored output.
  --height=<val>       Set the height in number of characters.
  --width=<val>        Set the width in number of characters
  --contrast=<factor>  Manually set contrast [default: 1.75].
"""
import subprocess
import os
import sys
from colors import *
from PIL import Image, ImageEnhance
from docopt import docopt

__version__ = '0.0.1'

ASCII = "Q0RMNWBDHK@$U8&AOkYbZGPXgE4dVhgSqm6pF523yfwCJ#TnuLjz7oeat1[]!?I}*{srlcxvi)><\\)|\"/+=^;,:'_-`. "

TTY_HEIGHT, TTY_WIDTH = map(int,subprocess.check_output(['stty', 'size']).split())

def old():
    im = Image.open('i2a.jpg')

    print(TTY_WIDTH,TTY_HEIGHT)

    print(im.size)
    aspect_ratio    = float(im.size[0])/im.size[1]
    print(aspect_ratio)
    scaled_height   = TTY_WIDTH / aspect_ratio
    scaled_width    = TTY_HEIGHT * aspect_ratio

    print(scaled_width, TTY_HEIGHT)
    print(TTY_WIDTH, scaled_height)

    im = im.resize((64,24))


    # img = enhancer.enhance(1.75).getdata()
    enhancer2 = ImageEnhance.Contrast(im)
    img = enhancer2.enhance(1.75).getdata()
    # img = im.getdata()
    im = im.convert('L') #Grayscale

    enhancer = ImageEnhance.Contrast(im)
    im2 = enhancer.enhance(1.75)
    _=0
    for count,i in enumerate(im2.getdata()):
        try:
            color = rgb(int((img[count][0]/255.0)*5),int((img[count][1]/255.0)*5),int((img[count][2]/255.0)*5))
        except:
            color = rgb(img[count],img[count],img[count])
        print_color(ASCII[int((1-(i/255.0))*(len((ASCII))-1))],end='', 
                    fg=color)
        _+=1
        if _==64:
            _=0
            print('')
# im.show()
def main():
    '''i2a creates ASCII representation of images right on your terminal.'''
    arguments = docopt(__doc__, version=__version__)

    if arguments['FILE'] or arguments['URL']:
        print(_get_image(arguments['URL']))
    else:
        print(__doc__)

if __name__ == '__main__':
    main()
