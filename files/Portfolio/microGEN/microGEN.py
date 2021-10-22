import modules as mx
import sys
sys.path.append('/Users/drebarrera/Documents/GitHub/WebGen/Portfolio')
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
gpioT = mx.T()
cMODER = mx.C()
cMODERT = mx.X()
cPUPDR = mx.C()
cPUPDRT = mx.X()
cODR = mx.C()
cODRT = mx.X()
timerT = mx.T()
cTIM1 = mx.C()
cTIM1T = mx.X()
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
commandC.content = [rccT, cAHBENR, cAPB1ENR, cAPB2ENR, gpioT, cMODER, cPUPDR, cODR, timerT, cTIM1, miscT, cCustom]

# Code
code.content = [codeTitle, codeC]
codeTitle.content = "Code"

# -- Codes --
rccT.content = 'RCC Configuration'
cAHBENR.content = [cAHBENRT]
cAHBENRT.content = '<div class="cT rcc">RCC: AHBENR Configuration <span class="ctriangle">&#9654;</span><br><span class="cinfo">Select EN to Enable or DIS to Disable for the bits below. If you wish to leave a bit unchanged, leave the select blank.<!----><span class="cR"><br>This configuration requires two registers. <select><option>r0</option><option>r1</option><option>r2</option><option>r3</option><option>r4</option><option>r5</option><option>r6</option><option>r7</option><option>r8</option><option>r9</option><option>r10</option><option>r11</option><option>r12</option></select><select><option>r0</option><option>r1</option><option>r2</option><option>r3</option><option>r4</option><option>r5</option><option>r6</option><option>r7</option><option>r8</option><option>r9</option><option>r10</option><option>r11</option><option>r12</option></select></span><!----><br><table class="ctable"><tr><td>Bit</td><td>Name</td><td>Selection</td></tr><tr title="DMAEN is used to enable the internal clock for the Digital Memory Access"><td>0</td><td>DMAEN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr><tr><td>1</td><td>DAM2EN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr><tr title="SRAMEN is used to keep SRAM enabled in sleep mode."><td>2</td><td>SRAMEN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr><tr><td>4</td><td>FLITFEN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr><tr><td>6</td><td>CRCEN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr><tr title="IOPAEN is used to enable the internal clock for Peripheral A"><td>17</td><td>IOPAEN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr><tr title="IOPBEN is used to enable the internal clock for Peripheral B"><td>18</td><td>IOPBEN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr><tr title="IOPCEN is used to enable the internal clock for Peripheral C"><td>19</td><td>IOPCEN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr><tr title="IOPDEN is used to enable the internal clock for Peripheral D"><td>20</td><td>USART4RST</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr><tr title="IOPEEN is used to enable the internal clock for Peripheral E"><td>21</td><td>IOPEEN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr><tr title="IOPFEN is used to enable the internal clock for Peripheral F"><td>22</td><td>IOPFEN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr><tr><td>24</td><td>TSCEN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr></table></span></div>'
cAPB1ENR.content = [cAPB1ENRT]
cAPB1ENRT.content = '<div class="cT rcc">RCC: APB1ENR Configuration <span class="ctriangle">&#9654;</span><br><span class="cinfo">Select EN to Enable or DIS to Disable for the bits below. If you wish to leave a bit unchanged, leave the select blank.<!----><span class="cR"><br>This configuration requires two registers. <select><option>r0</option><option>r1</option><option>r2</option><option>r3</option><option>r4</option><option>r5</option><option>r6</option><option>r7</option><option>r8</option><option>r9</option><option>r10</option><option>r11</option><option>r12</option></select><select><option>r0</option><option>r1</option><option>r2</option><option>r3</option><option>r4</option><option>r5</option><option>r6</option><option>r7</option><option>r8</option><option>r9</option><option>r10</option><option>r11</option><option>r12</option></select></span><!----><br><table class="ctable"><tr><td>Bit</td><td>Name</td><td>Selection</td></tr><tr title="TIM2EN is used to enable the internal clock for Timer TIM2"><td>0</td><td>TIM2EN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr><tr title="TIM3EN is used to enable the internal clock for Timer TIM3"><td>1</td><td>TIM3EN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr><tr title="TIM6EN is used to enable the internal clock for Timer TIM6"><td>4</td><td>TIM6EN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr><tr title="TIM7EN is used to enable the internal clock for Timer TIM7"><td>5</td><td>TIM7EN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr><tr title="TIM14EN is used to enable the internal clock for Timer TIM14"><td>8</td><td>TIM14EN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr><tr><td>11</td><td>WWDGEN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr><tr title="SPI2EN is used to enable the internal clock for Serial Peripheral Interface SPI2"><td>14</td><td>SPI2EN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr><tr><td>17</td><td>USART2EN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr><tr><td>18</td><td>USART3EN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr><tr><td>19</td><td>USART4EN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr><tr><td>20</td><td>USART5EN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr><tr><td>21</td><td>I2C1EN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr><tr><td>22</td><td>I2C2EN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr><tr><td>23</td><td>USBEN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr><tr><td>25</td><td>CANEN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr><tr><td>27</td><td>CRSEN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr><tr><td>28</td><td>PWREN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr><tr title="DACEN is used to enable the internal clock for the Digital to Analog Converter"><td>29</td><td>DACEN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr><tr><td>30</td><td>CECEN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr></table></span></div>'
cAPB2ENR.content = [cAPB2ENRT]
cAPB2ENRT.content = '<div class="cT rcc">RCC: APB2ENR Configuration <span class="ctriangle">&#9654;</span><br><span class="cinfo">Select EN to Enable or DIS to Disable for the bits below. If you wish to leave a bit unchanged, leave the select blank.<!----><span class="cR"><br>This configuration requires two registers. <select><option>r0</option><option>r1</option><option>r2</option><option>r3</option><option>r4</option><option>r5</option><option>r6</option><option>r7</option><option>r8</option><option>r9</option><option>r10</option><option>r11</option><option>r12</option></select><select><option>r0</option><option>r1</option><option>r2</option><option>r3</option><option>r4</option><option>r5</option><option>r6</option><option>r7</option><option>r8</option><option>r9</option><option>r10</option><option>r11</option><option>r12</option></select></span><!----><br><table class="ctable"><tr><td>Bit</td><td>Name</td><td>Selection</td></tr><tr><td>0</td><td>SYSCFGCOMPEN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr><tr><td>5</td><td>USART6EN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr><tr><td>6</td><td>USART7EN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr><tr><td>7</td><td>USART8EN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr><tr title="ADCEN is used to enable the internal clock for the Analog to Digital Converter"><td>9</td><td>ADCEN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr><tr title="TIM1EN is used to enable the internal clock for Timer TIM1"><td>11</td><td>TIM1EN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr><tr title="SPI1EN is used to enable the internal clock for Serial Peripheral Interface SPI1"><td>12</td><td>SPI1EN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr><tr><td>14</td><td>USART1EN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr><tr title="TIM15EN is used to enable the internal clock for Timer TIM15"><td>16</td><td>TIM15EN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr><tr title="TIM16EN is used to enable the internal clock for Timer TIM16"><td>17</td><td>TIM16EN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr><tr title="TIM17EN is used to enable the internal clock for Timer TIM17"><td>18</td><td>TIM17EN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr><tr><td>22</td><td>DBGMCUEN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr></table></span></div>'
gpioT.content = 'GPIO Configuration'
cMODER.content = [cMODERT]
cMODERT.content = '<div class="cT gpio">GPIOx: MODER Configuration <span class="ctriangle">&#9654;</span><br><span class="cinfo">Select IN for Input, OUT for Output, ALT for Alternate Function Mode, or AM for Analog Mode for the bits below. If you wish to leave a bit unchanged, leave the select blank.<!----><span class="cSel"><br>Select the peripheral you wish to use. <select><option>GPIOA</option><option>GPIOB</option><option>GPIOC</option><option>GPIOD</option><option>GPIOE</option><option>GPIOF</option></select></span><!----><span class="cR"><br>This configuration requires two registers. <select><option>r0</option><option>r1</option><option>r2</option><option>r3</option><option>r4</option><option>r5</option><option>r6</option><option>r7</option><option>r8</option><option>r9</option><option>r10</option><option>r11</option><option>r12</option></select><select><option>r0</option><option>r1</option><option>r2</option><option>r3</option><option>r4</option><option>r5</option><option>r6</option><option>r7</option><option>r8</option><option>r9</option><option>r10</option><option>r11</option><option>r12</option></select></span><!----><br><table class="ctable"><tr><td>Bit</td><td>Name</td><td>Selection</td></tr><tr title="The Mode Register designates the I/O mode of each port."><td>1:0</td><td>MODER0</td><td><select><option></option><option>IN</option><option>OUT</option><option>ALT</option><option>AM</option></select></td></tr><tr title="The Mode Register designates the I/O mode of each port."><td>3:2</td><td>MODER1</td><td><select><option></option><option>IN</option><option>OUT</option><option>ALT</option><option>AM</option></select></td></tr><tr title="The Mode Register designates the I/O mode of each port."><td>5:4</td><td>MODER2</td><td><select><option></option><option>IN</option><option>OUT</option><option>ALT</option><option>AM</option></select></td></tr><tr title="The Mode Register designates the I/O mode of each port."><td>7:6</td><td>MODER3</td><td><select><option></option><option>IN</option><option>OUT</option><option>ALT</option><option>AM</option></select></td></tr><tr title="The Mode Register designates the I/O mode of each port."><td>9:8</td><td>MODER4</td><td><select><option></option><option>IN</option><option>OUT</option><option>ALT</option><option>AM</option></select></td></tr><tr title="The Mode Register designates the I/O mode of each port."><td>11:10</td><td>MODER5</td><td><select><option></option><option>IN</option><option>OUT</option><option>ALT</option><option>AM</option></select></td></tr><tr title="The Mode Register designates the I/O mode of each port."><td>13:12</td><td>MODER6</td><td><select><option></option><option>IN</option><option>OUT</option><option>ALT</option><option>AM</option></select></td></tr><tr title="The Mode Register designates the I/O mode of each port."><td>15:14</td><td>MODER7</td><td><select><option></option><option>IN</option><option>OUT</option><option>ALT</option><option>AM</option></select></td></tr><tr title="The Mode Register designates the I/O mode of each port."><td>17:16</td><td>MODER8</td><td><select><option></option><option>IN</option><option>OUT</option><option>ALT</option><option>AM</option></select></td></tr><tr title="The Mode Register designates the I/O mode of each port."><td>19:18</td><td>MODER9</td><td><select><option></option><option>IN</option><option>OUT</option><option>ALT</option><option>AM</option></select></td></tr><tr title="The Mode Register designates the I/O mode of each port."><td>21:20</td><td>MODER10</td><td><select><option></option><option>IN</option><option>OUT</option><option>ALT</option><option>AM</option></select></td></tr><tr title="The Mode Register designates the I/O mode of each port."><td>23:22</td><td>MODER11</td><td><select><option></option><option>IN</option><option>OUT</option><option>ALT</option><option>AM</option></select></td></tr><tr title="The Mode Register designates the I/O mode of each port."><td>25:24</td><td>MODER12</td><td><select><option></option><option>IN</option><option>OUT</option><option>ALT</option><option>AM</option></select></td></tr><tr title="The Mode Register designates the I/O mode of each port."><td>27:26</td><td>MODER13</td><td><select><option></option><option>IN</option><option>OUT</option><option>ALT</option><option>AM</option></select></td></tr><tr title="The Mode Register designates the I/O mode of each port."><td>29:28</td><td>MODER14</td><td><select><option></option><option>IN</option><option>OUT</option><option>ALT</option><option>AM</option></select></td></tr><tr title="The Mode Register designates the I/O mode of each port."><td>31:30</td><td>MODER15</td><td><select><option></option><option>IN</option><option>OUT</option><option>ALT</option><option>AM</option></select></td></tr></table></span></div>'
cPUPDR.content = [cPUPDRT]
cPUPDRT.content = '<div class="cT gpio">GPIOx: PUPDR Configuration <span class="ctriangle">&#9654;</span><br><span class="cinfo">Select PU for Pull Up, PD for Pull Down, or DIS to Disable for the bits below. If you wish to leave a bit unchanged, leave the select blank.<!----><span class="cSel"><br>Select the peripheral you wish to use. <select><option>GPIOA</option><option>GPIOB</option><option>GPIOC</option><option>GPIOD</option><option>GPIOE</option><option>GPIOF</option></select></span><!----><span class="cR"><br>This configuration requires two registers. <select><option>r0</option><option>r1</option><option>r2</option><option>r3</option><option>r4</option><option>r5</option><option>r6</option><option>r7</option><option>r8</option><option>r9</option><option>r10</option><option>r11</option><option>r12</option></select><select><option>r0</option><option>r1</option><option>r2</option><option>r3</option><option>r4</option><option>r5</option><option>r6</option><option>r7</option><option>r8</option><option>r9</option><option>r10</option><option>r11</option><option>r12</option></select></span><!----><br><table class="ctable"><tr><td>Bit</td><td>Name</td><td>Selection</td></tr><tr title="The Pull-Up/Pull-Down Register designates the I/O resistor state of each port."><td>1:0</td><td>PUPDR0</td><td><select><option></option><option>PU</option><option>PD</option><option>DIS</option></select></td></tr></tr><tr title="The Pull-Up/Pull-Down Register designates the I/O resistor state of each port."><td>3:2</td><td>PUPDR1</td><td><select><option></option><option>PU</option><option>PD</option><option>DIS</option></select></td></tr></tr><tr title="The Pull-Up/Pull-Down Register designates the I/O resistor state of each port."><td>5:4</td><td>PUPDR2</td><td><select><option></option><option>PU</option><option>PD</option><option>DIS</option></select></td></tr></tr><tr title="The Pull-Up/Pull-Down Register designates the I/O resistor state of each port."><td>7:6</td><td>PUPDR3</td><td><select><option></option><option>PU</option><option>PD</option><option>DIS</option></select></td></tr></tr><tr title="The Pull-Up/Pull-Down Register designates the I/O resistor state of each port."><td>9:8</td><td>PUPDR4</td><td><select><option></option><option>PU</option><option>PD</option><option>DIS</option></select></td></tr></tr><tr title="The Pull-Up/Pull-Down Register designates the I/O resistor state of each port."><td>11:10</td><td>PUPDR5</td><td><select><option></option><option>PU</option><option>PD</option><option>DIS</option></select></td></tr></tr><tr title="The Pull-Up/Pull-Down Register designates the I/O resistor state of each port."><td>13:12</td><td>PUPDR6</td><td><select><option></option><option>PU</option><option>PD</option><option>DIS</option></select></td></tr></tr><tr title="The Pull-Up/Pull-Down Register designates the I/O resistor state of each port."><td>15:14</td><td>PUPDR7</td><td><select><option></option><option>PU</option><option>PD</option><option>DIS</option></select></td></tr></tr><tr title="The Pull-Up/Pull-Down Register designates the I/O resistor state of each port."><td>17:16</td><td>PUPDR8</td><td><select><option></option><option>PU</option><option>PD</option><option>DIS</option></select></td></tr></tr><tr title="The Pull-Up/Pull-Down Register designates the I/O resistor state of each port."><td>19:18</td><td>PUPDR9</td><td><select><option></option><option>PU</option><option>PD</option><option>DIS</option></select></td></tr></tr><tr title="The Pull-Up/Pull-Down Register designates the I/O resistor state of each port."><td>21:20</td><td>PUPDR10</td><td><select><option></option><option>PU</option><option>PD</option><option>DIS</option></select></td></tr></tr><tr title="The Pull-Up/Pull-Down Register designates the I/O resistor state of each port."><td>23:22</td><td>PUPDR11</td><td><select><option></option><option>PU</option><option>PD</option><option>DIS</option></select></td></tr></tr><tr title="The Pull-Up/Pull-Down Register designates the I/O resistor state of each port."><td>25:24</td><td>PUPDR12</td><td><select><option></option><option>PU</option><option>PD</option><option>DIS</option></select></td></tr></tr><tr title="The Pull-Up/Pull-Down Register designates the I/O resistor state of each port."><td>27:26</td><td>PUPDR13</td><td><select><option></option><option>PU</option><option>PD</option><option>DIS</option></select></td></tr></tr><tr title="The Pull-Up/Pull-Down Register designates the I/O resistor state of each port."><td>29:28</td><td>PUPDR14</td><td><select><option></option><option>PU</option><option>PD</option><option>DIS</option></select></td></tr></tr><tr title="The Pull-Up/Pull-Down Register designates the I/O resistor state of each port."><td>31:30</td><td>PUPDR15</td><td><select><option></option><option>PU</option><option>PD</option><option>DIS</option></select></td></tr></table></span></div>'
cODR.content = [cODRT]
cODRT.content = '<div class="cT gpio">GPIOx: ODR Configuration <span class="ctriangle">&#9654;</span><br><span class="cinfo">Select EN to Enable or DIS to Disable for the bits below. If you wish to leave a bit unchanged, leave the select blank.<!----><span class="cSel"><br>Select the peripheral you wish to use. <select><option>GPIOA</option><option>GPIOB</option><option>GPIOC</option><option>GPIOD</option><option>GPIOE</option><option>GPIOF</option></select></span><!----><span class="cR"><br>This configuration requires two registers. <select><option>r0</option><option>r1</option><option>r2</option><option>r3</option><option>r4</option><option>r5</option><option>r6</option><option>r7</option><option>r8</option><option>r9</option><option>r10</option><option>r11</option><option>r12</option></select><select><option>r0</option><option>r1</option><option>r2</option><option>r3</option><option>r4</option><option>r5</option><option>r6</option><option>r7</option><option>r8</option><option>r9</option><option>r10</option><option>r11</option><option>r12</option></select></span><!----><br><table class="ctable"><tr><td>Bit</td><td>Name</td><td>Selection</td></tr><tr title="The Output Data Register designates the I/O output state of each port."><td>0</td><td>ODR0</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr></tr><tr title="The Output Data Register designates the I/O output state of each port."><td>1</td><td>ODR1</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr></tr><tr title="The Output Data Register designates the I/O output state of each port."><td>2</td><td>ODR2</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr></tr><tr title="The Output Data Register designates the I/O output state of each port."><td>3</td><td>ODR3</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr></tr><tr title="The Output Data Register designates the I/O output state of each port."><td>4</td><td>ODR4</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr></tr><tr title="The Output Data Register designates the I/O output state of each port."><td>5</td><td>ODR5</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr></tr><tr title="The Output Data Register designates the I/O output state of each port."><td>6</td><td>ODR6</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr></tr><tr title="The Output Data Register designates the I/O output state of each port."><td>7</td><td>ODR7</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr></tr><tr title="The Output Data Register designates the I/O output state of each port."><td>8</td><td>ODR8</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr></tr><tr title="The Output Data Register designates the I/O output state of each port."><td>9</td><td>ODR9</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr></tr><tr title="The Output Data Register designates the I/O output state of each port."><td>10</td><td>ODR10</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr></tr><tr title="The Output Data Register designates the I/O output state of each port."><td>11</td><td>ODR11</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr></tr><tr title="The Output Data Register designates the I/O output state of each port."><td>12</td><td>ODR12</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr></tr><tr title="The Output Data Register designates the I/O output state of each port."><td>13</td><td>ODR13</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr></tr><tr title="The Output Data Register designates the I/O output state of each port."><td>14</td><td>ODR14</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr></tr><tr title="The Output Data Register designates the I/O output state of each port."><td>15</td><td>ODR15</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr></tr></table></span></div>'
timerT.content = 'Timer Configuration'
cTIM1.content = [cTIM1T]
cTIM1T.content = '<div class="cT tim">TIM1 Configuration <span class="ctriangle">&#9654;</span><br><span class="cinfo">Select EN to Enable or DIS to Disable for the bits below. If you wish to leave a bit unchanged, leave the select blank.<!----><span class="cR"><br>This configuration requires two registers. <select><option>r0</option><option>r1</option><option>r2</option><option>r3</option><option>r4</option><option>r5</option><option>r6</option><option>r7</option><option>r8</option><option>r9</option><option>r10</option><option>r11</option><option>r12</option></select><select><option>r0</option><option>r1</option><option>r2</option><option>r3</option><option>r4</option><option>r5</option><option>r6</option><option>r7</option><option>r8</option><option>r9</option><option>r10</option><option>r11</option><option>r12</option></select></span><!----><span class="cVals" style="color: black"><br>PSC: <input></input><br>ARR: <input></input></span><br>TIM1 CR1 & CR2 Control Register<table class="ctable"><tr><td>Bit</td><td>Name</td><td>Selection</td></tr><tr title="The Counter Enable state enables the counter to start counting. This bit should be set after the output configurations have been set."><td>CR1.0</td><td>CEN</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr></tr><tr title="The Update Disable state disables the update event on counter overflow/underflow when enabled."><td>CR1.1</td><td>UDIS</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr></tr><tr><td>CR1.2</td><td>URS</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr></tr><tr><td>CR1.3</td><td>OPM</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr></tr><tr title="The counter counts as an Upcounter when the Direction state is Disabled and a Downcounter when the Direction state is Enabled"><td>CR1.4</td><td>DIR</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr></tr><tr title="The Center-Aligned Mode Selection determines the counting configuration. Select EDG for Edge-Mode, where the counter counts as selected by DIR. Select CM1, CM2, or CM3 for Alternating Up-Down Counting, where output compare interrupt flags are set when counting down, counting up, or both, respectively."><td>CR1.6:5</td><td>CMS</td><td><select><option></option><option>EDG</option><option>CM1</option><option>CM2</option><option>CM3</option></select></td></tr></tr><tr><td>CR1.7</td><td>ARPE</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr></tr><tr><td>CR1.9:8</td><td>CKD</td><td><select><option></option><option>00</option><option>01</option><option>10</option></select></td></tr></tr><tr><td>CR2.0</td><td>CCPC</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr></tr><tr><td>CR2.2</td><td>CCUS</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr></tr><tr><td>CR2.3</td><td>CCDS</td><td><select><option></option><option>EN</option><option>DIS</option></select></td></tr></tr></table></span></div>'
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
gpioT.cl = "ctitle"
cMODER.cl = "c"
cMODER.background_color = ""
cMODER.id = "gpioMODER"
cPUPDR.cl = "c"
cPUPDR.background_color = ""
cPUPDR.id = "gpioPUPDR"
cODR.cl = "c"
cODR.background_color = ""
cODR.id = "gpioODR"
timerT.cl = "ctitle"
cTIM1.cl = "c"
cTIM1.background_color = ""
cTIM1.id = "tim1"
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