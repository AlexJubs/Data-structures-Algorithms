# Complete the utopianTree function below.
cache = [1]

def helper (n: int):
    if n < len(cache): return cache[n]
    if n%2 == 1:
        cache.append(2*helper(n-1)) 
        return 2*helper(n-1)
    else: 
        cache.append(helper(n-1)+1)
        return helper(n-1)+1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = helper(n)

        fptr.write(str(result) + '\n')

    fptr.close()
