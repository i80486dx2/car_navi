import tkinter
import datetime
import PIL.Image, PIL.ImageTk
import read
import screen_shot

class car_navi(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master, bg="lightblue")
        self.data = read.get_info()  #API 情報入手
        self.num = 1 #ナビ情報の案内番号
        self.grid()
        #各画面の生成
        self.menubar()
        self.navi()
        self.navigation()
        self.default()

    def menubar(self):
        menubar = tkinter.Frame(self, bg="gray", width=200, height=600)
        menubar.grid(column=0, row=0)

        #メニューボタン
        self.button1 = tkinter.Button(
            menubar, text="Menu", command=lambda : self.raise_default(), width=15, height=11,
            font=("Courie")
        )
        self.button1.pack(padx=9, pady=10 )

        #Naviボタン
        self.button2 = tkinter.Button(
            menubar, text="Navi", command=lambda : self.raise_navi() ,  width=15, height=11,
            font=("Courie")
        )
        self.button2.pack(padx=9, pady=10)

        #キャンセルボタン
        self.button3 = tkinter.Button(
            menubar, text="Cancel",  width=15, height=11,
            font=("Courie")
        )
        self.button3.pack(padx=9, pady=10)

    def default(self):
        self.default = tkinter.Frame(self, bg="#dcdcdc", width=900, height=600)
        self.default.grid(column=1, row=0)

        #時計
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

        #画像生成
        #dest1 = "37.3980187,140.3879142"  # 郡山
        #dest2 = "37.5242475,139.9404067"  # 会津
        #screen_shot.make_photo(dest1,dest2)

        #距離 
        self.estimate_distance = tkinter.Label(
            self,font=("Courier",35,"bold") ,bg="#dcdcdc",
        )
        self.estimate_distance.place(rely =0.57, relx=0.18)

        self.estimate_distance["text"] = "距離:{:.1f}km".format(
            self.data[0][0]/1000
        )

        #所用時間
        self.estimate_time = tkinter.Label(
            self,font=("Courier",35,"bold") ,bg="#dcdcdc",
        )
        self.estimate_time.place(rely =0.67, relx=0.18)

        self.estimate_time["text"] = "所用時間:{:.1f}分".format(
            self.data[0][1]/60
        )

        #案内マップ(画像)    
        self.ep = tkinter.PhotoImage(file="screen_shot.gif")

        self.estimate_photo = tkinter.Label(
            self,image=self.ep
        )
        self.estimate_photo.place(rely =0.05, relx=0.55)

        #スタートボタン
        self.start_button = tkinter.Button(
            self.navi, text="Start",command=lambda : self.raise_navigation() , 
            font=("Courie",50,"bold")
        )
        self.start_button.place(rely =0.85, relx=0.03, relwidth = 0.9)

    def navigation(self):
        self.navigation = tkinter.Frame(self, bg="#dcdcdc", width=900, height=600)
        self.navigation.grid(column=1, row=0)

        #ナビのインストラクションを表示
        self.inst(0)

        #右矢印
        self.right_arrow = tkinter.Button(
            self.navigation, text=">",command=lambda : self.inst(1) , 
            font=("Courie",50,"bold")
        )
        self.right_arrow.place(rely =0.85, relx=0.75, relwidth = 0.2)

        #左矢印
        self.left_arrow = tkinter.Button(
            self.navigation, text="<",command=lambda : self.inst(2) , 
            font=("Courie",50,"bold")
        )
        self.left_arrow.place(rely =0.85, relx=0.03, relwidth = 0.2)

    #ナビのインストラクションを表示
    def inst(self,state):
        if state == 0:
            self.num = self.num
        elif state == 1:
            self.num = self.num + 1
        elif state == 2:
            self.num = self.num - 1

        self.instruction = tkinter.Label(
            self,font=("Courier",35,"bold") ,bg="#dcdcdc"
        )
        self.instruction.place(rely =0.05, relx=0.2)
        text = self.data[self.num][2]
        text = text.replace("\u003c/b\u003e","").replace("\u003cwbr/\u003e","").replace("\u003cb\u003e","")
        self.instruction["text"] = text
    #デフォルト画面の時計表示の関数
    def update(self):
        now = datetime.datetime.now()

        self.info["text"] = "{:02}/{:02}/{:02}".format(
            now.year,now.month,now.day
        )
        
        self.time["text"] = "{:02}:{:02}:{:02}".format(
            now.hour,now.minute,now.second
        )
        self.after(100,self.update)

    #デフォルト画面を最上位に表示
    def raise_default(self):
        self.default.tkraise()
        self.info.tkraise()
        self.time.tkraise()

    #ナビ確認画面を最上位に表示
    def raise_navi(self):
        self.navi.tkraise()
        self.estimate_distance.tkraise()
        self.estimate_time.tkraise()
        self.estimate_photo.tkraise()

    #ナビゲーション画面を最上位に表示
    def raise_navigation(self):
        self.navigation.tkraise()
        
if __name__ == '__main__':
    root = tkinter.Tk()
    root.title("Beetle Navi")
    root.geometry("1024x600")
    app = car_navi(master=root)
    root.mainloop()
