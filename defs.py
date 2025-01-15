import time

# decorator function
def get_productivity(func):
    def wrapper(*args, **kwargs):
        start_timestamp = time.time()
        result = func(*args, **kwargs)
        end_timestamp = time.time()
        execution_duration = end_timestamp - start_timestamp
        print(f"Function {func.__name__} took {execution_duration} seconds to execute")
        return result
    return wrapper


def get_numbers_digits(n):
    if not isinstance(n, int):
        return 'ERROR: only integer may be parameter here'
    return get_numbers_digits(n//10)+[n%10] if n//10>0 else [n%10]


@get_productivity
def exec_recursion(n):
    return get_numbers_digits(n)


@get_productivity
def get_numbers_digits_2(n):
    if not isinstance(n, int):
        return 'ERROR: only integer may be parameter here'
    return list(map(int, str(n)))


@get_productivity
def get_numbers_digits_cicl(n):
    if not isinstance(n, int):
        return 'ERROR: only integer may be parameter here'
    result = []
    while n>0:
        result = [n%10] + result
        n //= 10
    return result


n = 1234567890123456789012345678901234567890
print(exec_recursion(n))
print(get_numbers_digits_2(n))
print(get_numbers_digits_cicl(n))
