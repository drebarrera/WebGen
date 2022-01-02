import sys
import os

def main(folder, filename):
    path = "files/"+folder+"/"+filename+"/"
    sys.path.insert(1, path)
    x = __import__(filename)

    jquery = False
    head = "<head>"+x.data.c()
    if os.path.exists(path+filename+".js"):
        head += '<script src="..\JQuery.js"></script>'
        head += '<script src="..\JQuery-UI.js"></script>'
        jquery = True
        fjs = open(path+filename+".js", 'r')
        head += "<script>" + fjs.read() + "</script>"
        fjs.close()
    if os.path.exists(path+filename+".css"):
        fcss = open(path+filename+".css", 'r')
        head += "<style>" + fcss.read().replace("\n"," ") + "</style>"
        fcss.close()
    if os.path.exists("files/"+folder+"/"+"gf.txt"):
        gftxt = open("files/"+folder+"/"+"gf.txt",'r')
        gf = [x for x in gftxt.read().split("\n") if x != '']
        [(x.replace('.py','.js')) for x in gf]
        for g in gf:
            if os.path.exists("files/"+folder+"/"+g.replace('.py','.js')) and (g.replace('.py','') in sys.modules):
                if jquery == False:
                    head += '<script src="..\JQuery.js"></script>'
                    head += '<script src="..\JQuery-UI.js"></script>'
                    jquery = True
                f = open("files/"+folder+"/"+g.replace('.py','.js'), 'r')
                head += "<script>" + f.read() + "</script>"
                f.close()
            if os.path.exists("files/"+folder+"/"+g.replace('.py','.css')) and (g.replace('.py','') in sys.modules):
                f = open("files/"+folder+"/"+g.replace('.py','.css'), 'r')
                head += "<style>" + f.read() + "</style>"
                f.close()
        
    head += "</head>"
    
    body = x.body.c(x.mx.inadmissible, x.mx.dynamic)
    fhtml = open(path+"index.html", 'w+')
    fhtml.write("<!DOCTYPE html><html>"+head+"\n"+body+"</html>")
    fhtml.close()
    sys.modules.pop(filename)
    return
