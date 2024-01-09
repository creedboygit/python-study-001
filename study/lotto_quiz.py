import random

lotto_num = []  # 빈 로또 번호 리스트 생성


def get_random_number():
    number = random.randint(1, 45)
    return number


count = 0  # 횟수를 저장할 변수

# for i in range(6):  # 0, 1, 2, 3, 4, 5
# 무한 반복
while True:

    if count > 5:
        break

    random_number = get_random_number()  # 로또 번호 하나를 뽑는다.

    if random_number not in lotto_num:  # 로또 번호 리스트 안에 뽑은 로또 번호가 없으면
        lotto_num.append(random_number)  # 로또 번호 리스트에 뽑은 로또 번호를 추가해라
        count += 12

lotto_num.sort()
print(lotto_num)
