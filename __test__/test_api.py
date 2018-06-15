
from analysis_FB.collect.api import api

"""
#url=api.fb_gen_url(node='jtbcnews/posts', a=10, b=20,s='sinae')
url=api.fb_gen_url(node='jtbcnews',a=10,b=20)
print(url)
"""

"""
id=api.fb_name_to_id("jtbcnews")
print(id)
"""

"""
api.fb_fetch_posts("jtbcnews",'2017-01-01','2017-03-31')
"""

"""
results = api.fb_fetch_posts("jtbcnews",'2017-01-01','2017-12-31')
print(len(results))
"""


#yield 사용
for posts in api.fb_fetch_posts("jtbcnews",'2017-01-01','2017-12-31'):
    print(posts)
