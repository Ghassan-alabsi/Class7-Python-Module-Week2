first = input("first word:  ")
second = input("second word:  ")
set(first)
set(second)
print(set(first).intersection(set(second)))
print(set(first).difference(set(second)))
print(set(second).difference(set(first)))
