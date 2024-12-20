# def min_number(*agrs):
#     """
#     This function returns the minimum number of the given arguments.
#     """
#     return min(agrs)


# min=min_number(1,2,3,4,5,6,7,8,9,10,2) #*args collects all the positional arguments passed to the function into a tuple named args.
# print(min)


# print(min_number.__doc__) # __doc__ is used to print the docstring of the function.


year=2022

if year%4==0 or year%100!=0 and year%400==0:
    print("Leap Year")
else:
    print("Not a Leap Year")



salary=10000
year_of_servic=5


if year_of_servic>5:
    bonus=salary*5/100
    print(f"Bonus is {bonus}")
