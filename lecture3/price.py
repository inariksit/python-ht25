def increment(price, incr):
  new_price = price * (1 + incr / 100)
  return new_price

def main():
  price_2025 = int(input("Price in 2025? "))
  price_2026 = increment(price_2025, 2.6)
  print("Price in 2026 will be:", price_2026)

if __name__=="__main__":
  main()