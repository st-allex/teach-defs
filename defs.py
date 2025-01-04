def ret_append(l, e):
    l.append(e)
    return l

def get_numbers_digits(n):
    if not isinstance(n, int):
        return 'ERROR: only integer may be parameter here'
    return ret_append(get_numbers_digits(n//10), n%10) if n//10>0 else [n%10]

n = 123456
print(get_numbers_digits(n))
