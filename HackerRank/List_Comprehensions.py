if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

g = [[i,o,p] for i in range(x+1) for o in range(y+1) for p in range(z+1) if (i+o+p) != n]
print(g)
