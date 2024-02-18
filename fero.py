import os
def install_tool():
    if os.system("feroxbuster --help >>/dev/null"):
        print("requirements satisfied no need to install")
    else:
        os.system("apt install -y feroxbuster")



def main_feroxbuster(url, path):
    if path == "null":
        os.system(f"feroxbuster -u {url} >> ./outputs/feroxbuster_output")
    elif path!="null":
        os.system(f"feroxbuster -u {url} -w {path} >> ./outputs/feroxbuster_output")