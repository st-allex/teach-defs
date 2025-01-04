def get_numbers_digits(n):
    if not isinstance(n, int):
        return 'ERROR: only integer may be parameter here'
    if n//10>0:
        r = get_numbers_digits(n//10)
        r.append(n%10)
        return r
    else:
        return [n%10]

n = 123456
print(get_numbers_digits(n))
