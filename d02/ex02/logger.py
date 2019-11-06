import time
import getpass
import datetime
from random import randint


def log(func):
    def inner(*args, **kwargs):
        f = open("machine.log", "a+")
        start = datetime.datetime.now()
        f.write('({:s})'.format(getpass.getuser()))
        f.write("Running: ".format(end=' '))
        if func.__name__ == 'start_machine':
            f.write("Start Machine".format(end=' '))
        elif func.__name__ == 'boil_water':
            f.write("Boil Water".format(end=' '))
        elif func.__name__ == 'make_coffee':
            f.write("Make Coffee".format(end=' '))
        elif func.__name__ == 'add_water':
            f.write("Add Water".format(end=' '))
        f.write('\t')

        ret = func(*args, **kwargs)

        end = datetime.datetime.now()
        delta = end-start
        if (delta / datetime.timedelta(seconds=1)) >= 1:
            f.write('[ exec-time = {:.3f}  s ]'
                    .format(delta / datetime.timedelta(seconds=1)))
        else:
            f.write('[ exec-time = {:5.0f} ms ]'
                    .format(delta / datetime.timedelta(microseconds=1)))
        f.write('\n')
        f.close()
        return ret
    return inner


class CoffeeMachine():

    water_level = 100

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")


if __name__ == "__main__":

    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()

    machine.make_coffee()
    machine.add_water(70)
