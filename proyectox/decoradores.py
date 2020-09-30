import time


def timer(method):
    '''Decorator to time a function runtime'''
    def wrapper(*args, **kwargs):
        
        t0 = time.time()
        output = method(*args, **kwargs)
        dt = time.time() - t0
        
        print(f'<{method.__name__} finished in {dt} seconds>')
        return output
    
    return wrapper