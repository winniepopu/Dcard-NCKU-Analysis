from dcard import Dcard
import json

if __name__ == '__main__':
    dcard=Dcard()
    number=10000
    metas = dcard.forums('ncku').get_metas(num=number,sort='new')

    def collect_ids(metas):
        return [meta['id'] for meta in metas]

    def content(number):
        ids = dcard.forums('ncku').get_metas(num=number, callback=collect_ids)

        with open('content.txt','w+',encoding='utf-8-sig') as f:
            articles = dcard.posts(ids).get(comments=False, links=False)
            for article in articles.result():
                f.write(article['content'])
                
    content(number)

    