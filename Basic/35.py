# Question:-
'''
Given 3 numbers A,B,C process and print 'yes' if they can form the sides of a triangle otherwise print 'no'.
Input Size : A,B,C <= 100000
Sample Testcase :
INPUT
3 4 5
OUTPUT
yes
'''



# Solution:-
A,B,C=(int(no) for no in input().split())

if (B * B) != C * C:
  print('no')
else:
  print('yes')