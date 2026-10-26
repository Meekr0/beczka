def correct_str(name):
    return name.lower().capitalize()


def is_role_str(s):
    roles = ['adc', 'bot', 'bottom', 'mid', 'top', 'jungle', 'jg', 'jgl', 'sup', 'supp', 'support']
    try:
        roles.index(s.lower())
        return True
    except ValueError:
        return False


def is_tier_str(s):
    roles = ['s', 'a', 'b', 'c', 'd']
    try:
        roles.index(s.lower())
        return True
    except ValueError:
        return False


def is_champ_str(s):
    try:
        with open('data/champs.txt') as file:
            [line.rstrip() for line in file].index(correct_str(s))
        return True
    except ValueError:
        return False
