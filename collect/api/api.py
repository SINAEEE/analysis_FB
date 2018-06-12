
# FB API Wrapper Functions

from urllib.parse import urlencode
from .web_request import json_request

ACCESS_TOKEN="EAACEdEose0cBAIHGiZCi3Xm4M7wEFQ0deF2aAHSvn81vu1ZAWNeZA9dye46aFOtkrnniRBOD96X6ylfnoeXYkVBM3tftUpsLYBMHZAsDwD3rWuWPamUSjTCowX7XuWm0cSCQ9xefahnaOZCAgpoqjxvwh537pZAfvcbSvk0t8FlF0JkcdiTSyOhP6U4ggu4tYZD"
BASE_URL_FB_API = "https://graph.facebook.com/v3.0"


def fb_gen_url(
       base = BASE_URL_FB_API,
       node ='',
       **params):
    url = '%s/%s/?%s' % (base, node, urlencode(params))
    return url


def fb_name_to_id(pagename):
    url = fb_gen_url(node=pagename, access_token=ACCESS_TOKEN)
    json_result = json_request(url=url)
    return json_result.get("id")


def fb_fetch_posts(pagename, since, until):
    url = fb_gen_url(
        node=fb_name_to_id(pagename)+"/posts",
        fields='id,message,link,name,type,shares,reactions,created_time,comments.limit(0).summary(true).limit(0).summary(true)',
        since = since,
        until = until,
        limit = 50,
        access_token = ACCESS_TOKEN)

    json_result = json_request(url=url)
    #print(json_result)

    results = []
    isnext = True
    while isnext is True:
        json_result = json_request(url=url)

        paging = None if json_result is None else  json_result.get('paging')
        posts = None if json_result is None else json_result.get('data')

#        results = results + posts

        url = None if paging is None else paging.get("next")
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











