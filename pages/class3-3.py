# random stuff practice
import streamlit as st
import random

# random number 1
R1 = random.randrange(6)  # 0~5
print("R1=", R1)

# random number 2
R2 = random.randrange(1, 11)  # 0~10
print("R2=", R2)

# random number 3
R3 = random.randrange(1, 10, 2)  # 0, 2, 4, 6, 8
print("R3=", R3)

# randrange respond
num = 1000
count = [0, 0, 0, 0, 0]
for i in range(num):
    r = random.randrange(1, 6)
    count[r - 1] += 1
for i in range(1, 6):
    print(f"{i} 出現的次數: {count[i - 1]}")

print("-" * 30)

# randint stuff
R4 = random.randint(1, 5)  # 1~5
print("R4=", R4)

# totalind randint results
num = 1000
count = [0, 0, 0, 0, 0]
for i in range(num):
    r = random.randint(1, 5)
    count[r - 1] += 1
for i in range(1, 6):
    print(f"{i} 出現的次數: {count[i - 1]}")
