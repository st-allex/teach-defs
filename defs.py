def get_numbers_digits(prm):
    if isinstance(prm, int):
        prm = {'num': prm, 'rez': []}
    elif not isinstance(prm, dict):
        return 'ERROR: only integer may be parameter here'
    prm['rez'].insert(0, prm['num'] % 10)
    prm['num'] //= 10
    return get_numbers_digits(prm) if prm['num']>0 else prm['rez']

n = 123456
print(get_numbers_digits(n))
