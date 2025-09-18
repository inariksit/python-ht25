l = [42, 1337, 0, -5, 50000, 1]
print("sorted:", sorted(l))
print("original:", l)

print("----------------------------")
l.sort()
print("Now l is mutated:", l)
print("----------------------------")

print()
print()



##### Sorting with keys
def negate(n):
  return -n

l = [42, 1337, 0, -5, 50000, 1]

print(f"l before sorting: {l}")
print(f"l after sorting in increasing order: {sorted(l)}")
print(f"l after sorting in decreasing order: {sorted(l, key=negate)}")

print()
print("----------------------------")
print()

## Can also do like this:
l.sort()
l.reverse()
print(f"l after sorting and reversing: {l}")
print("same as sorting in decreasing order!")