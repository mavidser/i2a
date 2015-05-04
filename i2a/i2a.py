"""
    ###     ####         ######
          ###  ###      #    ###
    ###         ###       ######
    ###      ####       ###   ##
    ###    ####        ###    ##
    ###   ##########    ##### ###

i2a creates ASCII art from images right on your terminal.

Usage: i2a [options] [FILE]

Options:
  -h --help            Show this screen.
  -v --version         Show version.
  -c --colors          Show colored output.
  -b --bold            Output bold characters
  -i --invert          Invert the colors.
  --bg=(BLACK|WHITE)   Specify the background color.
  --height=<val>       Set the height in number of characters.
  --width=<val>        Set the width in number of characters.
  --contrast=<factor>  Manually set contrast [default: 1.5].
  --alt-chars          Use an alternate set of characters.
"""

from __future__ import print_function
from setuptools import setup, find_packages
import subprocess
from colors import *
from PIL import Image, ImageEnhance
from docopt import docopt

__version__ = '1.2'

_ASCII = "@80GCLft1i;:,. "
_ASCII_2 = "Q0RMNWBDHK@$U8&AOkYbZGPXgE4dVhgSqm6pF523yfwCJ#TnuLjz7oeat1[]!?I}*{srlcxvi)><\\)|\"/+=^;,:'_-`. "

try:
    _HEIGHT, _WIDTH = map(int,subprocess.check_output(['stty', 'size']).split())
except:
    _HEIGHT, _WIDTH = 50, 50

def display_output(arguments):
    '''Display the ASCII art from the image.'''
    global _ASCII
    if arguments['--alt-chars']:
        _ASCII=_ASCII_2
    try:
        im = Image.open(arguments['FILE'])
    except:
        raise IOError('Unable to open the file.')
    im = im.convert("RGBA")
    aspect_ratio    = float(im.size[0])/im.size[1]
    scaled_height   = _WIDTH / aspect_ratio
    scaled_width    = _HEIGHT * aspect_ratio*2

    if scaled_width > _WIDTH:
        width = int(_WIDTH)
        height = int(scaled_height/2)

    elif scaled_height > _HEIGHT:
        width = int(scaled_width)
        height = int(_HEIGHT)

    if arguments['--width']:
        width = int(arguments['--width'])
        height = int(width / aspect_ratio / 2)

    elif arguments['--height']:
        height = int(arguments['--height'])
        width = int(height * aspect_ratio * 2)

    if arguments['--width'] and arguments['--height']:
        height = int(arguments['--height'])
        width = int(arguments['--width'])

    im = im.resize((width,height),resample=Image.ANTIALIAS)

    enhancer = ImageEnhance.Contrast(im)
    im = enhancer.enhance(float(arguments['--contrast']))
    img = im.getdata()
    im = im.convert('L') #Grayscale

    if not arguments['--invert']:
        _ASCII = _ASCII[::-1]

    bg=None;
    if arguments['--bg']=='BLACK':
        bg=rgb(0,0,0)
        fg=rgb(5,5,5)
    elif arguments['--bg']=='WHITE':
        bg=rgb(5,5,5)
        fg=rgb(0,0,0)

    row_len=0
    if arguments['--bold']:
        bold=True
    else:
        bold=False
    for count,i in enumerate(im.getdata()):
        ascii_char = _ASCII[int(((i/255.0))*(len((_ASCII))-1))]
        try:
            if not arguments['--colors']:
                raise Exception
            color = rgb(int((img[count][0]/255.0)*5),int((img[count][1]/255.0)*5),int((img[count][2]/255.0)*5))
            print_color(ascii_char, end='', fg=color, bg=bg, bold=bold)
        except:
            if bg and bold:
                print_color(ascii_char, end='', fg=fg, bg=bg, bold=bold)
            elif bold:
                print_color(ascii_char, end='', bold=bold)
            elif bg:
                print_color(ascii_char, end='', fg=fg, bg=bg)
            else:
                print(ascii_char, end='')
        row_len+=1
        if row_len==width:
            row_len=0
            print('')

def main():
    '''i2a creates ASCII art from images right on your terminal.'''
    arguments = docopt(__doc__, version=__version__)
    if arguments['FILE']:
        display_output(arguments)
    else:
        print(__doc__)

if __name__ == '__main__':
    main()
