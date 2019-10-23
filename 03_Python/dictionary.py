# 1. 딕셔너리 만들기(2가지)
lunch = {
    '중국집' : '032'
}
lunch = dict(중국집 = '032')

# 2.딕셔너리 추가하기
lunch['분식집'] = '031'

# 3. 딕셔너리 내용 가져오기 (2가지)
artists = {
    '아티스트' : {
        '민수' : '민수는 혼란스럽다',
        '아이유' : '좋은날'
    }
}
# 민수의 대표곡은 ?
# print(artists['아티스트']['민수'])
# print(artists.get('아티스트').get('아이유'))


# 1.4 딕셔너리 반복문 활용하기 
# 1.4.1 기본 활용
print(lunch) 
for key in lunch:
    print(key)              # key 출력됨
    print(lunch[key])       # key로 value 추출


# 1.4.2 Key, Value 모두 가져오기
for key,value in lunch.items():
    print(key,value)




# 1.4.3 Value만 가져오기
for value in lunch.items():
    print(value)
    # =>중국집, 분식집

# 1.4.4 key만 가져오기
for value in lunch.items():
    print(key)