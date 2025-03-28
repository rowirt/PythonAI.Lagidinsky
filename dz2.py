class cat:
    def __init__(self, age, satiety):
        self.age = age
        self.satiety = satiety
        print("meow")

    def get_satiety(self):
        return self.satiety

    def set_satiety(self, satiety):
        self.satiety = satiety

    def age_up(self):
        self.age += 1
        print(f" cat aged 1 year {self.age} years old.")

my_cat = cat(age=3, satiety=5)
my_cat.set_satiety(3)
print(f"age: {my_cat.age}, satiety: {my_cat.get_satiety()}")


my_cat.age_up()
print(f"age: {my_cat.age}, satiety: {my_cat.get_satiety()}")