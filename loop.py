# While loop

i = 1
while i <= 5:
    print(i)
    i += 1

print("========================")
# print the start like this
# *
# **
# ***
# ****
# *****
i = 1
while i <= 5:
    print(i * '*')
    i += 1

print("=========== Break =============")

i = 0
while i <= 5:
    i += 1
    if i == 3:
        break
    print(i)

print("=========== Continue =============")

i = 0
while i <= 5:
    i += 1
    if i == 3:
        continue
    print(i)

print("=========== For Loop using range =============")

for i in range(10):
    print(i)

print("=========== For Loop using list =============")

for text in ["imran", "tamim", "najma"]:
    print(text)

print("=========== For Loop using string =============")

for char in "Imran":
    print(char)
