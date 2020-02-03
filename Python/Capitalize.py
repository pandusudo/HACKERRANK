# Complete the solve function below.
def solve(s):
    cap = s.split(" ")
    for i in range(len(cap)):
        cap[i] = cap[i].capitalize()
    return " ".join(cap)
