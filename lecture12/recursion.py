import time

def facr(n):
    if n <= 1:
        return 1
    else:
        return facr(n-1) * n


def facl(n):
    acc = 1
    for k in range(1,n+1):
        acc *= k
    return acc



start = time.process_time()

facr(15)

end = time.process_time()

print(end-start)


start = time.process_time()

facl(15)

end = time.process_time()

print(end-start)