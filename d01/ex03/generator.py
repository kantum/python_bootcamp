from random import shuffle

def unique(list1):
    unique_list = []

    for x in list1:
        if x not in unique_list:
            unique_list.append(x)
    return x

def generator(text, sep=" ", option=None):
    '''Option is an optional arg, sep is mandatory'''
    if isinstance(text, str):

        if option is None:
            return text.split(sep)
        elif option == 'shuffle':
            tmp = text.split(sep)
            shuffle(tmp)
            return tmp
        elif option == 'unique':
            tmp = text.split(sep)
            unique_list = []
            for x in tmp:
                if x not in unique_list:
                    unique_list.append(x)
            return tmp
        elif option == 'ordered':
            tmp = text.split(sep)
            tmp.sort()
            return tmp
        else:
            raise ValueError('ERROR, wrong option')
    else:
        raise ValueError('ERROR, this is not text')

t = "Le Lorem Ipsum est simplement du faux texte."

for word in generator(t, ' ', 'shuffle'):
    print(word)
print()

for word in generator(t, ' ', 'unique'):
    print(word)
print()

for word in generator(t, ' ', 'ordered'):
    print(word)
print()

try:
    for word in generator(t, ' ', 'carots'):
        print(word)
except ValueError as e:
    print(e)

try:
    for word in generator(42, ' ', 'carots'):
        print(word)
except ValueError as e:
    print(e)

