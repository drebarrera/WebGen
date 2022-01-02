import modules as mx
import sys
import importlib
sys.path.append(r'C:\Users\dreba\Documents\GitHub\WebGen\files\Portfolio')
from prop import *
info = info()
data = mx.Data()
body = mx.Body()
from header import *
importlib.reload(sys.modules['header'])

### OBJECTS ###
main = mx.C()

### CONTENT ###
# Body
body.content = [main]

# Main
main.content = [nav]

### PROPERTIES ###
body.background_color = '#fefefe'
main.id = "main"