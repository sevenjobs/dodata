import functools

functiondict={"add":add}

@functools.lru_cache(maxsize=None)
def add(num1,num2):
    return num1+num2