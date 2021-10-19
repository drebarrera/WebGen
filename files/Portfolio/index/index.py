import modules as mx
import sys
from prop import *
info = info()
data = mx.Data()
body = mx.Body()

### INFO ###
data.title = 'Dre Barrera'
data.author = 'Andres Barrera'

### OBJECTS ###
alert = mx.C()
alertText = mx.T()
center = mx.C()
main = mx.C()
mainLayer0 = mx.C()
trackRedMain = mx.Image()
trackBlueMain = mx.Image()
trackYellowMain = mx.Image()
trackPurpleMain = mx.Image()
trackLabelMain = mx.T()
trainRedMain = mx.Image()
trainBlueMain = mx.Image()
trainYellowMain = mx.Image()
trainPurpleMain = mx.Image()
mainClouds = mx.C()
mainLayerZ = mx.C()
mainText = mx.C()
mainTitle = mx.T()
mainSubtitle = mx.T()
mainInstructions = mx.T()
trackMergeAll = mx.Image()
redTrack = mx.Image()
blueTrack = mx.Image()
yellowTrack = mx.Image()
slide1 = mx.C()
slide1Textbox = mx.C()
slide1Title = mx.T()
slide1Text = mx.T()
slide1ResumeA = mx.Link()
slide1ResumeT = mx.T()
slide1ContactA = mx.Link()
slide1ContactT = mx.T()
slide1Image = mx.Image()
slide2 = mx.C()
slide2Textbox1 = mx.C()
slide2Title1 = mx.T()
slide2Text1 = mx.T()
slide2Textbox2 = mx.C()
slide2Title2 = mx.T()
slide2Text2 = mx.T()
slide2Textbox3 = mx.C()
slide2Title3 = mx.T()
slide2Text3 = mx.T()


### CONTENT ###
# Body
body.content = [center]

# Center
center.content = [main, alert]

# Alert
alert.content = [alertText]

# Main
main.content = [slide1, slide2, mainLayer0]

# Main Layer 0
mainLayer0.content = [trackRedMain, trackBlueMain, trackYellowMain, trackPurpleMain, trainRedMain, trainBlueMain, trainYellowMain, trainPurpleMain, trackLabelMain,  mainLayerZ, mainClouds, mainText]
mainText.content = [mainTitle, mainSubtitle, mainInstructions]
mainTitle.content = 'dre barrera'
mainSubtitle.content = 'Ambition. Innovation. Dedication.'
mainInstructions.content = 'Welcome! Choose a track and then press <span style="padding: 0.8vh; padding-left: 3.25%; padding-right: 3.25%; border-radius: 5px; cursor: pointer;">Start!</span> to begin.'

# Slide 1
slide1.content = [trackMergeAll, slide1Textbox]
slide1Textbox.content = [slide1Title, slide1Image, slide1Text, slide1ContactA, slide1ResumeA]
slide1Title.content = 'hello world.'
slide1Text.content = 'My name is Andrés Barrera, but you can call me Dre. I am a Computer Engineering senior at <a href="https://www.purdue.edu" target="_blank" class="textLink">Purdue University</a>. With a background in <span class="pseudoLink">Multidisciplinary Engineering</span>, <span class="pseudoLink">UI/UX</span>, and <span class="pseudoLink">Business Development</span>, I am much more than just a Computer Engineer.<br><br><span style="font-weight: 500;text-align: center; width:100%; display: block;">I am an ambitious creator.</span>'
slide1ResumeA.content = [slide1ResumeT]
slide1ResumeT.content = 'My Resume'
slide1ContactA.content = [slide1ContactT]
slide1ContactT.content = 'Contact Me'

# Slide 2
slide2.content = [redTrack, blueTrack, yellowTrack, slide2Textbox1, slide2Textbox2, slide2Textbox3]
slide2Textbox1.content = [slide2Title1, slide2Text1]
slide2Title1.content = 'My Skills'
slide2Text1.content = 'My skills are not confined to my field or degree, but are the culmination of my experiences. I am very ambitious - almost to a fault. Having graduated high school at 16, I have always found myself to be the youngest in the room. But through perserverance, trial and error, and continuous learning, I grow everyday.<br><br><span style="margin-left:30px;"><span style="font-weight: 500; font-size: 2.75vh;">What I Bring to the Team</span><ul style="color: #005580; text-align: left; margin-left: 75px;font-weight: 300; font-size: 2.5vh;line-height: 1.2;margin-top: 1vh;"><li>Ambitious Undertaker</li><li>Goal Setter / Self Starter</li><li>Natural Leader</li><li>Diligent Organizer</li><li>Jack of All Trades</li></ul></span>'
slide2Textbox2.content = [slide2Title2, slide2Text2]
slide2Title2.content = 'Circuit Design'
slide2Text2.content = 'As a Computer Engineer, I have been formally trained to understand the fundamentals of electricity, analog and digial hardware design, and the connection between the physical and digital world. I have applied my skills in this field to a number of projects, both in an educational and professional landscape.<br><br><span style="font-weight: 500; font-size: 2.75vh;">Circuit Design Projects</span><br><ul style="color: #005580; font-weight: 300; font-size: 2.0vh;margin-block-start: 0em; margin-block-end: 0em; margin-top: 0.25vh;text-align: left;width: 100%;margin-left: 25px;"><li>Geoamperic Interpreter (Device / PCB Design and Industrial Application, 2021)</li><li>Optical Heart Rate Sensor Design (Device / Circuit Design With Analog and Digital Output, 2021)</li></ul><br><span style="font-weight: 500; font-size: 2.75vh; text-align: left;width: 100%;margin-left: 25px;">Related Coursework</span><br><ul style="color: #005580; font-weight: 300; font-size: 2.0vh; margin-block-start: 0em; margin-block-end: 0em; margin-top: 0.25vh;margin-left: 25px;"><li><a href="https://engineering.purdue.edu/ECE/Academics/Undergraduates/UGO/CourseInfo/courseInfo?courseid=725&show=true&type=undergrad" target="_blank" class="textLink2">Purdue University ECE - Electrical Engineering Fundamentals I and II</a></li><li><a href="https://engineering.purdue.edu/ECE/Academics/Undergraduates/UGO/CourseInfo/courseInfo?courseid=607&show=true&type=undergrad" target="_blank" class="textLink2">Purdue University ECE 270 - Introduction to Digital Logic Design</a></li><li><a href="https://engineering.purdue.edu/ECE/Academics/Undergraduates/UGO/CourseInfo/courseInfo?courseid=612&show=true&type=undergrad" target="_blank" class="textLink2">Purdue University ECE 362 - Microprocessor Systems and Interfacing</a></li></ul><br><a style="font-size: 1; text-decoration: underline; width: 100%; text-align: center; display: block;" class="textLink3">Full Curriculum</a>'
slide2Textbox3.content = [slide2Title3, slide2Text3]
slide2Title3.content = 'Graphic Design'
slide2Text3.content = 'For the last eight years, I have honed my visual design skills to create eye-catching marketing media, infographics, and creative designs. Capable of creating in <span style="color:#005580;">Adobe Photoshop</span>, <span style="color:#005580;">Lightroom</span>, <span class="pseudoLink">AutoCAD</span>, and <span class="pseudoLink">Solidworks</span>, as well as other creative software platforms, I find myself producing beautiful products in both the professional and artistic realms. <br><br><br><a style="font-size: 1; text-decoration: underline; width: 100%; text-align: center; display: block;" class="textLink">VISIT THE GALLERY</a>'

### PROPERTIES ###
# Body
body.background_color = '#fefefe'

# Center
center.display = 'flex'
center.justify_content = 'center'
center.background_color = 'white'
center.background_color = '#242323'

# Alert
alert.id = 'alert'
alert.background_color = 'rgba(255, 255, 255, 0.9)'
alertText.id = 'alertText'

# Main
main.id = 'main'
main.display = 'flex'
main.justify_content = 'center'
main.background_color = '#efefef'
mainLayer0.background_color = '#efefef'
mainLayer0.id = 'mainLayer0'
trackRedMain.id = 'trackRedMain'
trackRedMain.cl = 'trackMain'
trackRedMain.src = "images/main_trackRed.png"
trackBlueMain.id = 'trackBlueMain'
trackBlueMain.cl = 'trackMain'
trackBlueMain.src = "images/main_trackBlue.png"
trackYellowMain.id = 'trackYellowMain'
trackYellowMain.cl = 'trackMain'
trackYellowMain.src = "images/main_trackYellow.png"
trackPurpleMain.id = 'trackPurpleMain'
trackPurpleMain.cl = 'trackMain'
trackPurpleMain.src = "images/main_trackPurple.png"
trackLabelMain.id = 'trackLabelMain'
trainRedMain.id = 'trainRedMain'
trainRedMain.cl = 'trainMain'
trainRedMain.src = "images/red_train.png"
trainBlueMain.id = 'trainBlueMain'
trainBlueMain.cl = 'trainMain'
trainBlueMain.src = "images/blue_train.png"
trainYellowMain.id = 'trainYellowMain'
trainYellowMain.cl = 'trainMain'
trainYellowMain.src = "images/yellow_train.png"
trainPurpleMain.id = 'trainPurpleMain'
trainPurpleMain.cl = 'trainMain'
trainPurpleMain.src = "images/purple_train.png"
mainLayerZ.background_color = ''
mainLayerZ.id = 'mainLayerZ'
mainClouds.background_color = ''
mainClouds.id = 'mainClouds'
mainText.id = 'mainText'
mainText.background_color = ''
mainTitle.id = 'mainTitle'
mainTitle.type = 'h1'
mainSubtitle.id = 'mainSubtitle'
mainSubtitle.type = 'h3'
mainInstructions.id = 'mainInstructions'

# Tracks
trackMergeAll.id = 'trackMergeAll'
trackMergeAll.background_color = ''
trackMergeAll.cl = 'trackSlide track1'
trackMergeAll.src = "images/slides_trackMergeAll.png"
redTrack.id = 'redTrack'
redTrack.background_color = ''
redTrack.cl = 'trackSlide track1'
redTrack.src = "images/slides_trackRed.png"
blueTrack.id = 'blueTrack'
blueTrack.background_color = ''
blueTrack.cl = 'trackSlide track2'
blueTrack.src = "images/slides_trackBlue.png"
yellowTrack.id = 'yellowTrack'
yellowTrack.background_color = ''
yellowTrack.cl = 'trackSlide track3'
yellowTrack.src = "images/slides_trackYellow.png"

# Slide 1
slide1.background_color = '#fefefe'
slide1.id = 'slide1'
slide1.cl = 'slide'
slide1Textbox.id = 'slide1Textbox' #
slide1Textbox.cl = 'textboxSlide'
slide1Textbox.background_color = ''
slide1Image.id = 'slide1Image'
slide1Image.src = "images/portrait.jpeg"
slide1Title.type = 'h6'
slide1Title.color = '#ff5938'
slide1Title.cl = 'slideTitle'
slide1Text.cl = 'slideText'
slide1ResumeA.id = 'resumeLink'
slide1ResumeA.cl = 'slideButton1'
slide1ResumeA.target = '_blank'
slide1ResumeA.src = 'https://www.google.com'
slide1ContactA.id = 'contactLink'
slide1ContactA.cl = 'slideButton2'
slide1ContactA.target = '_blank'
slide1ContactA.src = 'https://www.google.com'

# Slide 2
slide2.background_color = '#fefefe'
slide2.id = 'slide2'
slide2.cl = 'slide'
slide2Textbox1.id = 'slide2TextboxRed'
slide2Textbox1.cl = 'textboxSlide'
slide2Textbox1.background_color = ''
slide2Title1.type = 'h6'
slide2Title1.color = '#ff5938'
slide2Title1.cl = 'slideTitle'
slide2Text1.cl = 'slideText'
slide2Textbox2.id = 'slide2TextboxBlue'
slide2Textbox2.cl = 'textboxSlide'
slide2Textbox2.background_color = ''
slide2Title2.type = 'h6'
slide2Title2.color = '#006497'
slide2Title2.cl = 'slideTitle'
slide2Text2.cl = 'slideText'
slide2Textbox3.id = 'slide2TextboxYellow'
slide2Textbox3.cl = 'textboxSlide'
slide2Textbox3.background_color = ''
slide2Title3.type = 'h6'
slide2Title3.color = '#ffba00'
slide2Title3.cl = 'slideTitle'
slide2Text3.cl = 'slideText'
