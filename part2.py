'''
***PART 2***

Write a program that prompts the user to enter a number. The program then prints "Hunter" the number of times the user entered. Use a while loop.

Example of what should appear when the program runs:

Times to print: 3
Hunter
Hunter
Hunter

'''
times = int(input("Enter a number: "))
count = 0
while count < times:
  print ("Hunter")
  count += 1

#i used a counter and also times as a range, and print within the while loop so that it would print hunter each time