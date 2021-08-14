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
        self.graph = Graph('bolt://40.114.125.234:7687',username='neo4j',password='123456aa')
        self.init_window_name.title("Search Engine")          
        self.init_window_name.geometry('240x240+280+280')       #1068x681 is window size, +10 +10 is position shows
        Label(self.init_window_name, text="Publication Search", font=('Arial', 20)).grid(row=0, column=4)
        Label(self.init_window_name, text="title", font=('Arial', 17)).grid(row=3, column=4)
        self.title = Text(self.init_window_name, width=20, height=1)
        self.title.grid(row=5,column=4,rowspan = 4)
        Label(self.init_window_name, text="keyword", font=('Arial', 17)).grid(row=9, column=4)
        self.keyword = Text(self.init_window_name, width=20, height=1)
        self.keyword.grid(row=11,column=4,rowspan = 4)
        Label(self.init_window_name, text="year", font=('Arial', 17)).grid(row=15, column=4)
        self.year = Text(self.init_window_name, width=20, height=1)
        self.year.grid(row=17, column=4)
        self.button = Button(self.init_window_name, text="Search", bg="lightblue", width=10,command=self.textsearch)  # 调用内部方法  加()为直接调用
        self.button.grid(row=19, column=4)

    #功能函数
    def textsearch(self):
        title = self.title.get(1.0,END).strip('\n')
        keyword = self.keyword.get(1.0,END).strip('\n')
        year = self.year.get(1.0,END).strip('\n')
        res = None
        if (keyword == "") :
            print("fuck")
            if year=="":
                res = search(title, title_only=True)
            else:
                res = search(title, start_year = year, title_only=True)
    
        title = [str(hit['_source']['title']) for hit in res['hits']['hits']]
        scores = [hit['_score'] for hit in res['hits']['hits']]
        index = [hit['_index'] for hit in res['hits']['hits']]
        year = [hit['_source']['year'] for hit in res['hits']['hits']]
        n_citation = [hit['_source']['n_citation'] for hit in res['hits']['hits']]
        res_window = Tk()
        res_window.title('result')
        for i in range(10):
            print('result',i+1,':','score:',scores[i])
            print('index: ', index[i])
            print('title:',title[i])
            print('year: ', year[i])
            print('n_citation: ', n_citation[i])
            # print('authors:',authors[i])
            print('--------------------------------------------------------------')
        res_window.geometry('600x681+400+400')       #1068x681 is window size, +10 +10 is position shows
        Label(res_window, text="Search Result -- Top 5", font=('Arial', 20)).grid(row=0, column=5)

        Label(res_window, text="Result 1", font=('Arial', 17)).grid(row=3, column=4)
        res1 = Text(res_window, width=40, height=5)
        res1.grid(row=5,column=0,rowspan = 4, columnspan=10)
        res1.insert(1.0, ("scores:" + str(scores[0]) + '\ntitle:' + title[0] + '\nyear:'+str(year[0])+'\nn_citation:'+str(n_citation[0])))
        Label(res_window, text="Related To", font=('Arial', 17)).grid(row=3, column=40)
        rel1 = Text(res_window, width=25, height=5)
        rel1.grid(row=5,column=40,rowspan = 4, columnspan=4)
        aso1 = associate_paper(self.graph, title[0])
        while (len(aso1)<=2):
            aso1.append("")
        rel1.insert(1.0, aso1[0]+'\n'+aso1[1])

        Label(res_window, text="Result 2", font=('Arial', 17)).grid(row=13, column=4)
        res2 = Text(res_window, width=40, height=5)
        res2.grid(row=15,column=0,rowspan = 4, columnspan=10)
        res2.insert(1.0, ("scores:" + str(scores[1]) + '\ntitle:' + title[1] + '\nyear:'+str(year[1])+'\nn_citation:'+str(n_citation[1])))
        Label(res_window, text="Related To", font=('Arial', 17)).grid(row=13, column=40)
        rel2 = Text(res_window, width=25, height=5)
        rel2.grid(row=15,column=40,rowspan = 4, columnspan=4)
        aso2 = associate_paper(self.graph, title[1])
        while (len(aso2)<=2):
            aso2.append("")
        rel2.insert(1.0, aso2[0]+'\n'+aso2[1])
        
        Label(res_window, text="Result 3", font=('Arial', 17)).grid(row=23, column=4)
        res3 = Text(res_window, width=40, height=5)
        res3.grid(row=25,column=0,rowspan = 4, columnspan=10)
        res3.insert(1.0, ("scores:" + str(scores[2]) + '\ntitle:' + title[2] + '\nyear:'+str(year[2])+'\nn_citation:'+str(n_citation[2])))
        Label(res_window, text="Related To", font=('Arial', 17)).grid(row=23, column=40)
        rel3 = Text(res_window, width=25, height=5)
        rel3.grid(row=25,column=40,rowspan = 4, columnspan=4)
        aso3 = associate_paper(self.graph, title[2])
        while (len(aso3)<=2):
            aso3.append("")
        rel3.insert(1.0, aso3[0]+'\n'+aso3[1])

        Label(res_window, text="Result 4", font=('Arial', 17)).grid(row=33, column=4)
        res4 = Text(res_window, width=40, height=5)
        res4.grid(row=35,column=0,rowspan = 4, columnspan=10)
        res4.insert(1.0, ("scores:" + str(scores[3]) + '\ntitle:' + title[3] + '\nyear:'+str(year[3])+'\nn_citation:'+str(n_citation[3])))
        Label(res_window, text="Related To", font=('Arial', 17)).grid(row=33, column=40)
        rel4 = Text(res_window, width=25, height=5)
        rel4.grid(row=35,column=40,rowspan = 4, columnspan=4)
        aso4 = associate_paper(self.graph, title[3])
        while (len(aso4)<=2):
            aso4.append("")
        rel4.insert(1.0, aso4[0]+'\n'+aso4[1])

        Label(res_window, text="Result 5", font=('Arial', 17)).grid(row=43, column=4)
        res5 = Text(res_window, width=40, height=5)
        res5.grid(row=45,column=0,rowspan = 4, columnspan=10)
        res5.insert(1.0, ("scores:" + str(scores[4]) + '\ntitle:' + title[4] + '\nyear:'+str(year[4])+'\nn_citation:'+str(n_citation[4])))
        Label(res_window, text="Related To", font=('Arial', 17)).grid(row=43, column=40)
        rel5 = Text(res_window, width=25, height=5)
        rel5.grid(row=45,column=40,rowspan = 4, columnspan=4)
        aso5 = associate_paper(self.graph, title[4])
        while (len(aso5)<=2):
            aso5.append("")
        rel5.insert(1.0, aso5[0]+'\n'+aso5[1])

        res_window.mainloop()
            

def gui_start():
    init_window = Tk()           
    Engine = MY_GUI(init_window)
    Engine.set_init_window()
    init_window.mainloop()          #父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示


if __name__ == '__main__':
    gui_start()