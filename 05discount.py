"""A program to calculate discount on the basis of following assumption:
a) If purchased amount is greater than or equal to 5000, discount is 10%
b) If purchased amount is greater than or equal to 4000 and less than 5000, discount is 7%
c) If purchased amount is greater than or equal to 3000 and less than 4000, discount is 5%
d) If purchased amount is greater than or equal to 2000 and less than 3000, discount is 3%
e) If purchased amount is less than 2000, discount is 2%"""
amount = float(input("Enter the purchased amount : "))
discount_percentage = 0 
discount_amount = 0
final_amount = 0
if amount >= 5000 :
    discount_percentage = 0.1
elif amount >= 4000 and amount < 5000 :
    discount_percentage = 0.07
elif amount >= 3000 and amount< 4000 :
    discount_percentage = 0.05
elif amount >= 2000 and amount < 3000 :
    discount_percentage = 0.03
elif amount < 2000 and amount > 0 :
    discount_percentage = 0.02
else :
    print("Error")
discount_amount = discount_percentage * amount
final_amount = amount - discount_amount
print("\n\n-------------------Bill-------------------")
print("________________________________________")
print("|Particulars\t\t|Details\t|")
print("|-----------------------|---------------|")
print(f"|Total Amount\t\t|Rs.{amount}\t|")
print("|-----------------------|---------------|")
print(f"|Discount rate\t\t|{discount_percentage*100}%\t\t|")
print("|-----------------------|---------------|")
print(f"|Discount Amount\t|Rs.{discount_amount}\t|")
print("|-----------------------|---------------|")
print(f"|Final Amount\t\t|Rs.{final_amount}\t|")
print("|_______________________|_______________|\n\n")