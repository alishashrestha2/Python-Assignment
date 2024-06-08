"""Write a program to calculate the simple interest on the basis of following assumption:
a) If balance is greater than 99999, interest is 7 %
b) If balance is greater than or equal to 50000 and less than 100000 interest is 5 %
c) If balance is less than 50000, interest is 3%"""
balance = int(input("Enter the balance amount / Principal : "))
time = int(input("Enter the time (in years) :  "))
rate = 0
if balance > 99999 :
    rate = 7
elif balance >= 50000 and balance < 100000 :
    rate = 5
elif balance < 50000 and balance > 0 :
    rate = 3
else :
    print('Please enter valid number.')
interest = (balance * time * rate)/100
print(f"\n\nPrincipal       :\tRs.{balance}")
print(f"Time            :\t{time} years")
print(f"Interest rate   :\t{rate}%")
print(f"Simple interest :\tRs.{interest}\n\n")