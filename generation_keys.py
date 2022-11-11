from modules import gcd, find_inverse_elem
from Cryptodome.Util import number


def gen_p():
    p = number.getPrime(512)
    return p


def gen_q():
    q = number.getPrime(512)
    return q


def calculate_n(p, q):
    n = p * q
    return n


def euler_function(p, q):
    euler_func = (p - 1) * (q - 1)
    return euler_func


def public_key_e(euler_func):
    while True:
        e = number.getPrime(512)
        if e % 2 != 0 and gcd(e, euler_func) == 1:
            return e


def private_key_d(euler_func, e):
    d = find_inverse_elem(e, euler_func)
    return d


def create_file_with_public_keys(n, e):
    public_keys = [n, e]
    with open('file_with_public_keys', 'w') as file_with_public_keys:
        for key in public_keys:
            file_with_public_keys.writelines(str(key) + '\n')


def create_file_with_private_key(d):
    with open('file_with_private_key', 'w') as file_with_private_key:
        file_with_private_key.write(str(d) + '\n')


def generation_keys():
    p, q = gen_p(), gen_q()
    n = calculate_n(p, q)
    euler_func = euler_function(p, q)
    e = public_key_e(euler_func)
    d = private_key_d(euler_func, e)
    print(f'p = {p} \nq = {q}')
    print(f'n = {n}')
    print(f'euler_func = {euler_func}')
    print(f'public_key_e = {e}')
    print(f'private_key_d = {d}')
    create_file_with_private_key(d)
    create_file_with_public_keys(n, e)


generation_keys()
