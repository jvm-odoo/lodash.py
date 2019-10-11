"""

    Lists

"""

def every(arr, fun, i=0):
    if not arr or len(arr) == 0:
        return False

    return True if fun(arr[i]) and i == len(arr) - 1 \
        else False if not fun(arr[i]) and i == len(arr) - 1 \
        else every(arr, fun, i + 1)

def some(arr, fun, i=0):
    if not arr or len(arr) == 0:
        return False

    return True if fun(arr[i]) \
        else False if not fun(arr[i]) and i == len(arr) - 1 \
        else some(arr, fun, i + 1)

def filtered(arr, fun):
    return [item for item in arr if fun(item)]

def pull(arr, *args):
    for arg in args:
        arr = [item for item in arr if item != arg]

    return arr

def flatten(arr):
    next_arr = []

    for i in arr:
        if isinstance(i, list):
            next_arr += i
        else:
            next_arr.append(i)

    for i in next_arr:
        if isinstance(i, list):
            return flatten(next_arr)

    return next_arr

def diff(a, b):
    return [i for i in a if i not in b]

def compact(arr):
    return list(filter(None, arr))

def chunk(arr, size=1):
    return [arr[i:i + size] for i in range(0, len(arr), size)]

def concat(arr, *args):
    return flatten(arr + [i for i in args])

def intersection(a, b):
    return [i for i in a if i in b]

def xor(arr, *args):
    return diff(arr, flatten(list(args)))

def without(arr, *args):
    return [i for i in arr if i not in args]

def drop(arr, n=1):
    return arr[n:]

def drop_right(arr, n=1):
    return arr[:-n]

def drop_while(arr, fun):
    for item in arr:
        if not fun(item):
            break
        else:
            arr = arr[1:]

    return arr

def drop_while_right(arr, fun):
    for item in arr:
        if not fun(item):
            break
        else:
            arr = arr[:-1]

    return arr

def fill(arr, value, start=0, end=-1):
    end = len(arr) if end == -1 else end

    for i in range(start, end):
        arr[i] = value

    return arr

def find_index(arr, arg, fromIndex=0):
    for i in range(fromIndex, len(arr)):
        if arg(arr[i]):
            return i
    return -1

def find_last_index(arr, arg, fromIndex=0):
    for i in reversed(range(0 + fromIndex, len(arr))):
        if arg(arr[i]):
            return i
    return -1

def head(arr):
    return arr[0]

def first(arr):
    return head(arr)
