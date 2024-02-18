import os
import dirsearch
R = '\033[31m'  # red
G = '\033[32m'  # green
C = '\033[36m'  # cyan
W = '\033[0m'  # white
Y = '\033[33m'  # yellow
version = '1.0'


def start_me():
    os.system('clear')
    banner = r'''
    < Dumb tool by Dumb coder >
    ===========================
         \  ^__^    /
          \ (oo)\__/_____
            (__)\        )\/\  /
                ||-w--w |    \/
                ||     ||
                                '''
    print(R + banner + W + '\n')
    print(R + '[>] ' + R + 'Version : ' + W + version)


start_me()
dirsearch.install_tool()
dirsearch.dirsearch()
dirsearch.fero()
