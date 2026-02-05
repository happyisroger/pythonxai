L1 = []
print([])  # blank list

L2 = [1, 2, 3, 4, 5]
print(L2)  # number list

L3 = ["apple", "banana", "berry"]
print(L3)  # word list

L4 = [1, "apple", True, 3.14]
print(L4)  # mixed list

L5 = [1, 2, 3, [4, 5]]
print(L5)  # list 'n list

# select things in a list
print(L5[1])  # 2
print(L5[3])  # [4, 5]
print(L5[3][0])  # 4

L6 = [1, 2, 3, "a", "b", "c"]
L7 = L6[::2]  # spaced usage
print(L7)  # [1, 3, b]
L8 = L6[1:4]
print(L8)  # [2, 3, "a"]
L9 = L6[1:4:2]
print(L9)  # [2, "a"]
