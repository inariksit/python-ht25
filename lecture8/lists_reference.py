from tournament import print_matrix

##### How lists work

n = 3 # change to whatever
verbose = True # Change to True if you want printouts of the more trivial examples

# Accumulator loop
T1 = []
for _ in range(n):
  T1.append([0] * n)
  # At every iteration of the for-loop,
  # a new list is constructed and placed into T1.
  # All these lists have different reference.
if verbose:
    print("T1, built with accumulator loop")
    T1[0][0] = 99
    print_matrix(T1)
    print("---------------------------------")

# List comprehension
T2 = [[0] * n for _ in range(n)]
# Just like for-loop but more compact.
# [0] * n is executed again every iteration
# of the `for _ in range(n)`.
if verbose:
    print("T2, built with list comprehension")
    T2[0][0] = 99
    print_matrix(T2)
    print("---------------------------------")

# Multiplication of the same value
T3 = [[0] * n] * n
# The same as if we had done this:
t4 = [0] * n  # 0 is a different reference every time
T4 = [t4] * n # t4 is the same reference every time (like the list literal was in T3)

print("T4 before modifications")
print_matrix(T4)
print("---------------")
T4[0][0] = 10
t4[1]    = 20
print("T4 after modifications")
print_matrix(T4)
print("---------------")

## Can we force the internal things to be same?
num = 0
t5 = [num] * n
T5 = [t5] * n

print("T5 before modifications")
print(f"num = {num}")
print_matrix(T5)
print("---------------")

T5[0][0] = 10
print("T5 after modifications")
print_matrix(T5)
print("---------------")

num = 99 # There's a num in every cell—does this change them all?
print("T5 after num = 99: no change!")
print_matrix(T5)
# No—it didn't change anything! 🤯
# 10   0    0
# 10   0    0
# 10   0    0
print(f"num = {num}")
print("Looks like what was stored in the list was a /value/, not /reference/")

print("---------------")

#### Final round: what if we have a mutable variable in the inner list?

## Can we force the internal things to be same?
mutable_variable = {} # let's make this dict to distinguish from lists
t6 = [mutable_variable] * n
T6 = [t6] * n

print("T6 before modifications")
print_matrix(T6)
print("---------------")
print("T6 after T6[0][0] = 10")
T6[0][0] = 10
print_matrix(T6)

print("---------------")
mutable_variable["a"] = "b" # There's a num in every cell—does this change them all?
print("After changing mutable_variable")
print_matrix(T6)