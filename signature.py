from modules import power_mod
import hashlib


def digital_signature(name_of_file, file_with_private_key, file_with_public_keys, file_with_signature):
    with open(name_of_file, 'rb') as f:
        m = hashlib.sha1()
        while True:
            data = f.read(1024)
            if not data:
                break
            m.update(data)
        hash_file = int(m.hexdigest(), 16)
    with open(file_with_private_key, 'r') as private_file:
        for elem in private_file:
            private_key = int(elem)
    numbers_public = []
    with open(file_with_public_keys, 'r') as public_file:
        for elem in public_file:
            numbers_public.append(int(elem))
    n, e = numbers_public[0], numbers_public[1]
    signature = power_mod(hash_file, private_key, n)
    with open(file_with_signature, 'w') as file_with_signature:
        file_with_signature.write(name_of_file + '\n')
        file_with_signature.write(str(signature))

    print(f'Подпись = {signature}\nХэш файла = {hash_file}')


digital_signature('Document.txt', 'file_with_private_key', 'file_with_public_keys', 'signature')
