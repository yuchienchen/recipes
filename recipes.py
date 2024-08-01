
def read_dict_from_file(filename):
    """
    Takes in the name of a file containing a recipe or
    pantry list and reads it into a dictionary.

    An example doctest using the file above:
    >>> read_dict_from_file('recipe.txt')
    {'flour': 200.0, 'salt': 2.5}
    """
    dict = {}
    with open(filename) as file:
        for line in file: 
            line = line.strip()
            # print(line)
            parts = line.split(':: ')
            # print(parts)
            key = parts[0]
            value = float(parts[-1])
            # print(key)
            # print(value)
            dict[key] = value

        print(dict)


def can_make(recipe, pantry):
    """
    Given the contents of the pantry, returns a boolean indicating
    whether or not it is possible to follow the recipe. Note that
    the parameters to this function are dictionaries, and not
    filenames. The pantry should not be modified in this function.

    >>> can_make({'flour': 5.0, 'salt': 1.0}, {'flour': 200.0, 'salt': 2.5})
    True
    >>> can_make({'flour': 5.0, 'salt': 5.0}, {'flour': 200.0, 'salt': 2.5})
    False
    """
    pass


def make_recipe(recipe, pantry):
    """
    Given a recipe and a pantry with enough ingredients to make the recipe,
    modify the contents of the pantry to remove as many quantities as the
    recipe requires. You may modify the pantry in place, but return the modified
    pantry in order to test the output using doctests.

    >>> make_recipe({'flour': 5.0, 'salt': 1.0}, {'flour': 200.0, 'salt': 2.5})
    {'flour': 195.0, 'salt': 1.5}
    """
    pass


def main():
    pantry_file = input("What pantry file would you like to use? ")
    pantry = read_dict_from_file(pantry_file)
    recipe_file = input("What recipe would you like to make? ")
    while recipe_file != "":
        recipe = read_dict_from_file(recipe_file)
        if can_make(recipe, pantry):
            print('Pantry before:')
            print(pantry)
            make_recipe(recipe, pantry)
            print('Pantry after:')
            print(pantry)
        else:
            print('You do not have the ingredients for that recipe!')
        recipe_file = input("What recipe would you like to make next? ")


if __name__ == "__main__":
    main()