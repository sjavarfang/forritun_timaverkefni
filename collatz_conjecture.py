x = int(input())  # Do not change this line


while x > 1:
        print(x, end=' ')
        if x % 2 == 0:
            x = x // 2
        else:
            x = 3 * x + 1

print(1, end='')
       