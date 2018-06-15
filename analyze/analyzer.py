import json
import re  # 정규표현식, 어떤 string을 표현한 식(regular expression)
from konlpy.tag import Twitter
from collections import Counter


def json_to_str(filename, key):
    jsonfile = open(filename, 'r', encoding='utf-8')
    json_string = jsonfile.read()
    jsonfile.close()

    data = ''

    # print(json_string) #test
    # 크롤러에선 네트워크에서, analyzer에선 파일에서 json내용을 받아옴
    json_data = json.loads(json_string)  # json string을 파이썬에서 다루는 데이터로 parsing (string ->파이썬객체)
    # print(json_data) #test

    for item in json_data:
        value = item.get(key)  # 메세지 부분만 수집
        if value is None:
            continue

        data += re.sub(r'[^\w]', '', value)  # sub:대체하라, r:정규표현식, value에서 공백문자가 발생되면 제거하기

    return data


def count_wordfreq(data): #data로부터 각 단어의 갯수 추출
    twitter = Twitter()
    nouns = twitter.nouns(data)
    print(nouns)

    count = Counter(nouns)
    return count
