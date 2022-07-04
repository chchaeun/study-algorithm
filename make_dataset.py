# id, name, email, password

import random
import csv

# 필요한 key 리스트로 만들기

datas = [['id', 'name', 'email', 'password']]

# 랜덤으로 가져올 것들
first_name = ['Brad', 'Peter', 'Tom', 'Alex']
last_name = ['James', 'Alban', 'Holland', 'Potter']

for i in range(5):
    # first name 인덱스 랜덤으로 가져오기
    random1 = random.randrange(0, len(first_name))

    # last name 인덱스 랜덤으로 가져오기
    random2 = random.randrange(0, len(last_name))

    # 알파벳 소문자 랜덤으로 가져오기 (아스키코드)
    random_lowercase = chr(random.randrange(97, 123))

    # 세자리 수 숫자 랜덤으로 가져오기
    random_num = str(random.randrange(100, 1000))

    data = [i, first_name[random1] + ' ' + last_name[random2], random_lowercase + random_num + '@gmail.com',
            random_lowercase.upper() + random_lowercase + random_num * 1 + '!']

    datas.append(data)

with open('./data1.csv', 'w', encoding='UTF-8') as f:
    w = csv.writer(f)

    for d in datas:
        w.writerow(d)
