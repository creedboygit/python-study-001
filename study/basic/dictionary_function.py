# 1. 승패 여부
# 2. 챔피언 이름
# 3. 킬
# 4. 데스
# 5. 어시스트

play_data = {
    "result": "승리1",
    "champ_name": "티모",
    "kill": 13,
    "death": 9,
    "assist": 13,
}

for key in play_data.keys():
    print(key)

print()

for value in play_data.values():
    print(value)

print()

for key, value in play_data.items():
    print(key, value)
