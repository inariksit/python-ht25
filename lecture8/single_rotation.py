def is_group_complete(m,i,j):
    not_too_small = i >= 0 and j >= 0
    not_too_big = i <= len(m)-2 and j <= len(m[0]) - 2
    return not_too_small and not_too_big

def occ(m,i,j):
    return int(m[i][j] != None)

def is_single_group(m,i,j):
    sum = occ(m,i,j) + occ(m,i,j+1), occ(m,i+1,j), occ(m,i+1,j+1)
    return sum == 1

### You can try the rest on your own!
### Instructions and tests on self-practice under subheading Matrices