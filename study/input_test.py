from datetime import datetime

x = input("숫자1을 입력해 주세요 >>> ")
y = input("숫자2를 입력해 주세요 >>> ")

print("quiz1 : " + str(int(x) + int(y)))

print()

a = int(input("숫자3을 입력해 주세요 >>> "))
b = int(input("숫자4를 입력해 주세요 >>> "))

print("quiz2 : " + str(a + b))

print()

birth_year = int(input("태어난 연도를 입력해 주세요 >>> "))
# age = str(2024 - birth_year + 1)
age = str(datetime.today().year - birth_year + 1)
print("당신의 나이는 " + age + "세입니다.")
