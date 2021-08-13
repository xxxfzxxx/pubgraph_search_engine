from tkinter import *
import time
from text_search import search
from graph_search import *
from py2neo import Graph, Node, Relationship
# from elasticsearch import Elasticsearch

LOG_LINE_NUM = 0

class MY_GUI():
    def __init__(self,init_window_name):
        self.init_window_name = init_window_name


    #设置窗口
    def set_init_window(self):
        self.init_window_name.title("Search Engine")          
        # self.init_window_name.geometry('200x200+280+280')       #1068x681 is window size, +10 +10 is position shows
        self.init_window_name['width']=400
        self.init_window_name['height']=400
        Label(self.init_window_name, text="Publication Search", font=('Arial', 20)).place(x=110,y=20)
        Label(self.init_window_name, text="title", font=('Arial', 17)).place(x=160,y=55)
        self.title = Text(self.init_window_name, width=40, height=1)
        self.title.place(x=50,y=85)
        Label(self.init_window_name, text="keyword", font=('Arial', 17)).place(x=145,y=110)
        self.keyword = Text(self.init_window_name, width=40, height=1)
        self.keyword.place(x=50,y=145)
        Label(self.init_window_name, text="year", font=('Arial', 17)).place(x=155,y=167)
        self.year = Text(self.init_window_name, width=40, height=1)
        self.year.place(x=50,y=195)
        # Label(self.init_window_name, text="keyword", font=('Arial', 17)).place(x=145,y=110)
        # self.keyword = Text(self.init_window_name, width=40, height=1)
        # self.keyword.place(x=50,y=145)
        # self.label2 = Label(self.init_window_name, text="title")
        # self.label2.grid(row=10, column=30)
        # self.log_label = Label(self.init_window_name, text="日志")
        # self.log_label.grid(row=12, column=0)
        #文本框
        # self.init_data_Text = Text(self.init_window_name, width=67, height=35)  #原始数据录入框
        # self.init_data_Text.grid(row=1, column=0, rowspan=10, columnspan=10)
        # self.result_data_Text = Text(self.init_window_name, width=70, height=49)  #处理结果展示
        # self.result_data_Text.grid(row=1, column=12, rowspan=15, columnspan=10)
        # self.log_data_Text = Text(self.init_window_name, width=66, height=9)  # 日志框
        # self.log_data_Text.grid(row=13, column=0, columnspan=10)
        # #按钮
        self.button = Button(self.init_window_name, text="Search", bg="lightblue", width=10,command=self.textsearch)  # 调用内部方法  加()为直接调用
        self.button.place(x=115, y = 245)


    #功能函数
    def textsearch(self):
        title = self.title.get(1.0,END).strip('\n')
        keyword = self.keyword.get(1.0,END).strip('\n')
        year = self.year.get(1.0,END).strip('\n')
        # if src:
        #     try:
        #         myMd5 = hashlib.md5()
        #         myMd5.update(src)
        #         myMd5_Digest = myMd5.hexdigest()
        #         #print(myMd5_Digest)
        #         #输出到界面
        #         self.result_data_Text.delete(1.0,END)
        #         self.result_data_Text.insert(1.0,myMd5_Digest)
        #         self.write_log_to_Text("INFO:str_trans_to_md5 success")
        #     except:
        #         self.result_data_Text.delete(1.0,END)
        #         self.result_data_Text.insert(1.0,"字符串转MD5失败")
        # else:
        #     self.write_log_to_Text("ERROR:str_trans_to_md5 failed")


    # Get current time
    def get_current_time(self):
        current_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        return current_time


def gui_start():
    init_window = Tk()           
    Engine = MY_GUI(init_window)
    Engine.set_init_window()
    init_window.mainloop()          #父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示


if __name__ == '__main__':
    gui_start()