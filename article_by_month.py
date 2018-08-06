from dcard import Dcard
import json
import numpy as np
import pandas as pd 
from pandas import DataFrame 
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties 

if __name__ == '__main__':

    dcard = Dcard()
    number=11500
    def articles_month():
        with open('month.text','a+',encoding='utf-8-sig') as s:
            article_metas = dcard.forums('ncku').get_metas(num=number, sort='new')
            i=0
            month_count=[0]*13
            while (i<number):
                
                date=article_metas[i]["createdAt"]      
                index=[5,6]        #日期形式: "2018-07-21T15:41:03.486Z"
                month=''           #預設月份為空字串

                if date[3]=='8' and date[6]=='8':   #不記2018年8月
                    pass
                else:
                    for j in index:
                        digit=date[j]
                        month+=digit
                    month=int(month)          #記錄該文章月份，並轉為int

                for k in range(1,13):
                    if month == k:      
                        month_count[k]+=1      #該月份文章數+1
                i+=1

            month_count[7]=773                 #107/7 實質為773篇
            month_index=0
            for num in month_count:
                if num!=0:
                    result=str(month_index)+"月: "+str(num)+"篇\n"
                    s.write(result)
                month_index+=1

        # make diagram
            myfont = FontProperties(fname='C:/Windows/Fonts/MSYH.TTC') 
            data=[]
            labels=[]

            for j in range(8,13):                   #106/8 - 106/12
                text="106/"+str(j)
                labels.append(text)                 #x軸label
                data.append(month_count[j])         #每月發文數記到list

            for k in range(1,8):                    #107/1 - 107/7
                text="107/"+str(k)
                labels.append(text)
                data.append(month_count[k])

            df = DataFrame(data, labels) 
            ax = df.plot(kind = 'bar', rot = 0,legend=False)  #bar chart ,legend:不要有圖例
            ax.set_xlabel('month')
            ax.set_ylabel('posts')
            plt.title('過去一年Dcard成大板每月發文數',fontproperties=myfont)
            plt.show()

    articles_month()