class Tomato:
    states = [None, "bloom", "green", "red"]

    def __init__(self, index):
        self._index = index
        self._state = 0

    def grow(self):
        if self._state == len(self.states) - 1:
            return
        self._state += 1

    def get_stage(self): return states[self._state]

    def is_ripe(self):
        return self._state == len(self.states) - 1


class TomatoBush:
    def __init__(self, tomatoesCount):
        self.tomatoes = [];
        for i in range(tomatoesCount + 1):
            self.tomatoes.append(Tomato(i))

    def grow_all(self):
        for tomato in self.tomatoes:
            if tomato.is_ripe():
                continue
            tomato.grow()

    def all_are_ripe(self):
        for tomato in self.tomatoes:
            if not tomato.is_ripe():
                return False
        return True

    def give_away_all(self):
        for tomato in self.tomatoes:
            tomato = Tomato(tomato._index);


class Gardner:

    @staticmethod
    def knowlange_base():
        print("Справка... какая-то там инфа....")

    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        self._plant.grow_all();

    def harvest(self):
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print("Плоды собраны")
            return True
        else:
            print("Плоды еще не созрели")
            return False


Gardner.knowlange_base();
bash = TomatoBush(11);
gardner = Gardner("Виталик", bash);

while not gardner.harvest():
    gardner.work()
