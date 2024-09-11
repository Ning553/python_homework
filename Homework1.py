""" 计算 1 + 2 + ... + 99 + 100"""
def cal_arithmetic(n):
    if n == 1: return 1
    return cal_arithmetic(n-1) + n
print(cal_arithmetic(100))
print('-'*40)

""" 输出列表中的元素 a_list = ['a'] """
a_list = ['a','b','mpigrim','z','example']
for val in a_list:
    print(val,end=' ')
print()
print('-'*40)

""" 求 1 - 100  之间能被 7 整除，同时不能被 5 整除的所有整数 """
for i in range(1,101):
    if i % 7 == 0 and i % 5 != 0:
        print(i,end=' ')
print()
print('-'*40)

""" 求一个3位的十进制数，其各位数字的立方和等于该数本身。"""
for num in range(100,1000):
    i = num
    tmp = 0
    while i:
        tmp += (i % 10) ** 3
        i //= 10
    if num == tmp:
        print(num,end=' ')
        break
print()
print('-'* 40)

""" 求平均分 """
def cal_avg(lst):
    return sum(lst)/len(lst)
lst = [1,2,3,4,5,6,7,8,9,10]
print(cal_avg(lst))
print('-'*40)

""" 打印九九乘法表 """
def multiply_table():
    for i in range(1,10):
        for j in range(1,i+1):
            print(f'{i} * {j} = {i * j}',end='   ')
        print()
multiply_table()
print('-'*40)

""" 求 200 以内能被 17 整除的最大正整数 """
for i in range(200,-1,-1):
    if i % 17 == 0:
        print(i)
        break
print('-'*40)

""" 判断一个数是不是素数 """
# 法一 ：O(n) 遍历
def is_prime(n):
    if n == 1:return False
    for i in range(2,n):
        if n % i == 0:return False
        return True
print(is_prime(200))
# 法二 ：当一个数不是质数时，必定存在两个约数，一个大于等于sqrt(n)，另一个小于sqrt(n)
import math
def is_prime2(n):
    if n == 1:return False
    for i in range(2,int(math.sqrt(n)) + 1):
        if n % i == 0:return False
    return True
for i in range(1,10):
    print(i,is_prime2(i))
print('-'*40)
""" 输出由 1234 这四个数字组成的每位数都不相同的对所有三位数 """
# 法一 ：O(n^3) 咳咳，不太优雅，肯定要优化
def input_three_num(n):
    if n < 3:return False
    if n == 3:return n
    res = []
    lst = list(str(n))
    # print(lst)
    for i in range(len(lst) - 2):
        for j in range(i+1,len(lst) - 1):
            for k in range(j+1,len(lst)):
                res.append(lst[i] + lst[j] + lst[k])
    return res
print(*input_three_num(12345))
print('-'*40)
""" 计算组合数 """
def fib(n): #计算阶乘
    if n == 0 or n == 1:return 1
    if n == 2:return 2
    return n * fib(n-1)
def comb(n,i):
    i = min(i,n-i)
    return int(fib(n) / (fib(i) * fib(n - i)))
print(comb(4,2))
print('-' * 40)

""" 冒泡排序 """
# 原地排个序吧
def bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j+1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]
import random
lst = [i for i in range(100)]
random.shuffle(lst)
print(lst)
bubble_sort(lst)
print(lst)
print('-' * 40)

""" 选择排序 """
def selection_sort(lst):
    for i in range(len(lst)):
        min_index = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]
lst = [i for i in range(100)]
random.shuffle(lst)
print(lst)
selection_sort(lst)
print(lst)
print('-' * 40)
""" 二分查找 """
def binary_search(lst,target):
    l = 0
    r = len(lst) - 1
    while l <= r:
        mid = (r + l) // 2
        if lst[mid] == target:
            return mid
        if lst[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return None

lst = [1,2,3,4,5,6,7,8,9,10]
print(binary_search(lst,3))
print('-'*40)
""" 截头去尾取平均 """
def find_avg_score(lst):
    lst.remove(max(lst))
    lst.remove(min(lst))
    # print(lst)
    return sum(lst) / len(lst)
lst = [90,98,97,93,100,89,87]
print(find_avg_score(lst))
print('-'*40)

""" 实现十进制到任意进制的转换  """
def system_exchange(n):
    isNeg = True if n < 0 else False
    obj = eval(input("请输入想转成的进制(2/8/16)："))
    integer = int(n)
    # 算一下小数有几位
    s = str(n)
    dot_i = s.find('.')
    f_len = 0 if dot_i == -1 else len(s) - dot_i - 1
    fractions = int((n - integer) * 10**f_len) / 10**f_len # 保留下小数部分 round()不准，会四舍五入掉
    s = ''
    # 如果 obj < 10
    if obj < 10:
        while integer > 0:
            # 转整数部分 (除 R 取余)
            s += (str(integer % obj))
            integer //= obj
        s = s[::-1] # 逆置一下
        s += '.'
        cnt = 0
        while fractions > 0 and cnt < 5: # 小数部分存在，控制位数
            # 转小数部分 (* R 取整)
            # m = fractions
            fractions *= obj #在 Python 中，由于浮点数的表示方式（遵循 IEEE 754 标准），可能会出现精度误差
            s += str(int(fractions))
            fractions -= int(fractions)
            cnt += 1
            # if fractions == m:
            #     break # 死循环了，没法转 -- 还是精度误差的问题，不能这样判断死循环。直接手动计数吧。
    else: # obj >= 10 有字母了
        # 整数部分
        while integer > 0:
            tmp = integer % obj
            s += str(int(tmp)) if tmp < 10 else str(chr(int(tmp) + 55))
            # if tmp < 10:
            #     s += str(int(tmp))
            # else:
            #     s += str(chr(int(tmp) + 55))
            integer //= obj
        s = s[::-1]
        s += '.'
        #小数部分
        cnt = 0
        while fractions > 0 and cnt < 10:
            fractions *= obj
            s += str(int(fractions)) if fractions < 10 else str(chr(int(fractions + 55)))
            # if fractions < 10:
            #     s += str(int(fractions))
            # else:
            #     s += str(chr(int(fractions) + 55))
            fractions -= int(fractions)
            cnt += 1
    return s if not isNeg else '-' + s
n = eval(input())
print(f"{n} -> {system_exchange(n)}")









