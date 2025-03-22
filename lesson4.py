# from multiprocessing.pool import worker
#
#
# class Human:
#     height = 170
#
# class Student(Human):
#     satiety = 0
#
# class Worker(Human):
#     satiety = 0
#
#
# h = Human()
# s = Student()
# w  = worker()
# print(h.height)
# print("*"+20)
# print(s.satiety)
# print(s.height)
# print("*"+20)
# print(w.satiety)
# print(w.height)
#

class Grandparent:
    height = 170
    satiety = 100
    age = 60


class Perent(Grandparent):
    age = 40

class Child(Perent):
    height = 50
    def __init__(self):
        print(f"height = {self.height}")
        print(f"satiety = {self.satiety }")
        print(f"age = {self.age}")



nich = Child()



class Hello:
    def __init__(self):
        print('Hello')


class Helooworld(Hello):
    def __init__(self):
        super().__init__()
        print('World')


hw = Helooworld


class Camputer:
    def __init__(self, model, *agrs, **kaywsrds):
        super().__init__(*agrs, **kaywsrds)
        self.model = model
        self.memory = 128
    def calculate(self):
        print("Calculeyting...")

class Display:
    def __init__(self, *agrs, **kaywards):
        super().__init__(*agrs, **kaywsrds):

    print("i display the image on the screen...")



class Smartphone(Camputer,Display):
    def print_info(self):
        print(self.Display())
        print(self.calculate())

sp = Smartphone()
sp.print_info()


