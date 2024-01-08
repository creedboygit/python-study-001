price = int(input("삼성전자의 현재 가격은? >>> "))

if price >= 90000:
    print("매도합니다.")
elif price >= 80000:
    print("대기중입니다.")
else:
    print("매수합니다.")
