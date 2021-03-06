
# FB API Wrapper Functions

from urllib.parse import urlencode
from .web_request import json_request
#from config import CONFIG

ACCESS_TOKEN="EAACEdEose0cBAAtvdxF9HF9N8Vl8lMQV8ewcOZBtM2hILiTZB5ITVgxApJaKwQ4WcmzRDGd3CMcqloF9waeeLq2AfEa0P2bKskmPasys1bazKjjAPy9COGFGgM6MiOGHg7ZBAyZConFiItN2UWcoYZAfMaB4faysT9cEuyLIC6QyrtvL99eTvUub7P0zGyOIZD"
BASE_URL_FB_API = "https://graph.facebook.com/v3.0"


def fb_gen_url(
       base=BASE_URL_FB_API,
       node ='',
       **params):
    url = '%s/%s/?%s' % (base, node, urlencode(params))
    return url


def fb_name_to_id(pagename):
    url = fb_gen_url(node=pagename, access_token=ACCESS_TOKEN)
    json_result = json_request(url=url)
    return json_result.get("id")


def fb_fetch_posts(pagename, since, until): #매개변수예시 : "jtbcnews",'2017-01-01','2017-12-31'
    url = fb_gen_url(
        node=fb_name_to_id(pagename)+"/posts",
        #fields='id,message,link,name,type,shares,reactions,created_time,comments.limit(0).summary(true).limit(0).summary(true)',
        since = since,
        until = until,
        limit = 50,
        access_token=ACCESS_TOKEN)

    json_result = json_request(url=url)
    #print(json_result)


    results = []
    isnext = True
    while isnext is True:
        json_result = json_request(url=url)

        paging = None if json_result is None else json_result.get('paging')
        posts = None if json_result is None else json_result.get('data')

        results = results + posts

        url = None if paging is None else paging.get("next")
        #next속성은 cursor 파라미터가 포함된 전체 url
        #끝과 처음을 판별하기 위해서는 next 또는 privious 존재유무로 판단하면 됨
        isnext = url is not None

        yield posts

#    return results




"""
    while isnext is True:
        json_result = json_request(url=url)
        paging = None
        if json_result is None:
            paging = None
        else:
            paging = json_result.get('paging')
"""











