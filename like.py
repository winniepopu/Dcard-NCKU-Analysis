from dcard import Dcard
import json
import pandas as pd

if __name__ == '__main__':
    dcard = Dcard()
    number=10000
    def like(number):
        article_metas = dcard.forums('ncku').get_metas(num=number, sort='new')
        with open('like.json','w+',encoding='utf-8-sig') as s:
            i=0
            like_list=[]
            a={"like_max":189,"id":0,"index":0,"title":'0'}  #預設一個較高的值讓夠高like的文章可以存進list
            for k in range(1):
                like_list.append(a)
        
            while (i<number):     #開始有title功能時
                for d in range(len(like_list)):
                    if article_metas[i]["likeCount"] > like_list[d]["like_max"]:
                        b={"like_max":article_metas[i]["likeCount"],"id":article_metas[i]["id"],"index":i,"title":article_metas[i]["title"]}
                        like_list.insert(d,b)
                        break
                i+=1

            while len(like_list)>10:    #只留下前十大
                like_list.pop()   
            
            for like in like_list:
                # print(like["title"]," : ",like["like_max"],end="\n")
                t1=json.dumps(like, indent=4,ensure_ascii=False)
                s.write(t1)

            s.write("\n文章網址: \n")
            for like in like_list:
                url=like["title"]+" : "+'https://www.dcard.tw/f/ncku/p/'+str(like["id"])+"\n"
                s.write(url)

            select_df = pd.DataFrame(like_list)
            out_df = select_df[select_df.loc[:,"like_max"] > 200] # 選出讚數超過 200 的文章  
            print(out_df)
    like(number)

