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
from alert import *
importlib.reload(sys.modules['alert'])
from visitInfoIndex import *

### DATA ###
data.title = "Dre Barrera"
data.author = "Andres Barrera"

### OBJECTS ###
main = mx.C()
welcome = mx.C()
slide1Textbox = mx.C()
slide1Title = mx.T()
slide1Text = mx.T()
slide1Links = mx.C()
slide1ResumeA = mx.Link()
slide1ResumeT = mx.T()
slide1ContactA = mx.Link()
slide1ContactT = mx.T()
slide1Image = mx.Image()
interactiveButtonA = mx.C()
interactiveButtonT = mx.T()
githubA = mx.Link()
githubT = mx.T()
musicA = mx.Link()
musicT = mx.T()
galleryA = mx.Link()
galleryT = mx.T()
currA = mx.Link()
currT = mx.T()

### CONTENT ###
# Body
body.content = [main]

# Main
main.content = [nav, welcome, alert]

# Welcome
welcome.content = [slide1Textbox]
slide1Textbox.content = [slide1Title, slide1Image, slide1Text, slide1Links]
slide1Title.content = 'hello world.'
slide1Text.content = 'My name is Andr&eacute;s Barrera, but you can call me Dre. I am a <class="pseudoLink bookmark" data-slide="2" data-track = "2">Computer Engineering</span> senior at <a href="https://www.purdue.edu" target="_blank" class="textLink">Purdue University</a>. With a background in <span class="pseudoLink bookmark" data-slide="6" data-track = "2">Multidisciplinary Engineering</span>, <span class="pseudoLink bookmark" data-slide="3" data-track = "3">UI/UX</span>, and <span class="pseudoLink bookmark" data-slide="5" data-track = "2">Business Development</span>, I am much more than just a Computer Engineer.<br><br><em style="font-weight: 500;text-align: center; width:100%; display: block;">I am an ambitious creator.</em>'
slide1Links.content = [slide1ResumeA, interactiveButtonA, slide1ContactA, githubA, currA, galleryA, musicA]
slide1ResumeA.content = [slide1ResumeT]
slide1ResumeT.content = 'My Resume'
slide1ContactA.content = [slide1ContactT]
slide1ContactT.content = 'Contact Me'
interactiveButtonA.content = [interactiveButtonT]
interactiveButtonT.content = 'Try the Interactive Portfolio!'
githubA.content = [githubT]
githubT.content = 'GitHub'
musicA.content = [musicT]
musicT.content = 'Music'
galleryA.content = [galleryT]
galleryT.content = 'Behance Gallery'
currA.content = [currT]
currT.content = 'Curriculum'

### PROPERTIES ###
body.background_color = '#fefefe'

# Main
main.id = "main"
main.background_color = ""

# Welcome
welcome.id = "welcome"
welcome.background_color = ""
slide1Textbox.id = 'slide1Textbox' 
slide1Textbox.cl = 'textboxSlide'
slide1Textbox.background_color = ''
slide1Image.id = 'slide1Image'
slide1Image.src = "images/portrait.jpeg"
slide1Title.type = 'h6'
slide1Title.color = '#ff5938'
slide1Title.cl = 'slideTitle'
slide1Text.cl = 'slideText'
slide1Links.background_color = ""
slide1Links.id = "welcomeLinks"
slide1ResumeA.id = 'resumeLink'
slide1ResumeA.cl = 'button buttonBlue'
slide1ResumeA.target = '_blank'
slide1ResumeA.src = 'https://www.drebarrera.com/resources/resume.pdf'
slide1ContactA.id = 'contactLink'
slide1ContactA.cl = 'button buttonRedRing'
slide1ContactA.target = '_blank'
slide1ContactA.src = 'https://www.drebarrera.com/contact/'
interactiveButtonA.background_color = ""
interactiveButtonA.cl = 'button buttonRed'
interactiveButtonA.id = 'interactive'
githubA.cl = 'button buttonPurple'
githubA.target = '_blank'
githubA.src = 'https://github.com/drebarrera'
musicA.cl = 'button buttonBlue'
musicA.target = '_blank'
musicA.src = 'https://www.drebarrera.com/music/'
galleryA.cl = 'button buttonYellow'
galleryA.target = '_blank'
galleryA.src = 'https://behance.net/drebarrera'
currA.cl = 'button buttonPurple'
currA.target = '_blank'
currA.src = 'https://www.drebarrera.com/resources/curriculum.pdf'