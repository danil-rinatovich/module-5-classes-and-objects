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

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.numbers_of_floors}'

    def __len__(self):
        return self.numbers_of_floors


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
print(h1)
print(h2)
print(len(h1))
print(len(h2))