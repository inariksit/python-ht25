## List operations vs. string operations
## basic stuff: 100% same as strings

uni = "chalmers"
print(uni.count('a'))

## List methods
my_list = [95236, 2398423, 129, 23]
print(my_list)

my_list.reverse()  # modify
print(my_list)     # print modified list

## Mutability
my_list.append(42)
print("appended 42", my_list)

my_list[2] = 100
print("replaced 3rd value with 100", my_list)



## Index loops vs. foreach

# index loop: loop over indices
for i in range( len(my_list) ):
    my_list[i] = my_list[i] + 1

print("added +1 to all values", my_list)


## Conversion between strings and lists

uni = "chalmers"
#uni[-1] = 'z'  ## Not allowed to modify strings in place!

uni_list = list(uni)
uni_list[-1] = 'z'
uni = ''.join(uni_list)
print(uni)

## Unpacking