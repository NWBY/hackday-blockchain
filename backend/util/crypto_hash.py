import hashlib
import json

def crypto_hash(*args):
    """
    Return a SHA-256 hash of the given arguments
    """
    stringified_args = sorted(map(lambda data: json.dumps(data), args))
    joined_data = ''.join(stringified_args)

    return hashlib.sha256(joined_data.encode('utf-8')).hexdigest()

def main():
    print(f"crypto_hash('testing', [1, 2, 3], 900): {crypto_hash('testing', [1, 2, 3], 900)}")
    print(f"crypto_hash([1, 2, 3], 900, 'testing'): {crypto_hash([1, 2, 3], 900, 'testing')}")

if __name__ == '__main__':
    main()
