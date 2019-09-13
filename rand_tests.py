from rand import rand
from datetime import datetime as dt
import sys

def test_hash_size():
    r = rand(dt.now())
    entropy = r._create_entropy()
    hash = r._hash(entropy)
    assert(sys.getsizeof(hash)==113)
    print('passed')

def test_validate_two_hashes_not_equal():
    r = rand(dt.now())
    entropy = r._create_entropy()
    hash1 = r._hash(entropy)
    hash2 = r._hash(entropy)
    assert(hash1 != hash2)
    print('passed', hash1, hash2)


if __name__ == '__main__':
    test_hash_size()
    test_validate_two_hashes_not_equal()