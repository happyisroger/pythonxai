# weird ahh calculations

a = 10
b = 3
a += b  # a = a + b
print("a += b 的結果:", a)

a = 10
b = 3
a -= b  # a = a - b
print("a -= b 的結果:", a)

a = 10
b = 3
a *= b  # a + a * b
print("a *= b 的結果:", a)

a = 10
b = 3
a /= b  # a = a / b
print("a /= b 的結果:", a)

a = 10
b = 3
a //= b  # a = a // b
print("a //= b 的結果:", a)

a = 10
b = 3
a %= b  # a = a % b
print("a %= b 的結果:", a)

a = 10
b = 3
a **= b  # a = a ** b
print("a **= b 的結果:", a)

print("-" * 30)

# while practice
i = 0
while i <= 10000:
    print("i=", i)
    i += 1


# while loop break
i = 1
while i < 6:
    if i == 3:
        break
    print("i=", i)
    i += 1

print("-" * 30)

# for loop break
for i in range(1, 6):
    if 1 == 3:
        break
    print("i=", i)
