# Given integer N. Print all square of number until N

if __name__ == '__main__':
    n = int(input())

i = 0
while i < n:
    print(str(i * i))
    i += 1
