# import random
#
# my_list = []
#
# for i in range(10):
#     my_list.append(random.randint(-10,10))
#
#
#
# iterator =iter(my_list)
# print(iterator)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
#
#
# print(my_list)
# print("-"*20)
#
# for elem in iterator:
#     print(elem)
from collections import Counter


class  Caunter:
    def __int__(self,max_number):
        self.i= 0
        self.max_number = max_number


    def __init__(self):
        self.i = 0
        return self

    def __next__(self):
        self.i += 1
        if self.i > self.max_number:
            raise StopIteration

        return   self.i



cont = Caunter(5)
for elem in cont:
    print(elem)


print('-'+30)
cont = Counter
print(cont.__next__())
print(cont.__next__())
print(next(cont))
