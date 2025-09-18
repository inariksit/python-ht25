## Read contacts from the file people.txt into a dictionary
# Alice: 1234567890
# Bob: 9876543210

## Add a new contact
phonebook = {}

## Fill phonebook with data in the file
with open("people.txt") as file:
  lines = file.readlines()
  for line in lines:
    # unpack result of splitting line (which is a list)
    name, number = line.split(':')

    # strip() for security:
    # does nothing if string already clean of trailing whitespace
    phonebook[name.strip()] = number.strip()

## Search for contacts
def search(dict):
  contact = input("Who do you want to call? ")
  number = dict.get(contact, "not in your contacts")
  # Does not crash, even if contact not found
  print(f"{contact}'s number is {number}")


if __name__=='__main__':
  print(phonebook)

  for _ in range(3):  # or use while True for infinite loop
    search(phonebook)

  ## Output updated phonebook into a new file, in the same format
  ## Didn't have time to do it in class, but here's how to do it
  phonebook['Vaktmästare'] = '0317728800'
  with open("people-updated.txt", "w") as file:
    for name, number in phonebook.items():
      file.write(f"{name}: {number}\n")
  print("Updated the file people-updated.txt")