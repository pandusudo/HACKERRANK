if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

def findRunnerUp(inp, arr):
    lst = list(arr)
    maxVal = max(lst)
    while lst.count(maxVal) != 0:
        lst.remove(maxVal)
    runnerUp = max(lst)
    return runnerUp

print(findRunnerUp(n, arr))
