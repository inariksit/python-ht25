import price

## Helper function to print in fancy colors
def color_print(color, arg):
    # Coercing arg with str() just in case
    print(color + str(arg) + "\033[0m")

# Will print the price progression
# with every year in different color!
vt_price = 37
for year in range(2025,2031):
  color = f"\033[{1};{year-1994};{40}m"
  color_print(color, f"{year}: {vt_price:.2f}")
  vt_price = price.increment(vt_price, 2.6)