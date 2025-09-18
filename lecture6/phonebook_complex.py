phonebook = {}

## Fill phonebook with data in the file
with open("people.txt") as file:
  lines = file.readlines()
  for line in lines:
    # unpack result of splitting line (which is a list)
    name, number = line.split(':')

    # strip() for security:
    # does nothing if string already clean of trailing whitespace
    # Now all entries in phonebook are
    phonebook[name.strip()] = [number.strip()]


## Search for contacts—slightly modified for lists as values
def search(dict):
  contact = input("Who do you want to call? ")
  # Does not crash, even if contact not found
  numbers = dict.get(contact, ["not in your contacs"])

  # Prettier printout, if multiple numbers:
  numbers_pretty = " or ".join(numbers)
  print(f"{contact}'s number is {numbers_pretty}")

# Using setdefault: we can update a contact even if it doesn't exist
def update(dict):
  contact = input("Who do you want to update? ")
  number = input("What is the new number? ")
  existing_numbers = dict.setdefault(contact, [])
  existing_numbers.append(number)
  print("Contact list updated:", dict)


if __name__=='__main__':
  ## Demo search function: you can test first someone
  ## who is there, then someone who is not
  print("Available numbers:", phonebook)
  for _ in range(2):
    search(phonebook)

  ## Demo update function
  ## Press Ctrl+C or Ctrl+D to get out of the loop
  ## (Same command on all platforms!)
  while True:
    update(phonebook)
