from dcard import Dcard
import json
import numpy as np
import pandas as pd 
from pandas import DataFrame 
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties 

if __name__ == '__main__':
    dcard = Dcard()
    number=10000

    def department(number):
        article_metas = dcard.forums('ncku').get_metas(num=number, sort='new')
        department={}   #建立科系的字典，key為科系，value為數量
        anony=0
        nonanony=0
        use_depart=0
        with open('department.text','w+',encoding='utf-8-sig') as s:
            i=0
            while(i<number):
                if article_metas[i]["anonymousDepartment"]==True:
                    anony+=1
                else:
                    nonanony+=1
                    if article_metas[i]["withNickname"]==False: 
                        use_depart+=1

                        depart=article_metas[i]["department"]   #紀錄該科系到變數depart

                        if  depart in department.keys() : #如果已有該科系的key
                            department[depart]+=1         #該系value+1
                        else:
                            department[depart]=1          #新增該系的key，value=1
                i+=1
            
            department_sorted=sorted(department.items(), key = lambda item:item[1],reverse=True) #將此字典翻轉
            data=[]
            labels=[]

            for j in range(10):
                data.append(department_sorted[j][1])
                labels.append(department_sorted[j][0])
            
            print("匿名 : ",anony,"\n不匿名 : ",nonanony,"\n使用科系:",use_depart)

            total="總共"+str(anony+nonanony)
            text=total+"\n 匿名:"+str(anony)+" 不匿名:"+str(nonanony)+" 使用科系: \n"+str(use_depart)+" 使用暱稱: \n"+str(nonanony-use_depart)+"\n"
            s.write(text)
            for j in department_sorted:
                s.write(str(j))             #紀錄科系
                s.write("\n")  

        # make diagram
            myfont = FontProperties(fname='C:/Windows/Fonts/MSYH.TTC') #引入中文字體
        # make anony diagram - pie chart
            label_annoy = ['Annoy','Use Nick Name','Use Department']
            separated = (0,0,.1)
            size = [anony,nonanony-use_depart,use_depart]              
            plt.title('成大板匿系比例圖',fontproperties=myfont)
            plt.pie(size , labels = label_annoy,autopct='%1.1f%%',explode=separated) 
            plt.axis('equal')
            plt.show()  
        # make department diagram - bar chart
            df = DataFrame(data, labels) 
            ax = df.plot(kind = 'barh', rot = 0,legend=False) 
            for label in ax.get_yticklabels() : 
                label.set_fontproperties(myfont) 
            ax.set_xlabel('Number of Posts')
            ax.set_ylabel('Depaetment')
            ax.invert_yaxis()
            plt.title('前十大高發文數之科系',fontproperties=myfont)
            plt.show()

    department(number)


  
