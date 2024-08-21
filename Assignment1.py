# *** PROGRAMMING TASKS FOR REFRESHING ***


# 1 : CALCULATE THE AREA OF A RECTANGLE :


length_of_rectangle = 5
width_of_rectangle = 3
area_of_rectangle = length_of_rectangle * width_of_rectangle
print(f"Area of Rectangle is : {area_of_rectangle}")


# 2 : CHECK IF A NUMBER IS EVEN OR ODD : 


a = int(input("Enter Number : "))
b = a % 2
if b == 0 :
    print(f"{a} is Even")
else:
    print(f"{a} is Odd")


# 3 : REVERSE A STRING : 


a = "Hello"
b = a[::-1]
print(b)


# 4 : FIND THE FACTORIAL OF A NUMBER : 


def factorial(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))


# 5 : CHECK IF A STRING IS PALINDROME OR NOT : 


a = "radar"
b = a[::-1]
if a == b :
    print(f"{a} is a palindrome")
else:
    print(f"{a} is not a palindrome")


# 6 : GENERATE FIBONACCI SERIES UP TO N TERMS : 


first_num = 0 
second_num = 1
print(first_num)
for i in range (10):
    print(second_num)
    third_num = first_num + second_num
    first_num = second_num
    second_num = third_num


# 7 : FIND THE LARGEST AMONG THREE NUMBERS : 


a = input("Enter First Number : ")
b = input("Enter Second Number : ")
c = input("Enter Third Number : ")
def check_largest(a, b, c):
    largest = max(a, b, c)
    return largest
print(check_largest(a, b, c))


# 8 : CALCULATE SIMPLE INTEREST : 


principal_amount = 1000
rate_of_interest = 5
time_period = 2
simple_interest = (principal_amount * rate_of_interest * time_period) / 100
print(f"Simple Interest : {simple_interest}")


# 9 : CONVERT CELSIUS TO FAHRENHEIT : 


celsius = 37
fahrenheit = ( celsius * 9 / 5 ) + 32
print(f"Temperature in Fahrenheit : {fahrenheit}")


# 10 : CHECK LEAP YEAR : 


year = 1996
leap_year = year % 4
if leap_year == 0: 
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")


# *** PROGRAMMING CHALLENGES ***


# 1 : FIND THE MEDIAN OF THREE NUMBERS : 


numbers = [10, 5, 20]
numbers.sort()
center_number = len(numbers) // 2
print(numbers[center_number])


# 2 : COUNT THE NUMBER OF WORDS IN A SENTENCE : 


sentence = "the quick brown fox jumps over the lazy dog"
split_sentence = sentence.split(" ")
print(len(split_sentence))


# 3 : CALCULATE THE SUM OF DIGITS IN A NUMBER : 


numbers = "12345"
numbers_1 = []
for i in numbers:
    numbers_1.append(int(i))
print(sum(numbers_1))


# 4 : CHECK IF A NUMBER IS A PRIME NUMBER : 


number = 5
if number == 1:
    print(f"{number} is not a Prime Number")
else:
    for i in range(2, number):
        if number % i == 0:
            print(f"{number} is not a Prime Number")
            break
    else:
        print(f"{number} is a Prime Number")