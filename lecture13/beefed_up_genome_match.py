### You will find the standard solution in the repo of old exams
### https://github.com/jyp/python-courses-exams/blob/main/2403/q2.py

# Create some artificial data and put it in genome.txt
f = open("genome.txt", "w")
f.write("GTACACAGT"*1000)
f.close()


## This is now a generator!
## This would more typically be /library code/, not main application
def gene_match_generator(gene,genome):
  i = 0 # Index where the gene begins
  l = len(gene)
  with open(genome) as file:
    candidate = file.read(l)
    while True:
      #print(f"candidate at the start of loop: {candidate}")
      if candidate == gene:
        yield i  ## A generator! it yields

      c = file.read(1)
      if c == '':
        return  # because I want to exit the whole function!
      else:
        i = i+1
        candidate = candidate[1:] + c
        #print(f"candidate if file was not exhausted and we added c: {candidate}")

## End user application that uses the generator
## It is user-friendly to give access as a generator
## so that the library function doesn't load potentially millions of
## lines of data into memory at once.
def main():
  for index in gene_match_generator("CAGTG", "genome.txt"):
    print(index)
    action_to_take = input("Do you want to react to this info? ")
    ## Then assume we actually did something based on the user input

## Press Ctrl+C or Ctrl+D to exit from the program!
if __name__=="__main__":
  main()

