## Tuples vs. lists
for x in (1,2,3,4,5):
    print(x)

## Unpacking / pattern matching

a,b = eval(input("write a 2-tuple: "))
print(a)
print(b)

## enumerate and zip: functions that produce tuples
## unpack values in for-loop

ages = [10,20,30,40]
people = ["Alice", "Bob", "Carol", "David"]

for person, age in zip(people, ages):
    print(f'{person} is {age} years old')

