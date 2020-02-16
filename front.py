import tkinter
import datetime
import PIL.Image, PIL.ImageTk

class car_navi(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master, bg="lightblue")
        self.grid()
        self.menubar()
        self.default()
        self.navi()

    def menubar(self):
        menubar = tkinter.Frame(self, bg="gray", width=200, height=600)
        menubar.grid(column=0, row=0)
        self.label = tkinter.Label(menubar,font=("",20),width=15)
        self.label.place()

        self.button1 = tkinter.Button(
            menubar, text="Menu", command=lambda : self.delete_default(), width=15, height=11,
            font=("Courie")
        )
        self.button1.pack(padx=9, pady=10 )

        self.button2 = tkinter.Button(
            menubar, text="Navi", command=lambda : self.delete_navi() ,  width=15, height=11,
            font=("Courie")
        )
        self.button2.pack(padx=9, pady=10)

        self.button3 = tkinter.Button(
            menubar, text="Cancel",  width=15, height=11,
            font=("Courie")
        )
        self.button3.pack(padx=9, pady=10)

    def default(self):
        self.default = tkinter.Frame(self, bg="#dcdcdc", width=900, height=600)
        self.default.grid(column=1, row=0)

        self.info = tkinter.Label(
            self,width=12,font=("Courier",50,"bold") ,bg="#dcdcdc"
        )
        self.info.place(rely =0.7, relx=0.2)

        self.time = tkinter.Label(
            self,width=12,font=("Courier",100,"bold") ,bg="#dcdcdc"
        )
        self.time.place(rely =0.8, relx=0.3)
        self.update()

    def navi(self):
        self.navi = tkinter.Frame(self, bg="#dcdcdc", width=900, height=600)
        self.navi.grid(column=1, row=0)

        self.ok_button = tkinter.Button(
            self.navi, text="OK",command=lambda : self.delete_navi() ,  width=2, height=3 ,
            font=("Courie")
        )
        self.ok_button.place(rely =0.85, relx=0.03, relwidth = 0.9)

    def update(self):
        now = datetime.datetime.now()

        self.info["text"] = "{:02}/{:02}/{:02}".format(
            now.year,now.month,now.day
        )
        
        self.time["text"] = "{:02}:{:02}:{:02}".format(
            now.hour,now.minute,now.second
        )
        self.after(100,self.update)

    def delete_default(self):
        self.default.tkraise()
        self.info.tkraise()
        self.time.tkraise()

    def delete_navi(self):
        self.navi.tkraise()

if __name__ == '__main__':
    root = tkinter.Tk()
    root.title("Beetle Navi")
    root.geometry("1024x600")
    app = car_navi(master=root)
    root.mainloop()
