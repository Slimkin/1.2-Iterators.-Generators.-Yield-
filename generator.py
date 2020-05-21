from hashlib import md5

def generator(file_path):
    with open(file_path, 'r', encoding='utf8') as f:
        for line in f:
            hash_line = md5(line.encode())
            yield hash_line.hexdigest()

if __name__ == "__main__":
    for i, line in enumerate(generator('result.txt'), 1):
        print(f'{i} - {line}')
