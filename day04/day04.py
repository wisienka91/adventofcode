# -*- coding: utf-8 -*-
import hashlib

def get_md5_hash(s_key):
    return hashlib.md5(s_key).hexdigest()

def is_nonce_good(md5_str, condition):
    md5_hash = get_md5_hash(md5_str)
    if md5_hash.startswith(condition):
        return True
    return False

def get_secret_key():
    input_file = open('day04.txt', 'r')
    secret_key = input_file.readline().rstrip()
    return secret_key

def get_ideal_nonce(condition, secret_key):
    nonce = 0
    key_with_nonce = '%s%s' % (secret_key, nonce)
    while not is_nonce_good(key_with_nonce, condition):
        nonce += 1
        key_with_nonce = '%s%s' % (secret_key, nonce)
    print 'Ideal nonce for condition %s is: %s' % (condition, nonce)

def get_ideal_nonces():
    secret_key = get_secret_key()
    conditions = ['00000', '000000']
    for condition in conditions:
        get_ideal_nonce(condition, secret_key)

if __name__ == '__main__':
    get_ideal_nonces()
