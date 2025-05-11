import hashlib
import itertools


def find_hash(key: str) -> int:
    secret = ""
    num = 0
    for num in itertools.count(1):
        secret = key + str(num)
        hashfunc = hashlib.md5(secret.encode())
        hash = hashfunc.hexdigest()
        if hash[0:6] == "000000":
            break
    return num


# print(find_hash("abcdef"))
# print(find_hash("pqrstuv"))

print(find_hash("bgvyzdsv"))
