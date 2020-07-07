'''
Write a Program to check whether the entered number by user is Deficient or not.
{Note: A Number is termed as deficient number, if sum of all of its perfect
divisors is less than the number itself. E.g. 15 is deficient number, since 1 + 3 + 5 = 9 < 15.}
Input: 45
Output: 45 is Deficient Number.
'''

num=int(input("Enter the number"));
count=0
if num%2==0:
    count=count+num

print(count)

if count< num:
    print(num,"is deficient Number");
else:
    print(num,"is not a deficient number")
