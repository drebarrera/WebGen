import modules as mx
import sys
import os
homedir = os.getcwd() + r'/files/Portfolio/'
sys.path.append(homedir)
data = mx.Data()
body = mx.Body()

### OBJECTS ###
nav = mx.Nav()
nav_title = mx.T()
nav_space = mx.X() # Custom HTML space
page_content = mx.C()
heading = mx.T()
subheading = mx.T()
paragraph = mx.T()
gitHub_link = mx.Link()
gitHub_linkText = mx.T()

### CONTENT ###
body.content = [nav, page_content] # Assign containers to body content
nav.content = [[nav_title, nav_space]]
nav_title.content = "WebGen Example"

# Create three nav option links named "nav_option_i"
text_content = ["WebGen Github","Creator's Portfolio","Contact Creator"]
src_content = ["https://github.com/drebarrera/WebGen/","https://www.drebarrera.com","https://www.drebarrera.com/contact"]
for i in range(1,4):
    objName = "nav_option_"+str(i)
    exec(objName + ' = mx.Link()')                                  # 1. Create link object
    exec(objName + 'Text = mx.T()')                                 # 2. Create text object
    exec(objName + 'Text.content = "' + text_content[i - 1] + '"')  # 3. Assign text_content[i - 1] to text object
    exec(objName + '.content = [' + objName + 'Text]')              # 4. Assign text object to link object content
    exec(objName + '.cl = "button buttonRed"')                      # 5. Assign button classes to link object
    exec(objName + '.src = "' + src_content[i - 1] + '"')           # 6. Assign source to link object
    exec('nav.content[0].append('+ objName +')')                    # 7. Append link object to nav content
    
page_content.content = [heading, subheading, paragraph, gitHub_link] # Assign objects to page content
heading.content = "Hello World"
subheading.content = "Webpage Made With WebGen"
paragraph.content = "This webpage was made with WebGen - a custom Python to User Interface compiler with the goal of making website and app design cleaner and more efficient.\nFor more information about WebGen, visit the link below."
gitHub_link.content = [gitHub_linkText]
gitHub_linkText.content = "WebGen GitHub"

### PROPERTIES ###
# Nav Components
nav.id = "nav"
nav.background_color = ""
nav.tableid = "navTable"
nav_title.type = "h1"

# Page Components
page_content.id = "pageContent"
page_content.background_color = ""
heading.type = "h2"
subheading.type = "h3"
subheading.color = "#005580"
subheading.font_weight = "500"
paragraph.padding = "10px"
paragraph.line_height = "1.2"
gitHub_link.cl = "button buttonBlue"
gitHub_link.src = "https://github.com/drebarrera/WebGen/"
