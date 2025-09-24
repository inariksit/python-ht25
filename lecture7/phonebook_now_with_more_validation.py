## Read contacts from the file people.txt into a dictionary
# Alice: 1234567890
# Bob: 9876543210

## Add a new contact
phonebook = {}

## Fill phonebook with data in the file
try:
  with open("../lecture6/people.txt", "r") as file:
    for line in file:
      # unpack result of splitting line (which is a list)
      split_line = line.split(':')
      if len(split_line) == 2:
        name, number = split_line

        # strip() for security:
        # does nothing if string already clean of trailing whitespace
        phonebook[name.strip()] = [number.strip()]
except FileNotFoundError:
  print("So sorry, couldn't find the file :(")

## Search for contacts
def search(dict):
  contact = input("Who do you want to call? ")
  number = dict.get(contact, "not in your contacts")
  # Does not crash, even if contact not found
  print(f"{contact}'s number is {number}")

def update(dict):
  contact = input("Who do you want to update? ")
  number = input("What is the new number? ")
  existing_numbers = dict.setdefault(contact, [])
  existing_numbers.append(number)
  print("Contact list updated:", dict)

if __name__=='__main__':
  print(phonebook)

  phonebook['Vaktmästare'] = ['0317728800']
  print(phonebook)

  try:
    while True:
      update(phonebook)
  except KeyboardInterrupt:
    print("Bye! Nice doing business with you :)))))")
  except EOFError:
    print("Exciting choice of keyboard commands, bye anyway!")
  except:
    print("Something else happened")

  ## Output updated phonebook into a new file, in the same format
  fname = input("Where do you want to save the phonebook?\n> ")
  with open(fname, "w") as file:
    for name,numbers in phonebook.items():
      numbers_pretty = " or ".join(numbers)
      file.write(f"{name}: {numbers_pretty}\n")

  print(f"Done! Saved in {fname}")