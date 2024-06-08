""" The rates of tax on gross salary are as shown below:
Income Tax
Less than 10,000 Nil
Rs. 10,000 to 19,999 10%
Rs. 20,000 to 39,999 15%
Rs. 40,000 to above 20%
Write a program to compute the net salary after deducting the tax for the given information and print the same."""
salary = float(input("Enter your gross salary : "))
tax_rate = 0
tax_amount = 0
net_salary = 0
if salary < 10000 and salary > 0 :
    tax_rate = 0
elif salary >= 10000 and salary < 20000 :
    tax_rate = 0.1
elif salary >= 20000 and salary < 40000 :
    tax_rate = 0.15
elif salary >= 40000 :
    tax_rate = 0.2
else :
    print('Error')
tax_amount = tax_rate * salary
net_salary = salary - tax_amount
print("\n________________________________________________________________")
print("|Gross Salary\t|Tax Rate\t|Tax Amount\t|Net Salary\t|")
print("|---------------|---------------|---------------|---------------|")
print(f"|Rs.{salary}\t|{tax_rate * 100}%\t\t|Rs.{tax_amount}\t|Rs.{net_salary}\t|")
print("|_______________|_______________|_______________|_______________|\n\n")