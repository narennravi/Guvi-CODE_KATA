# Question:-
'''
You are given given task is to print whether array is ‘majestic’ or not.A ‘majsetic’ array is an array whose sum of first three number is equal to last three number.

Input Description:
You are given a number ‘n’,Next line contains ‘n’ space separated

Output Description:
Print 1 if array is majestic and 0 if it is not

Sample Input :
7
1 2 3 4 6 0 0

Sample Output :
1
'''


# Solution:-
n = int(input())
l = [int(x) for x in input().split()]
f = l[0] + l[1] + l[2]
la = l[-1] + l[-2] + l[-3]
if f == la:
  print(1)
else:
  print(0)
