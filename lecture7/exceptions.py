def some_function(x):
	a,b,c = x

def main():
	some_function([1,2,3,4])

# Prints a stack trace
if __name__ == "__main__":
    main()


#######################
## Raising an exception

# Assume this is a library function, some other
# application will handle the error when it calls increment()
def increment(price, incr, years):
  if type(price) not in [int, float]:
    raise ValueError("Price must be a number")
  for _ in range(years):
    price = price * (1 + incr/100)
  return price