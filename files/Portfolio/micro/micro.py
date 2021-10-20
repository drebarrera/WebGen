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
selectLangC = mx.C()
selectLangT = mx.T()
commandToCode = mx.C()
command = mx.C()
commandTitle = mx.T()
commandC = mx.C()
code = mx.C()
codeTitle = mx.T()
codeC = mx.C()
compiledC = mx.C()
compiledT = mx.T()

# -- Codes --
cCustom = mx.C()
cCustomT = mx.T()

### CONTENT ###
# Body
body.content = [main]

# Main
main.content = [infoBlock, selectLangC, commandToCode, compiledC]

# infoBlock
infoBlock.content = [title, description]

# selectLangC
selectLangC.content = [selectLangT]
selectLangT.content = 'Select Language <select id="lang"><option value = "ASM">ASM</option><option value = "C">C</option></select>'

# Title
title.content = 'microGEN<br><span style="font-size: 2.75vh; font-weight: 300;">Assembly and C code for Microprocessor Systems</span>'
description.content = 'microGEN is a microprocessor program generator for Assembly and C. Select your programming language below to begin. Then, click the desired commands / register modifications from the "Commands" section to append them to the "Code" section. Click the commands appended to "Code" in order to remove them. Click the arrow on each command to edit their adjustable fields. When you are happy with your program, hit compile to write the command blocks to code.'

# Command To Code
commandToCode.content = [command, code]

# Command
command.content = [commandTitle, commandC]
commandTitle.content = "Commands"
commandC.content = [cCustom]

# Code
code.content = [codeTitle, codeC]
codeTitle.content = "Code"

# -- Codes --
cCustom.content = [cCustomT]
cCustomT.content = 'Custom Code <span class="ctriangle">&#9654;</span><br><span class="cinfo">Type your code in the textbox below:<br><textarea style="width: 98%; margin-top: 0.5vh;max-width: 98%; height: 12vh;resize: none;"></textarea></span>'

# Compiled
compiledC.content = [compiledT]
compiledT.content = 'Compiled Code<br><textarea style="width:80%; height: 36vh; margin-top: 2vh; font-size: 2vh;"></textarea>'

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

# Select Language
selectLangC.display = "flex"
selectLangC.id = "selectLangC"
selectLangC.justify_content = "center"
selectLangT.color = "white"
selectLangC.background_color = ''

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
codeC.display = "flex"
codeC.flex_direction = "column"
codeC.position = "relative"
codeC.background_color = "white"

# -- Codes --
cCustom.cl = "c"
cCustom.background_color = ""
cCustomT.cl = "cT misc"
cCustom.id = "custom"

# Compiled
compiledC.id = "compiledC"
compiledC.display = "flex"
compiledC.justify_content = "center"
compiledC.position = "relative"
compiledC.background_color = "#fafafa"
compiledT.id = "compiledT"