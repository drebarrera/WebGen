from time import sleep
import webbrowser
import os
import subprocess
import re
import comp
import sys
import shutil

def main():
    for i in "--------------- W E B G E N ---------------":
        print(i, end="")
        sleep(0.04)

    print("\nenter a command or 'help' for a list of commands\n")
    cmd = ""
    while cmd != "exit":
        try:
            cmd = input(">> ")
            if cmd == "help":
                print("\tf(folder,filename) -> opens or creates a new webfile\n\tgf(folder,filename) -> creates an importable global file\n\tfdir -> open file directory\n\texit -> exit WebGen\n\texport(folder, destination) -> exports all webpages to an destination\n\trestart -> restart program\n")
            elif re.search("f(.+,.+)", cmd):
                exec(cmd)
                print("\n\n--------------- W E B G E N ---------------")
            elif re.search("gf(.+)", cmd):
                exec(cmd)
                print("\n\n--------------- W E B G E N ---------------")
            elif cmd == "fdir":
                url = "file:///"+str(os.getcwd())
                webbrowser.get().open(url, new=1)
            elif re.search("export(.+,.+)", cmd):
                exec(cmd)
            elif cmd == "restart":
                os.execv(sys.executable, ['python'] + sys.argv)
            else:
                print('Unrecognized command. Type "help" for list of commands.')
        except Exception as exc:
            print('[!!!] {err}'.format(err=exc))

def f(folder, filename):
    if not re.search(".+///",filename):
        path = "files/"+folder+"/"+filename+"/"
        g = False
    else:
        path = "files/"+folder+"/"
        filename = filename[:-3]
        g = True
        if os.path.exists(path+"/gf.txt"):
            gftxt = open(path+"gf.txt",'r')
            if filename+".py" not in gftxt.read().split("\n"):
                gftxt.close()
                gftxt = open(path+"gf.txt",'a')
                gftxt.write(filename+".py\n")
            gftxt.close()
        else:
            gftxt = open(path+"gf.txt",'a')
            gftxt.write(filename+".py\n")
            gftxt.close()
    if not os.path.exists(path):
        os.makedirs(path)
        print("creating new file...")
    if not os.path.exists(path+filename+".py"):
        ftxt = open(path+filename+".py", 'a')
        ftxt.write("import modules as mx\nimport sys\nsys.path.append('"+os.getcwd()+"/"+folder+"')\nfrom prop import *\ninfo = info()\ndata = mx.Data()\nbody = mx.Body()\n")
        fpropdefault = open('prop_default.txt','r').read()
        fprop = open(path+"prop.py", 'a')
        fprop.write(fpropdefault)
        fprop.close()
    else:
        ftxt = open(path+filename+".py", 'a')
    if g == False:
        fhtml = open(path+"index.html", 'a')
        fhtml.close()
    ftxt.close()
    
    for i in range(int((43 - (len(filename)+2)) / 2)):
        print("-", end="")
        sleep(0.02)
    print(" ", end="")
    sleep(0.02)
    for i in filename:
        print(i.upper(), end="")
        sleep(0.02)
    print(" ", end="")
    sleep(0.02)
    for i in range(int((43 - (len(filename)+2)) / 2)):
        print("-", end="")
        sleep(0.02)
    print("\n")
    if sys.platform == "win32":
        subprocess.Popen(["notepad.exe", path+filename+".py"])
    elif sys.platform == "darwin":
        subprocess.call(['open', '-a', 'TextEdit', path+filename+".py"])
    fedit(folder,filename)

def gf(folder, filename):
    f(folder, filename+"///")
    return

def export(folder, destination):
    print('hi')

def fedit(folder,filename):
    path = "files/"+folder+"/"+filename+"/"
    cmd = ""
    modules, descriptions = getModules()
    while cmd != "exit":
        try:
            cmd = input(">> ")
            if cmd == "help":
                print("\tlm -> list modules\n\tmod m -> print the properties of mod m\n\tlgf -> list global files\n\te -> open file editor\n\tcss - > open a CSS document\n\tjs -> open a JavaScript document\n\tfdir -> open file directory\n\tr -> refresh\n\tdel -> delete file\n\texit -> exit file\n\trestart -> restart program\n")
            elif cmd == "lm":
                for m in descriptions:
                    print("\t"+m)
            elif re.search("mod .+", cmd):
                props = modules[cmd[4:]]
                for p in props:
                    print("\t"+p)
            elif cmd == "lgf":
                p = "files/"+folder+"/"
                if os.path.exists(p+"gf.txt"):
                    gftxt = open(p+"gf.txt",'r')
                    print([x for x in gftxt.read().split("\n")])
                    gftxt.close()
            elif cmd == "r":
                c(folder, filename)
            elif cmd == "css":
                css(folder, filename)
            elif cmd == "js":
                js(folder, filename)
            elif cmd == "fdir":
                url = "file:///"+str(os.getcwd())+"/"+path
                webbrowser.open(url, new=0)
            elif cmd == "e":
                if sys.platform == "win32":
                    subprocess.Popen(["notepad.exe", path+filename+".py"])
                elif sys.platform == "darwin":
                    subprocess.call(['open', '-a', 'TextEdit', path+filename+".py"])
            elif cmd == "del":
                print('Are you sure you want to delete '+filename+'? Type [y] or [n].')
                sure = input('>> ')
                if sure == 'y':
                    shutil.rmtree(path)
                    if len(os.listdir("files/"+folder+"/")) == 1 and os.listdir("files/"+folder+"/")[0] == '.DS_Store':
                        shutil.rmtree("files/"+folder+"/")
                    print('Files terminated.')
                    cmd = "exit"
                elif sure == 'n':
                    print('Files saved.')
                else:
                    print('Informal response. Files saved.')
            elif cmd == "restart":
                os.execv(sys.executable, ['python'] + sys.argv)
            else:
                print('Unrecognized command. Type "help" for list of commands.')
        except Exception as exc:
            print('[!!!] {err}'.format(err=exc))

def css(folder, filename):
    path = "files/"+folder+"/"+filename+"/"
    fcss = open(path+filename+".css", 'a')
    fcss.close()
    if sys.platform == "win32":
        subprocess.Popen(["notepad.exe", path+filename+".css"])
    elif sys.platform == "darwin":
        subprocess.call(['open', '-a', 'TextEdit', path+filename+".css"])

def js(folder, filename):
    path = "files/"+folder+"/"+filename+"/"
    copyrootf("JQuery.js", folder)
    copyrootf("JQuery-UI.js", folder)
    fjs = open(path+filename+".js", 'a')
    fjs.close()
    if sys.platform == "win32":
        subprocess.Popen(["notepad.exe", path+filename+".js"])
    elif sys.platform == "darwin":
        subprocess.call(['open', '-a', 'TextEdit', path+filename+".js"])

def copyrootf(filename, p):
    p = "files/"+p+"/"
    f = open(filename,'r')
    fr = open(p+filename,'w')
    fr.write(f.read())
    fr.close()
    f.close()
    
def getModules():
    modules = {}
    descriptions = []
    mf = open("modules.py","r")
    mfl = mf.read().split("\n")
    for l in mfl:
        if "# " in l:
            descriptions.append(l[2:])
        if "class" in l:
            if "def __init__(self):" in mfl[mfl.index(l) + 1]:
                mod = l[5:].replace(':','').replace(' ','')
                props = []
                ind = mfl.index(l) + 2
                while "self" in mfl[ind]:
                    bounds = (mfl[ind].index("."), mfl[ind].index("="))
                    props.append(mfl[ind][bounds[0]:bounds[1] - 1])
                    ind += 1
                modules[mod] = props
    mf.close()
    return modules, descriptions

def c(folder, filename):
    path = "files/"+folder+"/"+filename+"/"
    comp.main(folder,filename)
    url = "file:///"+str(os.getcwd())+"/"+path+"index.html"
    webbrowser.get().open(url, new=0)
    return
main()
