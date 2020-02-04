# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores.
# Store them in a list and find the score of the runner-up.

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
