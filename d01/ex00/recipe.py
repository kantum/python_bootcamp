import string


class Recipe:
    def __init__(self,
                 name,
                 cooking_lvl,
                 cooking_time,
                 ingredients,
                 recipe_type,
                 description=''):
        if isinstance(name, str):
            self.name = name
        else:
            raise ValueError('ERROR, name is not a string')
            quit()
        if isinstance(cooking_lvl, int) and 1 <= cooking_lvl <= 5:
            self.cooking_lvl = cooking_lvl
        else:
            raise ValueError('ERROR, cooking_lvl is not an int')
            quit()
        if isinstance(cooking_time, int) and 0 <= cooking_time:
            self.cooking_time = cooking_time
        else:
            raise ValueError('ERROR, cooking_time is not an int')
            quit()
        if isinstance(ingredients, list) \
           and all(isinstance(elem, str) for elem in ingredients):
            self.ingredients = ingredients
        else:
            raise ValueError('ERROR, ingredients is not a list of strings')
            quit()
        if isinstance(description, str):
            self.description = description
        else:
            raise ValueError('ERROR, description is not a string')
            quit()
        if isinstance(recipe_type, str):
            self.recipe_type = recipe_type
        else:
            raise ValueError('ERROR, recipe_type is not a string')
            quit()

    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = "{:s}\nlevel: {:d} time: {:d} type: {:s}" \
            .format(self.name,
                    self.cooking_lvl,
                    self.cooking_time,
                    self.recipe_type)
        txt += '\n' + self.description
        return txt
