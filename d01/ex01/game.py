class GotCharacter:
    def __init__(self, first_name):
        self.first_name = first_name
        self.is_alive = True


class Stark(GotCharacter):
    """
    A class representing the Stark family. \
    Or when bad things happen to good people.
    """
    def __init__(self, first_name=None):
        super().__init__(first_name=first_name)
        self.family_name = self.__class__.__name__
        self.house_words = "Winter is Coming"

    def __str__(self):
        txt = "{:s} {:s}".format(self.first_name, self.family_name)
        if self.is_alive:
            txt += " is alive\n"
        else:
            txt += " is dead\n"
        txt += "House words: {:s}\n".format(self.house_words)
        return(txt)

    def print_house_words(self):
        print(self.house_words)

    def die(self):
        self.is_alive = False


class Lannister(GotCharacter):
    def __init__(self, first_name=None):
        super().__init__(first_name=first_name)
        self.family_name = self.__class__.__name__
        self.house_words = "Hear Me Roar"

    def __str__(self):
        txt = "{:s} {:s}".format(self.first_name, self.family_name)
        if self.is_alive:
            txt += " is alive\n"
        else:
            txt += " is dead\n"
        txt += "House words: {:s}\n".format(self.house_words)
        return(txt)

    def print_house_words(self):
        print(self.house_words)


a = Stark('Bob')
b = Stark('Sylvain')
c = Stark('Bernadette')
d = Lannister('Jojo')
e = Lannister('Janina')
f = Lannister('Virginie')

print(a)
a.die()
print(a)

print(b)
b.print_house_words()
print(c)
print(d)
print(e)
print(f)
f.print_house_words()
