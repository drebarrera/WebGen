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
rccT = mx.T()
cAHBENR = mx.C()
cAHBENRT = mx.X()
cAPB1ENR = mx.C()
cAPB1ENRT = mx.X()
cAPB2ENR = mx.C()
cAPB2ENRT = mx.X()
miscT = mx.T()
cCustom = mx.C()
cCustomT = mx.X()

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
commandC.content = [rccT, cAHBENR, cAPB1ENR, cAPB2ENR, miscT, cCustom]

# Code
code.content = [codeTitle, codeC]
codeTitle.content = "Code"

# -- Codes --
rccT.content = 'RCC Configuration'
cAHBENR.content = [cAHBENRT]
cAHBENRT.content = '<div class="cT rcc">RCC: AHBENR Configuration <span class="ctriangle">&#9654;</span><br><span class="cinfo">Select EN to Enable or DN to Disable for the bits below. If you wish to leave a bit unchanged, leave the select blank.<br><table class="ctable"><tr><td>Bit</td><td>Name</td><td>Selection</td></tr><tr><td title="DMAEN is used to enable the internal clock for the Digital Memory Access">0</td><td>DMAEN</td><td><select></option><option>EN</option><option>DN</option></select></td></tr><tr><td>1</td><td>DAM2EN</td><td><select><option></option><option>EN</option><option>DN</option></select></td></tr><tr><td>2</td><td>SRAMEN</td><td><select><option></option><option>EN</option><option>DN</option></select></td></tr><tr><td>4</td><td>FLITFEN</td><td><select><option></option><option>EN</option><option>DN</option></select></td></tr><tr><td>6</td><td>CRCEN</td><td><select><option></option><option>EN</option><option>DN</option></select></td></tr><tr title="IOPAEN is used to enable the internal clock for Peripheral A"><td>17</td><td>IOPAEN</td><td><select><option></option><option>EN</option><option>DN</option></select></td></tr><tr title="IOPBEN is used to enable the internal clock for Peripheral B"><td>18</td><td>IOPBEN</td><td><select><option></option><option>EN</option><option>DN</option></select></td></tr><tr><td title="IOPCEN is used to enable the internal clock for Peripheral C">19</td><td>IOPCEN</td><td><select><option></option><option>EN</option><option>DN</option></select></td></tr><tr><td title="IOPDEN is used to enable the internal clock for Peripheral D">20</td><td>USART4RST</td><td><select><option></option><option>EN</option><option>DN</option></select></td></tr><tr><td title="IOPEEN is used to enable the internal clock for Peripheral E">21</td><td>IOPEEN</td><td><select><option></option><option>EN</option><option>DN</option></select></td></tr><tr><td title="IOPFEN is used to enable the internal clock for Peripheral F">22</td><td>IOPFEN</td><td><select><option></option><option>EN</option><option>DN</option></select></td></tr><tr><td>24</td><td>TSCEN</td><td><select><option></option><option>EN</option><option>DN</option></select></td></tr></table></span></div>'
cAPB1ENR.content = [cAPB1ENRT]
cAPB1ENRT.content = '<div class="cT rcc">RCC: APB1ENR Configuration <span class="ctriangle">&#9654;</span><br><span class="cinfo">Select EN to Enable or DN to Disable for the bits below. If you wish to leave a bit unchanged, leave the select blank.<br><table class="ctable"><tr><td>Bit</td><td>Name</td><td>Selection</td></tr><tr title="TIM2EN is used to enable the internal clock for Timer TIM2"><td>0</td><td>TIM2EN</td><td><select><option></option><option>EN</option><option>DN</option></select></td></tr><tr title="TIM3EN is used to enable the internal clock for Timer TIM3"><td>1</td><td>TIM3EN</td><td><select><option></option><option>EN</option><option>DN</option></select></td></tr><tr title="TIM6EN is used to enable the internal clock for Timer TIM6"><td>4</td><td>TIM6EN</td><td><select><option></option><option>EN</option><option>DN</option></select></td></tr><tr title="TIM7EN is used to enable the internal clock for Timer TIM7"><td>5</td><td>TIM7EN</td><td><select><option></option><option>EN</option><option>DN</option></select></td></tr><tr title="TIM14EN is used to enable the internal clock for Timer TIM14"><td>8</td><td>TIM14EN</td><td><select><option></option><option>EN</option><option>DN</option></select></td></tr><tr><td>11</td><td>WWDGEN</td><td><select><option></option><option>EN</option><option>DN</option></select></td></tr><tr title="SPI2EN is used to enable the internal clock for Serial Peripheral Interface SPI2"><td>14</td><td>SPI2EN</td><td><select><option></option><option>EN</option><option>DN</option></select></td></tr><tr><td>17</td><td>USART2EN</td><td><select><option></option><option>EN</option><option>DN</option></select></td></tr><tr><td>18</td><td>USART3EN</td><td><select><option></option><option>EN</option><option>DN</option></select></td></tr><tr><td>19</td><td>USART4EN</td><td><select><option></option><option>EN</option><option>DN</option></select></td></tr><tr><td>20</td><td>USART5EN</td><td><select><option></option><option>EN</option><option>DN</option></select></td></tr><tr><td>21</td><td>I2C1EN</td><td><select><option></option><option>EN</option><option>DN</option></select></td></tr><tr><td>22</td><td>I2C2EN</td><td><select><option></option><option>EN</option><option>DN</option></select></td></tr><tr><td>23</td><td>USBEN</td><td><select><option></option><option>EN</option><option>DN</option></select></td></tr><tr><td>25</td><td>CANEN</td><td><select><option></option><option>EN</option><option>DN</option></select></td></tr><tr><td>27</td><td>CRSEN</td><td><select><option></option><option>EN</option><option>DN</option></select></td></tr><tr><td>28</td><td>PWREN</td><td><select><option></option><option>EN</option><option>DN</option></select></td></tr><tr title="DACEN is used to enable the internal clock for the Digital to Analog Converter"><td>29</td><td>DACEN</td><td><select><option></option><option>EN</option><option>DN</option></select></td></tr><tr><td>30</td><td>CECEN</td><td><select><option></option><option>EN</option><option>DN</option></select></td></tr></table></span></div>'
cAPB2ENR.content = [cAPB2ENRT]
cAPB2ENRT.content = '<div class="cT rcc">RCC: APB2ENR Configuration <span class="ctriangle">&#9654;</span><br><span class="cinfo">Select EN to Enable or DN to Disable for the bits below. If you wish to leave a bit unchanged, leave the select blank.<br><table class="ctable"><tr><td>Bit</td><td>Name</td><td>Selection</td></tr><tr><td>0</td><td>SYSCFGCOMPEN</td><td><select><option></option><option>EN</option><option>DN</option></select></td></tr><tr><td>5</td><td>USART6EN</td><td><select><option></option><option>EN</option><option>DN</option></select></td></tr><tr><td>6</td><td>USART7EN</td><td><select><option></option><option>EN</option><option>DN</option></select></td></tr><tr><td>7</td><td>USART8EN</td><td><select><option></option><option>EN</option><option>DN</option></select></td></tr><tr title="ADCEN is used to enable the internal clock for the Analog to Digital Converter"><td>9</td><td>ADCEN</td><td><select><option></option><option>EN</option><option>DN</option></select></td></tr><tr title="TIM1EN is used to enable the internal clock for Timer TIM1"><td>11</td><td>TIM1EN</td><td><select><option></option><option>EN</option><option>DN</option></select></td></tr><tr title="SPI1EN is used to enable the internal clock for Serial Peripheral Interface SPI1"><td>12</td><td>SPI1EN</td><td><select><option></option><option>EN</option><option>DN</option></select></td></tr><tr><td>14</td><td>USART1EN</td><td><select><option></option><option>EN</option><option>DN</option></select></td></tr><tr title="TIM15EN is used to enable the internal clock for Timer TIM15"><td>16</td><td>TIM15EN</td><td><select><option></option><option>EN</option><option>DN</option></select></td></tr><tr title="TIM16EN is used to enable the internal clock for Timer TIM16"><td>17</td><td>TIM16EN</td><td><select><option></option><option>EN</option><option>DN</option></select></td></tr><tr title="TIM17EN is used to enable the internal clock for Timer TIM17"><td>18</td><td>TIM17EN</td><td><select><option></option><option>EN</option><option>DN</option></select></td></tr><tr><td>22</td><td>DBGMCUEN</td><td><select><option></option><option>EN</option><option>DN</option></select></td></tr></table></span></div>'
miscT.content = 'Miscellaneous'
cCustom.content = [cCustomT]
cCustomT.content = '<div class="cT misc">Custom Code <span class="ctriangle">&#9654;</span><br><span class="cinfo">Type your code in the textbox below:<br><textarea style="width: 98%; margin-top: 0.5vh;max-width: 98%; height: 12vh;resize: none;"></textarea></span></div>'

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
commandC.overflow_y = 'scroll'

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
codeC.overflow_y = 'scroll'

# -- Codes --
rccT.cl = "ctitle"
cAHBENR.cl = "c"
cAHBENR.background_color = ""
cAHBENR.id = "rccAHBENR"
cAPB1ENR.cl = "c"
cAPB1ENR.background_color = ""
cAPB1ENR.id = "rccAPB1ENR"
cAPB2ENR.cl = "c"
cAPB2ENR.background_color = ""
cAPB2ENR.id = "rccAPB2ENR"
miscT.cl = "ctitle"
cCustom.cl = "c"
cCustom.background_color = ""
cCustom.id = "custom"

# Compiled
compiledC.id = "compiledC"
compiledC.display = "flex"
compiledC.justify_content = "center"
compiledC.position = "relative"
compiledC.background_color = "#fafafa"
compiledT.id = "compiledT"