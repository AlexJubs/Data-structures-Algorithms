
# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    birds = {}
    m = -1
    res = []
    for x in arr:
        if x not in birds: birds[x] = 0
        birds[x] = birds[x] +1
        m = max(birds[x],m)
    for x,y in birds.items():
        if y == m: res.append(x)
    return min(res)