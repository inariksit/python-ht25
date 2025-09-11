def factorial(n):
  fac = 1
  for k in range(2, n+1):
    print("k=", k, "fac=", fac)
    fac = fac * k      # alt: fac *= k
  return fac

if __name__=='__main__':
  print(factorial(5))