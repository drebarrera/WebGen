import modules as mx
import sys
sys.path.append('/Volumes/Software SSD/WebGen/files/Portfolio')
from prop import *
from header import *
data = mx.Data()
body = mx.Body()
info = info()

### OBJECT DEFINITIONS ###
class Project:
	def __init__(self):
		self.name = 'project'
		self.id = ''
		self.title = 'Project Title'
		self.type = 'Project Type'
		self.img = '/Volumes/Software SSD/WebGen/files/Portfolio/supporting/folder.jpeg'
		self.imgD = '/Volumes/Software SSD/WebGen/files/Portfolio/supporting/picture.png'
		self.content = 'This is an example project. Define a project with project properties.'
		self.oc = 'rgba(0,0,0,0.8)'
		self.tc = 'black'
		self.stc = '#005580'

	def c(self, a, b):
		i = ' id="'+self.id+'"' if self.id != "" else ""
		title = '<!--<h3 style="margin-top: 180px; font-size: 20px; position: absolute; font-weight: 500; color: '+self.tc+'; background-color: white; padding-top: 5px; width:250px; text-align: center;">'+self.title+'</h3>-->'
		subtitle = '<!--<h5 style="margin-top: 208px; font-size: 16px; position: absolute; font-weight: 300; color: '+self.stc+'; background-color: white; padding-bottom: 5px; width:250px; text-align: center;">'+self.type+'<h5>-->'
		imgD = '<img src = "'+self.imgD+'" style = "max-width:450px; max-height: 300px;"/>'
		
		text = '<div style = "height: 225px; width: 300px; margin-left: 125px; margin-top: 75px; background-color: #f5f5f5; opacity: 0.8;"></div>'
	
		return '<div style = "height: 275px; width: 375px; position: relative; display: inline-block; margin: 10px; margin-right: 75px; border: 2px solid black; border-radius: 25px;"><div '+i+' style = "height: 275px; width: 275px;background-image: url(\''+self.img+'\');background-size: 275px 275px;position: relative; display: inline-block;" onmouseover = "projectHover(\''+self.id+'\',\''+self.oc+'\')" onmouseout = "projectOut(\''+self.id+'\',\''+self.oc+'\')" onclick = "projectClick(\''+self.id+'\',\''+self.oc+'\')">'+text+'</div></div>'

### INFO ###
data.title = 'Dre Barrera'
data.author = 'Andres Barrera'

### OBJECTS ###
center = mx.C()
title = mx.T()
slide0 = mx.C()
slide1 = mx.C()
quoteC = mx.C()
quoteT = mx.T()
mainTable = mx.Table()
mainLeft = mx.C()
mainRight = mx.C()
profileImage = mx.Image()
profileName = mx.T()
profileContactA = mx.Link()
profileContact = mx.T()
projectsTitleE = mx.T()
projectsTableCE = mx.C()
projectsTableE = mx.C()
projectsTitleD = mx.T()
projectsTableCD = mx.C()
projectsTableD = mx.C()


### CONTENT ###
# Body
body.content = [header,center]

# Center
center.content = [slide0, slide1]

# Slides
slide0.content = [title]
slide1.content = [quoteC, mainTable]

# Title
title.content = ''

# Quote Container
quoteC.content = [quoteT]

# Caption1
quoteT.content = '"THERE IS NOTHING IMPOSSIBLE<br></span>TO HIM WHO WILL TRY"<br><span class="tab"></span><span class="tab"></span><span class="tab" style="font-family: Helvetica;font-size: 20px;font-weight: 300;color: #005580;">- Alexander the Great</span>'

# Main Table
mainTable.content = [[mainLeft, mainRight]]
mainLeft.content = [profileImage, profileName, profileContactA]
mainRight.content = [projectsTitleE, projectsTableCE, projectsTitleD, projectsTableCD]

# Profile
profileImage.src = '/Volumes/Software SSD/WebGen/files/Portfolio/supporting/portrait.JPEG'
profileName.content = 'Andrés Barrera'
profileContactA.content = [profileContact]
profileContactA.src = 'https://www.drebarrera.com/contact'
profileContact.content = 'Contact Me'

# Projects
projectsTitleE.content = 'ENGINEERING PROJECTS'
projectsTableCE.content = [projectsTableE]
projectsTitleD.content = 'DESIGN PROJECTS'
projectsTableCD.content = [projectsTableD]


### PROPERTIES ###
# Center
center.display = 'flex'
center.justify_content = 'center'
center.background_color = 'white'

# Title
title.id = 'title'
title.color = 'white'

# Slide0
slide0.id = 'slide0'
slide0.cl = 'slide'
slide0.text_align = 'center'
slide0.background_color = '#242323'

# Slide 1
slide1.id = 'slide1'
slide1.cl = 'slide'
slide1.display = 'flex'
slide1.justify_content = 'center'
slide1.background_color = '#f5f5f5'

# Quote Container
quoteC.id = 'quoteC'
quoteC.display = 'flex'
quoteC.justify_content = 'center'
quoteC.position = 'absolute'
quoteC.text_align = 'center'
quoteC.background_color = ''

# Main Table
mainTable.id = 'main'
mainTable.background_color = ''

# Main Left
mainLeft.id = 'mainLeft'
mainLeft.display = 'flex'
mainLeft.justify_content = 'center'
mainLeft.background_color = 'white'

# Main Right
mainRight.id = 'mainRight'
mainRight.background_color = 'white'

# Profile Image
profileImage.id = 'profileImage'
profileImage.position = 'absolute'

# Profile Name
profileName.id = 'profileName'
profileName.type = 'h1'
profileName.position = 'absolute'

# Profile Contact
profileContactA.id = 'profileContactA'
profileContactA.target = '_blank'
profileContactA.text_decoration = 'none'

# Projects Title
projectsTitleE.id = 'projectsTitle'
projectsTitleE.type = 'h2'
projectsTitleE.position = 'relative'
projectsTitleE.display = 'block'
projectsTitleE.text_align = 'center'
projectsTitleE.color = '#005580'
projectsTitleD.id = 'projectsTitle'
projectsTitleD.type = 'h2'
projectsTitleD.position = 'relative'
projectsTitleD.display = 'block'
projectsTitleD.text_align = 'center'
projectsTitleD.color = '#005580'

# Projects Table
projectsTableCE.display = 'flex'
projectsTableCE.justify_content = 'center'
projectsTableCE.position = 'relative'
projectsTableCE.background_color = ''
projectsTableCD.display = 'flex'
projectsTableCD.justify_content = 'center'
projectsTableCD.position = 'relative'
projectsTableCD.background_color = ''

# Projects Table
projectsTableE.id = 'projectsTable'
projectsTableE.display = 'block'
projectsTableE.position = 'relative'
projectsTableE.background_color = ''
projectsTableD.id = 'projectsTable'
projectsTableD.display = 'block'
projectsTableD.position = 'relative'
projectsTableD.background_color = ''

# Projects
p1 = Project()
p1.id = 'p1'
p2 = Project()
p2.id = 'p2'
f = open("/Volumes/Software SSD/WebGen/files/Portfolio/index/projects.txt",'r')
lines = f.read().split('\n')
f.close()
i = 0
#projectList = []
for p in lines[1:]:
	if p == '':
		break
	p = p.split(',')
	ob = Project()
	ob.id = p[0] if p[0] != "" else ob.id
	ob.title = p[1] if p[1] != "" else ob.title
	ob.type = p[2] if p[2] != "" else ob.type
	cat = p[3]
	ob.img = p[4] if p[4] != "" else ob.img
	ob.imgD = p[5] if p[5] != "" else ob.imgD
	ob.content = p[6] if p[6] != "" else ob.content
	ob.oc = p[7] if p[7] != "" else ob.oc
	ob.tc = p[8] if p[8] != "" else ob.tc
	ob.stc = p[9] if p[9] != "" else ob.stc
	if cat == "Engineering":
		projectsTableE.content.append(ob)
	#elif cat == "Design":
		#projectsTableD.content.append(ob)
		#overlay = '<div style = "height: 275px; width: 300px;position: absolute; cursor: pointer; overflow: hidden;">'+content+title+subtitle+'</div>'
		#content = '<!--<p style = "color:#005580; padding-top: 10px;padding-left:20px; padding-right:20px; position: relative; display: none;" id = "projectLink">Click to read more.</p><p style = "color: white; padding-right: 20px;padding-left: 20px; position: absolute; background: -webkit-linear-gradient(#fff 40%, #000); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-size: 200px 200px; height:165px; position: relative; display: none;">'+self.content+'</p>-->'