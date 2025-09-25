def print_matrix(M):
   for row in M:
      line = "".join(str(i).ljust(5) for i in row)
      print(line)

def tournament(n, filename):

  # Accumulator loop
  T = []
  for _ in range(n):
    T.append([0] * n)

   ## Alternative syntaxes to create matrix:
   # T = [[0] * n for _ in range(n)]
   # T = [[0] * n] * n


  with open(filename, "r") as f:
    for line in f:
      t1, t2, t1_score, t2_score = line.split()
      t1 = int(t1) - 1
      t2 = int(t2) - 1
      t1_score = int(t1_score)
      t2_score = int(t2_score)
      T[t1][t2] = t1_score - t2_score
      T[t2][t1] = t2_score - t1_score
  return T


print_matrix(tournament(4, "scores.txt"))