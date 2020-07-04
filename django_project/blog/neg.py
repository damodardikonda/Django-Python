'''

: Write a Program to that accepts 10 integers from user and breaks
the loop of accepting numbers if user enters a negative number.
{Note: Use Break Statement}
Input: 1 2 3 4 -6
Output: Negative Number Entered, Exiting The Loop!
 '''

for i in range(10):
    n=int(input("Enter the numbers"))
    if n==-n:
        print("Negative Number Entered, Exiting The Loop!")
        break;
    else:
        print(n)
