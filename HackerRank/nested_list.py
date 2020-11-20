if __name__ == '__main__':
    f = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        f.append([score, name])

    f.sort()
    g = [i for i in f if i[0] != f[0][0]]
    c = [j for j in g if j[0] == g[0][0]]
    
    c.sort(key=lambda x: x[1])
    for i in range(len(c)):
        print(c[i][1])