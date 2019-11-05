import datetime


class Book:
    def __init__(self, name, recipes_list):
        if isinstance(name, str):
            self.name = name
        else:
            print('ERROR, name is not a string')
            quit()
        self.last_update = datetime.datetime.now()
        self.creation_date = datetime.datetime.now()
        if isinstance(recipes_list, dict) \
           and all(k in recipes_list for k in ('starter', 'lunch', 'dessert')):
            self.recipes_list = recipes_list
        else:
            raise ValueError('ERROR, recipes_list is not a dictionnary')
            quit()

    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` and return the instance"""
        for key, val in self.recipes_list.items():
            for l in val:
                if l.name == name:
                    print(l)
                    return(l)
        raise ValueError('ERROR, no recipe with this name')

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        for key, val in self.recipes_list.items():
            if key == recipe_type:
                for l in self.recipes_list[key]:
                    print(l)
                return()
        raise ValueError('ERROR, no recipe with this type')

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        for key, val in self.recipes_list.items():
            if recipe.recipe_type == key:
                self.recipes_list[key].append(recipe)
                self.last_update = datetime.datetime.now()
                return()
        raise ValueError('ERROR, recipe_type does not exist')

    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = "{:#^80s}\n".format('')
        txt += "{:^80s}\n".format(self.name)
        txt += "{:#^80s}\n".format('')
        for key, val in self.recipes_list.items():
            txt += "\n†{:^78s}†\n".format(key)
            for l in val:
                txt += "\n{:s}\n".format(str(l))
            txt += "\n"
        txt += "{:^80s}\n".format('Ω')

        return txt
