# In Windows, Control+Z is the typical keyboard shortcut to mean "end of file",
# in Linux and Unix it's typically Control+D.


try:
    text=input('Enter something -->')
except EOFError:
    print('Why did you do an EOF on me?')
except KeyboardInterrupt:
    print('You cancelled the opration.')
else:
    print('You entered {}'.format(text))