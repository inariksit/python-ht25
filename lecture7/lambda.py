def negate(x):
    return -x

negate2 = lambda x : -x

my_list = [42, 1337, 0, -99]

print(sorted(my_list, key=negate))
print(sorted(my_list, key=negate2))
print(sorted(my_list, key=lambda x: -x))