import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import *
from tkinter import *


class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

    def show(self):
        self.lift()

class InitPage(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="Welcome to Samurai Piledrivers, \n The accessible game interface. \n Please select what you would like to do from the top menu bar. \n If you are new, build a new schema or select a premade schema from the options. \n If you wish to test the schema, select schema tutorial. \n If you are all set and ready to play, select launch game.", font=("Arial Bold", 15))
       label.pack(side="top", expand=True)

class Build(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="Build your Schema")
       label.pack(side="top", fill="both", expand=True)


def loadSchema(Sid):
    pass


class PickSchema(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="Select your schema")
       label.pack(side="top", expand=False)

       selected = IntVar()

       rad1 = Radiobutton(self, text='Cool Schema', value=1, variable=selected)

       rad2 = Radiobutton(self, text='Lame Schema', value=2, variable=selected)

       rad3 = Radiobutton(self, text='Cheating Schema', value=3, variable=selected)
       
       selects = Button(self, text='Select Schema', bg="#6c93d1", font=("Arial Bold", 15), command=loadSchema(selected))

       rad1.pack(side="top", fill="both", expand=False)

       rad2.pack(side="top", fill="both", expand=False)

       rad3.pack(side="top", fill="both", expand=False)
       
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
           pass
          #messagebox.showinfo('Launching', 'Will launch the game when plugged in')
       Launchbtn = tk.Button(self, text="Launch Game", bg="#6c93d1", font=("Arial Bold", 20), command= mclicked())
       Launchbtn.pack(side="top",)



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