import time

def timer_wrapper(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print("Час виконання:", end_time - start_time, "секунд")
        return result
    return wrapper

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

@timer_wrapper
def prime_num_getter(n):
    generator = (x for x in range(2, n**2) if is_prime(x))
    primes = [next(generator) for _ in range(n)]
    return primes

n = 10
prime_numbers = prime_num_getter(n)
print("Перші", n, "простих чисел:", prime_numbers)