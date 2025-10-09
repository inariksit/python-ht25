# import random
# haystack = [random.randrange(-30,100) for _ in range(20)]
# needle = random.randrange(-100,100)

haystack = [15, -8, 23, 7, -12, 31, 4, -3, 19, 11, -5, 28, 2, -15, 9, 6, -20, 14, 1, 25]
needle = 13

#####################################################################
## Find a specific value ('needle') from a collection ('haystack') ##
#####################################################################

def search(needle, haystack):
  for i in range(len(haystack)):
    straw = haystack[i]
    if straw == needle:
      return i

  return -1


#########################################################################
## Is there a pair of values in haystack whose sum is equal to needle? ##
#########################################################################

def pair_sum(needle, haystack):
  for i in range(len(haystack)):
    for j in range(len(haystack)):
      if i != j:
        if haystack[i] + haystack[j] == needle:
          return (i,j)

  return (-1, -1)
  # return indices of straws if found
  # return (-1,-1) if not found



###########################################################################
## Is there a triple of straws in haystack whose sum is equal to needle? ##
###########################################################################

def triple_sum(needle, haystack):
  for i in range(len(haystack)):
    for j in range(len(haystack)):
      for k in range(len(haystack)):
        if i != j and j != k and i != k:
          if haystack[i] + haystack[j] + haystack[k] == needle:
            return (i,j,k)

  return (-1, -1, -1)

