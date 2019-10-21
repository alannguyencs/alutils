

def _isArrayLike(obj):
    return hasattr(obj, '__iter__') and hasattr(obj, '__len__')


if __name__ == '__main__':
    demo_array = [1, 2, 3]
    print ('is_array', _isArrayLike(demo_array))