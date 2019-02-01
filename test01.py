import tkinter

class Application(tkinter.Frame):
    def __init__(self, master=None):
        tkinter.Frame.__init__(self, master)
        self.grid(sticky=tkinter.N+tkinter.S+tkinter.E+tkinter.W)
        self.createWidgets()
        self.createNugget()

    def createWidgets(self):
        top=self.winfo_toplevel()
        top.rowconfigure(0, weight=1)
        top.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.quit = tkinter.Button(self, text='Quit', command=self.quit)
        self.quit.grid()
        #self.quit.grid(row=0, column=0, sticky=tkinter.N+tkinter.S+tkinter.E+tkinter.W)

    def createNugget(self):
        top=self.winfo_toplevel()
        top.rowconfigure(0, weight=1)
        top.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.quit = tkinter.Button(self, text='Hello', command=self.quit)
        self.quit.grid()
        #self.quit.grid(row=0, column=0, sticky=tkinter.N+tkinter.S+tkinter.E+tkinter.W)

app = Application()
app.master.title('Sample application')
app.mainloop()
