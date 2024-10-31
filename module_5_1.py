class House:
    def __init__(self, name, numbers_of_floors):
        self.name = name
        self.numbers_of_floors = numbers_of_floors


    def go_to(self, new_floor):
        i = 1
        while i <= new_floor:
            if new_floor > self.numbers_of_floors or new_floor < 1:
                print('Такого этажа не существует')
                break
            else:
                print(i)
                i += 1
        print()

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
print(h1.name, h1.numbers_of_floors)
h1.go_to(2)
print(h2.name, h2.numbers_of_floors)
h2.go_to(2)