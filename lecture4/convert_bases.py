## Take a numeric notation in any base between 2-10 and compute its value.
# Examples:
# 235 in decimal:
#    2 · 10² + 3 · 10¹ + 5 · 10⁰
# =  200 + 30 + 5
# 235 in nonary:
#    2 · 9² + 3 · 9¹ + 5 · 9⁰
# =  162 + 27 + 5
# =  194

def convert(notation, base):
    notation_str = str(notation)
    notation_rev = reversed(notation_str)

    acc = 0
    # Will explain "for x, y in …" Monday's lecture!
    for power, char in enumerate(notation_rev):
        digit = int(char)

        # if digit belongs to base
        if digit < base:
            acc += digit * (base ** power)
        else:
            print("Digit", digit, "too large for base", base)
            return # returns nothing, exits function

    return acc

