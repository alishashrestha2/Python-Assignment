"""A program to calculate discount on the basis of following assumption:
a) If purchased amount is greater than or equal to 1000, discount is 5%"""
amount = float(input("Enter the purchased amount : "))
discount_percentage = 0 
discount_amount = 0
final_amount = 0
if amount >= 1000 :
    discount_percentage = 0.05
else :
    discount_percentage = 0
discount_amount = discount_percentage * amount
final_amount = amount - discount_amount
print("\n\n-------------------Bill-------------------")
print("________________________________________")
print("|Particulars\t\t|Details\t|")
print("|-----------------------|---------------|")
print(f"|Total Amount\t\t|Rs.{amount}\t|")
print("|-----------------------|---------------|")
print(f"|Discount rate\t\t|{discount_percentage * 100}%\t\t|")
print("|-----------------------|---------------|")
print(f"|Discount Amount\t|Rs.{discount_amount}\t|")
print("|-----------------------|---------------|")
print(f"|Final Amount\t\t|Rs.{final_amount}\t|")
print("|_______________________|_______________|\n\n")