from backend.util.crypto_hash import crypto_hash

def test_crypto_hash():
    # Testing it will create same hash with same args in different order
    assert crypto_hash('test', 1000, ['hello', 12345]) == crypto_hash(1000, ['hello', 12345], 'test')
