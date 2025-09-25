from tournament import print_matrix

##### How lists work

n = 3 # change to whatever
debug = True # Change to False if you don't want printouts

# Accumulator loop
T1 = []
for _ in range(n):
  T1.append([0] * n)
  # At every iteration of the for-loop,
  # a new list is constructed and placed into T1.
  # All these lists have different reference.
if debug:
    print("T1, built with accumulator loop")
    T1[0][0] = 99
    print_matrix(T1)
    print("---------------------------------")

# List comprehension
T2 = [[0] * n for _ in range(n)]
# Just like for-loop but more compact.
# [0] * n is executed again every iteration
# of the `for _ in range(n)`.
if debug:
    print("T2, built with list comprehension")
    T2[0][0] = 99
    print_matrix(T2)
    print("---------------------------------")

# Multiplication of the same value
T3 = [[0] * n] * n
if debug:
    print("T3, built by multiplying")
    T3[0][0] = 99   # The rows are all the same, this will change also T3[1][0] and T3[2][0]
    print_matrix(T3)
    #### Result:
    # 99   0    0
    # 99   0    0
    # 99   0    0

    print("---------------")
    T3[1][1] = 88 # Will also change 0,1 and 2,1
    print_matrix(T3)
    #### Result:
    # 99   88   0
    # 99   88   0
    # 99   88   0

    print("---------------")
    T3[2][2] = 77  # Will also change 0,2 and 1,2
    print_matrix(T3)
    #### Result:
    # 99   88   77
    # 99   88   77
    # 99   88   77