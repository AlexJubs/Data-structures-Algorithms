def reverse_diff(x):
    return abs(x-int(str(x)[::-1]))

def beautifulDays(i, j, k):
    res = 0
    for x in range(i,j+1):
        if reverse_diff(x)%k == 0: res = res +1
    return res