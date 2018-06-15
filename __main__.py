
import collect
import analyze
import visualize

#from collect import crawler as cw


if __name__ == '__main__':

    items = [
        {'pagename':'jtbcnews','since':'2017-01-01','until':'2017-12-31'},
        {'pagename': 'chosun', 'since':'2017-01-01', 'until':'2017-12-31'}
    ]


    # 데이터 수집(collection)
    for item in items:
        resultfile = collect.crawling(**item, fetch=False)
        item['resultfile'] = resultfile

    """
    collect.crawling("jtbcnews",
                "2017-01-01",
                "2017-12-31")
    """

    #데이터 분석(analysis)
    for item in items:
        data = analyze.json_to_str(item['resultfile'],'message')
        #print(data)
        item['count_wordfreq'] = analyze.count_wordfreq(data)
        print(item['count_wordfreq'])

        #item['count_wordfreq'] = analyze.count_wordfreq(data)   #각 단어에 대한 갯수

    """
    for item in items:
        print(item['resultfile'])
    """
    #데이터 시각화 (visualization)



#cw.crawling("jtbcnews","2017-01-01","2017-12-31")

#print('RUN analysis_FB..')