from datetime import datetime
from book import Book
from recipe import Recipe


try:
    r = Recipe(42, 2, 15, ['cake', 'friend'], 'dessert', 'try to eat the cake')
except ValueError as e:
    print(e)
try:
    r = Recipe('test', ' ', 15, ['cake', 'friend'], 'dessert',
               'try to eat the cake')
except ValueError as e:
    print(e)
try:
    r = Recipe('test', 2, ['asd', 'asdf'], ['cake', 'friend'], 'dessert',
               'try to eat the cake')
except ValueError as e:
    print(e)
try:
    r = Recipe('test', 2, 15, ['cake', 42], 'dessert', 'try to eat the cake')
except ValueError as e:
    print(e)
try:
    r = Recipe('test', 2, 15, ['cake', 'friend'], 42, 'try to eat the cake')
except ValueError as e:
    print(e)
try:
    r = Recipe('test', 2, 15, ['cake', 'friend'], 'dessert', 42)
except ValueError as e:
    print(e)
    # quit()

r = Recipe('Salad', 2, 15,
           ['salad', 'tomatoes', 'cheese'], 'starter',
           'Clean the salad and tomatoes, then cut the cheese and mix')
r2 = Recipe('Salada', 2, 15,
            ['salad', 'tomatoes', 'cheese'], 'starter',
            'Clean the salad and tomatoes, then cut the cheese and mix')
s = Recipe('Bourguignon', 4, 120,
           ['beef', 'carots', 'potatoes', 'thyme'], 'lunch',
           'very hard, ask your mother')
t = Recipe('Brownie', 2, 30,
           ['flour', 'butter', 'chocolat', 'sugar', '3eggs'], 'dessert',
           'Melt butter and chocolat, mix everything, then cook')

b = Book('Livre', {'starter': [r], 'lunch': [s, s], 'dessert': [t, t]})

# print(r)

try:
    b.get_recipe_by_name('Salada')
except ValueError as e:
    print(e)

try:
    b.add_recipe(r2)
    b.get_recipe_by_name('Salada')
except ValueError as e:
    print(e)

print("\n")
try:
    b.get_recipes_by_types('lunch')
except ValueError as e:
    print(e)

print(b)
