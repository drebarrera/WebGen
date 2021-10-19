import modules as mx
data = mx.Data()
body = mx.Body()
nav = mx.Nav()
menu = mx.Menu()
navp = mx.T()
vc = mx.C()
v = mx.Video()
mtc = mx.C()
menutable = mx.Table()
mblank1 = mx.T()
mblank2 = mx.T()
mclose = mx.Icon()
mimgC1 = mx.C()
mimgC2 = mx.C()
mimgC3 = mx.C()
mimg1 = mx.Image()
mimg2 = mx.C()
mimg3 = mx.C()
mopt1 = mx.T()
mopt2 = mx.T()
mopt3 = mx.T()
win2 = mx.C()
dreamsc = mx.Table()
dreamst1 = mx.T()
dreamst2 = mx.T()
projectsc = mx.C()
projectsf1 = mx.C()
projectsf2 = mx.C()
projectsf3 = mx.C()
blinkc = mx.C()
pimgC1 = mx.C()
pimg1 = mx.C()
popt1 = mx.T()
pbuttont = mx.T()
pbutton = mx.C()
pbtext = mx.T()
blink = mx.C()
win3 = mx.C()

#- Data
data.title = "Wanderlust Design | Welcome"
data.keywords = ["wanderlust","design","graphic","webiste","videography","production","audio"]
data.author = "Andres Barrera"

#- NavBar
menu.radius = "0"
menu.length = "20"
menu.width = "2"
menu.id = "menuicon"
nav.background_color = "rgba(0,0,0,0.7)"
navp.content = "<i style='font-weight:300'>WANDERLUST</i> DESIGN"
navp.font_weight = "normal"
navp.type = "h1"
navp.color = "white"
navp.padding_left = "25px"
menu.color = "white"
nav.content = [[navp, menu]]
nav.id = "navbar"
nav.position = "fixed"
nav.tableid = "navt"

#- Video
v.src = "/Users/drebarrera/Desktop/supporting/promo_video.mp4"
v.id = "vid"
vc.content = [v]
vc.id="video_cont"
vc.overflow_y = "hidden"
v.loop = "True"
v.autoplay = "True"

#- Menu
mopt1.content = "MISSION"
mopt2.content = "PORTFOLIO"
mopt3.content = "CONTACT"
menutable.content = [[mblank1, mblank2, mclose],[mimgC2, mimgC1, mimgC3],[mopt2, mopt1, mopt3]]
mimgC1.content = [mimg1]
mimgC2.content = [mimg2]
mimgC3.content = [mimg3]
mimgC1.cl = "mimgC"
mimgC2.cl = "mimgC"
mimgC3.cl = "mimgC"
mimgC1.background_color = mimgC2.background_color = mimgC3.background_color = ""
menutable.background_color = "rgba(255,255,255,0.85)"
menutable.id = "mt"
mtc.id = "mtc"
mtc.content = [menutable]
menutable.color = "black"
menutable.position = "absolute"
mtc.position = "fixed"
mtc.z_index = "6"
mtc.background_color = ""
mtc.display = "none"
mtc.justify_content = "center"
menutable.text_align = "center"
menutable.border_radius = "20px"
mclose.type = "x"
mclose.size = "16"
mclose.width = "1.5"
mclose.id = "closeicon"
mimg1.src = "/Users/drebarrera/Desktop/supporting/logo.png"
mimg1.id = "mimg1"
mimg2.background_image = "url('/Users/drebarrera/Desktop/supporting/portfolio.jpg')"
mimg2.id = "mimg2"
mimg3.background_image = "url('/Users/drebarrera/Desktop/supporting/contact.jpg')"
mimg3.id = "mimg3"

#- Window 2
win2.id = "win2"
win2.background_color = "white"
dreamsc.id = "dreamsc"
dreamsc.background_color = ""
dreamsc.text_align = "left"
dreamst1.content = "YOUR DREAMS"
dreamst2.content = "ARE OUR REALITY"
dreamst2.text_align="center"
dreamst1.font_family = dreamst2.font_family = "Helvetica"
dreamst1.color = dreamst2.color = "rgba(240,240,240,1)"
dreamsc.content = [[dreamst1], [dreamst2]]
projectsc.id = "projectsc"
projectsc.background_color = ""
projectsf1.border = "20px solid rgba(70,70,70,1)"
projectsf1.border_radius = "50px";
projectsf2.border_left = projectsf2.border_right = projectsf3.border_top = projectsf3.border_bottom = "20px solid rgba(255,255,255,1)"
projectsf1.id = "pf1"
projectsf2.id = "pf2"
projectsf3.id = "pf3"
projectsf3.background_color = projectsf2.background_color = projectsf1.background_color = "rgba(255,255,255,1)"
blinkc.id = "blinkc"
blinkc.background_color = "rgba(255,255,255,1)"
pimgC1.content = [pimg1]
pimgC1.cl = "pimgC"
pimgC1.background_color = ""
pimg1.background_color = ""
pimg1.background_image = "url('/Users/drebarrera/Desktop/supporting/reel.png')"
pimg1.id = "pimg1"
popt1.content = "Audiovisual"
popt1.color = "white"
pbutton.background_color = "" #"rgba(220,220,220,1)"
pbutton.id = "pbutton"
pbutton.border_bottom = "2px solid rgba(200,200,200,1)"
pbuttont.content = "limitless videography, audio, graphic, and website design..."
pbuttont.id = "pbuttont"
pbtext.content = "Contact Us"
pbtext.color = "rgba(70,70,70,1)"
pbutton.content = [pbtext]
blinkc.content = [pbuttont, pbutton, blink]
blink.background_color = ""
blink.background_image = "url('/Users/drebarrera/Desktop/supporting/blink.png')"
blink.id = "blink"
projectsc.content = [projectsf1, projectsf2, projectsf3, blinkc]
win2.content = [dreamsc, projectsc]


win3.id = "win3"
#win3.background_color = ""

#-
body.content = [nav, vc, mtc, win2, win3]
body.background_color = "rgba(35,35,35,1)"