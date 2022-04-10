import sys
inadmissible = ["type", "id", "cl", "onclick", "onhover", "target", "content", "name", "rows", "cols", "font_size", "height", "width", "margin", "margin_left", "margin_right", "margin_top", "margin_bottom", "src", "autoplay", "muted", "controls", "loop"]
dynamic = ["font_size", "height", "width", "margin", "margin_left", "margin_right", "margin_top", "margin_bottom"]

# Data -> Webpage Header Data
class Data:
    def __init__(self):
        self.name = "header_data"
        self.title = "Default Page"
        self.charset = "utf-8"
        self.description = "Default WebGen Page"
        self.keywords = []
        self.author = "Andres Barrera"
        self.viewport = "width=device-width, initial-scale=1"
        self.jquery_script = True
        self.jquery_ui_script = True
        self.scripts = []
            
    def c(self):
        title = '<title>'+self.title+'</title>'
        charset = '<meta charset="'+self.charset+'">'
        description = '<meta name="description" content="'+self.description+'">'
        keywords = '<meta name="keywords" content="'+','.join(self.keywords)+'">'
        author = '<meta name="author" content="'+self.author+'">'
        viewport = '<meta name="viewport" content="'+self.viewport+'">'
        return "".join([title,charset,description,keywords,author,viewport])
        
# Body -> Body Properties
class Body:
    def __init__(self):
        self.name = "body_properties"
        self.background_color = "white"
        self.overflow_x = "hidden"
        self.font_family = "Helvetica"
        self.color = "black"
        self.content = []
    
    def c(self,inadmissible, dynamic):
        content = [i.c(inadmissible, dynamic) for i in self.content]
        [print("Dynamic elements should be written in css. Enter css to fix.\nERROR: "+self.name+":"+p) for p, v in vars(self).items() if p in dynamic]
        return '<body style="margin:0;'+"".join([(p.replace("var__","--").replace("_","-")+":"+getattr(self, p))+";" for p, v in vars(self).items() if (p not in inadmissible and getattr(self, p) != "")])+'">'+"".join(content)+'</body>'

# T -> Text
class T:
    def __init__(self):
        self.name = "text"
        self.type = "p"
        self.id = ""
        self.cl = ""
        self.content = ""

    def c(self,inadmissible, dynamic):
        i = ' id="'+self.id+'"' if self.id != "" else ""
        c = ' class="'+self.cl+'"' if self.cl != "" else ""
        content = self.content
        [print("Dynamic elements should be written in css. Enter css to fix.\nERROR: "+self.name+":"+p) for p, v in vars(self).items() if p in dynamic]
        return '<'+self.type+i+c+' style="'+"".join([(p.replace("var__","--").replace("_","-")+":"+getattr(self, p))+";" for p, v in vars(self).items() if (p not in inadmissible and getattr(self, p) != "")])+'">'+content+'</'+self.type+'>'

# Link -> Link
class Link:
    def __init__(self):
        self.name = "text"
        self.src = ""
        self.id = ""
        self.cl = ""
        self.content = []
        self.target = "_self"

    def c(self,inadmissible, dynamic):
        i = ' id="'+self.id+'"' if self.id != "" else ""
        c = ' class="'+self.cl+'"' if self.cl != "" else ""
        t = ' target="'+self.target+'"' if self.target != "" else ""
        content = [i.c(inadmissible, dynamic) for i in self.content]
        [print("Dynamic elements should be written in css. Enter css to fix.\nERROR: "+self.name+":"+p) for p, v in vars(self).items() if p in dynamic]
        return '<a'+i+c+' href="'+self.src+'"'+t+' style="'+"".join([(p.replace("var__","--").replace("_","-")+":"+getattr(self, p))+";" for p, v in vars(self).items() if (p not in inadmissible and getattr(self, p) != "")])+'">'+"".join(content)+'</a>'

# C -> Container
class C:
    def __init__(self, background=False):
        self.name = "container"
        self.id = ""
        self.cl = ""
        self.onclick = ""
        self.onhover = ""
        self.attr = ""
        self.background_color = "lightblue" if background == True else ""
        self.overflow_x = "visible"
        self.overflow_y = "visible"
        self.content = []
        
    def c(self, inadmissible, dynamic):
        i = ' id="'+self.id+'"' if self.id != "" else ""
        c = ' class="'+self.cl+'"' if self.cl != "" else ""
        click = ' onclick="'+self.onclick+'"' if self.onclick != "" else ""
        hover = ' onclick="'+self.onhover+'"' if self.onhover != "" else ""
        content = [i.c(inadmissible, dynamic) for i in self.content]
        [print("Dynamic elements should be written in css. Enter css to fix.\nERROR: "+self.name+":"+p) for p, v in vars(self).items() if p in dynamic]
        return '<div'+i+c+click+hover+self.attr+' style="'+"".join([(p.replace("var__","--").replace("_","-")+":"+getattr(self, p))+";" for p, v in vars(self).items() if (p not in inadmissible and getattr(self, p) != "")])+'">'+"".join(content)+'</div>'
        
# Table -> Table
class Table:
    def __init__(self, background=False):
        self.name = "table"
        self.id = "table"
        self.cl = "table"
        self.background_color = "coral" if background == True else ""
        self.content = [[]]

    def rows(self):
        return len(self.content)

    def cols(self):
        return max([len(i) for i in self.content])
    
    def c(self, inadmissible, dynamic):
        i = ' id="'+self.id+'"' if self.id != "" else ""
        c = ' class="'+self.cl+'"' if self.cl != "" else ""
        content = [['<td id="'+self.id+"_"+str(i)+"_"+str(j)+'">'+self.content[i][j].c(inadmissible, dynamic)+'</td>' for j in range(len(self.content[i]))] for i in range(len(self.content))]
        [print("Dynamic elements should be written in css. Enter css to fix.\nERROR: "+self.name+":"+p) for p, v in vars(self).items() if p in dynamic]
        return '<table'+i+c+' style="'+"".join([(p.replace("var__","--").replace("_","-")+":"+getattr(self, p))+";" for p, v in vars(self).items() if (p not in inadmissible and getattr(self, p) != "")])+'">'+"".join(['<tr id="'+self.id+"_"+str(content.index(i))+'">'+"".join(i)+"</tr>" for i in content])+'</table>'

# NavTable -> Navigational Bar Inner Table
class NavTable:
    def __init__(self, background=False):
        self.name = "navtable"
        self.id = "navtable"
        self.cl = "navtable"
        self.background_color = "coral" if background == True else ""
        self.content = [[]]
        self.display = "table"

    def rows(self):
        return len(self.content)

    def cols(self):
        return max([len(i) for i in self.content])
    
    def c(self, inadmissible, dynamic):
        i = ' id="'+self.id+'"' if self.id != "" else ""
        c = ' class="'+self.cl+'"' if self.cl != "" else ""
        content = [['<div id="'+self.id+"_"+str(i)+"_"+str(j)+'" style="display:table-cell;">'+self.content[i][j].c(inadmissible, dynamic)+'</div>' for j in range(len(self.content[i]))] for i in range(len(self.content))]
        [print("Dynamic elements should be written in css. Enter css to fix.\nERROR: "+self.name+":"+p) for p, v in vars(self).items() if p in dynamic]
        return '<section'+i+c+' style="'+"".join([(p.replace("var__","--").replace("_","-")+":"+getattr(self, p))+";" for p, v in vars(self).items() if (p not in inadmissible and getattr(self, p) != "")])+'">'+"".join(['<header id="'+self.id+"_"+str(content.index(i))+'" style="display:table-row;">'+"".join(i)+"</header>" for i in content])+'</section>'


# Nav -> Navigational Bar
class Nav:
    def __init__(self, background=False):
        self.name = "nav_bar"
        self.id = "nav"
        self.cl = ""
        self.tableid = "navtable"
        self.tablecl = ""
        self.background_color = "orange" if background == True else ""
        self.position = "fixed"
        self.z_index = ""
        self.content = [[]]
        
    def c(self, inadmissible, dynamic):
        nav = C()
        navT = NavTable()
        nav.id = self.id
        nav.cl = self.cl
        nav.background_color = self.background_color
        nav.position = self.position
        nav.z_index = self.z_index
        navT.display = "table"
        navT.content = self.content
        navT.id = self.tableid
        navT.cl = self.tablecl
        navT.background_color = ""
        nav.content = [navT]
        return nav.c(inadmissible, dynamic)

# Menu -> Menu Icon
class Menu:
    def __init__(self):
        self.name = "menu_bar"
        self.id = "menubutton"
        self.length = "35"
        self.width = "4"
        self.spacing = "0.85"
        self.radius = "1.75"
        self.color = "black"
        self.custom = ""
        
    def c(self, inadmissible, dynamic):
        if(float(self.spacing) > 1 or float(self.spacing) < 0):
            print("menu spacing should be a decimal between 0-1\nERROR: "+self.name)
        dy1 = float(self.length)/2 - float(self.width)/2
        dy0 = dy1 * (1 - float(self.spacing))
        dy2 = dy1 * (1 + float(self.spacing))
        dy = [dy0, dy1, dy2]
        svg = '<svg id="'+self.id+'" height="'+self.length+'" width="'+self.length+'" style="cursor:pointer;">'
        path = ['<rect x="0" y="'+str(y)+'" rx="'+self.radius+'" ry="'+self.radius+'" width="'+self.length+'" height="'+self.width+'" style="fill:'+self.color+';"/>' for y in dy]
        return svg+"".join(path)+self.custom+'</svg>'

# Icon -> Icon
class Icon:
    def __init__(self):
        self.name = "icon"
        self.type = ""
        self.id = "icon"
        self.cl = ""
        self.height = "35"
        self.width = "35"
        self.color = "black"
        self.path = ""
        self.stroke = "3"

    def c(self, inadmissible, dynamic):
        svg = '<svg id="'+self.id+'" class="'+self.cl+'" height="'+self.height+'" width="'+self.width+'" style="cursor:pointer;">'
        if self.type == "x":
            path = '<line x1="0" y1="0" x2="'+self.width+'" y2="'+self.height+'" style="stroke:'+self.color+';stroke-width:'+self.stroke+'" />'
            path += '<line x1="0" y1="'+self.height+'" x2="'+self.width+'" y2="0" style="stroke:'+self.color+';stroke-width:'+self.stroke+'" />'
        return svg+path+'</svg>'
    
# Image - Image
class Image:
    def __init__(self):
        self.name = "image"
        self.id = ""
        self.cl = ""
        self.src = ""

    def c(self, inadmissible, dynamic):     
        i = ' id="'+self.id+'"' if self.id != "" else ""
        c = ' class="'+self.cl+'"' if self.cl != "" else ""
        [print("Dynamic elements should be written in css. Enter css to fix.\nERROR: "+self.name+":"+p) for p, v in vars(self).items() if p in dynamic]
        return '<img '+i+c+' style="'+"".join([(p.replace("var__","--").replace("_","-")+":"+getattr(self, p))+";" for p, v in vars(self).items() if (p not in inadmissible and getattr(self, p) != "")])+'" src="'+self.src+'"/>'

# Video - Video
class Video:
    def __init__(self):
        self.name = "video"
        self.id = "video"
        self.cl = ""
        self.autoplay = False
        self.muted = False
        self.controls = True
        self.loop = False
        self.src = ""

    def c(self, inadmissible, dynamic):
        if ".mp4" in self.src:
            ext = "mp4"
        elif ".video" in self.src:
            ext = "video"
        else:
            ext = self.src.split('.')[1]
        
        i = ' id="'+self.id+'"' if self.id != "" else ""
        c = ' class="'+self.cl+'"' if self.cl != "" else ""
        props = []
        if self.autoplay == True:
            props.append("autoplay")
        if self.muted == True:
            props.append("muted")
        if self.controls == True:
            props.append("controls")
        if self.loop == True:
            props.append("loop")
        [print("Dynamic elements should be written in css. Enter css to fix.\nERROR: "+self.name+":"+p) for p, v in vars(self).items() if p in dynamic]
        return '<video '+i+c+' style="'+"".join([(p.replace("var__","--").replace("_","-")+":"+getattr(self, p))+";" for p, v in vars(self).items() if (p not in inadmissible and getattr(self, p) != "")])+'" '+" ".join(props)+'><source src="'+self.src+'" type="video/'+ext+'"></video>'

# X -> Custom Element
class X:
    def __init__(self):
        self.name = ""
        self.content = ""

    def c(self, inadmissible, dynamic):
        return self.content
