
import sys
from urllib.request import Request, urlopen
from datetime import *

try :
    url = 'http://www.naver.com'
    request = Request(url)
    resp = urlopen(request)
    resp_body = resp.read().decode("utf-8")
    print(resp_body) #www.naver.com 첫화면의 소스가 출력됨 (브라우저 출력)
except Exception as e:
    print('%s %s' % (e,datetime.now), file=sys.stderr)

"""
System.out.println('Hell Word'); #-> standardout
write(0, "Hello World"); #
"""

