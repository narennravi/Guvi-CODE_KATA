# Question:-
'''
Rohan is teacher at “Sunsdfghpol” academy about dfg numbers.Assume you are student of his coaching batch .
He has given you some task.Your task is to print nth dfg  number.A dfg number is a number whose prime factors are only 2,3 or 5.

Input Description:
You are given a number ‘n’.

Output Description:
Print all the dfg numbers upto index ‘n’.

Sample Input :
2

Sample Output :
1 2
'''


# Solution;-
n = int(input())
def isprime(a):
    flag = True
    for i in range(2, a//2+1):
        if a%i==0:
            flag = False
            break
    return flag
def primeFactors(a):
    factor = []
    for i in range(2, a+1):
        if a%i==0:
            factor.append(i)
    p = []
    for i in factor:
        if isprime(i):
            p.append(i)
    return p
a = []
i = 1
while True:
    flag = True
    lst = primeFactors(i)
    for j in lst:
        if j not in (2,3,5):
            flag = False
            break
    if flag:
        a.append(i)
    if len(a) == n:break
    else:i += 1
print(*a)
