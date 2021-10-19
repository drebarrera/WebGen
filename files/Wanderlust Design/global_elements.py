import modules as mx
nav = mx.Nav()
menu = mx.Menu()
navp = mx.T()
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