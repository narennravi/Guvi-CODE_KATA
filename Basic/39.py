# Question:-
'''
Given a number N followed by N numbers.Find the smallest number and largest number and print both the indices(1 based indexing).
Input Size : N <= 100000

Sample Testcase :
INPUT
5
1 2 3 4 5

OUTPUT
1 5
'''


# Solution:-
n = int(input())
lst = list(map(int,input().split()))
n = lst.index(max(lst)) + 1
m = lst.index(min(lst)) + 1
print(m,n)
