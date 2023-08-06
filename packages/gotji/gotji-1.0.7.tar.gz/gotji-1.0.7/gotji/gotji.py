import platform
import os
from pystyle import *
from replit import web
from flask import Flask, render_template, request
from flask_restful import Api, Resource

meoaw_x = Flask(__name__)
meoaw = Api(meoaw_x)

meoaw.run(host='0.0.0.0', port=8080)

class connect:

    web.run(meoaw_x)

@meoaw.route('/')
def main():

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