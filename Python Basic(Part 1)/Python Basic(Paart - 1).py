"""
# Exercise 2
# Write a Python program to get the Python version you are using.

import sys

print("Python version")
print(sys.version)
print('Version info')
print(sys.version_info) """

"""""
# Exercise 3
# Write a Python program to display the current date and time.

import datetime

date = datetime.datetime.now()
print("Print the current date")
print(date.strftime("%Y - %m - %d  %H:%M:%S")) """""

"""""
#Exercise 4
# Write a Python program which accepts the radius of a circle from the user and compute the

r = float(input("Enter the radius of circle "))

Area = 3.14 * r**2

print('Area : ', Area) """""


"""
#Exercise 5
# Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.
name = str(input("Please enter your name "))
last_name = str(input("Please enter the your last_name "))
user_info = f"Surname {last_name}  Name {name}"
print(user_info) """

""""#Exercise 6
#  Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.

values = input("Please enter the some numbers ")
list = values.split(",")
tuple = tuple(list)
print("List : ", list)
print("Tuple : ", tuple)"""

"""#Exercise 7
#Write a Python program to accept a filename from the user and print the extension of that.

file_name = input("Please enter the file name with extension")
file = file_name.split(".")
print("File name extension is : " + file[-1])"""

"""#Exercise 8
# Write a Python program to display the first and last colors from the following list

colors = input("Please enter the 4 colors which you love")

color_list = colors.split(",")
fir_last = f"Firsrt color is {color_list[0]} and Last color {color_list[-1]}"
print(fir_last)"""

""" #Exercise 9
# Write a Python program to display the first and last colors from the following list

exam_st_date = (11, 4, 2020)
print("Exam will start from : %i / %i / %i" %exam_st_date) """

"""#Exercise 10
# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn
a = int(input("Please enter one integer number"))

n1 = int("%s" % a)
n2 = int("%s%s" % (a, a))
n3 = int("%s%s%s" % (a, a, a))
print(n1+n2+n3) """

"""#Exercise 11
# Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).

print(abs.__doc__)"""

""""# Exercise 12
#  Write a Python program to print the calendar of a given month and year.

import calendar

y =int(input("Please enter the year : "))
m = int(input("Please enter the month : "))

print(calendar.month(y, m))"""

"""# Exercise 13
#Write a Python program to calculate number of days between two dates.

from datetime import date

d1 = date(2020, 12, 1)
d2 = date(2020, 12, 31)
delta = d2 -d1
print(delta.days) """

""" 
# Exercise 14
# Write a Python program to get the volume of a sphere with radius 6.

r = 6
v = (4/3)*3.14 * r**2
print("The valume of sphere = ", int(v))"""

"""# Exercise 15
#Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.

a = int(input("Input the number "))

if a<17:
    print("The difference between given number and 17 : ", abs(a-17))
else:
    print("The absolute difference", (a-17)*2)"""

"""#Exercise 16
# Write a Python program to calculate the sum of three given numbers, if the values are equal then return thrice of their sum.

a = int(input("Enter the value of a "))
b = int(input("Enter the value of b "))
c = int(input("Enter the value of c "))
if a==b==c:
    print("The values are equal", 3*(a+b+c))
else:
    print("The sum of three values : ", (a+b+c))"""

"""# Exercise 17
#Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged.

def new_string(str):
    str = str(input("Enter the string : "))
    if len(str) >=2 and str[:2] == 'Is':
        return str
    return "Is" + str
print(new_string(str))"""

""""#Exercise 18
#Write a Python program to get a string which is n (non-negative integer) copies of a given string.

def copy_of(str, n):
    result = ""
    for i in range(n):
        result = result +str
    return result
print(copy_of('Sirojiddin', 5))"""

"""#Exercise 19
#Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user

a = int(input("Enter the value of a for checking is it even or odd : "))

if a % 2 == 0:
    print(f"The given number is even  ")
else:
    print(f"The given number is odd")"""

"""#Exercise 20
# Write a Python program to count the number 4 in a given list.


def list_count_4(nums):

    count = 0
    for num in nums:
        if num == 4:
            count +=1
    return count

print(list_count_4([4, 4, 4]))"""
""""
#Exercise 21
#Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. Return the n copies of the whole string if the length is less than 2def copy(str, n):
    result = ""
    for i in range(n):
        result = result + str[:2]
    return result
print(copy("Siroj", 4))"""

"""#Exercise 22
# Write a Python program to test whether a passed letter is a vowel or not.


def is_vowel(char):
    all_vowel = 'aeiou'
    return char in all_vowel


print(is_vowel('c'))
print(is_vowel('g'))
"""
"""#Exercise 23
#Write a Python program to check whether a specified value is contained in a group of values.
# 1
a = int(input("Enter the number for checking : "))
list = [1, 2, 3, 4, 5, 6, 7, 8,9, 10]

if a in list:
    print("True")
else:
    print("False")

# 2
def check_the(group_values, n):

    for values in group_values:
        if n == values:
            return True
    return False
print(check_the(group_values=[3,4,5,6,7,8,9,10], n=int(input("Enter the value of n : "))))"""

"""##Exercise 24
# Write a Python program to create a histogram from a given list of integers.

# My way
def histogram(sign):
    list = [2, 4, 5, 6, 7]
    for i in list:
        print(i*sign)
histogram('@')


# Solution of w3
def histogram( items ):
    for n in items:
        output = ''
        times = n
        while( times > 0 ):
          output += '*'
          times = times - 1
        print(output)

histogram([2, 3, 6, 5])"""

"""#Exercise 25
#Write a Python program to concatenate all elements in a list into a string and return it.


def concatenate(item):
    result = ""
    for elements in item:
        result = result + str(elements)
    return result
print(concatenate([1,2,3,4,5,67,9]))"""

"""#Exercise 26
#  Write a Python program to print all even numbers from a given numbers list in the same order and stop the printing if any numbers that come after 237 in the sequence.

numbers = [
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958,743, 527
    ]

for i in numbers:
    if i == 237:
        print(i)
        break
    elif i % 2 ==0:
        print(i)"""
"""""# Exercise 27
# Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2.

color_list_1 = set(['Red', 'Black', 'Green'])
color_list_2 = set(['Red', 'Yellow'])
print(color_list_1.difference(color_list_2))"""

# Exercise 28
#Write a Python program that will accept the base and height of a triangle and compute the area.
base = int(input("Enter the base of triangle : "))
height = int(input("Enter the height of triangle : "))

Area = (base*height)/2

print("Area of triangle : ", Area)

#Exercise 29
#
