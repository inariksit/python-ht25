## More examples of the accumulator pattern

#################################################################
# Return the highest and lowest number. Don't use min() or max().
# Input: [8, 5.5, 10, 6, 9, 9.5, 2.0]
# Expected result: [10, 2.0]
def hi_lo(numbers):
  highest = -float("inf")
  lowest = float("inf")
  for num in numbers:
    if num > highest:
      highest = num
    elif num < lowest:
      lowest = num
  return [highest, lowest]

################################################################
# Return how many numbers in the list are negative.
# Input: [-10.5, 5.5, -2.5, 1, 0, 12, -14.8]
# Expected result: 3

def count_negatives(numbers):
  acc = 0
  for num in numbers:
    if num < 0:
      acc += 1    #same as:   acc = acc + 1
  return acc


if __name__=='__main__':
    print("Demo the functions we wrote!")

    print(hi_lo([8, 5.5, 10, 6, 9, 9.5, 2.0]))

    print(count_negatives([-10.5, 5.5, -2.5, 1, 0, 12, -14.8]))