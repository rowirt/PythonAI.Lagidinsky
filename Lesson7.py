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
# from collections import Counter
#
#
# class  Caunter:
#     def __int__(self,max_number):
#         self.i= 0
#         self.max_number = max_number
#
#
#     def __init__(self):
#         self.i = 0
#         return self
#
#     def __next__(self):
#         self.i += 1
#         if self.i > self.max_number:
#             raise StopIteration
#
#         return   self.i
#
#
#
# cont = Caunter(5)
# for elem in cont:
#     print(elem)
#
#
# print('-'+30)
# cont = Counter
# print(cont.__next__())
# print(cont.__next__())
# print(next(cont))


# list_power_2 = [i ** 2 for i in range( 1,20,1)]
# print(list_power_2)

# def raise_to_the_degrees(number):
#     i = 0
#     # for _ in range(max_degrees):
#     while True:
#         result = number ** i
#         yield result
#         # i += 1
#         if result > 100**20:
#             return
#         i+=1
#
# res = raise_to_the_degrees(2)
# print(res)
#
# for elem in res:
#     print(elem)


class Helper:
    def __init__(self, work):
        self.work = work
    def __call__(self, work):
        return f"I will help you with your {self.work}. Afterward I will help you with {work}"

hepler = Helper("homework")
print(hepler("cleaning"))