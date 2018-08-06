from dcard import Dcard
import json
import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.font_manager import FontProperties 

if __name__ == '__main__':

    dcard = Dcard()
    myfont = FontProperties(fname='C:/Windows/Fonts/MSYH.TTC')      #製作圖表時引入中文字

    def gender(number):
    article_metas = dcard.forums('ncku').get_metas(num=number, sort='new')
        male=0
        female=0
        with open('gender.txt','w+',encoding='utf-8-sig') as s:
            i=0
            while (i<number):

                if article_metas[i]["gender"]=="M":
                    male+=1
                else:
                    female+=1
                i+=1

        # record into gender.txt
            text="男 : "+str(male)+"\n女 : "+str(female)
            s.write(text)

        # print
            print("男 : ",male)
            print("女 : ",female)
 
        # make diagram
            labels = ['Male','Female']
            size = [male,female]
            plt.title('成大板發文男女比',fontproperties=myfont)
            plt.pie(size , labels = labels,autopct='%1.1f%%') 
            plt.axis('equal')
            plt.show()  
    
    number=10000
    gender(number)