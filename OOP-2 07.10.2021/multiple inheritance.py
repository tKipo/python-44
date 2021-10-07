class Donkey:
    def move(self):
        print('Donkey Move')

    def weight(self):
        print('100 kg')

    def say(self):
        print('Ia-Ia')


class Horse:
    def move(self):
        print('Horse Move')

    def speed(self):
        print('100 miles/h')

    def say(self):
        print('I-go-go')
        super().say()


class Myl(Horse, Donkey):
    ...


print(Myl.mro())
m = Myl()
m.move()
m.weight()
m.speed()
m.say()
