import platform
import os
from pystyle import *

class connect:

    text = "[ ✅ ]"

    connect = "Connected"

    if platform.system() == 'Windows':

        os.system('cls & title GOTji API ( Beta )')

        print(" ")

        print(" ")

        print(Colorate.Color(Colors.blue, text, True) + " " + " " + Colorate.Color(Colors.green, connect, True))

        print(" ")

        print(" ")

    else:

        os.system('clear')

        print(" ")

        print(" ")

        print(Colorate.Color(Colors.blue, text, True) + " " + " " + Colorate.Color(Colors.green, connect, True))

        print(" ")

        print(" ")
