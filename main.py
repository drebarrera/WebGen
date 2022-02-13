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
                print("\tf(folder,filename) -> opens or creates a new webfile\n\tgf(folder,filename) -> creates an importable global file\n\tfdir -> open file directory\n\tkill(folder) -> delete a project (folder)\n\texit -> exit WebGen\n\texportf(folder, destination) -> exports all webpages to an destination\n\trestart -> restart program\n")
            elif re.search("f(.+,.+)", cmd):
                exec(cmd)
                print("\n\n--------------- W E B G E N ---------------")
            elif re.search("gf(.+)", cmd):
                exec(cmd)
                print("\n\n--------------- W E B G E N ---------------")
            elif cmd == "fdir":
                url = "file:///"+str(os.getcwd())
                webbrowser.get().open(url, new=1)
            elif re.search("exportf(.+,.+)", cmd):
                exec(cmd)
            elif re.search("kill(.+)", cmd):
                exec(cmd)
            elif cmd == "restart":
                os.execv(sys.executable, ['python'] + sys.argv)
            elif cmd == "exit":
                continue
            else:
                print('Unrecognized command. Type "help" for list of commands.')
        except Exception as exc:
            print('[!!!] {err}'.format(err=exc))
            if re.search("exportf(.+,.+)", cmd):
                print('When referencing the destination path, make sure to prepend with the letter r like so: r"THIS\IS\A\PATH"')

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
        if g == False:
            ftxt.write("import modules as mx\nimport sys\nimport os\nhomedir = os.getcwd() + r'/files/Portfolio/'\nsys.path.append(homedir)\ndata = mx.Data()\nbody = mx.Body()\n\n### OBJECTS ###\n\n### CONTENT ###\n\n### PROPERTIES ###")
        else:
            ftxt.write("import modules as mx\n\n### OBJECTS ###\n\n### CONTENT ###\n\n### PROPERTIES ###")
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
    fedit(folder,filename,g)

def kill(folder):
    print('Are you sure you want to delete '+folder+'? Type [y] or [n].')
    sure = input('>> ')
    if sure == 'y':
        print('Please double confirm [y] or [n]. By confirming you may be deleting multiple pages.')
        sure = input('>> ')
        if sure == 'y':
            shutil.rmtree('files/'+folder)
            print("Project terminated.")
        elif sure == 'n':
            print('Project saved.')
        else:
            print('Informal response. Project saved.')
    elif sure == 'n':
        print('Project saved.')
    else:
        print('Informal response. Project saved.')

def gf(folder, filename):
    f(folder, filename+"///")
    return

def exportf(folder, destination):
    home = destination
    os.makedirs(home+"/"+folder)
    for filename in os.listdir("files/"+folder+"/"):
        if "." in filename:
            continue
        if not os.path.exists("files/"+folder+"/"+filename+"/index.html"):
            continue
        path = "files/"+folder+"/"+filename+"/"
        newhome = home + "/" + folder + "/"
        os.makedirs(newhome+"/"+filename)
        comp.main(folder,filename)
        if os.path.exists(path+"/index.php"):
            f = open(path+"/index.php",'r')
            fr = open(newhome+"/"+filename+"/index.php",'w')
        else:
            f = open(path+"/index.html",'r')
            fr = open(newhome+"/"+filename+"/index.html",'w')
        fr.write(f.read())
        fr.close()
        f.close()
        print('copied '+filename)
        if os.path.exists(path+"/images"):
            os.makedirs(newhome+"/"+filename+"/images")
            for file_name in os.listdir(path+"/images"):
                source = path+"/images/" + file_name
                destination = newhome+"/"+filename+"/images/" + file_name
                shutil.copy(source, destination)
                print('copied', file_name)
    shutil.copy('JQuery.js', home+"/"+folder)
    shutil.copy('JQuery-UI.js', home+"/"+folder)
    prevdir = os.getcwd()
    os.chdir(home)
    shutil.make_archive(folder, 'zip', folder)
    shutil.rmtree(home+"/"+folder)
    print('zipped', folder+'.zip')
    os.chdir(prevdir)

def fedit(folder,filename,g):
    if g == True:
        path = "files/"+folder+"/"
    else:
        path = "files/"+folder+"/"+filename+"/"
    cmd = ""
    modules, descriptions = getModules()
    while cmd != "exit":
        cmd = input(">> ")
        if cmd == "help":
            print("\tlm -> list modules\n\tmod m -> print the properties of mod m\n\tlgf -> list global files\n\te -> open file editor\n\tcss - > open a CSS document\n\tjs -> open a JavaScript document\n\tphp -> open a PHP document (for global files only)\n\tfdir -> open file directory\n\timages -> open images directory\n\tr -> refresh\n\texport(directory_name) -> export compiled file\n\tkill -> delete file\n\texit -> exit file\n\trestart -> restart program\n")
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
                print([x for x in gftxt.read().split("\n") if x != ''])
                gftxt.close()
        elif cmd == "r":
            if g == True:
                print("[!!!] global file cannot be executed.")
            else:
                c(folder, filename)
        elif cmd == "css":
            css(folder, filename, g)
        elif cmd == "js":
            js(folder, filename, g)
        elif cmd == "php":
            php(folder, filename, g)
        elif cmd == "fdir":
            url = "file:///"+str(os.getcwd())+"/"+path
            webbrowser.open(url, new=0)
        elif cmd == "e":
            if(g == False):
                if sys.platform == "win32":
                    try:
                        subprocess.Popen([sys.exec_prefix+r"\Lib\idlelib\idle.bat", path+filename+".py"])
                    except Exception as exc:
                        print(exc)
                        print('opening notepad.exe as subtitute...')
                        subprocess.Popen(["notepad.exe", path+filename+".py"])
                elif sys.platform == "darwin":
                    try:
                        subprocess.call(['open', '-a', 'IDLE 3', path+filename+".py"])
                    except Exception as exc:
                        print(exc)
                        print('opening TextEdit as subtitute...')
                        subprocess.call(['open', '-a', 'TextEdit', path+filename+".py"])
            else:
                if sys.platform == "win32":
                    try:
                        subprocess.Popen([sys.exec_prefix+r"\Lib\idlelib\idle.bat", "files/"+folder+"/"+filename+".py"])
                    except Exception as exc:
                        print(exc)
                        print('opening notepad.exe as subtitute...')
                        subprocess.Popen(["notepad.exe", "files/"+folder+"/"+filename+".py"])
                elif sys.platform == "darwin":
                    try:
                        subprocess.call(['open', '-a', 'IDLE 3', "files/"+folder+"/"+filename+".py"])
                    except Exception as exc:
                        print(exc)
                        print('opening TextEdit as subtitute...')
                        subprocess.call(['open', '-a', 'TextEdit', "files/"+folder+"/"+filename+".py"])
        elif cmd == "images":
            if g == False:
                if not os.path.exists("files/"+folder+"/"+filename+"/images"):
                    os.makedirs("files/"+folder+"/"+filename+"/images")
                url = "file:///"+str(os.getcwd())+"/files/"+folder+"/"+filename+"/images"
                webbrowser.open(url, new=0)
        elif cmd == "kill":
            print('Are you sure you want to delete '+filename+'? Type [y] or [n].')
            sure = input('>> ')
            if sure == 'y':
                if g == False:
                    shutil.rmtree(path)
                    if len(os.listdir("files/"+folder+"/")) == 0 or len(os.listdir("files/"+folder+"/")) == 1 and os.listdir("files/"+folder+"/")[0] == '.DS_Store':
                        shutil.rmtree("files/"+folder+"/")
                elif g == True and os.path.exists("files/"+folder+"/"+filename+".py"):
                    os.remove("files/"+folder+"/"+filename+".py")
                    if os.path.exists("files/"+folder+"/"+filename+".css"):
                        os.remove("files/"+folder+"/"+filename+".css")
                    if os.path.exists("files/"+folder+"/"+filename+".js"):
                        os.remove("files/"+folder+"/"+filename+".js")
                print('Files terminated.')
                cmd = "exit"
            elif sure == 'n':
                print('Files saved.')
            else:
                print('Informal response. Files saved.')
        elif cmd == "restart":
            os.execv(sys.executable, ['python'] + sys.argv)
        elif re.search("export(.+)", cmd):
            dest = cmd.replace('export("','').replace('")','')
            export(dest,folder,filename)
        elif cmd == "exit":
            continue
        else:
            print('Unrecognized command. Type "help" for list of commands.')

def export(home,folder,filename):
    path = "files/"+folder+"/"+filename+"/"
    os.makedirs(home+"/"+filename)
    comp.main(folder,filename)
    if os.path.exists(path+"/index.php"):
        f = open(path+"/index.php",'r')
        fr = open(home+"/"+filename+"/index.php",'w')
    else:
        f = open(path+"/index.html",'r')
        fr = open(home+"/"+filename+"/index.html",'w')
    fr.write(f.read())
    fr.close()
    f.close()
    print('copied index')
    if os.path.exists(path+"/images"):
        os.makedirs(home+"/"+filename+"/images")
        for file_name in os.listdir(path+"/images"):
            source = path+"/images/" + file_name
            destination = home+"/"+filename+"/images/" + file_name
            shutil.copy(source, destination)
            print('copied', file_name)
    prevdir = os.getcwd()
    os.chdir(home)
    shutil.make_archive(filename, 'zip', filename)
    shutil.rmtree(home+"/"+filename)
    print('zipped', filename+'.zip')
    os.chdir(prevdir)

def css(folder, filename, g):
    if g == True:
        path = "files/"+folder+"/"
    else:
        path = "files/"+folder+"/"+filename+"/"
    fcss = open(path+filename+".css", 'a')
    fcss.close()
    if sys.platform == "win32":
        subprocess.Popen(["notepad.exe", path+filename+".css"])
    elif sys.platform == "darwin":
        subprocess.call(['open', '-a', 'TextEdit', path+filename+".css"])

def js(folder, filename, g):
    if g == True:
        path = "files/"+folder+"/"
    else:
        path = "files/"+folder+"/"+filename+"/"
    if not os.path.exists(path+"JQuery.js"):
        copyrootf("JQuery.js", folder)
        copyrootf("JQuery-UI.js", folder)
    fjs = open(path+filename+".js", 'a')
    fjs.close()
    if sys.platform == "win32":
        subprocess.Popen(["notepad.exe", path+filename+".js"])
    elif sys.platform == "darwin":
        subprocess.call(['open', '-a', 'TextEdit', path+filename+".js"])
    
def php(folder, filename, g):
    if g == True:
        path = "files/"+folder+"/"
        fcss = open(path+filename+".php", 'a')
        fcss.close()
        if sys.platform == "win32":
            subprocess.Popen(["notepad.exe", path+filename+".php"])
        elif sys.platform == "darwin":
            subprocess.call(['open', '-a', 'TextEdit', path+filename+".php"])
    else:
        print('[!!!] to add php to a file, create a global file and link it with "import"')

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
