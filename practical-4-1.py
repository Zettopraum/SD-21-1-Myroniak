def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_num_generator():
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1
        
generator = prime_num_generator()
for _ in range(10):
    print(next(generator))