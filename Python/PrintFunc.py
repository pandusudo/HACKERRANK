# Given integer N. Write a loop print 123 ... N

if __name__ == '__main__':
    n = int(input())

i = 1
while i <= n:
    print(i, end = '')
    i += 1
