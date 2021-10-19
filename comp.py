import sys
import os

def main(folder, filename):
    path = "files/"+folder+"/"+filename+"/"
    sys.path.insert(1, path)
    x = __import__(filename)

    head = "<head>"+x.data.c()
    if os.path.exists(path+filename+".js"):
        head += '<script src="..\JQuery.js"></script>'
        head += '<script src="..\JQuery-UI.js"></script>'
        fjs = open(path+filename+".js", 'r')
        head += "<script>" + fjs.read() + "</script>"
        fjs.close()
    if os.path.exists(path+filename+".css"):
        fcss = open(path+filename+".css", 'r')
        head += "<style>" + fcss.read().replace("\n"," ") + "</style>"
        fcss.close()
    head += "</head>"
    
    body = x.body.c(x.mx.inadmissible, x.mx.dynamic)
    fhtml = open(path+"index.html", 'w+')
    fhtml.write("<!DOCTYPE html><html>"+head+"\n"+body+"</html>")
    fhtml.close()
    sys.modules.pop(filename)
    return
