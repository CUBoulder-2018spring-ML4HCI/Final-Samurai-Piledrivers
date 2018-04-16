import tkinter as tk
from tkinter.ttk import *
from tkinter import *
import os
import webbrowser

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
        label = tk.Label(self, text="Build your Schema")
        label.pack(side="top", fill="both", expand=True)

        def RecSelected(sid):
            print("cactus", var.get())
            temp = var.get()
            global RecSel
            if RecSel:
                print("Recording value", temp)
            else:
                print("Stopped recording")

        def RecSelText(RecSel):
            if RecSel:
                return "Record"
            else:
                return "Stop Recording"

        def sel():
            global selected
            selected = var.get()

        var = IntVar()

        rad1 = Radiobutton(self, text="Jump", variable=var, value=1, command=sel)
        rad2 = Radiobutton(self, text="Crouch", variable=var, value=2, command=sel)
        rad3 = Radiobutton(self, text="Left", variable=var, value=3, command=sel)
        rad4 = Radiobutton(self, text="Right", variable=var, value=4, command=sel)
        rad5 = Radiobutton(self, text="A", variable=var, value=5, command=sel)
        rad6 = Radiobutton(self, text="B", variable=var, value=6, command=sel)
        rad7 = Radiobutton(self, text="X", variable=var, value=7, command=sel)
        rad8 = Radiobutton(self, text="Combo 1", variable=var, value=8, command=sel)
        rad9 = Radiobutton(self, text="Combo 2", variable=var, value=9, command=sel)

        RecSel = True
        tempText = RecSelText(RecSel)
        RecStop = Button(self, text=tempText, bg="#6c93d1", font=("Arial Bold", 15),
                         command=lambda: RecSelected(selected))

        rad1.pack(side="top", fill="both", expand=False)
        rad2.pack(side="top", fill="both", expand=False)
        rad3.pack(side="top", fill="both", expand=False)
        rad4.pack(side="top", fill="both", expand=False)
        rad5.pack(side="top", fill="both", expand=False)
        rad6.pack(side="top", fill="both", expand=False)
        rad7.pack(side="top", fill="both", expand=False)
        rad8.pack(side="top", fill="both", expand=False)
        rad9.pack(side="top", fill="both", expand=False)

        RecStop.pack(side="top", expand=False)


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


        selects = Button(self, text='Select Schema', bg="#6c93d1", font=("Arial Bold", 15), command=lambda: loadSchema(selected))

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

class LaunchGame(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)

       def mclicked():
           url = 'https://chrome.google.com/webstore/detail/super-nintendo-emulator-s/ckpjobcmemfpfeaeolhhjkjdpfnkngnd?hl=en'
           chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
           webbrowser.get(chrome_path).open(url)

       Launchbtn = tk.Button(self, text="Launch Game", bg="#6c93d1", font=("Arial Bold", 20), command= mclicked)
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
