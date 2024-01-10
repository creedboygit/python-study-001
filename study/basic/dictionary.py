# 1. 승패 여부
# 2. 챔피언 이름
# 3. 킬
# 4. 데스
# 5. 어시스트

play_data = {
    'result': '승리',
    'champ_name': '티모',
    'kill': 13,
    'death': 9,
    'assist': 13,
}

print(play_data['result'])
print(play_data['champ_name'])

play_data['result'] = '패배'

print(play_data)

play_data['winner'] = '위너'

print(play_data)

del play_data['death']

print(play_data)
