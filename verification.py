import hashlib
from modules import power_mod


def verification(signature, file_with_public_keys):
    numbers_public = []
    with open(file_with_public_keys, 'r') as public_file:
        for elem in public_file:
            numbers_public.append(int(elem))
    n, e = numbers_public[0], numbers_public[1]
    with open(signature, 'r', encoding='UTF-8') as signature:
        file = signature.readlines()[0].replace('\n', '')
        signature.seek(0)
        sign = int(signature.readlines()[1])
    x = power_mod(sign, e, n)
    with open(file, 'rb') as f:
        m = hashlib.sha1()
        while True:
            data = f.read(1024)
            if not data:
                break
            m.update(data)
        hash_file = int(m.hexdigest(), 16)
    calculated_hash = power_mod(x, 1, n)
    print(f'{hash_file} = {calculated_hash}')
    if calculated_hash == hash_file:
        print('Файл не изменялся')
    else:
        print('Файл изменился')


verification('signature', 'file_with_public_keys')
