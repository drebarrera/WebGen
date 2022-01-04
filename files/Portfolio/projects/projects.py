import modules as mx
import sys
sys.path.append(r'C:\Users\dreba\Documents\GitHub\WebGen\files\Portfolio')
data = mx.Data()
body = mx.Body()
from header import *
from visitInfo import *
from alert import *

data.title = "Dre Barrera | Projects"
data.author = "Andres Barrera"

### OBJECTS ###
center = mx.C()
main = mx.C()
title = mx.T()
caption = mx.T()
captionLinks = mx.C()
interactiveA = mx.C()
interactiveT = mx.T()
contactA = mx.Link()
contactT = mx.T()
projectList = mx.X()

### CONTENT ###
# Body
body.content = [center]

# Center
center.content = [nav, main, alert]

# Main
main.content = [title, caption, captionLinks, projectList]
title.content = 'Projects'
caption.content = 'The best way to view my previous projects is with my <span class="pseudoLink" id="interactive">Interactive Portfolio UI</span>, but if you would rather peruse this page, feel free to do so. If you have any questions or comments, feel free to reach out on my <a href="https://drebarrera.com/contact/" target="_blank" class="pseudoLink">Contact Page</a>'
captionLinks.content = [interactiveA, contactA]
interactiveA.content = [interactiveT]
interactiveT.content = 'Try the Interactive Portfolio!'
contactA.content = [contactT]
contactT.content = 'Contact'
projectList.content = '<p></p>'

### PROPERTIES ###
# Center
center.id = 'center'
center.background_color = ""

# Main
main.id = 'main'
main.background_color = ""
title.id = 'title'
caption.id = "caption"
captionLinks.id = "captionLinks"
captionLinks.background_color = ""
interactiveA.id = "interactive2"
interactiveA.cl = 'button buttonYellow'
interactiveA.background_color = ""
contactA.cl = 'button buttonRedRing'
contactA.src = 'https://www.drebarrera.com/contact/'