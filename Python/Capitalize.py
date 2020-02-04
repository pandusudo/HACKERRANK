# You are asked to ensure that the first and last names of people begin with a capital letter in their passports. 
# For example, alison heck should be capitalised correctly as Alison Heck.

# Complete the solve function below.
def solve(s):
    cap = s.split(" ")
    for i in range(len(cap)):
        cap[i] = cap[i].capitalize()
    return " ".join(cap)
