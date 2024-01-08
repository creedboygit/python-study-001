animals = []

print(animals)

animals = ["사자", "호랑이", "고양이", "강아지"]

print(animals)

name = animals[3]

print(name)

animals.append("쥐")

print(animals)

del animals[1]

print(animals)

animals2 = animals[1:3]

print(animals2)

animals3 = animals[0:3]

print(animals3)

animals_len = len(animals)

print(animals_len)

animals_len3 = len(animals3)

print(animals_len3)

animals.sort()

print(animals)

animals.sort(reverse=True)

print(animals)

animals.sort(reverse=False)

print(animals)

del animals[-1] # 마지막 데이터 삭제

print(animals)

animals.append("하마")
animals.append("뱀")

print(animals)

slicing = animals[1:3]

print(animals)
print(slicing)


