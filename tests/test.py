from __future__ import print_function
import unittest
import os

class TestGeneratedArt(unittest.TestCase):

  def test_basic(self):
    command = 'python ../i2a/i2a.py nyan.png'
    print('\n'+('-'*70)+'\n\n'+command+'\n\n')
    os.system(command)

  def test_color(self):
    command = 'python ../i2a/i2a.py nyan.png --colors'
    print('\n'+('-'*70)+'\n\n'+command+'\n\n')
    os.system(command)

  def test_bold_chars(self):
    command = 'python ../i2a/i2a.py nyan.png --bold'
    print('\n'+('-'*70)+'\n\n'+command+'\n\n')
    os.system(command)

  def test_invert(self):
    command = 'python ../i2a/i2a.py nyan.png --invert'
    print('\n'+('-'*70)+'\n\n'+command+'\n\n')
    os.system(command)

  def test_bg_black(self):
    command = 'python ../i2a/i2a.py nyan.png --bg=BLACK'
    print('\n'+('-'*70)+'\n\n'+command+'\n\n')
    os.system(command)

  def test_bg_white(self):
    command = 'python ../i2a/i2a.py nyan.png --bg=WHITE'
    print('\n'+('-'*70)+'\n\n'+command+'\n\n')
    os.system(command)

  def test_height(self):
    command = 'python ../i2a/i2a.py nyan.png --height=10'
    print('\n'+('-'*70)+'\n\n'+command+'\n\n')
    os.system(command)

  def test_width(self):
    command = 'python ../i2a/i2a.py nyan.png --width=40'
    print('\n'+('-'*70)+'\n\n'+command+'\n\n')
    os.system(command)

  def test_height_width(self):
    command = 'python ../i2a/i2a.py nyan.png --height=20 --width=40'
    print('\n'+('-'*70)+'\n\n'+command+'\n\n')
    os.system(command)

  def test_contrast(self):
    command = 'python ../i2a/i2a.py nyan.png --contrast=3'
    print('\n'+('-'*70)+'\n\n'+command+'\n\n')
    os.system(command)

  def test_alt_chars(self):
    command = 'python ../i2a/i2a.py nyan.png --alt-chars'
    print('\n'+('-'*70)+'\n\n'+command+'\n\n')
    os.system(command)


if __name__ == '__main__':
  unittest.main()
