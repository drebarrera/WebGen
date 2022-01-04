import modules as mx

### OBJECTS ###
nav = mx.C()
nav_center = mx.C()
menu = mx.C()
htitleA = mx.Link()
htitleT = mx.T()
option1A = mx.Link()
option1T = mx.T()
option2A = mx.Link()
option2T = mx.T()
option3A = mx.Link()
option3T = mx.T()
option4A = mx.Link()
option4T = mx.T()

### CONTENT ###
# Nav
nav.content = [nav_center]
nav_center.content = [htitleA, menu]

# Menu
menu.content = [option1A, option2A, option3A, option4A]

# Title
htitleA.content = [htitleT]
htitleT.content = 'dre barrera_'

# Options
option1A.content = [option1T]
option1T.content = 'Home'
option2A.content = [option2T]
option2T.content = 'Resume'
option3A.content = [option3T]
option3T.content = 'Contact'
option4A.content = [option4T]
option4T.content = 'Projects'

### PROPERTIES ###
nav.id = "nav"
nav.background_color = "#fefefe"
nav_center.id = "nav_center"
nav_center.background_color = ""
menu.id = "menu"
menu.background_color = ""
htitleA.id = "htitle"
htitleA.src = "https://www.drebarrera.com"
option1A.cl = 'button buttonRed'
option2A.cl = 'button buttonBlue'
option3A.cl = 'button buttonYellow'
option4A.cl = 'button buttonPurple'
option1A.src = 'https://www.drebarrera.com'
option2A.src = 'https://www.drebarrera.com/resources/resume.pdf'
option2A.target = "_blank"
option3A.src = 'https://www.drebarrera.com/contact/'
option3A.target = "_blank"
option4A.src = 'https://www.drebarrera.com/projects/'
option4A.target = "_blank"