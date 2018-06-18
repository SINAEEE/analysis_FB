
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
        #print(resultfile)
        item['resultfile'] = resultfile


    """
    collect.crawling("jtbcnews",
                "2017-01-01",
                "2017-12-31")
    """


    #데이터 분석(analysis)
    for item in items:
        #print(item)
        data = analyze.json_to_str(item['resultfile'],'message')
        item['count_wordfreq'] = analyze.count_wordfreq(data)   #각 단어에 대한 갯수
        #print(item['count_wordfreq'])

    """
        for item in items:
            print(item['resultfile'])
    """

    #데이터 시각화 (visualization)
    for item in items:
        count = item['count_wordfreq']
        count_m50 = dict(count.most_common(50))
        #Counter클래스의 most_common()메소드 : 등장한 횟수를 내림차순으로 정리하여 보여줌
        #print(count_m50)

        filename = "%s_%s_%s" % (item['pagename'],item['since'],item['until'])
        visualize.wordcloud(filename, count_m50)
        visualize.graph_bar(
            #title='JTBC News 단어 빈도분석',
            values=list(count_m50.values()),
            ticks=list(count_m50.keys()),
            showgrid=False, #grid를 보일건지 여부
            filename=filename,
            showgraph=False
        )
        #print(count_m50)



#cw.crawling("jtbcnews","2017-01-01","2017-12-31")

#print('RUN analysis_FB..')