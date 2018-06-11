

import sys
from urllib.request import Request, urlopen
from datetime import *
import json

try:
    url = 'http://kickscar.cafe24.com:8080/myapp-api/api/user/list'
    #->json lib을 사용하여 이 String을 파이썬객체로 변경해주자

    request = Request(url)
    resp = urlopen(request)
    resp_body = resp.read().decode("utf-8")
    print(type(resp_body), " : ", resp_body) # type : str, http 전통적인 형식으로 읽어들인것

    json_result = json.loads(resp_body)
    print(type(json_result), " : ", json_result) # type : dict, json으로 body를 읽어들인것
    data = json_result['data']
    print(type(data), " : ", data) # type : list, data라는 key값을 통해 상응하는 value값 출력

except Exception as e:
    print('%s %s' % (e, datetime.now), file = sys.stderr)
