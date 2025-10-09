### Files as generators
with open("mobydick.txt") as file:
    for line in file: ### File is a generator
        print(line.strip())

    # File is exhausted, nothing printed out
    for line in file:
        print(line+"XXXXXXXXXXXX")



### Make our own generator

## I am a square provider…
def squares():
    n = 1
    while True:
        yield n**2
        n = n + 1

# You decide how many squares you want!
for x in squares():
    if x > 100:
        break
    print(x)