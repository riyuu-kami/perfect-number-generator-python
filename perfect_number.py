
n = 2
def perfect(n):
    sum_ = 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            sum_ = sum_ + i + n/i
        i += 1
    if sum_ == n and n!= 1:
        return True
    else:
        False

for n in range(3000000,35000000):
    if perfect(n):
        print(n)
