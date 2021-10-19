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
main = mx.C()
infoBlock = mx.C()
title = mx.T()
description = mx.T()
commandToCode = mx.C()
command = mx.C()
commandTitle = mx.T()
commandC = mx.C()
code = mx.C()
codeTitle = mx.T()
codeC = mx.C()

# -- Codes --
cUndefined = mx.C()
cUndefinedT = mx.T()

### CONTENT ###
# Body
body.content = [main]

# Main
main.content = [infoBlock, commandToCode]

# infoBlock
infoBlock.content = [title, description]

# Title
title.content = 'microGEN<br><span style="font-size: 2.75vh; font-weight: 300;">Assembly and C code for Microprocessor Systems</span>'
description.content = 'microGEN is a microprocessor program generator for Assembly and C. Select your programming language below to begin. Then, drag and drop the desired commands / register modifications from the "Commands" section to the "Code" section. Click the arrow on each command to edit their adjustable fields. When you are happy with your program, hit compile to write the command blocks to code.'

# Command To Code
commandToCode.content = [command, code]

# Command
command.content = [commandTitle, commandC]
commandTitle.content = "Commands"
commandC.content = [cUndefined]

# Code
code.content = [codeTitle, codeC]
codeTitle.content = "Code"

# -- Codes --
cUndefined.content = [cUndefinedT]
cUndefinedT.content = 'Undefined <span class="triangle">&#9654;</span>'

### PROPERTIES ###
# Body
body.background_color = '#fefefe'

# Main
main.background_color = 'white'
main.background_color = '#242323'

# infoBlock
infoBlock.display = 'flex'
infoBlock.justify_content = 'center'
infoBlock.align_items = 'center'
infoBlock.position = 'relative'
infoBlock.background_color = ''

# Title
title.id = "title"
title.color = "white"
title.display = "inline-block"
title.position = "relative"

# Description
description.color = "white"
description.id = "description"
description.display = "inline-block"
description.position = "relative"

# Command To Code
commandToCode.id = "commandToCode"
commandToCode.display = "flex"
commandToCode.justify_content = "center"
commandToCode.align_items = "center"
commandToCode.position = "relative"
commandToCode.background_color = ""

# Command
command.id = "command"
command.display = "inline-block"
command.position = "relative"
command.background_color = "#fafafa"
commandTitle.cl = "ctcTitle"
commandC.id = "commandC"
commandC.cl = "ctcContainer"
commandC.display = "block"
commandC.position = "relative"
commandC.background_color = "white"

# Code
code.id = "code"
code.display = "inline-block"
code.position = "relative"
code.background_color = "#fafafa"
codeTitle.cl = "ctcTitle"
codeC.id = "codeC"
codeC.cl = "ctcContainer"
codeC.display = "block"
codeC.position = "relative"
codeC.background_color = "white"

# -- Codes --
cUndefined.cl = "c"
cUndefined.background_color = ""
cUndefinedT.cl = "cT misc"