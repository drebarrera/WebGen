import modules as mx
import sys
sys.path.append(r'C:\Users\dreba\Documents\GitHub\WebGen\files\test')
data = mx.Data()
body = mx.Body()
from header import *

data.title = 'Our First Webpage!'
data.author = 'Andres Barrera'

### OBJECTS ###
text1 = mx.T()
container = mx.C()
text2 = mx.T()
modX = mx.X()

### CONTENT ###
# Body
body.content = [title, text1, container, container, container, modX]

# Text1
text1.content = 'hello world!'

# Container
container.content = [text2]
text2.content = 'This is a container with text'

modX.content = '<div style="color: green; width: 500px; height: 500px; background-color: orange"><p>this is a X element</p></div>'

### PROPERTIES ###
# Body
body.background_color = 'grey'
container.background_color = 'red'
container.color = 'white'
container.id = 'container'
text2.padding = '5px'