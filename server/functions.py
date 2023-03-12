import functools

functiondict={"add":add}

@functools.lru_cache(maxsize=None)
def add(*numlist):
    answer = 0
    for i in numlist:
        answer += i
    return answer