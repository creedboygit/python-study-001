test_list = [1, 2, 3, 4, 5]

if 3 in test_list:
    print("yes")
else:
    print("n0")

print()

if 6 not in test_list:
    print("yes")
else:
    print("no")

print()

if 6 not in test_list:
    test_list.append(6)

print(test_list)

print()

del test_list[5]

print(test_list)

print()

length = len(test_list)

print(length)
