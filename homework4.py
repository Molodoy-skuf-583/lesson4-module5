class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return super().__new__(cls)


    def hous_his(cls):
        return cls.houses_history


    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        floor = 0
        print(f'I call the elevator to the {new_floor} floor')
        if new_floor < 1 or new_floor > self.number_of_floors:
            print('Such a floor does not exist')
        else:
            for floor in range(new_floor):
                print(floor + 1)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Name: {self.name}, number of floors: {self.number_of_floors}'

    def __del__(self):
        print(f'{self.name} demolished, but it will remain in history')


h1 = House('Хрущевка', 5)
print(House.houses_history)
h2 = House('Москва сити', 76)
print(House.houses_history)
h3 = House('Башни близнецы', 110)
print(House.houses_history)
del h2
del h3
print(House.houses_history)
