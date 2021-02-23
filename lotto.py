import random

# lottery = 6
#
# random_int = {}
# while len(random_int) < lottery:
#     x = random.randint(1, 50)
#     random_int.add(x)
# print(random_int)

random_six_num = set()

while len(random_six_num) < 6:
    x = random.randint(1,50)
    random_six_num.add(x)
print(random_six_num)
print(type(random_six_num))