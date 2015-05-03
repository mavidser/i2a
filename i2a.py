from __future__ import print_function
from PIL import Image
from PIL import ImageEnhance
import subprocess

def rgb(red, green, blue):
    return 16 + (red * 36) + (green * 6) + blue

def set_color(fg=None, bg=None):
    print(_set_color(fg, bg), end='')

def _set_color(fg=None, bg=None):
    result = ''
    if fg:
        result += '\x1b[38;5;%dm' % fg
    if bg:
        result += '\x1b[48;5;%dm' % bg
    return result

def reset_color():
    print(_reset_color(), end='')

def _reset_color():
    return '\x1b[0m'

def print_color(*args, **kwargs):
    fg = kwargs.pop('fg', None)
    bg = kwargs.pop('bg', None)
    set_color(fg, bg)
    print(*args, **kwargs)
    reset_color()

def format_color(string, fg=None, bg=None):
    return _set_color(fg, bg) + string + _reset_color()

ASCII = "Q0RMNWBDHK@$U8&AOkYbZGPXgE4dVhgSqm6pF523yfwCJ#TnuLjz7oeat1[]!?I}*{srlcxvi)><\\)|\"/+=^;,:'_-`. "

im = Image.open('bat.gif')


height, width = map(int,subprocess.check_output(['stty', 'size']).split())
print(width,height)

print(im.size)
aspect_ratio    = float(im.size[0])/im.size[1]
print(aspect_ratio)
scaled_height   = width / aspect_ratio
scaled_width    = height * aspect_ratio

print(scaled_width, height)
print(width, scaled_height)

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
    color = rgb(int((img[count][0]/255.0)*5),int((img[count][1]/255.0)*5),int((img[count][2]/255.0)*5))
    print_color(ASCII[int((1-(i/255.0))*(len((ASCII))-1))],end='', 
                fg=color)
    _+=1
    if _==64:
        _=0
        print()
im.show()
