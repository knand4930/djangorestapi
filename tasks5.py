#1
# number = int(input("Enter a number to find the square root : "))

# #2
# if number < 0 :
#   print("Please enter a valid number.")
# else :
#   #3
#   sq_root = number ** 0.5
#   #4
#   print("Square root of {} is {} ".format(number,sq_root))
  
  
# num = int(input("Enter a number your Number : "))
# if num < 0 :
#     print("Please enter a valid number")
# else:
#     sq_root = num ** 2
#     print("Square root of {} is {} ".format(num, sq_root))
    


num = int(input("Enter a number to find the square root :- " ))

x = num/2

t = 0.00000001

def root(a):
    if ((a*a > num - t) and (a*a <= num + t)):
        return a
    a = (a + num/a)/2
    return root(a)
b = root(int(x))
print(b)