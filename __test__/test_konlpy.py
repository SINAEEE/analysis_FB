
from konlpy.tag import Kkma

kkma = Kkma()

sentences = kkma.sentences(u'네 안녕하세요 반갑습니다.')
print(sentences)

nouns = kkma.nouns(u'명사만을 추출하여 다빈도 분석을 합니다.')
print(nouns)

pos = kkma.pos('오류보고는 실행환경, 에러메시지와 함께 설명을 최대상세히')
print(pos)