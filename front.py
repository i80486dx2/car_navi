import tkinter
import re
import datetime
import PIL.Image
import PIL.ImageTk
from PIL import Image, ImageTk
import read
import screen_shot
from IPython.core.page import page
import time

bg_color = "#7F7F7F"
navigation_bar_color = "#97D077"
previous_color = "#dcdcdc"
font_color = "white"


class car_navi(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master, bg="lightblue")
        self.data = read.get_info()  # API 情報入手
        self.num = 1  # ナビ情報の案内番号
        self.grid()

        # 各画面の生成
        self.menubar()
        self.navi()
        self.navigation()
        self.inst(0)
        self.default()

    # メニュー画面
    def menubar(self):
        menubar = tkinter.Frame(self, bg="white", width=200, height=600)
        menubar.grid(column=0, row=0)

        # アイコン
        self.menu_icon = ImageTk.PhotoImage(Image.open("./icon/home_icon.png"))
        self.search_icon = ImageTk.PhotoImage(
            Image.open("./icon/search_icon.png"))
        self.back_icon = ImageTk.PhotoImage(Image.open("./icon/back_icon.png"))
        self.car_icon = ImageTk.PhotoImage(Image.open("./icon/car_icon.png"))

        # メニューボタン
        self.button1 = tkinter.Button(
            menubar, command=lambda: self.changePage(self.default), width=130, height=146,
            image=self.menu_icon
        )
        self.button1.pack()

        # Naviボタン
        self.button2 = tkinter.Button(
            menubar, command=lambda: self.changePage(self.navi),  width=130, height=145,
            image=self.search_icon
        )
        self.button2.pack()

        # ボタン4
        self.button4 = tkinter.Button(
            menubar,  width=130, height=146,
            image=self.car_icon
        )
        self.button4.pack()

        # キャンセルボタン
        self.button3 = tkinter.Button(
            menubar,  width=130, height=145,
            image=self.back_icon
        )
        self.button3.pack()

    # デフォルト画面
    def default(self):
        self.default = tkinter.Frame(self, bg=bg_color, width=900, height=600)
        self.default.grid(column=1, row=0)

        #ビートルアイコン
        self.beetle_icon = ImageTk.PhotoImage(Image.open("./icon/beetle2.png"))
        self.beetle = tkinter.Label(
            self.default, image=self.beetle_icon , width=2000, height=650,
        )
        self.beetle.place(rely=-0.4, relx=-0.65)

        # 時計
        self.info = tkinter.Label(
            self.default, width=12, font=("Courier", 50, "bold"), bg=bg_color, fg=font_color
        )
        self.info.place(rely=0.7, relx=0.1)

        self.time = tkinter.Label(
            self.default, width=12, font=("Courier", 100, "bold"), bg=bg_color, fg=font_color
        )
        self.time.place(rely=0.8, relx=0.2)
        self.update()

    # ナビ開始画面
    def navi(self):
        self.navi = tkinter.Frame(self, bg=bg_color, width=900, height=600)
        self.navi.grid(column=1, row=0)

        # 画像生成
        # dest1 = "37.3980187,140.3879142"  # 郡山
        # dest2 = "37.5242475,139.9404067"  # 会津
        # screen_shot.make_photo(dest1,dest2)

        # 距離
        self.estimate_distance = tkinter.Label(
            self.navi, font=("Courier", 35, "bold"), bg=bg_color, fg=font_color
        )
        self.estimate_distance.place(rely=0.57, relx=0.05)

        self.estimate_distance["text"] = "距離:{:.1f}km".format(
            self.data[0][0]/1000
        )

        # 所用時間
        self.estimate_time = tkinter.Label(
            self.navi, font=("Courier", 35, "bold"), bg=bg_color, fg=font_color
        )
        self.estimate_time.place(rely=0.67, relx=0.05)

        self.estimate_time["text"] = "所用時間:{:.1f}分".format(
            self.data[0][1]/60
        )

        # 案内マップ(画像)
        self.ep = tkinter.PhotoImage(file="screen_shot.gif")

        self.estimate_photo = tkinter.Label(
            self.navi, image=self.ep
        )
        self.estimate_photo.place(rely=0.05, relx=0.49)

        # スタートボタン
        self.start_button = tkinter.Button(
            self.navi, text="Start", command=lambda: [self.changePage(self.navigation), self.inst(0)],
            font=("Courie", 50, "bold")
        )
        self.start_button.place(rely=0.85, relx=0.03, relwidth=0.9)

    # ナビ画面
    def navigation(self):
        self.navigation = tkinter.Frame(
            self, bg=bg_color, width=900, height=600)
        self.navigation.grid(column=1, row=0)

        # 終了
        self.finish = tkinter.Button(
            self.navigation, text="終了", command=lambda: self.inst(1),
            font=("Courie", 40, "bold")
        )
        self.finish.place(rely=0.85, relx=0.04, relwidth=0.22)

        # 右矢印
        self.right_arrow = tkinter.Button(
            self.navigation, text=">", command=lambda: self.inst(1),
            font=("Courie", 40, "bold")
        )
        self.right_arrow.place(rely=0.85, relx=0.7, relwidth=0.22)

        # ナビに戻る
        self.go_back_navi = tkinter.Button(
            self.navigation, text="ナビに戻る", command=lambda: self.inst(1),
            font=("Courie", 40, "bold")
        )
        self.go_back_navi.place(rely=0.85, relx=0.48, relwidth=0.22)

        # 左矢印
        self.left_arrow = tkinter.Button(
            self.navigation, text="<", command=lambda: self.inst(2),
            font=("Courie", 40, "bold")
        )
        self.left_arrow.place(rely=0.85, relx=0.26, relwidth=0.22)

    #残り距離表示用ウィンドウ
    def rest(self):
        self.rest = tkinter.Frame(
            self, width=400, height=300)
        self.rest.grid(column=1, row=0)

        self.rest_distance = tkinter.Label(
                self.rest,font=("Courier",40,"bold") ,bg=bg_color ,fg=font_color 
        )
        self.rest_distance.place(rely =0.2, relx=0.2)
        self.rest_distance["text"] = self.data[1][0]
        self.distance()


    # ナビのインストラクション・アローを表示
    def inst(self,state):
        # イメージ
        self.r_photo = ImageTk.PhotoImage(Image.open("./icon/right.png"))
        self.l_photo = ImageTk.PhotoImage(Image.open("./icon/left.png"))
        self.s_photo = ImageTk.PhotoImage(Image.open("./icon/straight.png"))
        self.u_photo = ImageTk.PhotoImage(Image.open("./icon/uturn.png"))

        # ナンバー管理
        if state == 0:
            self.num = 1

        elif state == 1:
            if self.num == len(self.data)-1:
                self.num = 1
            else:
                self.num = self.num + 1

        elif state == 2:
            if self.num == 1:
                self.num = len(self.data)-1
            else:
                self.num = self.num - 1
        
        if state != 0:
            self.instruction.destroy()
        
        # テキスト配置
        self.instruction = tkinter.Label(
            self.navigation,font=("Courier",40,"bold") ,bg=navigation_bar_color ,fg=font_color ,width= 41,height = 2 ,anchor="w" 
        )
        self.instruction.place(rely =0, relx=0.0)

        # テキスト処理
        text = self.data[self.num][2]
        text = text.replace("\u003c/b\u003e","").replace("\u003cwbr/\u003e","").replace("\u003cb\u003e","").replace("\u003cdiv style=\"font-size:0.9em\"\u003e","").replace("\u003c/div\u003e","")
        if len(text) > 16:
            text = text.replace(text[16:],"...")
        self.instruction["text"] = "  {}. ".format(self.num) + text

        # アロー表示
        self.arrow = tkinter.Label(
            self.navigation,image  = self.r_photo
        )
        self.arrow["bg"] = bg_color
        self.arrow.place(rely =0.2, relx=0.5)

        # イメージセット
        if len(self.data[self.num]) == 6:
            if "right" in self.data[self.num][5]:
                self.arrow.configure(image = self.r_photo)
            elif "uturn" in self.data[self.num][5]:
                self.arrow.configure(image = self.u_photo)
            elif "left" in self.data[self.num][5]:
                self.arrow.configure(image = self.l_photo)
            elif "straight" in self.data[self.num][5]:
                self.arrow.configure(image = self.s_photo)
            elif "merge" in self.data[self.num][5]:
                self.arrow.configure(image = self.r_photo)

    # デフォルト画面の時計表示の関数
    def update(self):
        now = datetime.datetime.now()

        self.info["text"] = "{:02}/{:02}/{:02}".format(
            now.year,now.month,now.day
        )
        
        self.time["text"] = "{:02}:{:02}:{:02}".format(
            now.hour,now.minute,now.second
        )
        self.after(100,self.update)

    # 選択ページを最上位に表示
    def changePage(self, page):
        page.tkraise()

    # ナビの距離表示
    def distance(self):
        # GPS連動距離表示
        num = self.data[self.num][0]
        self.rest_distance.destroy()
        self.rest_distance["text"] = num
        self.after(2000,self.distance()) 
        
if __name__ == '__main__':
    root = tkinter.Tk()
    root.title("Beetle Navi")
    root.geometry("1024x600")
    app = car_navi(master=root)
    root.mainloop()
