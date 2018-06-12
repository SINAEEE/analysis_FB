
# Test for web_request.json_request


from analysis_FB.collect.api import web_request as wr


#html_request("http://www.naver.com")
#json_request('http://kickscar.cafe24.com:8080/myapp-api/api/user/list')


url='http://kickscar.cafe24.com:8080/myapp-api/api/user/list'

"""
# 3방식
def error_fetch_user_list(e):
    print(e)

wr.json_request(url=url, error=error_fetch_user_list)
"""



# 2 방식
def sucess_fetch_userlist(response):
    print(response)
    
wr.json_request(url=url, success=sucess_fetch_userlist)




"""
#1 방식
json_result = wr.json_request(url)
print(json_result)
"""

