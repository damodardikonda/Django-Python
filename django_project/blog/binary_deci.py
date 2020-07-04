'''

Write a Program to Convert entered Decimal Number to Binary
Number
Input: Binary Number: 35
Output: Octal Number: 100011 '''



b = ""
dec = int(input("Enter decimal num : "))
while(True):
    quo = int(dec / 2)
    print(quo)
    rem = dec % 2
    print(rem)

    dec = quo
    print(dec)
