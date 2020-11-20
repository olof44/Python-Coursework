def is_leap(year):
    leap = False
    l = 5
    n = year % 4
    m = year % 100
    b = year % 400
    if n<=0:
        if m<=0:
            if b<=0:
                leap = True
                return leap
            leap = False
            return leap
        leap = True
        return leap
    else:
        leap = False
        return leap

year = int(input())
print(is_leap(year))
