

def roll_call_dwarves(dwarves_list):
    x = 0
    for dwarf in dwarves_list:
        x += 1
        print(f'{x}. {dwarf}')


def summon_captain_planet(list):
    capitalized = [element.capitalize() + "!" for element in list]
    return capitalized


def long_planeteer_calls(words):
    for word in words:
        if len(word) > 3:
            return False
        else:
            return True


def find_the_cheese(snacks_to_check):
    types_of_chesse = ["gouda", "cheddar", "camembert"]
    for cheese in types_of_chesse:
        if cheese in snacks_to_check:

            return cheese
    else:

        return None
