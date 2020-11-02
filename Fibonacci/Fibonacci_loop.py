# coding: utf-8
# @Time: 2020/10/28 $ {TIME}
# @File : Fibonacci_loop.py

'''用循环语句实现斐波那契数列'''


def fib_loop(n):
    a, b = 0, 1
    for i in range(1, n + 1):
        print(a, end=' ')
        a, b = b, a + b
        if i % 5 == 0:  # 每五个输出一行  // 这个不用写在函数里面，用return返回，在使用函数的时候再考虑输出样式
            print("\n")


n = int(input('请输入斐波那契数列的长度n：'))  # 输入斐波那契数列的长度
fib_loop(n)
