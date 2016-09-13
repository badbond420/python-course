#!/usr/bin/env  python
#factorial of nufmber recurssion

def fact_rec(n):
    if n == 1:
        return 1
    else:
        return n * fact_rec(n-1)


#Let's have a look at an iterative version of the factorial function.

def fact(n):
    res=1
    while n > 0:
        res=res * n
        n -= 1
    return res

#fibonacee number

def rec_fibo(n):
    if n==0:
        return 0
    elif n == 1:
        return 1
    else:
        return rec_fibo(n-1) + rec_fibo(n-2)

#iterative solution is also easy to write

def fib(n):
    old,new=0,1
    if n == 0:
        return 0
    for i in range(n-1):
        old,new=new,old+new
    return new

#memorization version

memo={0:0,1:1}

def memofib(n):
    if not n in memo:
        memo[n]=memofib(n-1)+memofib(n-2)
    return memo[n]
print memofib(1)
