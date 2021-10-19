import modules as mx
import sys
sys.path.append('/Users/drebarrera/Documents/GitHub/WebGen/Micro')
from prop import *
info = info()
data = mx.Data()
body = mx.Body()

### INFO ###
data.title = 'Dre Barrera'
data.author = 'Andres Barrera'

### OBJECTS ###

center = mx.C()
title = mx.T()
subtitle = mx.T()

### CONTENT ###
# Body
body.content = [center]

# Center
center.content = [title, subtitle]

# Title
title.content = "microGEN"
subtitle.content = "Assembly and C code for Microprocessor Systems"

### PROPERTIES ###
# Body
body.background_color = '#fefefe'

# Center
center.display = 'flex'
center.justify_content = 'center'
center.background_color = 'white'
#center.background_color = '#242323'
