def factorial(n):
  fac = 1
  for k in range(2, n+1):
    #print("k=", k, "fac=", fac)
    fac = fac * k      # alt: fac *= k
  return fac

def factorial_float(n):
  fac = 1.0 # initialize accumulator to a float

  # k cannot be float: range only takes integers
  for k in range(2, n+1):
    fac = fac * k
  return fac

if __name__=='__main__':
  print(factorial(5))