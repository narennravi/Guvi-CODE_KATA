# Question:-
'''
Given a number N, print the odd digits in the number(space seperated) or print -1 if there is no odd digit in the given number.
Input Size : N <= 100000

Sample Testcase :
INPUT
2143

OUTPUT
1 3
'''


# Solution:-
no=int(input())
ls=[]
for i in range(len(str(no))):
  digit=no%10
  if digit%2!=0:
    ls.append(digit)
  no=no//10
if not ls:
  print("-1")
else:
  ls.reverse()
  print(*ls,sep=" ")
