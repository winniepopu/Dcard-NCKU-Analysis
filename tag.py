from dcard import Dcard
import json

if __name__ == '__main__':
    dcard = Dcard()

    def tag():
        number=4500
        with open('topic.txt','w+',encoding='utf-8-sig') as s:
            article_metas = dcard.forums('ncku').get_metas(num=number, sort='new')
            i=0
            count=0
            A=set()         #紀錄tag的集合
            topic={}        #建立tag的dict，key為tag，value為數量
            
            while (article_metas[i]["id"]>=228480142):  #首篇有tag的文章  
                if article_metas[i]["topics"]: # 當topic不為空集合時
                    for j in range(len(article_metas[i]["topics"])):
                        tags=article_metas[i]["topics"][j]
                    count+=1
                    A.add(tags)

                    if tags in topic.keys() : # 如果已有該tag
                        topic[tags]+=1        
                    else:
                        topic[tags]=1
                i+=1
            
            print("不重複tag數",len(A))  # 不重複tag數為len(A)個
            print("總tag數",count)            # 總tag數為count個
            key_list=list(topic)    # Dict -> List
            topic_sorted=sorted(topic.items(), key = lambda item:item[1],reverse=True)
            
            for j in range(50):             #將前50常用tag存入topic.txt
                text=str(j+1)+"\t- "+str(topic_sorted[j][0])+"\t\t: "+str(topic_sorted[j][1])+"\n"
                s.write(text)
            for topic in range(20):         #顯示前20常用tag     
                print(topic+1,"- ",topic_sorted[topic][0],topic_sorted[topic][1])
    tag()




    

