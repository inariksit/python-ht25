with open("test.txt") as file:
    print("Reading incrementally, 2 characters at a time")
    print("---------------------------------------------")

    for _ in range(10):
        c = file.read(2)
        print(c)
    print()

    print("The rest of the file below")
    print("--------------------------")

    rest_of_file = file.read()
    print(rest_of_file)


    desperate_attempt_to_squeeze_last_drops = file.read(1)

## If you open this file in interactive shell:
## python -i general_file_handling.py
## and see the value of desperate_attempt_to_squeeze_last_drops
## it is an empty string!