from abc import ABC, abstractmethod


class Human(ABC):

    def status(self):
        print('Alive!')

    @abstractmethod
    def mid_age(self):
        pass

    def mid_pay_in_hour(self):
        pass

    def mid_busyness(self):
        pass

    def mid_activity(self):
        pass

    def salary(self):
        pass


class Manager(Human):

    def mid_age(self):
        print('25')

    def mid_pay_in_hour(self):
        self.pay = 20
        print(f'Manager dollar an hour: {self.pay}$')

    def mid_busyness(self):
        self.busy = 50
        print(f'Manager busyness: {self.busy} hours')

    def mid_activity(self):
        print('Manager status: Active')

    def salary(self):
        print(f'Manager salary: {self.busy * self.pay}$')


class Programmer(Human):

    def mid_age(self):
        print('Programmer age: 23')

    def mid_pay_in_hour(self):
        self.pay = 50
        print(f'Programmer dollar an hour: {self.pay}$')

    def mid_busyness(self):
        self.busy = 50
        print(f'Programmer busyness: {self.busy} hours')

    def mid_activity(self):
        print('Programmer status: lazy')

    def salary(self):
        print(f'Programmer salary: {self.busy * self.pay}$')


class BA(Human):

    def mid_age(self):
        print('Busyness analyst age: 31')

    def mid_pay_in_hour(self):
        self.pay = 50
        print(f'Busyness analyst dollar an hour: {self.pay}$')

    def mid_busyness(self):
        self.busy = 60
        print(f'Busyness analyst busyness: {self.busy} hours')

    def mid_activity(self):
        print('Busyness analyst status: Superactive')

    def salary(self):
        print(f'Busyness analyst salary: {self.busy * self.pay}$')


class Tester(Human):

    def mid_age(self):
        print('Tester age: 20')

    def mid_pay_in_hour(self):
        self.pay = 15
        print(f'Tester dollar an hour: {self.pay}$')

    def mid_busyness(self):
        self.busy = 0
        print(f'Tester busyness: {self.busy} hours')

    def mid_activity(self):
        print('Tester status: vacation')

    def salary(self):
        print(f'Tester salary: {self.busy * self.pay}$')


m = Manager()
p = Programmer()
b = BA()
t = Tester()
for i in [m, p, b, t]:
    i.mid_age()
    i.mid_activity()
    i.mid_busyness()
    i.mid_pay_in_hour()
    i.salary()
