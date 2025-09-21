## Examples from the slides about generators and list comprehensions
def increment(price, incr, years):
  for _ in range(years):
    price = price * (1 + incr/100)
  return price

def my_range(start,end):
   i = start
   while i < end:
      yield i
      i = i + 1

def gen123():
  yield 1
  yield 2
  yield 3

## Infinite generator that keeps yielding prime numbers
def primes():
    i = 2
    ps = []
    while True:
        is_prime = True
        for p in ps:
            if i % p == 0:
                is_prime = False
                break
        if is_prime:
            ps.append(i)
            yield i
        i = i + 1

## The full list of TA names is on Canvas,
## the file in this repo is just pretend names
with open("TAs.txt") as file:
  lines = file.readlines()
  tas_by_len = sorted(lines, key=len)
  tas_by_3rd_letter = sorted(lines, key=lambda x:x[2])
  print(tas_by_len)
  print(tas_by_3rd_letter)


with open("TAs.txt") as file:
  tas_sorted = sorted(file, key=len)
  tas_by_3rd_letter = (sorted(file, key=lambda x:x[2]))
  print(tas_sorted)
  print(tas_by_3rd_letter)


##############################################
## List comprehensions & generator expressions

def remove_vowels(s):
  cs = [c for c in s if c not in 'aeiouyäöå']
  return ''.join(cs)

discount100 = ['b', 'se']
discount25 = ['u', 'st', 'f']

status = input("Välj: [b]arn, [u]ngdom, [st]udent, [v]uxen, [f]örmånstagare, [se]nior? ")
status = status.lower()
if any(status.startswith(x) for x in discount100):
   price = 0
elif any(status.startswith(x) for x in discount25):
   price = 28
else:
   price = 37

print(f"The price is {price}")

ls = [x**2 for x in range(10)]
gen = (x**2 for x in range(10))

# New infinite generator based on previously defined primes
primes_squared_gen = (x**2 for x in primes())

# If you uncomment this, it will just hang and you have to kill the process
# primes_squared_list_BAD = [x**2 for x in primes()]
