while True:
    print("[메뉴를 입력해 주세요]")
    num = int(input("1. 게임시작 2. 랭킹보기 3. 게임종료 >>> "))

    if num == 1:
        print("게임을 시작합니다")
    elif num == 2:
        print("랭킹 보기")
    elif num == 3:
        print("게임을 종료합니다")
        break
    else:
        print("다시 입력해 주세요")

    print()
