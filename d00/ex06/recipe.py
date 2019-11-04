import time


cookbook = {
    'sandwich': {
        'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],
        'meal': 'lunch',
        'prep_time': 10
    },
    'cake': {
        'ingredients': ['flour', 'sugar', 'eggs'],
        'meal': 'dessert',
        'prep_time': 60
    },
    'salad': {
        'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'],
        'meal': 'lunch',
        'prep_time': 15
    }
}


def print_keys(dic):
    for key, val in dic.items():
        print(key)


def print_values(dic):
    for key, val in dic.items():
        print(val)


def print_items(dic):
    for key, val in dic.items():
        print(key, '=', val)


def print_recipe(name):
    print(cookbook[name])


def nice_print_recipe(name):
    print(name, ' is a ', cookbook[name]['meal'])
    print('ingredients:')
    for i in cookbook[name]['ingredients']:
        print('- ', i)
    print('It will take you ',
          cookbook[name]['prep_time'],
          ' minutes to prepare')


def delete_recipe(name):
    del cookbook[name]


def add_recipe(name, ingredients, meal, prep_time):
    cookbook[name] = {
        'ingredients': ingredients,
        'meal': meal,
        'prep_time': prep_time
    }


def print_cookbook():
    print('### COOKBOOK ##')
    for key, val in cookbook.items():
        print('--- ', key, ' ---')
        print('This is a ', val['meal'])
        print('It takes ', val['prep_time'], ' to prepare')
        print('Ingredients:')
        for i in val['ingredients']:
            print('- ', i)
        print()


def main():
    while True:
        print('Please select an option by typing the corresponding number:')
        print('1: Add a recipe')
        print('2: Delete a recipe')
        print('3: Print a recipe')
        print('4: Print the cookbook')
        print('5: Quit')
        choice = input()
        if choice.isdigit() is False:
            print('This option does not exist,')
            print('please type the corresponding number.')
        else:
            choice = int(choice)
            if (choice == 1):
                name = input('name: ')
                n = input("Enter number of ingredients : ")
                if n.isdigit() is False:
                    print('Please try again')
                    continue
                else:
                    n = int(n)
                ingredients = []
                for i in range(0, n):
                    ingredients.append(input())

                meal = input('meal: ')
                prep_time = input('preparation time: ')

                if prep_time.isdigit() is False:
                    print('Please try again')
                    continue
                else:
                    add_recipe(name, ingredients, meal, prep_time)
                    print(name, ' added')
                    time.sleep(1)
            elif (choice == 2):
                print('Which recipe do you want to delete?')
                print_keys(cookbook)
                recipe = input()
                if recipe in cookbook:
                    delete_recipe(recipe)
                    print(recipe, ' deleted')
                else:
                    print('wtf')
            elif (choice == 3):
                print('Which recipe do you want?')
                print_keys(cookbook)
                recipe = input()
                if recipe in cookbook:
                    nice_print_recipe(recipe)
                    time.sleep(4)
            elif (choice == 4):
                print_cookbook()
            elif (choice == 5):
                print('Cookbook closed')
                exit()


main()
# print_keys(cookbook)
# print_values(cookbook)
# print_recipe('cake')
# delete_recipe('cake')
# print_items(cookbook)
# add_recipe('brownie', ['chocolat', 'butter', 'sugar'], 'dessert', 45)
# print_items(cookbook)
# print_cookbook()
