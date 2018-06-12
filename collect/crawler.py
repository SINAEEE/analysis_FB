import os
import json
from datetime import datetime, timedelta
from .api import api

RESULT_DIRECTORY = '__results__/crawling'

def preprocess_post(post): #데이터전처리 : 공개할필요없는 함수
    # 공유수
    if 'shares' not in post:
        post['count shares'] = 0
    else:
        post['count shares'] = post['shares']['count']

    # 전체 리액션 수
    if 'reaction' not in post:
        post['count_reactions'] = 0
    else:
        post['count_reactions'] = post['reactions']['summary']['total_count']

    # 전체 코멘트 수
    if 'comments' not in post:
        post['count_comments'] = 0
    else:
        post['count_comments'] = post['comments']['summary']['total_count']

    # KST = UTC + 9
    kst = datetime.strptime(post['created_time'],'%Y-%m-%dT%H:%M:%S+0000')
    kst = kst + timedelta(hours=9)
    post['created_time'] = kst.strftime('%Y-%m-%d %H:%M:%S:')



def crawling(pagename, since, until):
    results = []
    filename = '%s_%s_%s_%s.json' % (RESULT_DIRECTORY,pagename,since,until)

    for posts in api.fb_fetch_posts(pagename, since, until):
        for post in posts: #개별전처리(50개씩받아서 하나씩)
            preprocess_post(post)

        results += posts

    #save results to file(저장/적재)
    #outfile = open(filename, 'w', encoding='utf-8')
    with open(filename, 'w', encoding='utf-8') as outfile:
        json_string = json.dumps(results, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(json_string)


if os.path.exists(RESULT_DIRECTORY) is False:
    os.makedirs(RESULT_DIRECTORY)

