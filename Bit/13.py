# Question:-
'''
You are given a large number made of only 0’s and 1’s.Your task is to find the max no of consecutive 1’s. If there are no 1’s print -1

Input Description:
A large number ‘n’

Output Description:
Print the max no of consecutive 1 in the number

Sample Input :
101011111
Sample Output :
5
'''



# Solution:-
s = input()
if "1" not in s:
    print(-1)
else:
    n = s.split("0")
    m = str(max(n))
    print(m.count("1"))