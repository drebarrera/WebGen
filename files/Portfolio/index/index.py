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
redTrack2 = mx.Image()
blueTrack = mx.Image()
yellowTrack = mx.Image()
trackMergeBY = mx.Image()
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
slide3 = mx.C()
slide3Textbox1 = mx.C()
slide3Title1 = mx.T()
slide3Text1 = mx.T()
slide3Textbox2 = mx.C()
slide3Title2 = mx.T()
slide3Text2 = mx.T()
slide4 = mx.C()
slide4Textbox1 = mx.C()
slide4Title1 = mx.T()
slide4Text1 = mx.T()
slide4Textbox2 = mx.C()
slide4Title2 = mx.T()
slide4Text2 = mx.T()
slide4Textbox3 = mx.C()
slide4Title3 = mx.T()
slide4Text3 = mx.T()
slide5 = mx.C()
slide5Textbox1 = mx.C()
slide5Title1 = mx.T()
slide5Text1 = mx.T()
slide5Textbox2 = mx.C()
slide5Title2 = mx.T()
slide5Text2 = mx.T()
slide6 = mx.C()
slide6Textbox1 = mx.C()
slide6Title1 = mx.T()
slide6Text1 = mx.T()
slide6Textbox2 = mx.C()
slide6Title2 = mx.T()
slide6Text2 = mx.T()
slide6Textbox3 = mx.C()
slide6Title3 = mx.T()
slide6Text3 = mx.T()
slide7 = mx.C()
slide7Textbox1 = mx.C()
slide7Title1 = mx.T()
slide7Text1 = mx.T()
slide7Textbox2 = mx.C()
slide7Title2 = mx.T()
slide7Text2 = mx.T()

### CONTENT ###
# Body
body.content = [center]

# Center
center.content = [main, alert]

# Alert
alert.content = [alertText]

# Main
main.content = [slide1, slide2, slide3, slide4, slide5, slide6, slide7, mainLayer0]

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
slide1Text.content = 'My name is Andr&eacute;s Barrera, but you can call me Dre. I am a Computer Engineering senior at <a href="https://www.purdue.edu" target="_blank" class="textLink">Purdue University</a>. With a background in <span class="pseudoLink">Multidisciplinary Engineering</span>, <span class="pseudoLink">UI/UX</span>, and <span class="pseudoLink">Business Development</span>, I am much more than just a Computer Engineer.<br><br><span style="font-weight: 500;text-align: center; width:100%; display: block;">I am an ambitious creator.</span>'
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

# Slide 3
slide3.content = [redTrack2, trackMergeBY, slide3Textbox1,slide3Textbox2]
slide3Textbox1.content = [slide3Title1,slide3Text1]
slide3Title1.content = 'My Curiosity'
slide3Text1.content = 'Upon writing this, I was initially going to call this section of my portfolio "My Interests". But I thought that "My Curiosity" is a much more fitting title, as a curiosity expresses one&#39s eagerness to learn and explore.<br><br>I am curious of just about everything. You will often find me <span class="pseudoLink">creating something innovative or new</span>, <span class="pseudoLink">speaking a new language</span>, or <span class="pseudoLink">analyzing the world around me and my place within it</span>. These are pretty broad topics, so here is a list of some of my more specific passions:<br><ol style="color: #005580; text-align: left; margin-left: 75px;font-weight: 300; font-size: 2.5vh;line-height: 1.2;margin-top: 1vh;"><li>Writing and Producing Music</li><li>Green Engineering Paper</li><li>Organizing and Optimizing</li><li>Warm Espresso</li><li>Project Management</li><li>Summiting Mountains</li><li>Exploring New Cities</li></ol></span>'
slide3Textbox2.content = [slide3Title2,slide3Text2]
slide3Title2.content = 'UI/UX Design'
slide3Text2.content = 'Whether a software or hardware design problem, I am always excited to put my UI and UX skills to the test. For the last nine years, I have worked to develop my UI skills with website and product design. When it comes to UX, I am very keen to gather data and analyze the user mindset.<br>A list of my most recent UI/UX projects can be found below:'

# Slide 4
slide4.content = [redTrack, blueTrack, yellowTrack, slide4Textbox1, slide4Textbox2, slide4Textbox3]
slide4Textbox1.content = [slide4Title1, slide4Text1]
slide4Title1.content = 'My Creative Process'
slide4Text1.content = 'My creative process usually starts with a sheet of green engineering paper and a mug of warm green tea.'
slide4Textbox2.content = [slide4Title2, slide4Text2]
slide4Title2.content = 'Data Processing and Algorithms'
slide4Text2.content = 'I am very fond of using data to ...'
slide4Textbox3.content = [slide4Title3, slide4Text3]
slide4Title3.content = 'Music Production'
slide4Text3.content = 'Ever I was three years old, music has perpetuated my life...'

# Slide 5
slide5.content = [redTrack2, trackMergeBY, slide5Textbox1,slide5Textbox2]
slide5Textbox1.content = [slide5Title1,slide5Text1]
slide5Title1.content = 'My Identity'
slide5Text1.content = 'A person&#39s identity is important, not because it determines the expectations of who they should be, but becuase it helps us understand how they fit within our world. I am a Latino of Dominican and Mexican descent with an open-minded, yet ever-callibrating view of the world. I was raised by a military family and taught by my immigrant father to never squander oppertunity and by my mother to be compassionate and conscious. I am goal-oriented and incrediby ambitious. Nomadic by nature, I am never hesitant to travel or explore new ideas.<br><br>My motto: Life is a choice we make everyday.<br><br>This phrase becomes ever clearer when faced with difficulty and strife. Embracing it, I never shy away from a challenge.'
slide5Textbox2.content = [slide5Title2,slide5Text2]
slide5Title2.content = 'Business and Entrepeneurship'
slide5Text2.content = 'I am an entrepeneur by heart. With technical training from the <a href="https://purduefoundry.com/" target="_blank" class="textLink2">Purdue University Foundry</a> and pracitce with many business building opportunities, I am notorious for taking leadership and being excited to take on innovative challenges in industry.'

# Slide 6
slide6.content = [redTrack, blueTrack, yellowTrack, slide6Textbox1, slide6Textbox2, slide6Textbox3]
slide6Textbox1.content = [slide6Title1, slide6Text1]
slide6Title1.content = 'My Travels'
slide6Text1.content = 'I am not your average traveller. When I decide to venture into the unknown, I like to pack light and... I often travel to visit art galleries, '
slide6Textbox2.content = [slide6Title2, slide6Text2]
slide6Title2.content = 'Mechanical Engineering and Manufacturing'
slide6Text2.content = 'Experience with MechE...'
slide6Textbox3.content = [slide6Title3, slide6Text3]
slide6Title3.content = 'Art and Cinematography'
slide6Text3.content = 'Ever I was three years old, music has perpetuated my life...'

# Slide 7
slide7.content = [redTrack2, trackMergeBY, slide7Textbox1,slide7Textbox2]
slide7Textbox1.content = [slide7Title1,slide7Text1]
slide7Title1.content = 'Why Trains?'
slide7Text1.content = 'When I was a child...'
slide7Textbox2.content = [slide7Title2,slide7Text2]
slide7Title2.content = 'Computer Aided Design'
slide7Text2.content = 'Experience with Solidworks...'

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
redTrack2.id = 'redTrack'
redTrack2.background_color = ''
redTrack2.cl = 'trackSlide track1'
redTrack2.src = "images/slides_trackRed2.png"
blueTrack.id = 'blueTrack'
blueTrack.background_color = ''
blueTrack.cl = 'trackSlide track2'
blueTrack.src = "images/slides_trackBlue.png"
yellowTrack.id = 'yellowTrack'
yellowTrack.background_color = ''
yellowTrack.cl = 'trackSlide track3'
yellowTrack.src = "images/slides_trackYellow.png"
trackMergeBY.id = 'trackMergeBY'
trackMergeBY.background_color = ''
trackMergeBY.cl = 'trackSlide track2'
trackMergeBY.src = "images/slides_trackMergeBY.png"

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

# Slide 3
slide3.background_color = '#fefefe'
slide3.id = 'slide3'
slide3.cl = 'slide'
slide3Textbox1.id = 'slide3TextboxRed'
slide3Textbox1.cl = 'textboxSlide'
slide3Textbox1.background_color = ''
slide3Title1.type = 'h6'
slide3Title1.color = '#ff5938'
slide3Title1.cl = 'slideTitle'
slide3Text1.cl = 'slideText'
slide3Textbox2.id = 'slide3TextboxBlue'
slide3Textbox2.cl = 'textboxSlide'
slide3Textbox2.background_color = ''
slide3Title2.type = 'h6'
slide3Title2.color = '#006497'
slide3Title2.cl = 'slideTitle'
slide3Text2.cl = 'slideText'

# Slide 4
slide4.background_color = '#fefefe'
slide4.id = 'slide4'
slide4.cl = 'slide'
slide4Textbox1.id = 'slide4TextboxRed'
slide4Textbox1.cl = 'textboxSlide'
slide4Textbox1.background_color = ''
slide4Title1.type = 'h6'
slide4Title1.color = '#ff5938'
slide4Title1.cl = 'slideTitle'
slide4Text1.cl = 'slideText'
slide4Textbox2.id = 'slide4TextboxBlue'
slide4Textbox2.cl = 'textboxSlide'
slide4Textbox2.background_color = ''
slide4Title2.type = 'h6'
slide4Title2.color = '#006497'
slide4Title2.cl = 'slideTitle'
slide4Text2.cl = 'slideText'
slide4Textbox3.id = 'slide4TextboxYellow'
slide4Textbox3.cl = 'textboxSlide'
slide4Textbox3.background_color = ''
slide4Title3.type = 'h6'
slide4Title3.color = '#ffba00'
slide4Title3.cl = 'slideTitle'
slide4Text3.cl = 'slideText'

# Slide 5
slide5.background_color = '#fefefe'
slide5.id = 'slide5'
slide5.cl = 'slide'
slide5Textbox1.id = 'slide5TextboxRed'
slide5Textbox1.cl = 'textboxSlide'
slide5Textbox1.background_color = ''
slide5Title1.type = 'h6'
slide5Title1.color = '#ff5938'
slide5Title1.cl = 'slideTitle'
slide5Text1.cl = 'slideText'
slide5Textbox2.id = 'slide5TextboxBlue'
slide5Textbox2.cl = 'textboxSlide'
slide5Textbox2.background_color = ''
slide5Title2.type = 'h6'
slide5Title2.color = '#006497'
slide5Title2.cl = 'slideTitle'
slide5Text2.cl = 'slideText'

# Slide 6
slide6.background_color = '#fefefe'
slide6.id = 'slide6'
slide6.cl = 'slide'
slide6Textbox1.id = 'slide6TextboxRed'
slide6Textbox1.cl = 'textboxSlide'
slide6Textbox1.background_color = ''
slide6Title1.type = 'h6'
slide6Title1.color = '#ff5938'
slide6Title1.cl = 'slideTitle'
slide6Text1.cl = 'slideText'
slide6Textbox2.id = 'slide6TextboxBlue'
slide6Textbox2.cl = 'textboxSlide'
slide6Textbox2.background_color = ''
slide6Title2.type = 'h6'
slide6Title2.color = '#006497'
slide6Title2.cl = 'slideTitle'
slide6Text2.cl = 'slideText'
slide6Textbox3.id = 'slide6TextboxYellow'
slide6Textbox3.cl = 'textboxSlide'
slide6Textbox3.background_color = ''
slide6Title3.type = 'h6'
slide6Title3.color = '#ffba00'
slide6Title3.cl = 'slideTitle'
slide6Text3.cl = 'slideText'

# Slide 7
slide7.background_color = '#fefefe'
slide7.id = 'slide7'
slide7.cl = 'slide'
slide7Textbox1.id = 'slide7TextboxRed'
slide7Textbox1.cl = 'textboxSlide'
slide7Textbox1.background_color = ''
slide7Title1.type = 'h6'
slide7Title1.color = '#ff5938'
slide7Title1.cl = 'slideTitle'
slide7Text1.cl = 'slideText'
slide7Textbox2.id = 'slide7TextboxBlue'
slide7Textbox2.cl = 'textboxSlide'
slide7Textbox2.background_color = ''
slide7Title2.type = 'h6'
slide7Title2.color = '#006497'
slide7Title2.cl = 'slideTitle'
slide7Text2.cl = 'slideText'