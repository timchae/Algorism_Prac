class person:
    def __init__(self, param_name):
        print("i am created", self)
        self.name = param_name
    pass

person1 = person()
print(person1)

person2 = person()
print(person2)