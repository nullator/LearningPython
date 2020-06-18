from random import randint

all_number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(len(all_number))
for i in range(3):
    n = randint(0, len(all_number) - 1)
    print(all_number.pop(n))
print(all_number)
