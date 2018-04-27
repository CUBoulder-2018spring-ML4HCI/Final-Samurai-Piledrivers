import tkinter as tk
from tkinter.ttk import *
from tkinter import *
import os
import webbrowser
# import control
import socket
import os, sys, string, subprocess
# import msvcrt
# import pyautogui
from sys import platform

# OSC Stuff
import argparse
import random
import time
from pythonosc import osc_message_builder
from pythonosc import udp_client

character = 0

# Create first OSC Client
parser = argparse.ArgumentParser()
parser.add_argument("--ip", default="127.0.0.1",
  help="The ip of the OSC server")
parser.add_argument("--port", type=int, default=6448,
  help="The port the OSC server is listening on")
args = parser.parse_args()
client = udp_client.SimpleUDPClient(args.ip, args.port)

# Create seconf OSC client
parser2 = argparse.ArgumentParser()
parser2.add_argument("--ip", default="127.0.0.1",
  help="The ip of the OSC server")
parser2.add_argument("--port", type=int, default=6669,
  help="The port the OSC server is listening on")
args2 = parser2.parse_args()
client2 = udp_client.SimpleUDPClient(args2.ip, args2.port)


SchemaList = ['Empty'] * 10


def ModelFinder():
    for root, dirs, files in os.walk("./Schemas"):
        i = 0
        for filename in files:
            SchemaList[i] = filename
            i = i + 1


class LoadedSchema():
    pass


class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

    def show(self):
        self.lift()


class InitPage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self,
                         text="Welcome to Samurai Piledrivers, \n The accessible game interface. \n Please select what you would like to do from the top menu bar. \n If you are new, build a new schema or select a premade schema from the options. \n If you wish to test the schema, select schema tutorial. \n If you are all set and ready to play, select launch game.",
                         font=("Arial Bold", 15))
        label.pack(side="top", expand=True)


class Build(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        label = tk.Label(self, text="To build a schema, select a control, and record your input for that control.")
        label.pack(side="top", fill="both", expand=False)

        def GlobalBuildHandler():
            global RecSel
            RecSel = True
            global tempText
            tempText = "Record"

            #RecCombos
            global RecCom
            RecCom = True
            global tempT
            tempT = "Record Combo"


        def update_btn_text(val):
            btn_text.set(val)

        def update_combo_text(val):
            combo_text.set(val)

        def RecSelected(sid):
            print("cactus", var.get())
            temp = var.get()
            global RecSel
            global tempText
            if RecSel:
                # Record
                client.send_message("/wekinator/control/startRecording", 1)
                RecSel = not RecSel
                update_btn_text("Stop")
                print("Recording value", temp)
            else:
                # Stop
                client.send_message("/wekinator/control/stopRecording", 1)
                print("Stopped recording")
                RecSel = not RecSel
                update_btn_text("Record Basic Moves")

        def RecCombos(sid):
            print("cactus", var.get())
            temp = var.get()
            global RecCom
            global tempT
            if RecCom:
                # Record
                client2.send_message("/wekinator/control/startRecording", 1)
                RecCom = not RecCom
                update_combo_text("Stop")
                print("Recording value", temp)
            else:
                # Stop
                client2.send_message("/wekinator/control/stopRecording", 1)
                print("Stopped recording")
                RecCom = not RecCom
                update_combo_text("Record Combo Moves")

        # Call train osc messages
        def TrainBasic():
            client.send_message("/wekinator/control/train", 1)

        def TrainCombo():
            client2.send_message("/wekinator/control/train", 1)

        def sel():
            global selected
            selected = var.get()

        def sel2():
            global character
            character = var.get()

        def save():
            global character
            character = charVar.get()
            print(character)

        # Choose a charcter
        chara = tk.Label(self, text="Choose the character this schema will be for:")
        chara.pack(side="top", fill="both", expand=False)

        charVar = IntVar()

        c1 = Radiobutton(self, text="Ryu", variable=charVar, value=1, command=sel2)
        c2 = Radiobutton(self, text="Sagat", variable=charVar, value=2, command=sel2)
        c3 = Radiobutton(self, text="M.Bison", variable=charVar, value=3, command=sel2)

        c1.pack(side="top", fill="both", expand=False)
        c2.pack(side="top", fill="both", expand=False)
        c3.pack(side="top", fill="both", expand=False)

        # Choose the move to map
        move = tk.Label(self, text="Select a move and map it to a control:")
        move.pack(side="top", fill="both", expand=False)

        var = IntVar()

        rad1 = Radiobutton(self, text="Jump", variable=var, value=1, command=sel)
        rad2 = Radiobutton(self, text="Crouch", variable=var, value=2, command=sel)
        rad3 = Radiobutton(self, text="Left", variable=var, value=3, command=sel)
        rad4 = Radiobutton(self, text="Right", variable=var, value=4, command=sel)
        rad5 = Radiobutton(self, text="A", variable=var, value=5, command=sel)
        rad6 = Radiobutton(self, text="B", variable=var, value=6, command=sel)
        rad7 = Radiobutton(self, text="X", variable=var, value=7, command=sel)

        GlobalBuildHandler()
        btn_text = tk.StringVar()
        combo_text = tk.StringVar()

        sel()
        RecStop = Button(self, textvariable=btn_text, bg="#6c93d1", font=("Arial Bold", 15),
                         command=lambda: RecSelected(selected))
        btn_text.set("Record Basic Moves")

        rad1.pack(side="top", fill="both", expand=False)
        rad2.pack(side="top", fill="both", expand=False)
        rad3.pack(side="top", fill="both", expand=False)
        rad4.pack(side="top", fill="both", expand=False)
        rad5.pack(side="top", fill="both", expand=False)
        rad6.pack(side="top", fill="both", expand=False)
        rad7.pack(side="top", fill="both", expand=False)

        RecStop.pack(side="top", expand=False)

        # Train button
        TrainButton = Button(self, text="Train Basic Moves", bg="#6c93d1", font=("Arial Bold", 15),
                         command=lambda: TrainBasic())

        TrainButton.pack(side="top", expand=False)

        SaveButton = Button(self, text="Save", bg="#6c93d1", font=("Arial Bold", 15),
                         command=lambda: save())
        SaveButton.pack(side="top", expand=False)

        # COMBO STUFF

        combos = tk.Label(self, text="Train combo moves:")
        combos.pack(side="top", fill="both", expand=False)

        RecCombo = Button(self, textvariable=combo_text, bg="#6c93d1", font=("Arial Bold", 15),
                         command=lambda: RecCombos(selected))
        combo_text.set("Record Combo Moves")

        RecCombo.pack(side="top", expand=False)

        # Train Combo button
        TrainComboButton = Button(self, text="Train Combo Moves", bg="#6c93d1", font=("Arial Bold", 15),
                         command=lambda: TrainCombo())

        TrainComboButton.pack(side="top", expand=False)


class PickSchema(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="Select your schema")
        label.pack(side="top", expand=False)

        def loadSchema(Sid):
            print("cactus", var.get())

        selected = 0

        def sel():
            global selected
            selected = var.get()

        var = IntVar()

        ModelFinder()

        rad1 = Radiobutton(self, text=SchemaList[0], variable=var, value=1, command=sel)
        rad2 = Radiobutton(self, text=SchemaList[1], variable=var, value=2, command=sel)
        rad3 = Radiobutton(self, text=SchemaList[2], variable=var, value=3, command=sel)
        rad4 = Radiobutton(self, text=SchemaList[3], variable=var, value=4, command=sel)
        rad5 = Radiobutton(self, text=SchemaList[4], variable=var, value=5, command=sel)
        rad6 = Radiobutton(self, text=SchemaList[5], variable=var, value=6, command=sel)
        rad7 = Radiobutton(self, text=SchemaList[6], variable=var, value=7, command=sel)
        rad8 = Radiobutton(self, text=SchemaList[7], variable=var, value=8, command=sel)
        rad9 = Radiobutton(self, text=SchemaList[8], variable=var, value=9, command=sel)

        selects = Button(self, text='Select Schema', bg="#6c93d1", font=("Arial Bold", 15),
                         command=lambda: loadSchema(selected))

        rad1.pack(side="top", fill="both", expand=False)
        rad2.pack(side="top", fill="both", expand=False)
        rad3.pack(side="top", fill="both", expand=False)
        rad4.pack(side="top", fill="both", expand=False)
        rad5.pack(side="top", fill="both", expand=False)
        rad6.pack(side="top", fill="both", expand=False)
        rad7.pack(side="top", fill="both", expand=False)
        rad8.pack(side="top", fill="both", expand=False)
        rad9.pack(side="top", fill="both", expand=False)

        selects.pack(side="top", expand=False)


class Tutorial(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="Test and try out your schema")
        label.pack(side="top", fill="both", expand=True)

        def tutorialbutton():
            print("something should go here at some point")

        Launchbtn = tk.Button(self, text="Launch Tutorial", bg="#6c93d1", font=("Arial Bold", 20),
                              command=tutorialbutton())
        Launchbtn.pack(side="top")


class LaunchGame(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)




        def mclicked():
            cmd = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe  --profile-directory=Default --app-id=ckpjobcmemfpfeaeolhhjkjdpfnkngnd"
            pro = subprocess.Popen(cmd, stdout=subprocess.PIPE)
            pro.wait()

        Launchbtn = tk.Button(self, text="Launch Game", bg="#6c93d1", font=("Arial Bold", 20), command=mclicked)
        Launchbtn.pack(side="top")


class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        ip = InitPage(self)
        bp = Build(self)
        ps = PickSchema(self)
        tu = Tutorial(self)
        lg = LaunchGame(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        ip.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        bp.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        ps.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        tu.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        lg.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        # Label = tk.Label(buttonframe, text="SelectedSchema", command=bp.lift)

        b1 = tk.Button(buttonframe, text="Build New Schema", command=bp.lift)
        b2 = tk.Button(buttonframe, text="Select Existing Schema", command=ps.lift)
        b3 = tk.Button(buttonframe, text="Schema Test", command=tu.lift)
        b4 = tk.Button(buttonframe, text="Launch Game", command=lg.lift)
        b5 = tk.Button(buttonframe, text="home", command=ip.lift)

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")
        b4.pack(side="left")
        b5.pack(side="left")

        ip.show()


if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("800x800")
    root.mainloop()
