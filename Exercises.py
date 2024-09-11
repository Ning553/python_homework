
def To_bin(n):
    lst = []
    while n :
        n *= 2
        tmp = int(n)
        if tmp == 1:
            lst.append(1)
        else:
            lst.append(0)
        n -= tmp
    return lst
print('.',*To_bin(0.375))

def To_bin2_int(n):
    flag = False
    if n < 0:
        flag = True
        n = -n
    res = ''
    while n:
        tmp = n // 2 # 整数
        sur = n - 2 * tmp # 余数
        res += str(sur)
        n //= 2
    return res if not flag else '-' + res
print(To_bin2_int(-13))

























