f = open("dummy.txt")
for line in f:
    print(line)
f.close()

## Same as

with open("dummy.txt") as f:
    for line in f:
        print(line)

## Read mode vs. write mode

with open("dummy.txt") as f:
    print("Is dummy.txt writable:", f.writable())
    #f.write("This will fail D:\n")

with open("dummy.txt", "a") as f:
    print("Is dummy.txt writable:", f.writable())
    f.write("\nI am writing this from Python!!!")