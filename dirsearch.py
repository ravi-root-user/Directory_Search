import os
import fero
def install_tool():
    if os.path.exists("~/dirsearch"):
        os.system(
            "cd ~/dirsearch")
        os.system("pip3 install -r requirements.txt >> /dev/null")
    else:
        os.system("cd ~/ && git clone https://github.com/maurosoria/dirsearch.git")
        os.system("cd ~/dirsearch")
        os.system("cd ~/dirsearch && pip3 install -r requirements.txt >> /dev/null")

def dirsearch():
    url = input("Enter Target URL:- ")
    directory = input("do you want to Select a custom file Y/N ").upper()
    if directory == "Y":
        path = input("enter your directory path:-")
        print(path)
    elif directory == "N":
        print("Using default wordlist")
        path = "null"
    else:
        print("Invalid Value")
    exclude = input("do you want to execlue any statuscodes Y/N ").upper()
    if exclude == "Y":
        exclusion = input("Enter exclusion codes ")
        print(exclusion)
    elif exclude == "N":
        print("continueing without exclusions")
        exclusion = "null"
    else:
        print("Invalid Input")
    main_dirsearch(url, path, exclusion)
    ferox.main_feroxbuster(url,path)


def main_dirsearch(url, path, exclusion):
    # os.system("mkdir ~/output")
    # os.system("mkdir")
    if path == "null" and exclusion == "null":
        os.system(f"cd ~/dirsearch && python3 dirsearch.py -u {url} >> ./outputs/dirsearch_output")
    elif path!="null" and exclusion=="null":
        os.system(f"cd ~/dirsearch && python3 dirsearch.py -u {url} -w {path} >> ./outputs/dirsearch_output")
    elif path!="null" and exclusion!="null":
        os.system(f"cd ~/dirsearch && python3 dirsearch.py -u {url} -w {path} -x {exclusion} > ./outputs/dirsearch_output")


def ferox():
    fero.install_tool()