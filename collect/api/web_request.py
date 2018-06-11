
import sys
from urllib.request import Request, urlopen
from datetime import *
import json




def print_error(e):
    print('%s %s' % (e, datetime.now), file=sys.stderr)



def html_request(url='',
                 encoding='utf-8',
                 success=None,
                 error=print_error
                 #error=lambda e: print('%s %s' % (e, datetime.now), file=sys.stderr) #람다로 정의 가능
                 ):
    try:
        request = Request(url)
        resp = urlopen(request)
        html = resp.read().decode(encoding)

        print('%s : suceess for request[%s]' % (datetime.now(), url))

        if(callable(success) is False): #호출이가능한지
            return html

            success(html)

    except Exception as e:
        if callable(error) is True:
            error(e)
        #print('%s %s' % (e, datetime.now), file=sys.stderr)




def json_request(url='',
                 encoding='utf-8',
                 success=None,
                 error=lambda e: print('%s %s' % (e, datetime.now), file=sys.stderr)
                 ):
    try:
        request = Request(url)
        resp = urlopen(request)
        json_body = resp.read().decode(encoding)
        json_result = json.loads(json_body)

        print('%s : suceess for request[%s]' % (datetime.now(), url))

        if(callable(success) is False):
            return json_result

        success(json_result)

    except Exception as e:
        if callable(error) is True:
            error(e)





