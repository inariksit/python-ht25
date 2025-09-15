## String literals
## Printing, formatting
name = input("Your name?\n> ")
uni = input("Your university?\n> ")
print(name, "@", uni, ".se", sep="^_^")

for _ in range(5):
    print("test", end="^_^")

## Unicode: code points
print(ord('A'))


## String operations:
# concat
name = "inari"
uni = "chalmers"
email = name + "@" + uni + ".se"
print(email)

# repeat
example = 3 * uni
print(example)

# index
a = uni[2]
print(a)

# uni[10000]
# IndexError: string index out of range

# slice: string[start:stop]
alm = uni[2:5]
print(alm)

# -1 is the last character
# slicing is exclusive
almer = uni[2:-1]
print(almer)

# 2 ways to get "almers"
almers1 = uni[2:]
almers2 = uni[2:10000]
print(almers1, almers2)

chal = uni[:4]
mers = uni[4:]
print(chal, mers)


# length & iteration
print(len(uni))

# index loop: loop over indices
for i in range( len(uni) ):
    print(i, uni[i])

# foreach: loop over elements
for c in uni:
    print(c, "code point:", ord(c))

# membership
print('s' in uni)
print('cha' in uni)
print('c h a' in uni)




## String methods