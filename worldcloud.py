import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba
from scipy.misc import imread

def make_wordcloud(readtext,imagename):
 
    text_from_file_with_apath = open(readtext,encoding='utf-8-sig').read()
    
    wordlist_after_jieba = jieba.cut(text_from_file_with_apath, cut_all = True)
    wl_space_split = " ".join(wordlist_after_jieba)    # jieba中文分词

    stopwords = set()    #停用詞
    stopwords.update(['https:imgur'],['https'],['imgur'],['jpg'],['com'],['dcard'],['tw'],['www'],['http'],['png']) 

    my_wordcloud = WordCloud(max_font_size = 35,mask=imagename,stopwords=stopwords,font_path='C:/Windows/Fonts/MSYH.TTC').generate(wl_space_split) #max_font_size:最大的文字大小
    
    process_word = WordCloud.process_text(my_wordcloud, wl_space_split)  # 查看詞頻，方便重新增加停用词
    sort = sorted(process_word.items(),key=lambda e:e[1],reverse=True) # sort為list
    print(sort[:50])

    plt.imshow(my_wordcloud,interpolation='bilinear')
    plt.axis("off")
    plt.show()

while True:
    mask_or_not=input("Do you want to use a Mask? enter Y or N ")
    if mask_or_not=="Y": 
        imagename= imread("D.png")   #mask遮罩圖
        break
    elif mask_or_not =="N":
        imagename=None
        break
    else:
        print("error,please enter the correct character")

readtext="content.txt"
make_wordcloud(readtext,imagename)
