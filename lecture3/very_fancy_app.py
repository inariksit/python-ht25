import price

## Helper function to print in fancy colors
def fancy_print(color, *args, **kwargs):
    colored = color + ' '.join(str(a) for a in args) + "\033[0m"
    print(colored, **kwargs)

# Will print the price progression
# with every year in different color!
vt_price = 37
for year in range(2025,2031):
  color = f"\033[{1};{year-1994};{40}m"
  fancy_print(color, f"{year}: {vt_price:.2f}")
  vt_price = price.increment(vt_price, 2.6)